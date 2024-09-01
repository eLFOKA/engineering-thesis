import pymupdf  # PyMuPDF

def extract_text_from_pdf(pdf_path):

    document = pymupdf.open(pdf_path)

    pages_text = []
    
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text = page.get_text()
        pages_text.append(text)
    
    return pages_text

def save_text_to_files(pages_text, output_dir):
    import os
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    for i, text in enumerate(pages_text):
        with open(f"{output_dir}/page_{i+1}.txt", "w", encoding="utf-8") as file:
            file.write(text)

def main():
    pdf_path = "C:\\Users\\Maks\\Documents\\GitHub\\engineering-thesis\\Scripts\\some_file.pdf"
 
    output_dir = "output_texts" 
    
    pages_text = extract_text_from_pdf(pdf_path)
    save_text_to_files(pages_text, output_dir)
    print(f"Text from {pdf_path} has been extracted and saved in {output_dir}")

if __name__ == "__main__":
    main()
