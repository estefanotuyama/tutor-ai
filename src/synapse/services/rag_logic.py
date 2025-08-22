from synapse.db.db_utils import connect_to_client, CS50_COLLECTION_NAME


def retrieve_documents_rag(query: str, limit: int, collection: str = CS50_COLLECTION_NAME):
    client = connect_to_client()

    if not client.collections.exists(collection):
        client.close()
        raise Exception(f"Collection {collection} does not exist") #todo: create exception

    collection = client.collections.get(collection)

    result = collection.query.hybrid(
        query=query,
        limit=limit,
    )
    client.close()

    documents = []
    for document in result.objects:
        documents.append(document.properties)
    return documents