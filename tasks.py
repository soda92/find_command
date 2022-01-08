from invoke import task
import shutil, os


def inject_path():
    with open("wh.ori.bat", mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [
            line.replace(
                "{file_path}",
                os.path.join(os.path.dirname(__file__), "where_command.py"),
            )
            for line in lines
        ]
        with open("wh.out.bat", mode="w", encoding="utf-8") as f:
            for line in lines:
                f.write(line)


@task
def dist(c):
    dest = "C:/MYBINDIR"
    inject_path()
    shutil.copy(
        os.path.join(os.path.dirname(__file__), "wh.out.bat"),
        os.path.join(dest, "wh.bat"),
    )
