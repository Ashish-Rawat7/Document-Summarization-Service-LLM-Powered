from google import genai
from google.genai.types import GenerateContentConfig
from config import GEMINI_API_KEY, GEMINI_MODEL


class Summarizer:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = GEMINI_MODEL

    def summarize(self, text: str) -> str:
        if not text or not text.strip():
            raise ValueError("Empty input")

        # HARD CAP INPUT (critical)
        text = text.strip()[:700]

        prompt = f"""
Summarize the following content in 3 to 4 clear sentences.
Write only factual content. Do not mention the text itself.

{text}
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
            config=GenerateContentConfig(
                temperature=0.3,
                max_output_tokens=250,
            ),
        )

        return response.text.strip() if response.text else ""
