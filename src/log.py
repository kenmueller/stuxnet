from os import system
from datetime import datetime

def add_line_to_log(log: str, line: str = '', extra_newline: bool = False, indentation: int = 0) -> str:
	return f'{log}{"  " * indentation}{line}\n' + ('\n' if extra_newline else '')

def write_log_file(log: str):
	system('mkdir logs &> /dev/null')
	with open(f'logs/{datetime.now().strftime("%Y-%m-%d--%I:%M:%S-%p")}.md', 'w+') as file:
		file.write(log)