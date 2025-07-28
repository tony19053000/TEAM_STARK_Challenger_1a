Approach Explanation
This project extracts a clean and structured outline from PDF files. The goal is to detect the document title and headings (H1 and H2) along with their page numbers. The solution is fully offline, lightweight, and runs inside a Docker container. It meets all challenge constraints: small size (under 200MB), fast runtime (under 10 seconds for 50 pages), and no GPU or internet required.

Method Used
1. Extracting Text and Layout
We use PyMuPDF (fitz) to read and analyze the PDF content. This allows us to extract not just the text, but also the font size, font style (bold or not), position on the page, and page number. These properties help us later decide which lines are headings.

2. Detecting Headings
To identify headings, we first find the most common font size in the document, which is assumed to be the body text size. Then we apply simple rules:

If a line’s font size is much larger (+3 or more), we label it H1

If slightly larger (+1 or more), we label it H2

Other lines are ignored

We also ignore lines that are too short, only contain numbers or symbols, or are too long to be meaningful headings.

3. Getting the Title
The title is usually the largest line of text on the first page. We pick the first such line that’s long enough and larger than the body font. This gives a reliable title for most documents.

4. Generating Output
The result is saved in a structured JSON format like this:
{
  "title": "Document Title",
  "outline": [
    {"level": "H1", "text": "Section Name", "page": 1},
    {"level": "H2", "text": "Subsection", "page": 2}
  ]
}
This can be used for building a table of contents or easy navigation.

How to Use This Solution
Make sure Docker is installed on your system.

Place your .pdf files inside the input/ folder.

Open a terminal in the project directory and run:

To build the Docker image:

docker build -t pdf-outline-extractor .
or
docker run --rm -v "C:/full/path/to/input:/app/input" -v "C:/full/path/to/output:/app/output" pdf-outline-extractor

The extracted JSON files will appear in the output/ folder.

Summary
This solution uses font size and layout rules to find titles and headings. It does not rely on machine learning, making it fast and reliable. Everything runs inside a Docker container, making it portable and easy to use on any machine.
