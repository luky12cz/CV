"""Run git commands to initialize repo and push to GitHub."""
import subprocess
import os

GIT = r"C:\Program Files\Git\bin\git.exe"
REPO = r"c:\Users\luky\Desktop\cline documents"

def run(cmd):
    full_cmd = f'"{GIT}" {cmd}'
    print(f"Running: {full_cmd}")
    result = subprocess.run(full_cmd, cwd=REPO, shell=True, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr)
    if result.returncode != 0:
        print(f"Exit code: {result.returncode}")
    return result

# Configure git user (needed for commit)
run('config user.email "lukskarpa@gmail.com"')
run('config user.name "Lukas Skarpa"')

# Commit
run('add .')
run('commit -m "Initial commit: CV in RenderCV format"')

# Branch and remote
run('branch -M main')
run('remote add origin https://github.com/luky12cz/CV.git')
run('push -u origin main')
