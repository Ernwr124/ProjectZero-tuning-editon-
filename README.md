# ⚡️ ProjectZero (Tuner Edition)
> **Vibe-driven MLOps Platform for Autonomous LLM Fine-Tuning**

[![Status](https://img.shields.io/badge/Status-Live_MVP-brightgreen)](http://178.88.115.250)
[![Brain](https://img.shields.io/badge/AI_Brain-gpt--oss:117b-white)](https://alem.ai)
[![Framework](https://img.shields.io/badge/Engine-Unsloth-green)](https://github.com/unslothai/unsloth)
[![Backend](https://img.shields.io/badge/Stack-FastAPI_%7C_SSE-black)](https://fastapi.tiangolo.com/)

---

## 🌪 The Philosophy: Vibe-driven MLOps
Fine-tuning Large Language Models is notoriously difficult. It requires deep knowledge of quantization, LoRA adapters, and boilerplate training code. 

**ProjectZero (Tuner Edition)** changes the game. Built on the "Vibe Coding" philosophy, it allows developers to describe their training goals in natural language. Our autonomous agent then architecturally analyzes the model and streams a production-ready training script in real-time.

[**🌐 View Live Demo**](http://178.88.115.250)

---

## 🛠 Features
* **Live Hub Validation:** Real-time integration with HuggingFace API to verify model IDs and dataset availability.
* **Real-time Code Streaming:** Watch the AI (gpt-oss:117b) write your `train.py` character by character using Server-Sent Events (SSE).
* **Unsloth Integration:** Every generated script is optimized for 2x faster training and 4-bit quantization, making fine-tuning possible even on consumer GPUs (like RTX 2050).
* **Autonomous Pipeline:** From prompt to executable training script in under 60 seconds.

## 🏗 System Architecture (Node-based Flow)
Our system follows a strictly linear pipeline inspired by modern low-code tools like n8n:
`User Input` ➜ `FastAPI Gateway` ➜ `Alem.plus Brain` ➜ `Live Script Generation` ➜ `Zero-Core Simulated Executor`

## 💻 Tech Stack
- **AI Core:** `gpt-oss` (117B) via Alem.plus API.
- **Backend:** Python / FastAPI (Asynchronous streaming).
- **Frontend:** Vanilla JS / Tailwind CSS (Cyber-monochrome Glassmorphism UI).
- **Deployment:** Live on Ubuntu 24.04 Cloud Node.

---

## ⚠️ Hackathon MVP Note for Judges
To provide a high-fidelity demonstration within a hackathon environment:
1.  **REAL GENERATION:** The AI Agent and code generation logic are **100% functional**. The Python code you see in the "Live Stream" window is generated in real-time by the LLM specifically for your prompt.
2.  **SIMULATED EXECUTION:** The "System Output" terminal simulates the GPU cluster allocation and training steps. While the generated `train_generated.py` is a valid executable script, real hardware execution is bypassed for instant demo purposes.

---

## 🚀 Getting Started (Local Node)

1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/Ernwr124/ProjectZero-tuner-edition.git](https://github.com/Ernwr124/ProjectZero-tuner-edition.git)
    cd ProjectZero-tuner-edition
    ```
2.  **Configure Environment:**
    Create a `.env` file and add your Alem API Key:
    ```text
    ALEM_API_KEY=your_key_here
    ```
3.  **Install & Run:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```

---

### 🔗 About the Project
ProjectZero (Tuner Edition) is a specialized module of the **ProjectZero AI** ecosystem.

**Powered by [ProjectZero ai](https://www.pzero.kz)** *(vibe coding service on Kazakhstan)*
