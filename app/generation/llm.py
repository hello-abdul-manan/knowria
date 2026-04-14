from groq import Groq
from app.core.config import GROQ_API_KEY

# Initialize groq client
client = Groq(api_key=GROQ_API_KEY)

def generate_answer(prompt: str):
    """Generate an AI response using Groq."""

    # Call Groq chat completion API
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    # Return generated text response
    return response.choices[0].message.content
