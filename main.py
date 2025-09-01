from synapse.services.llm_call import call_with_rag, start_chat
from synapse.services.populate_db import populate_db_cs50
import logging

def main(populating: bool = False):

    logging.basicConfig(
        level=logging.WARNING,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]
    )

    if populating:
        try:
            populate_db_cs50()
        except Exception as e:
            logging.error(f"Error populating the database: {e}")

    #continuous llm calls with rag context
    start_chat()



if __name__ == "__main__":
    #Change populating to True to populate the database (do it when running for the first time)
    main(populating=False)