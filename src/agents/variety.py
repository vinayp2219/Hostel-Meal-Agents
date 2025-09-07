import pandas as pd

class MealPreferenceAgent:
    def __init__(self, nutrition_df: pd.DataFrame):
        self.nutrition_df = nutrition_df

        # Tag some dishes by known spice or heaviness
        self.spice_tags = {
            "chole bhature": "heavy",
            "biryani": "spicy",
            "idli": "light",
            "dosa": "light",
            "paratha": "heavy",
            "puri": "heavy",
            "salad": "light",
            "fries": "heavy",
            "chicken tikka": "spicy"
        }
    def check_variety(self, menu_items: list, nutrition_data: dict = None):
        if nutrition_data is None:
            nutrition_data = {}

        categories = set()
        for item in menu_items:
            cat = self.classify_item(item, nutrition_data.get(item.lower(), {}))
            categories.add(cat)

        return {
            "total_items": len(menu_items),
            "variety": len(categories),
            "categories": list(categories)
        }


    def classify_item(self, item: str, nutrition: dict):
        item_lower = item.lower()

        if item_lower in self.spice_tags:
            return self.spice_tags[item_lower]

        calories = nutrition.get("Calories (kcal)", 0)
        sodium = nutrition.get("Sodium (mg)", 0)

        if calories < 150:
            return "light"
        elif calories > 300:
            return "heavy"
        elif sodium > 400:
            return "spicy"
        else:
            return "moderate"

    def analyze_preferences(self, menu_items: list, nutrition_data: dict, preference: str):
        matched, not_matched = [], []
        for item in menu_items:
            cat = self.classify_item(item, nutrition_data.get(item, {}))
            (matched if preference == cat else not_matched).append(item)

        return {
            "preference": preference,
            "matched": matched,
            "not_matched": not_matched
        }
