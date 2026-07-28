import fitz
def extract_pdf_text(pdf_path:str) -> str:
    document = fitz.open(pdf_path) #fitz.ope the document 
    text = "" #create the empty string 
    for page in document: 
        text += page.get_text() #get.text() will add text into empty string 

    document.close()

    return text 
