"""this file is called by .vscode/launch.json"""

import os
import sys
import subprocess


input_path = sys.argv[1]
print("INPUT PATH = " + input_path)


if os.name == "posix":
    if "/course/" not in input_path:
        print("ERROR: YOU MUST OPEN AN FILE IN THE COURSE")
        sys.exit()
    bundle_contents = "TEST:../course/" + input_path.split("/course/")[1] + "\n"
    with open("tools-macos/bundle-debug.txt", encoding="utf-8", mode="w") as f:
        f.write(bundle_contents)
    subprocess.run(["./build.sh"], cwd="tools-macos", check=False)
elif os.name == "nt":
    if "\\course\\" not in input_path:
        print("ERROR: YOU MUST OPEN AN FILE IN THE COURSE")
        sys.exit()
    bundle_contents = "TEST:..\\course\\" + input_path.split("\\course\\")[1] + "\n"
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "tools-windows/bundle-debug.txt")
    with open(filename, encoding="utf-8", mode="w") as f:
        f.write(bundle_contents)
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "tools-windows/build.bat")
    dir_ = os.path.dirname(os.path.abspath(filename))
    subprocess.run(
        [
            "bundler.exe",
            "bundle-debug.txt",
            "app/data/flutter_assets/assets/bundle-debug.json",
        ],
        cwd=dir_,
        shell=True,
        check=False,
    )
else:
    print("ERROR: UNSUPPORTED OPERATING SYSTEM!")
