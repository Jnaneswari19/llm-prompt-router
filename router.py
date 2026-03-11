import os
from openai import OpenAI
from dotenv import load_dotenv
from prompts import PROMPTS

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def route_and_respond(message: str, intent: str):

    if intent == "unclear":

        return "I'm not sure what you need. Are you asking about coding, data analysis, writing improvement, or career advice?"

    system_prompt = PROMPTS.get(intent)

    try:

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0.7
        )

        return response.choices[0].message.content

    except Exception:

        return "Sorry, something went wrong while generating the response."