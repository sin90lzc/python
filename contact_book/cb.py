#!/usr/bin/python

import ObjectDumper as od


print argvs


ro=od.ObjectDumper("object")

ro.write("hello world")

r=ro.read()


print r


