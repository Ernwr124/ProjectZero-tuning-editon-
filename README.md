# ⚡️ ProjectZero (Tuner Edition)
> **LLM модельдерін автономды баптауға (Fine-Tuning) арналған Vibe-driven MLOps платформасы**

[![Status](https://img.shields.io/badge/Status-Live_MVP-brightgreen)](http://178.88.115.250)
[![Brain](https://img.shields.io/badge/AI_Brain-gpt--oss:117b-white)](https://alem.ai)
[![Framework](https://img.shields.io/badge/Engine-Unsloth-green)](https://github.com/unslothai/unsloth)
[![Backend](https://img.shields.io/badge/Stack-FastAPI_%7C_SSE-black)](https://fastapi.tiangolo.com/)

---

## 🌪 Философиясы: Vibe-driven MLOps
Үлкен тілдік модельдерді (LLM) баптау — өте күрделі процесс. **ProjectZero (Tuner Edition)** бұл ережелерді өзгертеді. "Vibe Coding" философиясына негізделген платформа әзірлеушілерге өз мақсаттарын қарапайым тілде сипаттауға мүмкіндік береді. Біздің автономды агент модельді талдап, нақты уақыт режимінде дайын оқу скриптін (train.py) жазып береді.

[**🌐 Live Demo-ны көру (Server IP)**](http://178.88.115.250)

---

## 🏗 Vision & Engineering Truth (Қазылар назарына)

**Бұл жоба тек визуалды симуляция емес, бұл — нақты DeepTech PoC.**

1.  **Нақты код генерациясы:** Платформадағы "Code Stream" — алдын ала дайындалмаған. `gpt-oss` моделі сіздің промптыңызды архитектуралық тұрғыдан талдап, **дәл қазір орындауға дайын** Python кодын нақты уақытта жасайды.
2.  **Технологиялық басымдық:** Біздің агент жазған кодтар **Unsloth** пен **4-bit quantization** технологиясына негізделген. Бұл — оқыту процесін 2 есе жылдамдатып, видеожадты үнемдеуге мүмкіндік береді.
3.  **Simulation vs Reality:** Демо кезіндегі "System Output" (GPU оқыту қадамдары) симуляция түрінде көрсетілген. Себебі — нақты H100 кластерін жалға алу үлкен ресурстарды талап етеді. Алайда, генерацияланған `train_generated.py` файлы кез келген қуатты серверде дәл қазір іске қосуға 100% дайын.
4.  **Біздің мақсат:** ProjectZero-ны толық циклді MLOps экожүйесіне айналдырып, Қазақстаннан шыққан технологиямен әлемдік AI гиганттарымен бәсекелесу!

---

## 🛠 Мүмкіндіктері
* **Live Hub Validation:** HuggingFace API-мен интеграция (модельдер мен датасеттерді тексеру).
* **Real-time Code Streaming:** Жасанды интеллект сіздің `train.py` кодыңызды SSE арқылы көз алдыңызды жазады.
* **Unsloth Интеграциясы:** Барлық скрипттер RTX 2050 сияқты қарапайым карталарда да жұмыс істеуге оңтайландырылған.
* **Автономды Пайплайн:** Идеядан дайын оқу скриптіне дейін — 60 секунд.

---

## 💻 Технологиялық стек
- **AI Core:** `gpt-oss` (117B) Alem.plus API арқылы.
- **Backend:** Python / FastAPI (Асинхронды стриминг).
- **Frontend:** Vanilla JS / Tailwind CSS (Cyber-monochrome Glassmorphism UI).
- **Деплой:** Ubuntu 24.04 Cloud Node (Live).

---

## 🚀 Жұмысты бастау (Local Node)

1.  **Репозиторийді көшіру:**
    ```bash
    git clone [https://github.com/Ernwr124/ProjectZero-tuner-edition.git](https://github.com/Ernwr124/ProjectZero-tuner-edition.git)
    cd ProjectZero-tuner-edition
    ```
2.  **Ортаны баптау:**
    `.env` файлын ашып, Alem API кілтін енгізіңіз.
3.  **Орнату және іске қосу:**
    ```bash
    pip install -r requirements.txt
    uvicorn main:app --reload
    ```

---

### 🔗 Жоба туралы
ProjectZero (Tuner Edition) — бұл **ProjectZero AI** экожүйесінің арнайы модулі.

**Қуаттандырушы: [ProjectZero ai](https://www.pzero.kz)** *(Қазақстандағы vibe coding сервисі)*
