import os
from pathlib import Path


def write(file_name, content):
    Path(os.path.dirname(file_name)).mkdir(parents=True, exist_ok=True)
    with open(file_name, 'w') as file:
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
