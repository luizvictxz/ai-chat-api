import os

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from strands import Agent
from strands.models.ollama import OllamaModel
from strands_tools import calculator

# Carrega as variáveis de ambiente
load_dotenv()

# Configura o modelo do ollama
ollama_model = OllamaModel(
    host=os.getenv("OLLAMA_BASE_URL"),
    model_id=os.getenv("LLM_MODEL"),
)


class Message(BaseModel):  # Como o  FastAPI irá receber o json
    message: str


# Inicialização do app/agent
app = FastAPI()
agent = Agent(model=ollama_model, tools=[calculator], system_prompt=(
    "Você é um assistente útil. "
    "Responda normalmente perguntas gerais. "
    "Use a ferramenta calculator apenas quando a pergunta envolver cálculos matemáticos explícitos."
))


@app.post("/chat")  # Endpoint da api
def get_request(payload: Message):
    result = agent(payload.message)
    final_text = result.message["content"][0]["text"]
    return {"response": final_text}
