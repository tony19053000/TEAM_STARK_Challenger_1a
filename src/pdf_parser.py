import fitz  # PyMuPDF


def extract_pdf_elements(pdf_path):
    doc = fitz.open(pdf_path)
    elements = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue

            for line in block["lines"]:
                line_text = ""
                sizes = []
                fonts = []

                for span in line["spans"]:
                    line_text += span["text"].strip() + " "
                    sizes.append(span["size"])
                    fonts.append(span["font"])

                text = line_text.strip()
                if not text:
                    continue

                avg_size = round(sum(sizes) / len(sizes), 1)
                font_name = fonts[0]
                is_bold = "Bold" in font_name or "bold" in font_name

                elements.append({
                    "text": text,
                    "size": avg_size,
                    "font": font_name,
                    "bold": is_bold,
                    "y": round(line["bbox"][1], 2),
                    "page": page_num + 1,
                })

    return elements
