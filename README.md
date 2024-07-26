RAG based app is created for financial literacy. This project utilises Gemini LLM, Langchain, and Qdrant.

Setup and Install Docker
Create a docker container for `qdrant/qdrant` and run at port `6333:6333`
Create a venv and Install dependencies using `requirements.txt`
create a `.env` file and mention your Gemini API key in it.
Then run python files:
`ingest.py`, and check the database at `http://localhost:6333/dashboard`
`retriever.py`
Run `uvicorn rag:app` command on CLI, it will prompt you to go to `http://127.0.0.1:8000/`

The `Data` folder contains sample pdfs, more data can be added to it, based on which the FinnoRAG will answer the user's query.
