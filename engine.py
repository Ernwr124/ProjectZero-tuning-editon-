import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ALEM_API_KEY")
GPT_URL = "https://llm.alem.ai/chat/completions"
MODEL = "gpt-oss"

def stream_unsloth_script(model_name: str, dataset_url: str, prompt: str):
    """Генератор, который возвращает код по кусочкам (стриминг) от gpt-oss"""
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    system_prompt = f"""You are an elite Senior MLOps Engineer.
    Write a highly optimized Python script for fine-tuning a model using Unsloth.
    Base Model: {model_name}. Dataset: {dataset_url}. Objective: {prompt}.
    RETURN ONLY RAW, EXECUTABLE PYTHON CODE. Do not include markdown blocks (like ```python)."""
    
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Generate the script."}
        ],
        "temperature": 0.1,
        "stream": True # ВАЖНО: Включаем стриминг!
    }
    
    try:
        response = requests.post(GPT_URL, headers=headers, json=payload, stream=True)
        response.raise_for_status()
        
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                if decoded_line.startswith('data: '):
                    data_str = decoded_line[6:] # Убираем 'data: '
                    
                    if data_str == '[DONE]':
                        break
                        
                    try:
                        data_json = json.loads(data_str)
                        # Извлекаем кусочек текста
                        chunk = data_json['choices'][0]['delta'].get('content', '')
                        if chunk:
                            yield chunk
                    except json.JSONDecodeError:
                        continue
                        
    except Exception as e:
        yield f"# Ошибка API: {e}"
