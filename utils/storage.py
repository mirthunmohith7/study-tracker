import json
import os
def load_sessions():
    if not os.path.exists ("data/sessions.json"):
        return []
    try:
        with open ("data/sessions.json",'r') as file:
            sessions = json.load(file)
        return sessions
    except json.JSONDecodeError:
        return []

def save_sessions(sessions):
    with open ("data/sessions.json",'w') as file:
        json.dump(sessions,file,indent=4)