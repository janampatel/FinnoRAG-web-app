RAG based app is created for financial literacy. This project utilises Gemini LLM, Langchain, and Qdrant.

1. Setup and Install Docker
2. Create a docker container for `qdrant/qdrant` and run at port `6333:6333`
3. Create a venv and Install dependencies using `requirements.txt`
4. create a `.env` file and mention your Gemini API key in it.
5. Then run python files:
a. `ingest.py`, and check the database at `http://localhost:6333/dashboard`
b. `retriever.py`
c. Run `uvicorn rag:app` command on CLI, it will prompt you to go to `http://127.0.0.1:8000/`

The `Data` folder contains sample pdfs, more data can be added to it, based on which the FinnoRAG will answer the user's query.
