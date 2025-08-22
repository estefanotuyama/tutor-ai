from synapse.services.llm_call import call_llm
from synapse.services.populate_db import populate_db_cs50
import logging

def main(populating: bool = False):

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]  # Ensures logs go to the console
    )

    if populating:
        try:
            populate_db_cs50()
        except Exception as e:
            logging.error(f"Error populating the database: {e}")

    #testing an llm call
    query = str(input("Enter your query: "))
    call_llm(query)


if __name__ == "__main__":
    #Change populating to True to populate the database (do it when running for the first time
    main(populating=False)