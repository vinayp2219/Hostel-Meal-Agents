import easyocr

class MenuOCRAgent:
    def __init__(self, lang="en"):
        self.reader = easyocr.Reader([lang])

    def extract_menu(self, text=None, image_path=None):
        items = []
        if text:
            items = [line.strip() for line in text.split("\n") if line.strip()]
        elif image_path:
            try:
                results = self.reader.readtext(image_path, detail=0)
                items = [line.strip() for line in results if line.strip()]
            except Exception as e:
                print(f"Error processing image {image_path}: {e}")
                return []
        return items
