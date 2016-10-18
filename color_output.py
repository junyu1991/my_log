#!/usr/bin/python
#!encoding:utf-8

color_dict={'HEADER':'\033[95m','OKBLUE':'\033[94m','OKGREEN':'\033[92m',
            'WARNING':'\033[93m','FAIL':'\033[91m','ENDC':'\033[0m',
            'BOLD':'\033[1m','UNDERLINE':'\033[4m'}

def print2screen(str2print,print_flag):
    try:
        color=color_dict[print_flag]
        print(color+str2print+color_dict['ENDC'])
    except:
        print(str2print)

def test():
    for key in color_dict.iterkeys():
        print2screen("This is %s"%(str(key)),key)

if __name__=='__main__':
    test()
