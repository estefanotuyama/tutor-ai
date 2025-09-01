from synapse.services.rag_logic import retrieve_documents_rag
from synapse.utils.configuration import YOUTUBE_LINK, cs50_prompt_template
from synapse.utils.llm_utils import format_documents, call_llm_with_context


def call_with_rag(query: str, context: list, limit: int=3):

    documents = retrieve_documents_rag(query, limit)
    formatted_documents = format_documents(documents)

    reference_timestamp = documents[0].get('start_ms') // 1000
    reference_link = f"{YOUTUBE_LINK}&t={reference_timestamp}s"

    prompt = cs50_prompt_template.format(
        formatted_documents=formatted_documents,
        reference_link=reference_link,
        query=query
    )

    completion, context = call_llm_with_context(prompt, context, role='user')

    return completion, context


def start_chat():
    context = []
    while True:
        user_input = str(input("Enter your query: "))
        if user_input == "exit":
            break
        response, context = call_with_rag(user_input, context)
        print(f"Response: {response.content}")
