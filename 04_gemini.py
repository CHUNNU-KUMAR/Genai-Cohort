from google import genai

client = genai.Client(api_key='AIzaSyDx5qBaEXhc5S4sviOPzUp6Fu6BPiiM-mI')

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents = [
    "What is the meaning of life?",
    "What is the purpose of existence?",
    "How do I bake a cake?",
]

)

print(response.text)