class Classifier:
    def classify(self, material):
        print(f"[분류기] '{material}' 분류 중...")
        if material in ["plastic", "paper", "metal"]:
            return material
        return "unknown"
