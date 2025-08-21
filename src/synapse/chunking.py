

def group_events_into_chunks(events: list, max_pause_ms: int = 3000, max_chunk_chars: int = 1500):
    """
    Groups individual transcript events into larger, coherent chunks.

    Args:
        events: A list of cleaned event dictionaries from parse_lecture().
        max_pause_ms: The maximum pause in milliseconds between events before starting a new chunk.
        max_chunk_chars: The maximum number of characters for a chunk's text before starting a new one.

    Returns:
        A list of chunk dictionaries.
    """
    if not events:
        return []

    all_chunks = []
    # Start the first chunk with a *copy* of the first event
    current_chunk = events[0].copy()

    for i in range(1, len(events)):
        previous_event = events[i-1]
        current_event = events[i]

        # Calculate the pause between the end of the last event and the start of the current one
        pause = current_event['start_ms'] - (previous_event['start_ms'] + previous_event['duration_ms'])

        # Check for breakpoint conditions: a long pause or the chunk is too long
        if pause > max_pause_ms or len(current_chunk['text']) > max_chunk_chars:
            # Finalize the current chunk and add it to our list
            all_chunks.append(current_chunk)
            # Start a new chunk with a *copy* of the current event
            current_chunk = current_event.copy()
        else:
            # Merge the current event into the chunk
            current_chunk['text'] += ' ' + current_event['text']
            # The duration is the time from the chunk's start to the current event's end
            current_chunk['duration_ms'] = (current_event['start_ms'] + current_event['duration_ms']) - current_chunk['start_ms']

    # After the loop, the last chunk is still in current_chunk, so we need to add it
    all_chunks.append(current_chunk)

    return all_chunks