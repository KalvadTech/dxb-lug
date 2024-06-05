#!/usr/bin/env python3

import requests
from pyinfra import host
from pyinfra.operations import apk, files, server
from pyinfra.operations.server import hostname

hostname(name="Set the hostname", hostname=host.data.get("name"))

apk.update(
    name="Update apk repositories",
)
apk.upgrade(
    name="Upgrade apk packages",
)
apk.packages(
    name="Install latest packages",
    packages=[
        "htop",
        "iotop",
        "iftop",
        "curl",
        "emacs-nox",
        "net-tools",
        "ripgrep",
    ],
    latest=True,
)

files.put(
    name="Update the message of the day file",
    src="files/motd",
    dest="/etc/motd",
    mode="644",
)

github_users = ["wowi42", "hnb2"]
keys = []
for github_user in github_users:
    url = "https://github.com/{}.keys".format(github_user)
    response = requests.request("GET", url)
    for key in response.text.split("\n"):
        if key != "":
            keys.append(key)

server.user_authorized_keys(
    "root",
    keys,
)
