from fastapi import FastAPI
import ollama

def generate(prompt: str):
    response = ollama.chat(
        model="llama3.2",
        messages=[{
            "role": "user",
            "content": prompt,
        }]
    )
    print(response["message"]["content"])
    return response["message"]["content"]