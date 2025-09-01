import weaviate
from weaviate.auth import Auth
from weaviate.config import AdditionalConfig, Timeout
from synapse.utils.configuration import huggingface_api_key, weaviate_url, weaviate_api_key

headers={
        "X-HuggingFace-Api-Key": huggingface_api_key,
}

def connect_to_client():
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=weaviate_url,
        auth_credentials=Auth.api_key(weaviate_api_key),
        headers=headers,
        additional_config=AdditionalConfig(
            timeout=Timeout(init=30, query=60, insert=120)
        )
    )
    return client