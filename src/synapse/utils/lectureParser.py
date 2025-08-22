import json
import ftfy


def parse_lecture():
    """
    Parses the lecture JSON, cleans the text robustly, and returns a list of events.
    """
    with open('lecture.json3', encoding="utf-8") as f:
        lecture = json.load(f)

    cleaned_events = []
    for event in lecture['events']:
        if not event.get('segs'):
            continue

        try:
            text = ftfy.fix_text(event['segs'][0]['utf8'])
            cleaned_text = text.replace('\n', ' ')

            # Filter out junk text
            if cleaned_text.startswith('[') and cleaned_text.endswith(']'):
                continue

            cleaned_events.append({
                "text": cleaned_text,
                "start_ms": event['tStartMs'],
                "duration_ms": event['dDurationMs']
            })
        except IndexError:
            continue

    return cleaned_events