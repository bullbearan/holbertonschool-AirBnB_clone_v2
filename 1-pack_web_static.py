#!/usr/bin/python3
"This is a line of text"


def do_pack():
    "This is a function"
    from datetime import datetime
    from fabric.api import local
    import os.path

    date = datetime.now().strftime("%Y%m%d%H%M%S")
    local("mkdir -p versions")
    local("tar -czvf versions/web_static_{}.tgz web_static".format(date))
    return os.path.exists("versions/web_static_{}.tgz".format(date))
