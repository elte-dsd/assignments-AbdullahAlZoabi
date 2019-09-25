import numpy as np
import random


print("\n\nThe numpy is needed.\n\n");

print("\n\nI wrote a sample input as an array, you can change the array as well.\n\n");


# Input --------------------------------------------------------
# 5 unique elements
Stream = ["A", "A", "A", "A", "A","A","A","A","A",
          "B", "B", "B", "B", "B", "B",
          "X", "X","X","X","X", 
          "R","R","R","R","R","R","R","R",
          "Z","Z","Z","Z",];


random.shuffle(Stream);


# Hash function ---------------------------------------------------
def Hash(Char):

    ASCII = ord(Char);

    return (((ASCII%10) * 1022) - 106)%100;

# Calculate the Least Significant bit ----------------------------
def LeastSignificant(Val):

    if Val == 0:
        return 0;

    if Val == 1:
        return 1;

    Count = 0;

    while Val != 1:
        if Val%2 == 1:
            return 0;

        Count = Count + 1;

        Val = Val/2;


    return Count;


# Main Algorithm ------------------------------------------------------
def FM(S):

    Max = -1;

    for x in S:

        H = Hash(x);

        LS = LeastSignificant(H);

        if LS > Max:
            Max = LS;


    return (2**Max);




# Output ------------------------------------------------------
M = FM(Stream)

print("The output of FM is ", M, "while the exact number of unique elements is 5.");

        
































