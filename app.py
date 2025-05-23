import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2023-05-15",
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
)

def chat_com_ia(mensagem):
    resposta = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_MODEL"),
        messages=[
            {"role": "system", "content": "Você é um assistente útil."},
            {"role": "user", "content": mensagem}
        ]
    )
    return resposta.choices[0].message.content

if __name__ == "__main__":
    print("🤖 Bem-vindo ao Chatbot com Azure OpenAI!")
    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ["sair", "exit"]:
            break
        resposta = chat_com_ia(pergunta)
        print("IA:", resposta)