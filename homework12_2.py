import re


def find_phone_numbers(text):
    # Знаходить усі телефонні номери у тексті.
    # вираз для телефонних номерів
    pattern = r'''
        \(?\d{3}\)?          
        [\s.-]?              
        \d{3}                
        [\s.-]?             
        \d{4}                
    '''
    return re.findall(pattern, text, re.VERBOSE)

text = """
Ось декілька номерів телефонів:
(123) 456-7890, 123-456-7890, 123.456.7890, and 1234567890.
Call us!
"""

numbers = find_phone_numbers(text)
print("Знайдені номери:", numbers)
