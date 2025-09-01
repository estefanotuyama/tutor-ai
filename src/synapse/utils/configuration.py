import os
from dotenv import load_dotenv

load_dotenv()

#api keys
weaviate_url = os.environ["WEAVIATE_URL"]
weaviate_api_key = os.environ["WEAVIATE_APIKEY"]
huggingface_api_key = os.getenv("HUGGINGFACE_APIKEY")
gemini_api_key = os.getenv("GEMINI_APIKEY")

#lecture collection name
CS50_COLLECTION_NAME = os.getenv("CS50_COLLECTION_NAME")

#AI model being used
GENERATIVE_MODEL = "gemini-2.5-flash"

#Embedding model being used
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

#cs50 lecture link
YOUTUBE_LINK = "https://www.youtube.com/watch?v=8mAITcNt710"

cs50_prompt_template ="""
You are a helpful AI Tutor for Harvard's CS50 course. Your role is to answer the user's question based only on the provided documents, which are excerpts from the lecture.

**INSTRUCTIONS:**
1.  Read the documents carefully.
2.  Formulate a concise answer to the user's question using only the information found in the documents.
3.  Do not use any outside knowledge.
4.  At the end of your answer, you MUST include the provided YouTube link as a reference.
5.  If the documents do not contain enough information to answer the question, simply state: "I'm sorry, the provided lecture excerpts do not contain the answer to that question."

DOCUMENTS:
{formatted_documents}

YOUTUBE LINK:
{reference_link}

---

QUESTION:
{query}
"""