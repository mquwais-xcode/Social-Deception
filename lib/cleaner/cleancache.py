import subprocess

def cleanup():
    subprocess.call('find . -type d -name "__pycache__" -exec rm -rf {} +', shell=True)

