# -*- coding: utf-8 -*-

name = "ispc"

version = "1.9.2"

description = "Intel SPMD compiler"

tools = [
    "ispc"
]

def commands():
    env.PATH.append("{root}")
