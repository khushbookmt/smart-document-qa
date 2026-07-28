from utils.pdf_reader import extract_pdf_text

pdf_path ='sample.pdf'

text =extract_pdf_text(pdf_path)

print("=" * 50)
print(text[:1000])
print("=" * 50)

print(f"\nTotal Characters : {len(text)}")