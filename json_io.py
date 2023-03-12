import json
from config import json_file


def read_json():
    try:
        with open(json_file) as f:
            read_file = json.loads(f.read())
    except json.JSONDecodeError:
        return []
    except FileNotFoundError:
        open(json_file, 'w').close()
        return []
    else:
        return read_file


def write_json(notes_list):
    with open(json_file, 'w') as f:
        f.write(json.dumps(notes_list, indent=4, default=str, ensure_ascii=False))
