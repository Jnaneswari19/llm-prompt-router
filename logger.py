import json
from datetime import datetime


def log_route(intent, confidence, message, response):

    log_entry = {
        "timestamp": str(datetime.now()),
        "intent": intent,
        "confidence": confidence,
        "message": message,
        "response": response
    }

    with open("route_log.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")