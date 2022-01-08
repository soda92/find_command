from invoke import task
import shutil,os

@task
def dist(c):
    dest = "C:/MYBINDIR"
    srcs = ["where_command.bat", "where_command.py"]
    if os.path.exists(dest):
        for src in srcs:
            shutil.copy(src, dest)
