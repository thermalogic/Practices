"""
John V. Guttag. Introduction to Computation and Programming Using Python: 
                    With Application to Understanding Data, 3rd Edition,2021
    
    22.5 Statistical Measures Don’t Tell the Whole Story (Page521-522)
         F.J. Anscombe's Data Sets
"""

import os

if __name__ == "__main__":
    cur_abspath = os.path.abspath(os.path.dirname(__file__))
    data_file_name="/data/anscombe.csv"
    data_file_name_abspath = cur_abspath+data_file_name
    print(data_file_name_abspath)
    datafile=open(data_file_name_abspath)
    for row in datafile:
        print(row,end="")
    datafile.close()

