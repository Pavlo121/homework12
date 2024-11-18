import re

def contains_code_format(text):
    # вираз для формату AB12CD34
    pattern = r'\b[A-Z]{2}\d{2}[A-Z]{2}\d{2}\b'
    return bool(re.search(pattern, text))

texts = [
    "У цьому тексті є код AB12CD34.",
    "Тут немає потрібного формату.",
    "Інший приклад: XY99AB00.",
    "Код помилковий: AB123CD4."
]

for t in texts:
    print(f"Текст: {t}")
    print(f"Містить код формату AB12CD34? {'Так' if contains_code_format(t) else 'Ні'}")
    print("-" * 40)
