# ⚡️ ProjectZero (Tuner Edition)
> **LLM модельдерін автономды баптауға (Fine-Tuning) арналған Vibe-driven MLOps платформасы**

[![Status](https://img.shields.io/badge/Status-Live_MVP-brightgreen)](http://178.88.115.250)
[![Brain](https://img.shields.io/badge/AI_Brain-gpt--oss:117b-white)](https://alem.ai)
[![Framework](https://img.shields.io/badge/Engine-Unsloth-green)](https://github.com/unslothai/unsloth)
[![Backend](https://img.shields.io/badge/Stack-FastAPI_%7C_SSE-black)](https://fastapi.tiangolo.com/)

---

## 🌪 Философиясы: Vibe-driven MLOps
Үлкен тілдік модельдерді (LLM) дообучение жасау — өте күрделі процесс. Ол үшін кванттау, LoRA адаптерлері және жүздеген жол кодты жазу бойынша терең білім қажет.

**ProjectZero (Tuner Edition)** бұл ережелерді өзгертеді. "Vibe Coding" философиясына негізделген платформа әзірлеушілерге өз мақсаттарын қарапайым тілде сипаттауға мүмкіндік береді. Біздің автономды агент модельді талдап, нақты уақыт режимінде дайын оқу скриптін (train.py) жазып береді.

[**🌐 Live Demo-ны көру**](http://178.88.115.250)

---

## 🛠 Мүмкіндіктері
* **Live Hub Validation:** HuggingFace API-мен нақты уақытта интеграция жасап, модельдер мен датасеттерді тексереді.
* **Real-time Code Streaming:** Жасанды интеллект (gpt-oss:117b) сіздің `train.py` кодыңызды Server-Sent Events (SSE) арқылы көз алдыңызды жазады.
* **Unsloth Интеграциясы:** Барлық генерацияланған скрипттер Unsloth кітапханасына оңтайландырылған (4-bit LoRA), бұл тіпті RTX 2050 сияқты қарапайым карталарда баптау жасауға мүмкіндік береді.
* **Автономды Пайплайн:** Идеядан дайын оқу скриптіне дейін — 60 секундтан аз уақыт.

## 🏗 Жүйе архитектурасы (Node-based Flow)
Біздің жүйе n8n сияқты заманауи low-code құралдарынан шабыт алған:
`User Input` ➜ `FastAPI Gateway` ➜ `Alem.plus Brain` ➜ `Live Script Generation` ➜ `Zero-Core Simulated Executor`

## 💻 Технологиялық стек
- **AI Core:** `gpt-oss` (117B) Alem.plus API арқылы.
- **Backend:** Python / FastAPI (Асинхронды стриминг).
- **Frontend:** Vanilla JS / Tailwind CSS (Cyber-monochrome Glassmorphism UI).
- **Деплой:** Ubuntu 24.04 Cloud Node-да тікелей эфирде.

---

## ⚠️ Хакатон қазыларына арналған ескертпе
Жобаның мүмкіндіктерін жоғары сапамен көрсету үшін:
1.  **REAL GENERATION:** AI Агент және код генерациясы логикасы **100% жұмыс істеп тұр**. "Live Stream" терезесіндегі Python коды нақты уақытта сіздің сұранысыңызға сай жасалады.
2.  **SIMULATED EXECUTION:** "System Output" терминалы GPU кластерін бөлу мен оқыту қадамдарын симуляциялайды. Генерацияланған `train_generated.py` — нақты жұмыс істейтін скрипт, бірақ демо мақсатында физикалық оқыту процесі өткізіліп жіберіледі.

---

## 🚀 Жұмысты бастау (Local Node)

1.  **Репозиторийді көшіру:**
    ```bash
    git clone [https://github.com/Ernwr124/ProjectZero-tuner-edition.git](https://github.com/Ernwr124/ProjectZero-tuner-edition.git)
    cd ProjectZero-tuner-edition
    ```
2.  **Ортаны баптау:**
    `.env` файлын ашып, Alem API кілтін енгізіңіз:
    ```text
    ALEM_API_KEY=your_key_here
    ```
3.  **Орнату және іске қосу:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```

---

### 🔗 Жоба туралы
ProjectZero (Tuner Edition) — бұл **ProjectZero AI** экожүйесінің арнайы модулі.

**Қуаттандырушы: [ProjectZero ai](https://www.pzero.kz)** *(Қазақстандағы vibe coding сервисі)*
