from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()

client = genai.Client()
text = "Eiffel Tower is in Paris and is a famous landmark, it is 324 meters tall"

response= client.models.embed_content(
contents= text,
model="gemini-embedding-001"
)
print("Vector Embeddings:", response.embeddings[0].values)
