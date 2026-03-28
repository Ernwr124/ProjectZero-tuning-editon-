import os
import torch
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
)
from unsloth import FastLanguageModel, is_bfloat16_supported

# --------------------------- Settings ---------------------------
BASE_MODEL = "Qwen/Qwen3.5-2B"
DATASET_NAME = "amandyk/kazakh_wiki_articles"
OUTPUT_DIR = "zero_lora_kz"

MAX_SEQ_LENGTH = 512
PER_DEVICE_TRAIN_BATCH_SIZE = 2
GRADIENT_ACCUMULATION_STEPS = 4
NUM_TRAIN_EPOCHS = 3
LEARNING_RATE = 2e-4

# LoRA hyper‑parameters
LORA_R = 16
LORA_ALPHA = 16
LORA_TARGET_MODULES = ["q_proj", "v_proj"]

# --------------------------- Tokenizer ---------------------------
tokenizer = AutoTokenizer.from_pretrained(
    BASE_MODEL,
    trust_remote_code=True,
)
# Qwen models use eos as pad token
tokenizer.pad_token = tokenizer.eos_token

# --------------------------- Dataset ---------------------------
raw_dset = load_dataset(DATASET_NAME)

def preprocess_fn(examples):
    # The dataset contains a column named "text"
    return tokenizer(
        examples["text"],
        truncation=True,
        max_length=MAX_SEQ_LENGTH,
    )

train_dataset = raw_dset["train"].map(
    preprocess_fn,
    batched=True,
    remove_columns=raw_dset["train"].column_names,
)

# --------------------------- Model ---------------------------
# Load the model in 4‑bit + bfloat16/float16 (depending on hardware)
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=BASE_MODEL,
    max_seq_length=MAX_SEQ_LENGTH,
    dtype=torch.bfloat16 if is_bfloat16_supported() else torch.float16,
    load_in_4bit=True,
    device_map="auto",
)

# Attach LoRA adapters (only q_proj and v_proj)
lora_config = {
    "r": LORA_R,
    "alpha": LORA_ALPHA,
    "target_modules": LORA_TARGET_MODULES,
    "bias": "none",
    "task_type": "CAUSAL_LM",
}
model = FastLanguageModel.get_peft_model(model, lora_config)

# --------------------------- Training ---------------------------
training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    per_device_train_batch_size=PER_DEVICE_TRAIN_BATCH_SIZE,
    gradient_accumulation_steps=GRADIENT_ACCUMULATION_STEPS,
    num_train_epochs=NUM_TRAIN_EPOCHS,
    learning_rate=LEARNING_RATE,
    fp16=False,
    bf16=is_bfloat16_supported(),
    logging_steps=10,
    save_steps=500,
    save_total_limit=2,
    evaluation_strategy="no",
    optim="adamw_torch",
    warmup_steps=10,
    weight_decay=0.01,
    max_grad_norm=0.3,
    lr_scheduler_type="cosine",
    report_to="none",
)

data_collator = DataCollatorForLanguageModeling(tokenizer, mlm=False)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    data_collator=data_collator,
)

trainer.train()

# --------------------------- Save LoRA adapters ---------------------------
# The adapters are stored inside the PEFT wrapper; saving the model will
# persist only the adapter weights.
model.save_pretrained(OUTPUT_DIR)
tokenizer.save_pretrained(OUTPUT_DIR)

print(f"LoRA adapters saved to '{OUTPUT_DIR}'")