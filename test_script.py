#!/usr/bin/env python3

import numpy as np
import sys

def main(*argv):
    """

    :param argv:
    :return:
    """
    print("testing...")
    for a in argv:
        print(a)
    
    def new_method():
        print("testing...this print statement has been edited")
        print("new statement, but will change and commit to both the remote")
        print("and local to see what happens.")
    
    print("...done.\n")
    

if __name__ == "__main__":
    main(sys.argv)
