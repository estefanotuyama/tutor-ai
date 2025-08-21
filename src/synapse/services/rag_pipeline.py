from synapse.chunking import group_events_into_chunks
from synapse.embedder import generate_embeddings
from synapse.parsing.lectureParser import parse_lecture


def run_rag_pipeline():
    # parse and chunk events
    events = parse_lecture()
    documents = group_events_into_chunks(events)

    #embed chunks
    embeddings = generate_embeddings(documents)