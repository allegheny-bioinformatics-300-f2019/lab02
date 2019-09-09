#!/usr/bin/env python3

# Written by:
# email:
# Date:

# Library installation notes:
#
#


DATE = "9 Sept 2019"
VERSION = "i"
AUTHOR = " myName"
AUTHORMAIL = "@allegheny.edu"


def help():
        h_str = "   "+DATE+" | version: "+VERSION+" |"+AUTHOR+" | "+AUTHORMAIL
        print("  "+len(h_str) * "-")
        print(h_str)
        print("  "+len(h_str) * "-")

        print("\n\t Program: baseCounter.py .")
        print("\t+ \U0001f600  USAGE: programName <any key to launch>")
#        print("\t+ INPUT directory (your data files are here)     : ",INPUT_DIR)
#        print("\t+ OUTPUT directory (your output is placed here)  : ",OUTPUT_DIR)

#end of help()


def begin(task_str):
    """Driver function of program"""
    #print(" Task :",task_str)
    prompt = "\tEnter your sequence : "
    seq_str = input(prompt)

    print("\tEntered sequence is the following:",seq_str)
# your program should find counts for these variables.
    countA_int = 0
    countT_int = 0
    countC_int = 0
    countG_int = 0
    countAT_int = 0
    countTA_int = 0
    countCG_int = 0
    countGC_int = 0


    # TODO!!
    # determine the counts of the bases in your entered sequence


    print("\n\tBase Counts:")
    print("\tA's  :",countA_int)
    print("\tT's  :",countT_int)
    print("\tC's  :",countC_int)
    print("\tG's  :",countG_int)
    print("\tAT's :",countAT_int)
    print("\tTA's :",countTA_int)
    print("\tCG's :",countCG_int)
    print("\tGC's :",countGC_int)




######################################################
#end of begin()



import os, sys
#import math
# list other libraries here

#from sklearn.metrics import r2_score
#from sklearn.metrics import mean_squared_error
#import plotly.plotly as py
#import plotly.graph_objs as go
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#import matplotlib.pyplot as plt
#from scipy import stats
#import numpy as np



if __name__ == '__main__':

        if len(sys.argv) == 2: # one parameter at command line
        # note: the number of command line parameters is n + 1
                begin(sys.argv[1])#,sys.argv[2])#,sys.argv[3], sys.argv[4]),sys.argv[5])
        else:
                help()
                sys.exit()
