def SM(seq):
    SM=''
    list1 = ['G', 'A', 'S', 'R', 'D', 'V', 'T', 'E', 'L', 'C', 'H', 'K', 'I', 'Y', 'N', 'M', 'P', 'W', 'F', 'Q']

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
    #Y1 = 'OC(=O)C(N)CC1=CC=C(O)C=C1'            #Y
    Y1 = 'OC(=O)C(N)Cc1ccc(O)cc1'
    N1 = 'OC(=O)C(N)CC(=O)(N)'                  #N
    M1 = 'OC(=O)C(N)CCSC'                       #? Met
    P1 = 'OC(=O)C1CCCN1'                        #P
    #W1 = 'OC(=O)C(N)C(C1C2C=CC=CC=2N(H)C=1)'    #W
    W1 = 'OC(=O)C(N)C(c1c2ccccc2N(H)c1)'
    #F1 = 'OC(=O)C(N)CC1=CC=CC=C1'               #F
    F1 = 'OC(=O)C(N)Cc1ccccc1'
    Q1 = 'OC(=O)C(N)CCC(=O)(N)'                 #Q

    for l in list1:
        if seq[1]==l:
            if l=='G':
                SM = 'C'
            if l=='A':
                SM = A1[11:len(A1)]+'C'
            if l=='S':
                SM = S1[11:len(S1)]+'C'
            if l=='D':
                SM = D1[11:len(D1)]+'C'
            if l=='R':
                SM = R1[11:len(R1)]+'C'
            if l=='V':
                SM = V1[11:len(V1)]+'C'
            if l=='T':
                SM = T1[11:len(T1)]+'C'
            if l=='E':
                SM = E1[11:len(E1)]+'C'
            if l=='L':
                SM = L1[11:len(L1)]+'C'
            if l=='C':
                SM = C1[11:len(C1)]+'C'
            if l=='H':
                SM = H1[11:len(H1)]+'C'
            if l=='K':
                SM = K1[11:len(K1)]+'C'
            if l=='I':
                SM = I1[11:len(I1)]+'C'
            if l=='Y':
                SM = Y1[11:len(Y1)]+'C'
            if l=='N':
                SM = N1[11:len(N1)]+'C'
            if l=='M':
                SM = M1[11:len(M1)]+'C'
            if l=='P':
                SM = P1[11:len(P1)]+'C'
            if l=='W':
                SM = W1[11:len(W1)]+'C'
            if l=='F':
                SM = F1[11:len(F1)]+'C'
            if l=='Q':
                SM = Q1[11:len(Q1)]+'C'
            SM = SM + '(N'
            if seq[0]=='G':
                SM = SM + G1[1:len(G1)]
            if seq[0]=='A':
                SM = SM + A1[1:len(A1)]
            if seq[0]=='S':
                SM = SM + S1[1:len(S1)]
            if seq[0]=='D':
                SM = SM + D1[1:len(D1)]
            if seq[0]=='R':
                SM = SM + R1[1:len(R1)]
            if seq[0]=='V':
                SM = SM + V1[1:len(V1)]
            if seq[0]=='T':
                SM = SM + T1[1:len(T1)]
            if seq[0]=='E':
                SM = SM + E1[1:len(E1)]
            if seq[0]=='L':
                SM = SM + L1[1:len(L1)]
            if seq[0]=='C':
                SM = SM + C1[1:len(C1)]
            if seq[0]=='H':
                SM = SM + H1[1:len(H1)]
            if seq[0]=='K':
                SM = SM + K1[1:len(K1)]
            if seq[0]=='I':
                SM = SM + I1[1:len(I1)]
            if seq[0]=='Y':
                SM = SM + Y1[1:len(Y1)]
            if seq[0]=='N':
                SM = SM + N1[1:len(N1)]
            if seq[0]=='M':
                SM = SM + M1[1:len(M1)]
            if seq[0]=='P':
                SM = SM + P1[1:len(P1)]
            if seq[0]=='W':
                SM = SM + W1[1:len(W1)]
            if seq[0]=='F':
                SM = SM + F1[1:len(F1)]
            if seq[0]=='Q':
                SM = SM + Q1[1:len(Q1)]
            SM = SM + ')'

    for j in seq[2:len(seq)]:
        SM = SM + 'C(=O)NC'
        if j=='G':
            SM = SM
        if j=='A':
            SM = SM + '(' + A1[10:len(A1)] + ')'
        if j=='S':
            SM = SM + '(' + S1[10:len(S1)] + ')'
        if j=='D':
            SM = SM + '(' + D1[10:len(D1)] + ')'
        if j=='R':
            SM = SM + '(' + R1[10:len(R1)] + ')'
        if j=='V':
            SM = SM + '(' + V1[10:len(V1)] + ')'
        if j=='T':
            SM = SM + '(' + T1[10:len(T1)] + ')'
        if j=='E':
            SM = SM + '(' + E1[10:len(E1)] + ')'
        if j=='L':
            SM = SM + '(' + L1[10:len(L1)] + ')'
        if j=='C':
            SM = SM + '(' + C1[10:len(C1)] + ')'
        if j=='H':
            SM = SM + '(' + H1[10:len(H1)] + ')'
        if j=='K':
            SM = SM + '(' + K1[10:len(K1)] + ')'
        if j=='I':
            SM = SM + '(' + I1[10:len(I1)] + ')'
        if j=='Y':
            SM = SM + '(' + Y1[10:len(Y1)] + ')'
        if j=='N':
            SM = SM + '(' + N1[10:len(N1)] + ')'
        if j=='M':
            SM = SM + '(' + M1[10:len(M1)] + ')'
        if j=='P':
            SM = SM + '(' + P1[10:len(P1)] + ')'
        if j=='W':
            SM = SM + '(' + W1[10:len(W1)] + ')'
        if j=='F':
            SM = SM + '(' + F1[10:len(F1)] + ')'
        if j=='Q':
            SM = SM + '(' + Q1[10:len(Q1)] + ')'
    SM = SM +'C(=O)O'
    return SM
