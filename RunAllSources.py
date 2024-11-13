import os
import subprocess


if __name__ == '__main__':
    current_directory = os.getcwd()
    for file in os.listdir(current_directory):
        if file.startswith('Lab') and not (file.endswith('4')):
            lab_directory = os.path.join(current_directory, file)
            run_path = 'RunLabSources.py'
            print(f'======= RUNNING {lab_directory} SOURCES =======')
            subprocess.run(['python', run_path], cwd=lab_directory)
            for _ in range(3): print()