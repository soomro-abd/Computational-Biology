"""
As Dr. Aziz allowed us to make a program that fills the matrix for us, I am writing this script to do the job. 


The sequence in question:
5'-UGCUCCUAGUACGAGAGGACCGGAGUG-3'

Job: Apply NJ algorithm.
"""

import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

seq = 'UGCUCCUAGUACGAGAGGACCGGAGUG'

def score(i, j):
    ri = seq[i]
    rj = seq[j]

    if (ri == 'G' and rj == 'C') or (ri == 'C' and rj == 'G'):
        return 3
    
    if (ri == 'A' and rj == 'U') or (ri == 'U' and rj == 'A'):
        return 2

    if (ri == 'G' and rj == 'U') or (ri == 'U' and rj == 'G'):
        return 1

    return 0

def fourth_condition_calculator(i, j, matrix):
    k = i + 1

    vals = []

    if k >= j:
        return 0

    while (k > i and k < j):
        vals += [matrix[i][k] + matrix[k+1][j]]
        k += 1

    return max(vals)


def main():

    length = len(seq)
    matrix = np.zeros((length, length), dtype= int)
    
    for j in range(1,length):
        for i in range(0, j):

            if (j - i) < 4:
                matrix[i][j] = 0
                continue
            
            bottom = matrix[i+1][j]
            left = matrix[i][j-1]
            diag = matrix[i+1][j-1] + score(i,j)
            fourth_condition = fourth_condition_calculator(i,j, matrix)

            matrix[i][j] = max([bottom, left, diag, fourth_condition])

    """ 
    Using the below three lines to plot my matrix
    """
    from matplotlib.colors import ListedColormap

    with sns.axes_style('white'):
        sns.heatmap(matrix,
                    cbar=False, 
                    square=False, 
                    annot=True, 
                    fmt='d', 
                    xticklabels=False, 
                    yticklabels=False, 
                    cmap=ListedColormap(['white']), 
                    linewidths=0.5)
    
    plt.show()

main()