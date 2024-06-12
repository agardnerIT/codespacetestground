import os

CODESPACE_NAME = os.getenv(key="CODESPACE_NAME", default="blank")
with open("foo.log", mode="w") as file:

    lines = ["a line here\n", f"Codespace Name: {CODESPACE_NAME}"]
    file.writelines(lines)