import pandas as pd
from src.agents.menu_ocr import MenuOCRAgent
from src.agents.nutrition import NutritionAgent
from src.agents.variety import MealPreferenceAgent
from src.agents.preference import PreferenceAgent
from src.core.state import State

class Orchestrator:
    def __init__(self, dataset_path):
        self.state = State()
        self.menu_agent = MenuOCRAgent()
        self.nutrition_agent = NutritionAgent(dataset_path)
        nutrition_df = pd.read_csv(dataset_path)
        self.variety_agent = MealPreferenceAgent(nutrition_df)
        self.preference_agent = PreferenceAgent()

    def run(self, menu_text=None, image_path=None, preferences=None):
        self.state.menu_items = self.menu_agent.extract_menu(menu_text, image_path)

        for dish in self.state.menu_items:
            self.state.nutrition_data[dish] = self.nutrition_agent.get_nutrition(dish)

        self.state.diversity_report = self.variety_agent.check_variety(self.state.menu_items)

        if preferences:
            self.state.preferences = self.preference_agent.filter_menu(
                self.state.menu_items, preferences
            )

        return self.state
