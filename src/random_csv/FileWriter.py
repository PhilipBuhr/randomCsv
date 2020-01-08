import os
from pathlib import Path

from definitions import OUT_DIR


def write(file_name, content):
    Path(OUT_DIR).mkdir(parents=True, exist_ok=True)
    file_path = os.path.join(OUT_DIR, file_name)
    with open(file_path, 'w') as file:
        file.write(content)
