import os
import subprocess

CODESPACE_NAME = os.getenv(key="CODESPACE_NAME", default="blank")

if CODESPACE_NAME.startswith("dttest-"):

    # Do your testing logic here.
    # Testing done, force kill codespace
    subprocess.run(["gh", "codespace", "delete", "--codespace", CODESPACE_NAME, "--force"])
else:
    # This is a "real" startup, so do not test and proceed as normal
