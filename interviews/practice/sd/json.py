import json

def walk_json(obj):
    if isinstance(obj, dict):
        for v in obj.values():
            walk_json(v)
    elif isinstance(obj, list):
        for item in obj.values():
            walk_json(item)
    else:
        pass

def load_and_read_json(path):
    with open(path, "r") as f:
        data = json.load(f)
    walk_json(data)
