from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyBKOgKFvkIxswiyKeOjwXbHGqEl_l6mUPs")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="O que é IA?"
)
print(response.text)
