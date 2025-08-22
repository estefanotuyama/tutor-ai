from synapse.services.llm_call import call_llm
from synapse.services.populate_db import populate_db
import logging

def main(populating: bool = False):

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]  # Ensures logs go to the console
    )

    if populating:
        try:
            populate_db()
        except Exception as e:
            logging.error(f"Error populating the database: {e}")

    #testing an llm call
    call_llm("How does python implement its interpreter?")


if __name__ == "__main__":
    #Change populating to True to populate the database (do it when running for the first time
    main(populating=False)