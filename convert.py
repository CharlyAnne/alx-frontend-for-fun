import markdown2

with open('test.md', 'r') as f:
    text = f.read()
    html = markdown2.markdown(text)

with open('test.md', 'w') as f:
    f.write(html)
