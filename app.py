import os
import subprocess
CODESPACE_NAME = os.getenv(key="CODESPACE_NAME", default="blank")

if CODESPACE_NAME.startswith("dttest-platform-engineering-demo"):

    # TODO

    # Testing done, force kill codespace
    subprocess.run(["gh", "codespace", "delete" "--codespace", CODESPACE_NAME, "--force"])