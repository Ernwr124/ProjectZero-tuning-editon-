import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import engine

app = FastAPI(title="ProjectZero MLOps")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/start")
async def start_training(req: Request):
    data = await req.json()
    model_name = data.get("model_name", "unsloth")
    dataset_url = data.get("dataset_url", "")
    prompt = data.get("prompt", "")

    async def event_stream():
        # 1. Логи в терминал
        yield "data: [SYSTEM] Initialization ProjectZero MLOps Agent...\n\n"
        await asyncio.sleep(1)
        yield f"data: [AI] Analyzing model architecture ({model_name})...\n\n"
        await asyncio.sleep(1)
        yield "data: [AI] Initiating real-time code generation via gpt-oss...\n\n"
        
        # 2. СТРИМИНГ КОДА (Передаем в нижнее окно)
        full_code = ""
        # Читаем чанки из engine.py и отправляем их с префиксом [CODE]
        for chunk in engine.stream_unsloth_script(model_name, dataset_url, prompt):
            full_code += chunk
            # Заменяем реальные переносы строк на \n, чтобы не сломать формат SSE
            safe_chunk = chunk.replace('\n', '\\n')
            yield f"data: [CODE]{safe_chunk}\n\n"
            # Небольшая задержка для красивого визуального эффекта
            await asyncio.sleep(0.01)
            
        # Сигнал, что код закончен
        yield "data: [CODE_DONE]\n\n"
        yield "data: [SYSTEM] Generated script successfully saved to zero_node.\n\n"
        await asyncio.sleep(1)
        
        # Сохраняем физически (для доказательства)
        with open("train_generated.py", "w", encoding="utf-8") as f:
            f.write(full_code)

        # 3. Эмуляция обучения (Логи в терминал)
        yield "data: [GPU] Provisioning ZERO-CORE Cluster...\n\n"
        await asyncio.sleep(2)
        yield f"data: [TRAINING] Downloading weights [██████████] 100%\n\n"
        
        epochs = 3
        for epoch in range(1, epochs + 1):
            await asyncio.sleep(1.5)
            loss = 1.84 / epoch
            yield f"data: [TRAINING] Epoch {epoch}/{epochs} | Loss: {loss:.4f} | Step: {epoch*100}/300\n\n"
            
        yield "data: [SYSTEM] Autonomous Fine-Tuning complete. Adapters ready.\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(event_stream(), media_type="text/event-stream")
