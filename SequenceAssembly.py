"""
File: get_best_nucleotide.py
--------------
ADD YOUR DESCRIPTION HERE
"""
import os
import sys

from TextGrid import TextGrid, Cell

def get_best_nucleotide(nucleotide1, nucleotide2, nucleotide3):
    """
    Given three nucleotides, returns a nucleotide with the most common *non-blank* value. If multiple nucleotides have the same value, it doesn't matter which specific nucleotide is returned so long as its value is correct. You can assume there will never be ambiguity -- there will always be a clear majority non-blank character.

    Input:
        three nucleotides (Cells) to be compared
    Returns:
        best (Cell): nucleotide with most common non-blank value

    This doctest creates nucleotides for simple tests.
    >>> grid = TextGrid('ATCG_.txt')
    >>> A = grid.get_cell(0,0)
    >>> T = grid.get_cell(1,0)
    >>> C = grid.get_cell(2,0)
    >>> G = grid.get_cell(3,0)
    >>> blank = grid.get_cell(4,0)
    >>> best1 = get_best_nucleotide(A, A, A)
    >>> best1.value
    'A'
    >>> best2 = get_best_nucleotide(A, T, T)
    >>> best2.value
    'T'
    >>> best3 = get_best_nucleotide(A, blank, A)
    >>> best3.value
    'A'
    >>> best4 = get_best_nucleotide(blank, blank, T)
    >>> best4.value
    'T'
    """
    val1 = nucleotide1.value
    val2 = nucleotide2.value
    val3 = nucleotide3.value
    count_A = 0
    count_T = 0
    count_C = 0
    count_G = 0
    if val1 == 'A':
        if val2 == 'A' or val3 == 'A':
            count_A += 1
    elif val1 == 'T':
        if val2 == 'T' or val3 == 'T':
            count_T += 1
    elif val1 == 'C':
        if val2 == 'C' or val3 == 'C':
            count_C += 1
    elif val1 == 'G':
        if val2 == 'G' or val3 == 'G':
            count_G += 1
    elif val1 == '_':
        if val2 == '_' or val3 == '_':
            if val2 == 'A' or val3 == 'A':
                count_A += 1
            if val2 == 'T' or val3 == 'T':
                count_T += 1
            if val2 == 'C' or val3 == 'C':
                count_C += 1
            if val2 == 'G' or val3 == 'G':
                count_G += 1
    
    if val2 == 'A':
        if val3 == 'A':
            count_A += 1
    elif val2 == 'T':
        if val3 == 'T':
            count_T += 1
    elif val2 == 'C':
        if val3 == 'C':
            count_C += 1
    elif val2 == 'G':
        if val3 == 'G':
            count_G += 1
    elif val2 == '_':
        if val3 == '_':
            if val1 == 'A':
                count_A += 1
            elif val1 == 'T':
                count_T += 1
            elif val1 == 'C':
                count_C += 1
            elif val1 == 'G':
                count_G += 1

    best_val = ''
    if count_A > count_T and count_A > count_C and count_A > count_G:
        best_val = 'A'
    elif count_T > count_A and count_T > count_C and count_T > count_G:
        best_val = 'T'
    elif count_C > count_T and count_C > count_A and count_C > count_G:
        best_val = 'C'
    else:
        best_val = 'G'
    
    cell = Cell(best_val, 0, 0)
    return cell

    

######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

def main():
    n1 = get_valid_nucleotide()
    n2 = get_valid_nucleotide()
    n3 = get_valid_nucleotide()
    best = get_best_nucleotide(n1, n2, n3)
    print("The best nucleotide of", n1, n2, n3, "is", best.value)

VALID_NUCLEOTIDES = {'A', 'T', 'C', 'G', '_'}

def get_valid_nucleotide():
    nuc = input("Enter a nucleotide (A, T, C, or G): ").strip().upper()
    while nuc not in VALID_NUCLEOTIDES:
        print("Invalid entry.")
        nuc = input("Enter a nucleotide (A, T, C, or G): ").strip().upper()
    cell = Cell(nuc, 0, 0)
    return cell

if __name__ == '__main__':
    main()