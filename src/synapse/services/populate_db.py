from weaviate.collections.classes.config import Property, DataType
from synapse.chunking import group_events_into_chunks
from synapse.db.db_utils import connect_to_client, project_id
from synapse.parsing.lectureParser import parse_lecture
from weaviate.classes.config import Configure
import logging

logger = logging.getLogger(__name__)

def populate_db():

    logger.info("Starting database population. Connecting to Weaviate...")
    client = connect_to_client()
    logger.info(logging.INFO, "Connected to Weaviate")

    collection_name = "Lectures"

    if client.collections.exists(collection_name):
        client.collections.delete(collection_name)

    logger.info(f"Creating collection: {collection_name}...")

    lectures = client.collections.create(
        name=collection_name,
        vector_config=Configure.Vectors.text2vec_huggingface(
            model="sentence-transformers/all-MiniLM-L6-v2"
        ),
        generative_config=Configure.Generative.google(project_id=project_id),
        properties=[
            Property(name="content", data_type=DataType.TEXT),
            Property(name="start_ms", data_type=DataType.INT),
            Property(name="duration_ms", data_type=DataType.INT),
        ]
    )

    logger.info(f"Successfully created collection: {collection_name}")

    # parse and chunk events
    events = parse_lecture()
    documents = group_events_into_chunks(events)

    logger.info("Starting to populate the database...")
    with lectures.batch.fixed_size(100) as batch:
        for i, d in enumerate(documents):
            batch.add_object(
                properties={
                    "content": d['text'],
                    "start_ms": d['start_ms'],
                    "duration_ms": d['duration_ms'],
                }
            )

            logger.log(logging.INFO, f"Added document {i} to batch")
            if batch.number_errors > 10:
                client.close()
                raise Exception("Too many errors in batch")

    logger.info("Finished populating the database")
    client.close()