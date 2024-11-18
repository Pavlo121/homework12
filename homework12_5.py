import re

def html_tags(text):
    pattern = r'<[^>]*>'
    return re.sub(pattern, '', text)

html_text = '''
<h1>Привіт</h1>
<p>Це <b>тестове</b> текст із <a href="https://example.com">посилання</a>.</p>
'''

clean_text = html_tags(html_text)
print(clean_text)
