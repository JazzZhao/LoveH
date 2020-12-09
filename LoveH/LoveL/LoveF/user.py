import os
from time import sleep
from sys import argv

def get_user():
    if len(argv) > 1:
        uname = argv[1]
    else:
        uname = '1'  # input("输入用户标记名：")
    if check_uname(uname):
       os.makedirs("./user/{}".format(uname))
    return uname


def check_uname(uname):
    __check_status = True
    if os.path.exists("./user/{}".format(uname)):
        __check_status = False
    return __check_status

def get_a_log(uname):
    __a_log = 0
    if os.path.exists("./user/{}/a_log".format(uname)):
        with open("./user/{}/a_log".format(uname), "r", encoding="utf8") as fp:
            __a_log = int(fp.read())
    else:
        with open("./user/{}/a_log".format(uname), "w", encoding="utf8") as fp:
            fp.write(str(__a_log))
    return __a_log


def get_v_log(uname):
    __v_log = 0
    if os.path.exists("./user/{}/v_log".format(uname)):
        with open("./user/{}/v_log".format(uname), "r", encoding="utf8") as fp:
            __v_log = int(fp.read())
    else:
        with open("./user/{}/v_log".format(uname), "w", encoding="utf8") as fp:
            fp.write(str(__v_log))
    return __v_log


def get_d_log(uname):
    __d_log = 0
    if os.path.exists("./user/{}/d_log".format(uname)):
        with open("./user/{}/d_log".format(uname), "r", encoding="utf8") as fp:
            __d_log = int(fp.read())
    else:
        with open("./user/{}/d_log".format(uname), "w", encoding="utf8") as fp:
            fp.write(str(__d_log))
    return __d_log