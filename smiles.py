# -*- coding: cp1251 -*-
import numpy as np
import csv
import simpleSM
import chirSM


qest = input("Do you whant to enter sequence or you have  FASTA-file? Enter 1, if you want to enter seuence yourself. Enter 2, if you have FASTA-file.")


if qest == "1":
    qest2 = input("Do you have a file with strings or you want enter the ONE string by yourself? Enter 1/2. ")

    if qest2 == "1":
        name_of_files = input ("Enter the name of file with strings: ")
        with open(name_of_files) as file1:
            array = [row.strip() for row in file1]
        l = 0
        for i in open(name_of_files, "r"):
            l += 1
        seq1 = []
        for w in range(l):
            seq1.append([])
            seq1[w] = array[w]
        print("Sequence:  ", seq1)
        SM1 = []
        for e in range(l):
            SM1.append([])
            SM1[e]=simpleSM.SM(seq1[e])
        print('SMILEs for SM sequenses:  \n')
        print('\n\n'.join(SM1))
        f = open("SM1_sequences.txt", "w")
        for item in SM1:
            f.write('%s\n'%item)
        f.close()
        with open("SM1_sequences.csv", "w", newline='') as file:
            for it in SM1:
                csv.writer(file).writerow([it])
        
    if qest2 == "2":
        seq = input("Enter sequence  ")
        print("Sequence: ", seq)
        SM = simpleSM.SM(seq)
        print("SM: ", SM)

        
if qest == "2":
    qest22 = input("Do you have a file with filenames or you want enter the name of file with ONE protein? Enter 1/2. ")

    if qest22 == "1":
        name_of_files = input ("Enter the name of file with filenames: ")
        with open(name_of_files) as file1:
            array = [row.strip() for row in file1]
        seq2 = []
        for s in range(len(array)):
            seq2.append([])
            with open(array[s]) as file:
                array2 = [row.strip() for row in file]
            seq2[s] = array2[1]
        print("Sequences:   ", seq2)
        SM2 = []
        for q in range(len(seq2)):
            SM2.append([])
            SM2[q]=chirSM.SM2(seq2[q])
        print('SMILEs for SM2 sequenses:  \n')
        print('\n\n'.join(SM2))
        f = open("SM2_sequences.txt", "w")
        for item in SM2:
            f.write('%s\n'%item)
        f.close()
        with open("SM2_sequences.csv", "w", newline='') as file:
            for it in SM2:
                csv.writer(file).writerow([it])

    if qest22 == "2":
        namef = input("Enter name of the file you want to analyze: ")
        file_seq = open(namef, "r")
        file_r = file_seq.read()
        print("File contains the following: ")
        print(file_r)
        file_seq.close()
        with open(namef) as file:
            array = [row.strip() for row in file]
        seq = array[1]
        print("Sequence: ", seq)
        SM2 = chirSM.SM2(seq)
        print("SM2: ", SM2)
        

Gly1 = 'OC(=O)C(N)'                             #G
Ala1 = 'OC(=O)C(N)C'                          #A
Ser1 = 'OC(=O)C(N)CO'                           #S
Asp1 = 'OC(=O)C(N)CC(=O)O'                    #D
Arg1 = 'OC(=O)C(N)CCCNC(=N)N'                #R
Val1 = 'OC(=O)C(N)C(C)(C)'                    #V
Thr1 = 'OC(=O)C(N)C(O)C'                      #T
Glu1 = 'OC(=O)C(N)CCC(=O)O'                   #E
Leu1 = 'OC(=O)C(N)CC(C)(C)'                   #L
Cys1 = 'OC(=O)C(N)CS'                         #C
His1 = 'OC(=O)C(N)CC1[N]=CNC=1'               #H
Lys1 = 'OC(=O)C(N)CCCC(N)'                    #K
Ile1 = 'OC(=O)C(N)C(C)CC'                     #I
Tyr1 = 'OC(=O)C(N)CC1=CC=C(O)C=C1'            #Y
Asn1 = 'OC(=O)C(N)CC(=O)(N)'                  #N
Met1 = 'OC(=O)C(N)CCSC'                       #? Met
Pro1 = 'OC(=O)C1CCCN1'                        #P
Trp1 = 'OC(=O)C(N)C(C1C2C=CC=CC=2N(H)C=1)'    #W
Phe1 = 'OC(=O)C(N)CC1=CC=CC=C1'               #F
Gln1 = 'OC(=O)C(N)CCC(=O)(N)'                 #Q

G1 = 'OC(=O)C(N)'                             #G
A1 = 'OC(=O)C(N)C'                          #A
S1 = 'OC(=O)C(N)CO'                          #S
D1 = 'OC(=O)C(N)CC(=O)O'                    #D
R1 = 'OC(=O)C(N)CCCNC(=N)N'                #R
V1 = 'OC(=O)C(N)C(C)(C)'                    #V
T1 = 'OC(=O)C(N)C(O)C'                      #T
E1 = 'OC(=O)C(N)CCC(=O)O'                   #E
L1 = 'OC(=O)C(N)CC(C)(C)'                   #L
C1 = 'OC(=O)C(N)CS'                         #C
H1 = 'OC(=O)C(N)CC1[N]=CNC=1'               #H
K1 = 'OC(=O)C(N)CCCC(N)'                    #K
I1 = 'OC(=O)C(N)C(C)CC'                     #I
Y1 = 'OC(=O)C(N)CC1=CC=C(O)C=C1'            #Y
N1 = 'OC(=O)C(N)CC(=O)(N)'                  #N
M1 = 'OC(=O)C(N)CCSC'                       #? Met
P1 = 'OC(=O)C1CCCN1'                        #P
W1 = 'OC(=O)C(N)C(C1C2C=CC=CC=2N(H)C=1)'    #W
F1 = 'OC(=O)C(N)CC1=CC=CC=C1'               #F
Q1 = 'OC(=O)C(N)CCC(=O)(N)'                 #Q

# G2 = 'OC(=O)C(N)'                             #G
# A2 = 'OC(=O)[C@H](N)C'                          #A
# S2 = 'OC(=O)[C@@H](N)CO'                          #S if seq[7]=='[' then if seq[10]=='@' then ...
# D2 = 'OC(=O)[C@@H](N)CC(=O)O'                    #D
# R2 = 'OC(=O)(N)CCCCNC(=NH)N'                #R
# V2 = 'OC(=O)C(N)C(C)(C)'                    #V
# T2 = 'OC(=O)C(N)C(O)C'                      #T
# E2 = 'OC(=O)[C@@H](N)CCC(=O)O'                   #E
# L2 = 'OC(=O)[C@H](N)CC(C)C'                   #L
# C2 = 'OC(=O)[C@@H](N)CS'                         #C
# H2 = 'OC(=O)C(N)CC1[N]=CNC=1'               #H
# K2 = 'OC(=O)[C@@H](N)CCCC(N)'                    #K
# I2 = 'OC(=O)[C@H](N)C(C)CC'                     #I
# Y2 = 'OC(=O)C(N)CC1=CC=C(O)C=C1'            #Y
# N2 = 'OC(=O)[C@@H](N)CC(=O)(N)'                  #N
# M2 = 'OC(=O)C(N)CCSC'                       #? Met
# P2 = 'OC(=O)C1CCCN1'                        #P
# W2 = 'OC(=O)[C@@H](N)C(C1C2C=CC=CC=2N(H)C=1)'    #W
# F2 = 'OC(=O)C(N)CC1=CC=CC=C1'               #F
# Q2 = 'OC(=O)[C@@H](N)CCC(=O)(N)'                 #Q

#Исправленное
G2 = 'OC(=O)C(N)'                             #G
A2 = 'OC(=O)[C@H](N)C'                          #A
S2 = 'OC(=O)[C@@H](N)CO'                          #S if seq[7]=='[' then if seq[10]=='@' then ...
D2 = 'OC(=O)[C@@H](N)CC(=O)O'                    #D
R2 = 'OC(=O)C(N)CCCNC(=N)N'                #R
V2 = 'OC(=O)[C@@H](N)C(C)(C)'                    #V
T2 = 'OC(=O)[C@@H](N)[C@H](O)C'                      #T
E2 = 'OC(=O)[C@@H](N)CCC(=O)O'                   #E
L2 = 'OC(=O)[C@@H](N)CC(C)C'                   #L
C2 = 'OC(=O)[C@@H](N)CS'                         #C
H2 = 'OC(=O)[C@@H](N)CC1[N]=CNC=1'               #H
K2 = 'OC(=O)[C@@H](N)CCCC(N)'                    #K
I2 = 'OC(=O)[C@@H](N)[C@H](C)CC'                     #I
Y2 = 'OC(=O)[C@@H](N)CC1=CC=C(O)C=C1'            #Y
N2 = 'OC(=O)[C@@H](N)CC(=O)(N)'                  #N
M2 = 'OC(=O)C(N)CCSC'                       #? Met
P2 = 'OC(=O)C1CCCN1'                        #P
W2 = 'OC(=O)[C@@H](N)C(C1C2C=CC=CC=2N(H)C=1)'    #W
F2 = 'OC(=O)[C@@H](N)CC1=CC=CC=C1'               #F
Q2 = 'OC(=O)[C@@H](N)CCC(=O)(N)'                 #Q




