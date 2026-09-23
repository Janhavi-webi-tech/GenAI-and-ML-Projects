from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

print("Groq API key loaded:", bool(os.getenv("GROQ_API_KEY")))

model = ChatGroq(
    model="openai/gpt-oss-20b",
    groq_api_key=os.getenv("GROQ_API_KEY")
)

response = model.invoke("Who is Gen AI?")

print(response.content)
