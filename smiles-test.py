# -*- coding: cp1251 -*-
from pyfaidx import Fasta
import numpy as np
import csv
import simpleSM
import chirSM


proteins = Fasta('C:\\Users\\Мария\\Documents\\Универ\\Магистратура\\Биоинформатика\\Магистерская\\SMILES\\PDB-all.fa')
for prot in proteins.keys():
    print(prot)
    seq = str(proteins[prot])
    print(seq)
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

#пїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅпїЅ
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
