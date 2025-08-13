import json
import os
import shutil

def load_json(filepath, default=None):
    if not os.path.exists(filepath):
        return default if default is not None else []
    with open(filepath, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return default if default is not None else []

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

def center_text(text):
    width = shutil.get_terminal_size((80, 20)).columns
    return text.center(width)

def center_block(block):
    width = shutil.get_terminal_size((80, 20)).columns
    lines = block.splitlines()
    block_width = max(len(line) for line in lines) if lines else 0
    left_margin = max((width - block_width) // 2, 0)
    return '\n'.join((' ' * left_margin) + line for line in lines) 