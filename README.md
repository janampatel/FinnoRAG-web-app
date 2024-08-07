RAG based app is created for financial literacy. This project utilises Gemini LLM, Langchain, and Qdrant.

1. Setup and Install Docker
2. Create a docker container for `qdrant/qdrant` and run at port `6333:6333`
3. Create a venv and Install dependencies using `requirements.txt`
4. create a `.env` file and mention your Gemini API key in it.
5. Then run python files:
   
a. `ingest.py`, and check the database at `http://localhost:6333/dashboard`

b. `retriever.py`

c. Run `uvicorn rag:app` command on CLI, it will prompt you to go to `http://127.0.0.1:8000/`

The `templates` folder contains html based front-end part.

The `Data` folder contains sample pdfs, more data can be added to it, based on which the FinnoRAG will answer the user's query.


![1](https://github.com/user-attachments/assets/ed8f004e-0501-48d2-bb69-16013340cd98)
![2](https://github.com/user-attachments/assets/2f29b3d4-89ff-46b0-92ac-6424b7ce99e6)
![4](https://github.com/user-attachments/assets/e7c1dced-a843-45b2-9e62-519f4148e8d2)
![5](https://github.com/user-attachments/assets/178748b1-3b04-4096-851d-c96edfc720de)


