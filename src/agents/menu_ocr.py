import pytesseract
import cv2

class MenuOCRAgent:
    def extract_menu(self, text=None, image_path=None):
        items = []
        if text:
            items = [line.strip() for line in text.split("\n") if line.strip()]
        elif image_path:
            image = cv2.imread(image_path)
            # This check is excellent!
            if image is None:
                print(f"Error: Could not read image from path: {image_path}")
                return [] 

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            extracted_text = pytesseract.image_to_string(gray)
            items = [line.strip() for line in extracted_text.split("\n") if line.strip()]
        
        # Add this return statement
        return items