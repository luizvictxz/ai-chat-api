# API de Chat com IA

### FastAPI • Strands Agents • Ollama


---

# Pré-requisitos

Instale os seguintes itens antes de rodar o projeto:

-   Python 3.12+
-   Pip e virtualenv
-   Ollama instalado no sistema  
     https://ollama.com/download

---

# Instalação — Passo a Passo

## 1️⃣ Clone o repositório

```bash
git clone https://github.com/luizvictxz/ai-chat-api.git
cd ai-chat-api
```

---

## 2️⃣ Crie e ative o ambiente virtual

```bash
python3 -m venv venv
source venv/bin/activate      # Linux/macOS
```

> No Windows:  
> `venv\Scripts\activate`

---

## 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Instale o modelo no Ollama

Exemplo de modelo leve:

```bash
ollama pull qwen2.5
```

---

## 5️⃣ Configure o arquivo `.env`

Use o `.env.example` como base:

```bash
cp .env.example .env
```

E preencha:

```
OLLAMA_BASE_URL=http://localhost:11434
LLM_MODEL=qwen2.5
```

---

## 6️⃣ Inicie o servidor Ollama

```bash
ollama serve
```

Ou rode em background:

```bash
ollama serve &
```

---

## 7️⃣ Execute a API FastAPI

```bash
uvicorn main:app --reload
```

A aplicação ficará disponível em:  
 http://localhost:8000

Swagger UI:  
 http://localhost:8000/docs
