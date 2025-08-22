import os
from dotenv import load_dotenv
import weaviate
from weaviate.auth import Auth
from weaviate.config import AdditionalConfig, Timeout

load_dotenv()

weaviate_url = os.environ["WEAVIATE_URL"]
weaviate_api_key = os.environ["WEAVIATE_APIKEY"]
google_api_key = os.getenv("GOOGLE_APIKEY")
huggingface_api_key = os.getenv("HUGGINGFACE_APIKEY")
project_id = os.getenv("PROJECT_ID")

headers={
        "X-Goog-Api-Key": google_api_key,
        "X-HuggingFace-Api-Key": huggingface_api_key
}

def connect_to_client():
    client = weaviate.connect_to_weaviate_cloud(
        cluster_url=weaviate_url,
        auth_credentials=Auth.api_key(weaviate_api_key),
        skip_init_checks=True,
        headers=headers,
        additional_config=AdditionalConfig(
            timeout=Timeout(init=30, query=60, insert=120)
        )
    )
    return client