#! /bin/python3

import os
import sys
from setting import setting

def load_hosts():
    return setting.host


def select(n_i, i_n, trytimes, max_try = 3):
    if trytimes >= max_try:
        exit(0)
    trytimes += 1
        
    sel_host = input("select host index/name: ")
    host = None
    print(sel_host)
    if sel_host.lower() in ["q", "quite"]:
        exit(0)

    if sel_host in i_n:
        host = i_n[sel_host]
    elif sel_host in n_i:
        host = n_i[sel_host]
    else:
       host = select(n_i, i_n, trytimes, max_try) 
    return host

def connect():
    hosts = load_hosts()
    i_n = {}
    n_i = {}
    trytimes = 0
    print("hosts:")
    for index, host in enumerate(hosts):
        idx_key = index + 1
        print("\t{}: {}".format(idx_key, host["name"]))
        i_n[str(idx_key)] = host
        n_i[host["name"]] = host

    host = select(n_i, i_n, trytimes)
    sys_cmd(host)
        


def sys_cmd(host):
    print("connect {}".format(host["name"]))
    cmd = 'ssh -o ServerAliveInterval=30 {}@{} -p {}'.format(host["user"], host["host"], host["port"])
    os.system(cmd)

if __name__ == "__main__":
    connect()
