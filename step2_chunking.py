from utils.pdf_reader import extract_pdf_text
from utils.chunking import split_text

text = extract_pdf_text('sample.pdf')
chunks = split_text(text)

print("=" * 60)
print(f"Total Characters : {len(text)}")
print(f"Total Chunks     : {len(chunks)}")
print("=" * 60)

# Show first chunk
print("\nFirst Chunk:\n")
print(chunks[0])

print("\n" + "=" * 60)

# Show last chunk
print("\nLast Chunk:\n")
print(chunks[-1])