from collections import Counter

def detect_headings(elements):
    font_sizes = [e["size"] for e in elements]
    common_size = Counter(font_sizes).most_common(1)[0][0]

    title = ""
    for e in elements:
        if e["page"] == 1 and len(e["text"]) > 10 and e["size"] > common_size:
            title = e["text"]
            break

    outline = []

    for elem in elements:
        text = elem["text"]
        if not is_valid_heading(text):
            continue

        if elem["size"] >= common_size + 3:
            level = "H1"
        elif elem["size"] >= common_size + 1:
            level = "H2"
        else:
            continue

        outline.append({
            "level": level,
            "text": text.strip(),
            "page": elem["page"]
        })

    return title.strip(), outline

def is_valid_heading(text):
    text = text.strip()
    if len(text) < 3:
        return False
    if text.replace(".", "").isdigit():
        return False
    if all(char in " .:-–—•*" for char in text):
        return False
    if len(text.split()) > 30:
        return False
    return True
