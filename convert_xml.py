import os
import sys
import shutil
import subprocess
from pathlib import Path

script_dir = Path(__file__).resolve().parent
DUMP = script_dir / "_dump"

# Renew DUMP
if os.path.exists(DUMP): shutil.rmtree(DUMP)
shutil.copytree(sys.argv.pop(), DUMP)
if sys.argv[1] == "--internal": shutil.copytree(script_dir / "doc/classes", DUMP, dirs_exist_ok=True)
elif sys.argv[1] != "--no-internal":
    raise ValueError('Expected "--internal" or "--no-internal"')

process = subprocess.Popen(
    [sys.executable, script_dir / "src/make_rst.py",  *sys.argv[2:], DUMP],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

for line in process.stdout:
    print(line, end="")