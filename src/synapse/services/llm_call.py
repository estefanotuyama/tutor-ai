import logging

from synapse.db.db_utils import connect_to_client


def call_llm(query: str, limit: int=3):
    client = connect_to_client()
    try:
        collection = client.collections.get("Lectures")

        grouped_task = f"""Answer the following question based on the retrieved documents from the database. also provide 
                        Reference for the timestamp in the youtube lecture for which the information was retrieved.{query}"""

        response = collection.generate.hybrid(
            query=query,
            limit=limit,
            grouped_task=grouped_task
        )

        print(response.generated)
        print(response.objects)
    except Exception as e:
        logging.error("Error calling the LLM: ", e)
        client.close()
    client.close()