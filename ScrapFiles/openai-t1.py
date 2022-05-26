import openai
from api_secrets import API_KEY

openai.api_key = API_KEY

prompt = """Translate this into 1.French, 2.Spanish and 3.Japanese:

What rooms do you have available?
1."""

responese = openai.Completion.create(
    engine="text-davinci-002", prompt=prompt, max_tokens=6)

print(responese)

filteredResponse = responese["choices"][0]["text"].strip("\n\n")
print(f"\n[OpenAI]: {filteredResponse}")
