from typing import List, Dict, Any
from openai import OpenAI
from synapse.utils.configuration import GENERATIVE_MODEL, huggingface_api_key, gemini_api_key


def generate_with_single_input(prompt: str,
                               top_p: float = None,
                               temperature: float = None,
                               max_tokens: int = 1000):

    llm_client = connect_to_llm()

    completion = llm_client.chat.completions.create(
        model=GENERATIVE_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        top_p=top_p,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    llm_client.close()
    return completion.choices[0].message

    #return output_dict is the idea here.


def generate_with_multiple_input(messages: List[Dict],
                                 top_p: float = None,
                                 temperature: float = None,
                                 max_tokens: int = 1000):

    llm_client = connect_to_llm()
    completion = llm_client.chat.completions.create(
        model=GENERATIVE_MODEL,
        reasoning_effort="low",
        messages=messages,
        top_p=top_p,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    llm_client.close()
    return completion.choices[0].message

def call_llm_with_context(prompt: str, context: list, role: str = 'user'):
    """
    Calls a language model with the given prompt and context to generate a response.
    """

    # Append the prompt into the context list
    context.append({'role': role, 'content': prompt})

    # Call the llm with multiple input passing the context list
    response = generate_with_multiple_input(messages=context)

    # Append the LLM response
    context.append({'role':'assistant', 'content': response.content})

    return response, context

def connect_to_llm():
    llm_client = OpenAI(
        base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        api_key = gemini_api_key
    )
    return llm_client

def format_documents(documents):
    formatted_documents = ""
    for i, doc in enumerate(documents):
        formatted_documents += f"Document {i+1}:\n\"{doc['content']}\"\n\n"
    return formatted_documents