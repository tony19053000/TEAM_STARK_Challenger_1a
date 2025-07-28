import json
import os
from formatter import generate_output

from heading_detector import detect_headings
from pdf_parser import extract_pdf_elements

INPUT_DIR = "input"
OUTPUT_DIR = "output"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in os.listdir(INPUT_DIR):
        if not filename.lower().endswith(".pdf"):
            continue

        pdf_path = os.path.join(INPUT_DIR, filename)
        print(f"Processing: {filename}")

        try:
            elements = extract_pdf_elements(pdf_path)
            title, outline = detect_headings(elements)
            output_data = generate_output(title, outline)

            output_filename = os.path.splitext(filename)[0] + ".json"
            output_path = os.path.join(OUTPUT_DIR, output_filename)

            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(output_data, f, indent=4, ensure_ascii=False)

            print(f"✓ Done: {output_filename}")
        except Exception as e:
            print(f"✗ Error in {filename}: {e}")


if __name__ == "__main__":
    main()
