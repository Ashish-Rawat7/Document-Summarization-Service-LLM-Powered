from google import genai
from google.genai.types import GenerateContentConfig
from config import GEMINI_API_KEY, GEMINI_MODEL, DEBUG
from prompt import build_prompt
import time


class Summarizer:
    def __init__(self):
        self.client = genai.Client(api_key=GEMINI_API_KEY)
        self.model = GEMINI_MODEL

    def _split_text(self, text, chunk_size=1200):
        words = text.split()
        for i in range(0, len(words), chunk_size):
            yield " ".join(words[i:i + chunk_size])

    def _generate(self, prompt, max_tokens=1200):
        last_error = None

        for attempt in range(3):
            try:
                response = self.client.models.generate_content(
                    model=self.model,
                    contents=[{"role": "user", "parts": [{"text": prompt}]}],
                    config=GenerateContentConfig(
                        temperature=0.4,
                        max_output_tokens=max_tokens,
                    ),
                )

                if response:
                    # Primary response
                    if hasattr(response, "text") and response.text:
                        return response.text.strip()

                    # Fallback parsing
                    if hasattr(response, "candidates"):
                        return response.candidates[0].content.parts[0].text.strip()

            except Exception as e:
                last_error = str(e)
                if DEBUG:
                    print(f"[Retry {attempt+1}] {last_error}")
                time.sleep(2)

        raise RuntimeError(f"AI failed after retries: {last_error}")

    def summarize(self, text: str, style="brief") -> str:
        if not text.strip():
            raise ValueError("Empty input")

        chunks = list(self._split_text(text))

        partial_summaries = []

        # Step 1: Summarize each chunk
        for chunk in chunks:
            prompt = build_prompt(chunk, style)
            summary = self._generate(prompt)
            partial_summaries.append(summary)

        # Step 2: Combine intelligently (IMPORTANT)
        final_prompt = f"""
You are an expert summarizer.

Combine the following summaries into ONE complete and detailed summary.

Rules:
- DO NOT shorten the content
- Expand where needed
- Maintain structure
- Ensure full coverage of all points

SUMMARIES:
{" ".join(partial_summaries)}
"""

        max_tokens = 2000 if style == "notes (1500+ words)" else 1200

        return self._generate(final_prompt, max_tokens=max_tokens)