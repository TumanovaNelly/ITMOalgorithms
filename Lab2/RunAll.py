import os
import subprocess

current_directory = os.getcwd()
root_directory = os.path.dirname(current_directory)
for root, _, files in os.walk(current_directory):
    for file in files:
        if os.path.basename(root) == 'src' and file.endswith('.py'):
            run_path = os.path.relpath(os.path.join(root, file), root_directory)
            print(f'RUNNING {run_path}')
            subprocess.run(['python', run_path], cwd=root_directory)
            print('--------------------------------------')


