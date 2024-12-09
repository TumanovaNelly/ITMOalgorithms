import os
import subprocess

from utils import CYAN, RESET

if __name__ == '__main__':
    current_directory = os.getcwd()
    for file in os.listdir(current_directory):
        if file.startswith('Lab'):
            lab_directory = os.path.join(current_directory, file)
            run_path = 'RunLabSources.py'
            print(f'{CYAN}======= RUNNING {lab_directory} SOURCES ======={RESET}')
            subprocess.run(['python', run_path], cwd=lab_directory)
            print()
