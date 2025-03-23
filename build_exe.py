import os
import subprocess

main_script = "joystick_gremlin.py"
command = [
    "python",
    "-m",
    "nuitka",
    "--standalone",
    "--show-progress",
    "--enable-plugin=pyside6",
    "--output-dir=dist",
    "--nofollow-import-to=test",
    "--nofollow-import-to=examples",
    "--nofollow-import-to=img",
    main_script,
]
subprocess.run(command, check=True)