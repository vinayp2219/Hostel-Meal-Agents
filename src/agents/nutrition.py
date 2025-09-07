import pandas as pd
import sys

class NutritionAgent:
    """
    Loads a nutrition dataset and provides nutritional information for dishes.
    """
    def __init__(self, dataset_path):
        # --- Error Handling for File Loading ---
        try:
            self.df = pd.read_csv(dataset_path)
        except FileNotFoundError:
            print(f"FATAL ERROR: The dataset file at '{dataset_path}' was not found.")
            sys.exit(1) # Exit the program if data can't be loaded

        # --- Error Handling for Missing Columns ---
        # Define the columns that are essential for the agent to function
        required_columns = [
            "Dish Name", "Calories (kcal)", "Carbohydrates (g)", "Protein (g)", 
            "Fats (g)", "Free Sugar (g)", "Fibre (g)", "Sodium (mg)", 
            "Calcium (mg)", "Iron (mg)", "Vitamin C (mg)", "Folate (µg)"
        ]
        
        # Check if all required columns are present in the loaded DataFrame
        if not all(col in self.df.columns for col in required_columns):
            print("FATAL ERROR: The CSV file is missing one or more required columns.")
            sys.exit(1)

    def get_nutrition(self, dish_name):
        """
        Finds nutritional data for a dish, prioritizing exact matches.
        """
        # --- Improved Matching Logic ---
        # 1. First, try to find an exact (case-insensitive) match
        exact_match = self.df[self.df["Dish Name"].str.lower() == dish_name.lower()]

        if not exact_match.empty:
            match = exact_match
        else:
            # 2. If no exact match, fall back to a partial (contains) search
            match = self.df[self.df["Dish Name"].str.contains(dish_name, case=False, na=False)]

        # --- Return Results ---
        if match.empty:
            return {"error": f"No nutritional info found for '{dish_name}'"}

        # Return the data from the first matched row
        row = match.iloc[0]
        return {
            "Calories (kcal)": row["Calories (kcal)"],
            "Carbohydrates (g)": row["Carbohydrates (g)"],
            "Protein (g)": row["Protein (g)"],
            "Fats (g)": row["Fats (g)"],
            "Free Sugar (g)": row["Free Sugar (g)"],
            "Fibre (g)": row["Fibre (g)"],
            "Sodium (mg)": row["Sodium (mg)"],
            "Calcium (mg)": row["Calcium (mg)"],
            "Iron (mg)": row["Iron (mg)"],
            "Vitamin C (mg)": row["Vitamin C (mg)"],
            "Folate (µg)": row["Folate (µg)"]
        }