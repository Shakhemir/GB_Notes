import json
from config import json_file


def read_json():
    with open(json_file, encoding='utf-8') as f:
        read_file = json.loads(f.read())
    return read_file


def write_json(notes_list):
    with open(json_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(notes_list, indent=4, default=str, ensure_ascii=False))

