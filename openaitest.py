# openaitest.py
import openai
from config import apikey

openai.api_key = apikey

def ai_completion(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=256,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response['choices'][0]['text'])

if __name__ == '__main__':
    ai_completion("Write an email to my boss for resignation?")
