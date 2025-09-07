from src.core.orchestrator import Orchestrator

def test_pipeline():
    orch = Orchestrator("data/nutrition.csv")
    state = orch.run(menu_text="Idly\nPuri\nChicken curry", preferences={"diet": "veg"})
    assert "Idly" in state.menu_items
    assert "Puri" in state.nutrition_data
    print("✅ Pipeline works")
