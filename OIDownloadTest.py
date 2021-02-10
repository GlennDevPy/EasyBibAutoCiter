""" import requests
from tqdm import tqdm
for i in tqdm(range(100)):
    pass
f = requests.get("https://www.easybib.com/static/tag-example.docx", headers={
    "Referer": "https://www.easybib.com/project/style/mla8?id=5ef82109-e0b7-4c35-89d4-8359ac10dca9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36"
})
with open("bruh.docx", 'wb') as writefile:
    writefile.write(f.content)
 """
title = 's'
webtitle = 'dd'
authorF = 'f'
authorL = 'fff'
dD = '33'
dM = '31'
dY = '9202'

checklist = {
    "title": title,
    "webtitle": webtitle,
    "authorF": authorF,
    "authorL": authorL,
    "dD": dD,
    "dM": dM,
    "dY": dY,
} 




#figure out how to do indents lmao

#wont work until i figure out how to do hanging indents


from docx import Document
from docx.shared import Inches

worddoc = Document()
paragraph = worddoc.add_paragraph('')
paragraph.paragraph_format.left_indent = Inches(0.5)
paragraph.paragraph_format.first_line_indent = Inches(-0.5)
worddoc.save('left_indent.docx')

