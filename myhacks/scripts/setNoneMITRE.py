#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python

import myhacks as myh

cmds = [
    "nmcli con down ens33 ; nmcli con up staticNonMITRE",
    "sudo mv /etc/docker/daemon.json /root",
    "sudo mv /etc/systemd/system/docker.service.d/http-proxy.conf /root",
   ]

for cmd in cmds:
    myh.run(cmd)

myh.restart_docker()
