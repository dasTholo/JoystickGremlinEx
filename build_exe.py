import os
import subprocess

main_script = "joystick_gremlin.py"
command = [
    "uv", "run", "--frozen", "--",
    "nuitka",
    "--standalone",
    "--follow-imports",
    "--show-progress",
    "--enable-plugin=pyside6",
    "--include-plugin-directory=action_plugins",
    "--include-plugin-directory=container_plugins",
    "--include-data-files=dill.dll=dill.dll",
    "--include-data-files=vjoy/vJoyInterface.dll=vJoyInterface.dll",
    "--include-data-files=vigem/ViGEmClient.dll=ViGEmClient.dll",
    "--include-data-dir=icons=icons",
    "--include-data-dir=gfx=gfx",
    "--output-dir=dist",
    "--nofollow-import-to=test",
    "--nofollow-import-to=examples",
    "--nofollow-import-to=img",
    "--nofollow-import-to=jgEx-Example_pics",
    "--nofollow-import-to=unittest",
    main_script,
]
subprocess.run(command, check=True)
# include dll
## https://nuitka.net/user-documentation/user-manual.html#package-data-include-package-data-package
#vjoy
#dill
#vigem
#icons
#gfx
