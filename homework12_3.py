import re


def my_hashtags(text):
    # Знаходить усі хештеги у тексті
    pattern = r'#\w+'
    return re.findall(pattern, text)

text = '''
Привіт світ! #Python3 #щастя
 '''

hashtags = my_hashtags(text)
print(hashtags)



