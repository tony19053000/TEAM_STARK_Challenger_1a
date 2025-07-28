def generate_output(title, outline):
    output = {"title": title.strip(), "outline": []}

    for entry in outline:
        output["outline"].append({
            "level": entry["level"],
            "text": entry["text"].strip(),
            "page": entry["page"]
        })

    return output
