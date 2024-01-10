
from PyPDF2 import PdfReader

reader = PdfReader("sample2.pdf")
"""
no_of_pages=len(reader.pages)
page=reader.pages[0]
text=page.extract_text((0,90))

print(f"Number of pages -- {no_of_pages}")
print(f"Text ---> {text}")
"""
print(reader.documentInfo) ### gives info 
### diff diff functions 
print(reader.getNumPages())   ## no of pages
print(reader.getPage(0).extractText())  ## takes 0th page and extract text

###--by for loop we can extract text from many pages by applying above cmd
print("~"*30)
print(reader.getPage(0).getContents())




