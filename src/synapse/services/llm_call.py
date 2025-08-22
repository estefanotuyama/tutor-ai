from openai import OpenAI
from synapse.db.db_utils import huggingface_api_key
from synapse.services.rag_logic import retrieve_documents_rag


def call_llm(query: str, limit: int=3):

    documents = retrieve_documents_rag(query, limit)

    PROMPT = f"""Answer the user question based on  provided documents.
            User question: {query}
            Documents: {documents}
    """

    llm_client = connect_to_llm()

    completion = llm_client.chat.completions.create(
        model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B:nscale",
        messages=[
            {
                "role": "user",
                "content": PROMPT
            }
        ],
    )

    llm_client.close()
    print(completion.choices[0].message.content)

def connect_to_llm():
    llm_client = OpenAI(
        base_url = "https://router.huggingface.co/v1",
        api_key = huggingface_api_key
    )
    return llm_client