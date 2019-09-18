import numpy as np
import random

NumOfAddresses = 100;

Stream = ["A", "A", "A", "A", "A","A","A","A","A", #9
          "B", "B", "B", "B", "B", "B", #6
          "Y", "Y","Y","Y","Y", #5
          "R","R","R","R","R","R","R","R", #8
          "M","M","M","M", #4
          "C"]; #1

random.shuffle(Stream);


# Dummy hash functions
def H1(Char):

    ASCII = ord(Char);

    return (((ASCII%10) * 1022) - 106)%NumOfAddresses;

def H2(Char):

    ASCII = ord(Char);

    return (((ASCII - 10) + 100)*177)%NumOfAddresses;

def H3(Char):

    ASCII = ord(Char);

    return (((ASCII*2) + 27)*18)%NumOfAddresses;


def H4(Char):

    ASCII = ord(Char);

    return (((ASCII%10) * 102) - 100)%NumOfAddresses;


# Main Alg
def CountMinSketch(Stream):

    Sketch = np.zeros((4, NumOfAddresses));

    NumOfElem = len(Stream);

    for i in range(NumOfElem):

        h1 = H1(Stream[i]);

        h2 = H2(Stream[i]);

        h3 = H3(Stream[i]);

        h4 = H4(Stream[i]);

        Sketch[0, h1] = Sketch[0, h1] + 1;

        Sketch[1, h2] = Sketch[1, h2] + 1;

        Sketch[2, h3] = Sketch[2, h3] + 1;

        Sketch[3, h4] = Sketch[3, h4] + 1;

    return Sketch;

    

Sketch = CountMinSketch(Stream);

def GetFreq(Char, Sketch):

    h1 = H1(Char);

    h2 = H2(Char);

    h3 = H3(Char);

    h4 = H4(Char);

    return min(Sketch[0, h1], Sketch[1, h2], Sketch[2, h3], Sketch[3, h4]);

# Testing -----------------------    

AFreq = GetFreq("A", Sketch);

BFreq = GetFreq("B", Sketch);

YFreq = GetFreq("Y", Sketch);

RFreq = GetFreq("R", Sketch);

MFreq = GetFreq("M", Sketch);

CFreq = GetFreq("C", Sketch);

print("Calculate frequency of A is ", AFreq, "while true frequency is ", 9);

print("Calculate frequency of B is ", BFreq, "while true frequency is ", 6);

print("Calculate frequency of Y is ", YFreq, "while true frequency is ", 5);

print("Calculate frequency of R is ", RFreq, "while true frequency is ", 8);

print("Calculate frequency of M is ", MFreq, "while true frequency is ", 4);

print("Calculate frequency of C is ", CFreq, "while true frequency is ", 1);
