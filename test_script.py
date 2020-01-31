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
        print("testing")
    
    print("...done.\n")
    

if __name__ == "__main__":
    main(sys.argv)
