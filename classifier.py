import json
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def classify_intent(message: str):

    prompt = f"""
Your task is to classify the user's intent.

Choose ONE label from:
code, data, writing, career, unclear

Return ONLY a JSON object with this format:

{{
 "intent": "label",
 "confidence": 0.0
}}

User message:
{message}
"""

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        text = response.choices[0].message.content.strip()

        result = json.loads(text)

        return result

    except Exception:

        return {
            "intent": "unclear",
            "confidence": 0.0
        }