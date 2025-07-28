## 📝 Approach Explanation – CHALLENGE_1A

The goal of this project is to extract a clean, structured outline from any given PDF document. This outline includes the inferred document title, as well as hierarchical headings (H1 and H2) with their corresponding page numbers. The entire pipeline is fully offline, lightweight, and runs efficiently inside a Docker container — meeting all challenge constraints related to runtime, memory, and model size.

---

### 🔍 Problem Understanding

Many documents — manuals, reports, forms, and certifications — have clear visual structures but lack an embedded table of contents or headings metadata. Manually identifying important sections is slow and error-prone. This solution helps by automatically extracting title and heading structures from raw PDF documents using layout-based heuristics.

The input is a folder containing PDF files.  
The output is a set of `.json` files containing the title and structured outline of each PDF.

---

### 🧱 Methodology

Our pipeline consists of four main stages:

#### 1. **PDF Parsing**

We use the `PyMuPDF (fitz)` library to extract structured data from each PDF. For every line in the document, we gather:
- Font size
- Font name (to infer boldness)
- Text content
- Y-position on the page
- Page number

This allows us to distinguish between body text and headings using visual cues.

#### 2. **Heading Detection**

We compute the most common font size, which typically represents body text. Then, based on relative size:
- Text with font size ≥ common size + 3 is marked as **H1**
- Text with font size ≥ common size + 1 is marked as **H2**
- Others are ignored

We also apply filters to avoid noise like very short lines, numbers, or symbol-only text.

#### 3. **Title Inference**

The title is extracted from the first page as the largest line of text that is meaningful and long enough. This heuristic captures common title placements accurately.

#### 4. **Output Formatting**

The results are saved as structured JSON in the format:

```json
{
  "title": "Document Title",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "Overview", "page": 2 }
  ]
}
