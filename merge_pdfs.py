import os
from PyPDF2 import PdfReader, PdfWriter


# Put all the PDF files in the order you want them merged
pdf_files = [
    "Alternative Investments.pdf",
    "Corporate_Issuer.pdf",
    "Derivatives.pdf",
    "Economics.pdf",
    "Equity.pdf",
    "Ethics.pdf",
    "Financial_Statement_Analysis.pdf",
    "Fixed_Income.pdf",
    "Portfolio_Management.pdf",
    "Quantitative_Analysis.pdf"
]

output_file = "cfa_book.pdf"


def merge_pdfs(input_paths, output_path):
    if not input_paths:
        raise ValueError("No PDF files were provided.")

    writer = PdfWriter()

    for pdf_path in input_paths:
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"File not found: {pdf_path}")

        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)

    with open(output_path, "wb") as output_file_handle:
        writer.write(output_file_handle)

    print(f"Merged {len(input_paths)} PDF files into: {output_path}")


if __name__ == "__main__":
    try:
        merge_pdfs(pdf_files, output_file)
    except Exception as e:
        print(f"Error: {e}")
