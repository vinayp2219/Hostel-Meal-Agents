# Hostel Food Multi-Agent (OCR → Nutrition → Variety → Preference)

## Problem Statement
Hostel students face repetitive menus, limited choices, and unbalanced nutrition. Menus are often posted as banners, making it hard to track and personalize choices. This project uses a multi-agent AI system to parse menu posters via OCR, analyze nutrition, detect variety, and generate personalized meal suggestions aligned to health goals and preferences.

## Why Multi-Agent
- Menu OCR Agent extracts and structures menu from images.
- Nutrition Agent maps items to calories, protein, carbs, fat.
- Variety Agent detects repetition and monotony.
- Preference Agent personalizes recommendations per goal.
Agents specialize and collaborate to produce a plan better than any single step.

## Architecture
Pipeline: OCR → Parse → Nutrition Map → Variety → Preference Selection → Totals.
Coordinator: `Orchestrator` manages shared state and agent calls.

## Tools
- OCR: pytesseract (offline)
- Orchestration: pure Python state machine
- Validation: pydantic models
- UI: Streamlit
- Data: `data/nutrition.csv` (Indian hostel foods)

## LLM Selection
Ideal: GPT-4o or Claude 3.5 for richer reasoning and substitutions.
Free options: Llama 3.1/Mistral via Hugging Face or local (ollama).
This demo is offline and deterministic; LLMs can enhance suggestions in future.

## Setup
1) Install Tesseract (system)
2) `pip install -r requirements.txt`
3) `streamlit run app/streamlit_app.py`

## Usage
Upload a menu image or paste menu text. Select goal, preference, veg,vegan,non-veg or none. View parsed items, nutrition, variety, and a personalized plan with macro totals.

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
Nutrition values are approximate and limited to provided items. OCR quality depends on image clarity and language. Future work: LLM-powered substitutions, weekly planning, and recipe-level macros.
