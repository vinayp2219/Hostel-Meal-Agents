# Hostel Food Multi-Agent (OCR → Nutrition → Variety → Preference)

## Problem Statement
Repetitive menus, few choices, and poor nutrition are issues hostel students experience. Menus are frequently announced on banners, which is difficult to monitor and customize options. This project leverages a multi-agent AI framework for parsing menu posters through OCR, nutrition analysis, variety detection, and the creation of tailored meal recommendations based on health targets and preferences.

## Why Multi-Agent
- Menu OCR Agent extracts and organizes menu from images.
- Nutrition Agent maps food to calories, protein, carbs, fat.
- Variety Agent identifies repetition and boredom.
- Preference Agent tailors recommendations per target.
Agents specialize and interact to create a plan greater than any individual step.

## Architecture
Pipeline: OCR → Parse → Nutrition Map → Variety → Preference Selection → Totals.
Coordinator: `Orchestrator` coordinates shared state and agent invocation.

## Tools
- OCR: pytesseract (offline)
- Orchestration: pure Python state machine
- Validation: pydantic models
- UI: Streamlit
- Data: `data/nutrition.csv` (Indian hostel foods)
- Taken help from chatGPT and online for getting a better response
- The dataset i'm using here is a copy of kaggle dataset named indian food nutrional values

## LLM Selection
Ideal: GPT-4o or Claude 3.5 for more elaborate reasoning and substitutions.
Free options: Llama 3.1/Mistral via Hugging Face or local (ollama).
This demo is offline and deterministic; LLMs can improve suggestions in the future.

## Setup
1) Install Tesseract (system)
2) `pip install -r requirements.txt`
3) `streamlit run app/streamlit_app.py`

## Usage
Upload a menu picture or copy menu. Choose goal, preference, veg. Display parsed items, nutrition, variety, and a customized plan with macro totals.

## Repo Structure

""
hostel-food-agents/
  README.md
  requirements.txt
  data/
    nutrition.csv
  src/
    core/
      state.py
      orchestrator.py
    agents/
      menu_ocr.py
      nutrition.py
      variety.py
      preference.py
  app/
    streamlit_app.py
  tests/
    test_pipeline.py
""

## Limitations
Nutrition values are rough and restricted to items provided. Quality of OCR is based on image quality and language. Future work: LLM-driven substitutions, week planning, and recipe-level macros.
