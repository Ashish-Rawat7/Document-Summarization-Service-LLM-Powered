def build_prompt(text: str, style: str) -> str:
    if style == "brief":
        instruction = "Summarize in 4-6 sentences with clarity."
    elif style == "bullet":
        instruction = "Provide a detailed summary using structured bullet points."
    elif style == "notes (1500+ words)":
        instruction = "Create detailed structured notes (minimum 1200–1500 words). Cover all key concepts."
    else:
        instruction = "Provide a detailed, well-structured multi-paragraph summary."

    return f"""
You are an expert document summarizer.

{instruction}

Rules:
- Do NOT be too brief
- Cover ALL key ideas
- Expand important points
- Keep structure clean and readable

TEXT:
{text}
"""