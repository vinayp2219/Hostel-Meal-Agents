import sys
import os
# --- START OF FIX ---
# Add the project's root directory to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# --- DEBUGGING LINES ---
print("--- Project root added to path:", project_root)
print("---")
# --- END OF FIX ---

import streamlit as st
from src.core.orchestrator import Orchestrator
# The 'os' library is needed to handle file paths for the upload feature


DATASET_PATH = "data/nutrition.csv"

# --- Cached Function ---
@st.cache_resource
def load_orchestrator(path):
    """Loads and caches the Orchestrator to prevent reloading the dataset."""
    print("Loading Orchestrator and dataset for the first time...")
    return Orchestrator(path)

# --- Streamlit UI ---
st.title("🏫 Hostel Food Multi-Agent System")

menu_text = st.text_area("Enter Mess Menu (paste from poster or text):")

st.write("--- OR ---")

uploaded_file = st.file_uploader("Upload a menu image:", type=["png", "jpg", "jpeg"])

preferences = st.radio("Diet Preference:", ["none", "veg", "non-veg", "vegan"])

if st.button("Analyze Menu"):
    orch = load_orchestrator(DATASET_PATH)
    prefs = {} if preferences == "none" else {"diet": preferences}
    
    image_path = None
    # --- Logic to handle file upload ---
    if uploaded_file is not None:
        # To process the image, we need to save it to a temporary path
        # Create a directory for uploads if it doesn't exist
        os.makedirs("uploads", exist_ok=True)
        image_path = os.path.join("uploads", uploaded_file.name)
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Clear the text area if an image is uploaded
        menu_text = ""
    
    if not menu_text and not image_path:
        st.warning("Please enter a menu in the text box or upload an image.")
    else:
        # Run the analysis
        state = orch.run(menu_text=menu_text, image_path=image_path, preferences=prefs)

        # --- Display Results ---
        st.subheader("✅ Extracted Menu Items")
        st.write(state.menu_items)

        st.subheader("🍏 Nutrition Data")
        st.json(state.nutrition_data)

        st.subheader("📊 Variety Report")
        st.write(state.diversity_report)

        if prefs:
            st.subheader("🍴 Preference-Based Filtering")
            st.json(state.preferences)