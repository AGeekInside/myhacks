#!/home/mbrooks/.local/share/virtualenvs/mbrooks-hpmZt1LH/bin/python

import myhacks as myh

cmds = [
    "nmcli con down staticNonMITRE; nmcli con up ens33",
    "sudo cp /root/daemon.json /etc/docker",
    "sudo cp /root/http-proxy.conf /etc/systemd/system/docker.service.d",
    ]

for cmd in cmds:
    myh.run(cmd)

myh.restart_docker()
