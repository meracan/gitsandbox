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
        x = 4 + 9
        y = "random string"
        print("testing...this print statement has been edited")
        # merge worked fine above. lets try pushing
        # testing merge conflicts
    
    def method_dont_overwrite():
        x = 6
        """ nice script you got here, would be a shame if 
            someone were to overwrite this...
        """
    
    print("...done.\n")
    

if __name__ == "__main__":
    main(sys.argv)
