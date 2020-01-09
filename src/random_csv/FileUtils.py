import os
from pathlib import Path

from definitions import OUT_DIR


def write(file_name, content):
    Path(OUT_DIR).mkdir(parents=True, exist_ok=True)
    file_path = os.path.join(OUT_DIR, file_name)
    with open(file_path, 'w') as file:
        file.write(content)


def read_line_looping(file_name, count):
    i = 0
    lines = []
    with open(file_name, 'r') as file:
        line = file.readline()
        while i < count and line != '':
            lines.append(line.strip())
            i += 1
            line = file.readline()
    if i < count:
        lines = lines + read_line_looping(file_name, count - i)
    return lines
