from google import genai
from google.genai import types
client = genai.Client(api_key='AIzaSyCTY-6evaMbWR_e0whGTAfLuOc4CI9AoIY')
response = client.models.generate_content(
    model='gemini-2.5-flash', contents='Why is the sky blue?'
)
print(response.text)