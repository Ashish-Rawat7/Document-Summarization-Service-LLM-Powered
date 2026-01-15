def build_prompt(text: str, style: str) -> str:
    if style == "brief":
        instruction = "Summarize the document in 2–3 concise sentences."
    elif style == "bullet":
        instruction = "Summarize the document using clear bullet points."
    else:
        instruction = "Provide a detailed, multi-paragraph summary."

    return f"""{instruction}

Document:
{text}
"""
