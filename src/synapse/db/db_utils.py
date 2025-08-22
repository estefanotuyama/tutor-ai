import os
from dotenv import load_dotenv
import weaviate
from weaviate.auth import Auth
from weaviate.config import AdditionalConfig, Timeout

load_dotenv()

#api keys
weaviate_url = os.environ["WEAVIATE_URL"]
weaviate_api_key = os.environ["WEAVIATE_APIKEY"]
huggingface_api_key = os.getenv("HUGGINGFACE_APIKEY")

#lecture collection name
CS50_COLLECTION_NAME = os.getenv("CS50_COLLECTION_NAME")

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