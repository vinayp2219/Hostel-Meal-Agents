class PreferenceAgent:
    NON_VEG_KEYWORDS = ["chicken", "mutton", "lamb", "fish", "prawn", "egg", "beef", "pork"]
    VEGAN_RESTRICTED = ["paneer", "cheese", "milk", "yogurt", "ghee"] + NON_VEG_KEYWORDS

    def filter_menu(self, items, preferences):
        allowed = []
        restricted = []
        diet_type = preferences.get("diet", "").lower()

        for dish in items:
            dish_lower = dish.lower()
            is_restricted = False

            # --- Vegetarian ---
            if diet_type == "veg":
                if any(keyword in dish_lower for keyword in self.NON_VEG_KEYWORDS):
                    restricted.append(dish)
                    is_restricted = True

            # --- Vegan ---
            elif diet_type == "vegan":
                if any(keyword in dish_lower for keyword in self.VEGAN_RESTRICTED):
                    restricted.append(dish)
                    is_restricted = True

            # --- Non-Vegetarian ---
            elif diet_type == "non-veg":
                # A dish is restricted if it does NOT contain any non-veg keyword
                if not any(keyword in dish_lower for keyword in self.NON_VEG_KEYWORDS):
                    restricted.append(dish)
                    is_restricted = True

            # If the dish wasn’t restricted, it’s allowed
            if not is_restricted:
                allowed.append(dish)

        return {
            "allowed": allowed,
            "restricted": restricted,
            "preferences": preferences
        }
