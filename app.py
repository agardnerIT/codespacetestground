import os
import subprocess
from utils import *

CODESPACE_NAME = os.getenv(key="CODESPACE_NAME", default="blank")

if CODESPACE_NAME.startswith("dttest-"):

    send_startup_ping(codespace_mode="testing")
    # TODO
    # Testing done, force kill codespace
    subprocess.run(["gh", "codespace", "delete", "--codespace", CODESPACE_NAME, "--force"])
else:
    send_startup_ping(codespace_mode="standard")