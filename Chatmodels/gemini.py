from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

print("API key loaded:", bool(api_key))

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    google_api_key=api_key
)

response = model.invoke("Who is MS Dhoni?")

print(response.content)
