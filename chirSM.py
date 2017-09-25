def SM2(seq):
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
    #Y2 = 'OC(=O)[C@@H](N)CC1=CC=C(O)C=C1'            #Y
    Y2 = 'OC(=O)[C@@H](N)Cc1ccc(O)cc1'
    N2 = 'OC(=O)[C@@H](N)CC(=O)(N)'                  #N
    M2 = 'OC(=O)C(N)CCSC'                       #? Met
    P2 = 'OC(=O)C1CCCN1'                        #P
    #W2 = 'OC(=O)[C@@H](N)C(C1C2C=CC=CC=2N(H)C=1)'    #W
    W2 = 'OC(=O)[C@@H](N)C(c1c2ccccc2N(H)c1)'
    #F2 = 'OC(=O)[C@@H](N)CC1=CC=CC=C1'               #F
    F2 = 'OC(=O)[C@@H](N)Cc1ccccc1'
    Q2 = 'OC(=O)[C@@H](N)CCC(=O)(N)'                 #Q
    SM2 = ''
    list2 = ['G', 'A', 'S', 'R', 'D', 'V', 'T', 'E', 'L', 'C', 'H', 'K', 'I', 'Y', 'N', 'M', 'P', 'W', 'F', 'Q']
    for l in list2:
        if seq[1]==l:
            if l=='G':
                SM2 = 'C'
            if l=='R':
                SM2 = 'NC(=N)NCCC' + 'C'
            #if l=='V':
                #SM2 = V2[11:len(V2)]+'C'
            #if l=='T':
                #SM2 = T2[11:len(T2)]+'C'
            #if l=='H':
                #SM2 = H2[11:len(H2)]+'C'
            #if l=='Y':
                #SM2 = Y2[11:len(Y2)]+'C'
            if l=='M':
                SM2 = 'CSCC' +'C'
    ##        if l=='P':
    ##            SM2 = P2[10:len(P2)]+'C'
            #if l=='F':
                #SM2 = F2[11:len(F2)]+'C'

           # if seq[10]=='@':
    ##       if l=='S':
    ##            SM = S2[16:len(S2)]+'C'

            if l=='A':
                SM2 = A2[14:len(A2)]+'[C@H]'
            # if l=='L':
                # SM2 = L2[15:len(L2)]+'C'
            # if l=='I':
                # SM2 = I2[15:len(I2)]+'C'


            if l=='F':
                SM2 = F2[16:len(F2)]+'C[C@@H]'  #Чтобы был поворот
            if l=='L':
                SM2 = L2[15:len(L2)]+'[C@@H]'
            if l=='I':
                SM2 = 'CC[C@H](C)' +'[C@@H]'
            if l=='N':
                SM2 = N2[16:len(N2)]+'C[C@@H]'
            if l=='Y':
                SM2 = 'C1=CC(O)=CC=C1' +'C[C@@H]'  #Чтобы был поворот
            if l=='H':
                SM2 = H2[16:len(H2)]+'C[C@@H]'   #Чтобы был поворот
            if l=='T':
                SM2 = 'C[C@H](O)' +'[C@@H]'
            if l=='V':
                SM2 = V2[15:len(V2)]+'[C@@H]'
            if l=='S':
                SM2 = S2[15:len(S2)]+'[C@@H]'
            if l=='D':
                SM2 = D2[15:len(D2)]+'[C@@H]'
            # if l=='R':
                # SM2 = R2[16:len(R2)]+'C'
            if l=='E':
                SM2 = 'OC(=O)CC' +'[C@@H]'
            if l=='C':
                SM2 = 'SC' +'[C@@H]'
            if l=='K':
                SM2 = '(N)' + K2[15:(len(K2)-3)]+'[C@@H]'
            # if l=='N':
                # SM2 = N2[16:len(N2)]+'C'
            if l=='W':
                SM2 = W2[15:len(W2)]+'[C@@H]'
            if l=='Q':
                SM2 = 'NC(=O)CC' +'[C@@H]'
            SM2 = SM2 + '(N'

            if seq[0]=='G':
                SM2 = SM2 + G2[1:len(G2)]
            if seq[0]=='A':
                SM2 = SM2 + A2[1:len(A2)]
            if seq[0]=='S':
                SM2 = SM2 + S2[1:len(S2)]
            if seq[0]=='D':
                SM2 = SM2 + D2[1:len(D2)]
            if seq[0]=='R':
                SM2 = SM2 + R2[1:len(R2)]
            if seq[0]=='V':
                SM2 = SM2 + V2[1:len(V2)]
            if seq[0]=='T':
                SM2 = SM2 + T2[1:len(T2)]
            if seq[0]=='E':
                SM2 = SM2 + E2[1:len(E2)]
            if seq[0]=='L':
                SM2 = SM2 + L2[1:len(L2)]
            if seq[0]=='C':
                SM2 = SM2 + C2[1:len(C2)]
            if seq[0]=='H':
                SM2 = SM2 + H2[1:len(H2)]
            if seq[0]=='K':
                SM2 = SM2 + K2[1:len(K2)]
            if seq[0]=='I':
                SM2 = SM2 + I2[1:len(I2)]
            if seq[0]=='Y':
                SM2 = SM2 + Y2[1:len(Y2)]
            if seq[0]=='N':
                SM2 = SM2 + N2[1:len(N2)]
            if seq[0]=='M':
                SM2 = SM2 + M2[1:len(M2)]
            if seq[0]=='P':
                SM2 = SM2 + P2[1:len(P2)]
            if seq[0]=='W':
                SM2 = SM2 + W2[1:len(W2)]
            if seq[0]=='F':
                SM2 = SM2 + F2[1:len(F2)]
            if seq[0]=='Q':
                SM2 = SM2 + Q2[1:len(Q2)]
            SM2 = SM2 + ')'

            if l=='P':
                SM2 = 'N1('
                if seq[0]=='G':
                    SM2 = SM2 + G2[1:len(G2)]
                if seq[0]=='A':
                    SM2 = SM2 + A2[1:len(A2)]
                if seq[0]=='S':
                    SM2 = SM2 + S2[1:len(S2)]
                if seq[0]=='D':
                    SM2 = SM2 + D2[1:len(D2)]
                if seq[0]=='R':
                    SM2 = SM2 + R2[1:len(R2)]
                if seq[0]=='V':
                    SM2 = SM2 + V2[1:len(V2)]
                if seq[0]=='T':
                    SM2 = SM2 + T2[1:len(T2)]
                if seq[0]=='E':
                    SM2 = SM2 + E2[1:len(E2)]
                if seq[0]=='L':
                    SM2 = SM2 + L2[1:len(L2)]
                if seq[0]=='C':
                    SM2 = SM2 + C2[1:len(C2)]
                if seq[0]=='H':
                    SM2 = SM2 + H2[1:len(H2)]
                if seq[0]=='K':
                    SM2 = SM2 + K2[1:len(K2)]
                if seq[0]=='I':
                    SM2 = SM2 + I2[1:len(I2)]
                if seq[0]=='Y':
                    SM2 = SM2 + Y2[1:len(Y2)]
                if seq[0]=='N':
                    SM2 = SM2 + N2[1:len(N2)]
                if seq[0]=='M':
                    SM2 = SM2 + M2[1:len(M2)]
                if seq[0]=='P':
                    SM2 = SM2 + P2[1:len(P2)]
                if seq[0]=='W':
                    SM2 = SM2 + W2[1:len(W2)]
                if seq[0]=='F':
                    SM2 = SM2 + F2[1:len(F2)]

            SM2 = SM2 + ')CCCC1'

    for j in seq[2:len(seq)]:
        if j=='P':
            SM2 = SM2 + 'C(=O)N1CCCC1'
        else:
            SM2 = SM2 + 'C(=O)N'  #а здесь атом С с хиральностью!!! Соответственно, есть разделение
            if j=='G':
                SM2 = SM2 + 'C'
            if j=='R':
                SM2 = SM2 + 'C(' + R2[10:len(R2)] + ')'
            # if j=='V':
                # SM2 = SM2 + 'C(' + V2[10:len(V2)] + ')'
            # if j=='T':
                # SM2 = SM2 + 'C(' + T2[10:len(T2)] + ')'
            # if j=='H':
                # SM2 = SM2 + 'C(' + H2[10:len(H2)] + ')'
            # if j=='Y':
                # SM2 = SM2 + 'C(' + Y2[10:len(Y2)] + ')'
            if j=='M':
                SM2 = SM2 + 'C(' + M2[10:len(M2)] + ')'
        ##    if j=='P':
        ##        SM2 = SM2 + 'C(' + P2[10:len(P2)] + ')'
            # if j=='F':
                # SM2 = SM2 + 'C(' + F2[10:len(F2)] + ')'


            if j=='A':
                SM2 = SM2 + '[C@H](' + A2[14:len(A2)] + ')'
            # if j=='L':
                # SM2 = SM2 + '[C@H](' + L2[14:len(L2)] + ')'
            # if j=='I':
                # SM2 = SM2 + '[C@H](' + I2[14:len(I2)] + ')'


            if l=='F':
                SM2 = SM2 + '[C@@H](' + F2[15:len(F2)] + ')'
            if j=='L':
                SM2 = SM2 + '[C@@H](' + L2[15:len(L2)] + ')'
            if j=='I':
                SM2 = SM2 + '[C@@H](' + I2[15:len(I2)] + ')'
            if j=='V':
                SM2 = SM2 + '[C@@H](' + V2[15:len(V2)] + ')'
            if j=='T':
                SM2 = SM2 + '[C@@H](' + T2[15:len(T2)] + ')'
            if j=='H':
                SM2 = SM2 + '[C@@H](' + H2[15:len(H2)] + ')'
            if j=='Y':
                SM2 = SM2 + '[C@@H](' + Y2[15:len(Y2)] + ')'
            if j=='N':
                SM2 = SM2 + '[C@@H](' + N2[15:len(N2)] + ')'
            if j=='S':
                SM2 = SM2 + '[C@@H](' + S2[15:len(S2)] + ')'
            if j=='D':
                SM2 = SM2 + '[C@@H](' + D2[15:len(D2)] + ')'
            # if j=='R':
                # SM2 = SM2 + '[C@@H](' + R2[15:len(R2)] + ')'
            if j=='E':
                SM2 = SM2 + '[C@@H](' + E2[15:len(E2)] + ')'
            if j=='C':
                SM2 = SM2 + '[C@@H](' + C2[15:len(C2)] + ')'
            if j=='K':
                SM2 = SM2 + '[C@@H](' + K2[15:len(K2)] + ')'
            # if j=='N':
                # SM2 = SM2 + '[C@@H](' + N2[15:len(N2)] + ')'
            if j=='W':
                SM2 = SM2 + '[C@@H](' + W2[15:len(W2)] + ')'
            if j=='Q':
                SM2 = SM2 + '[C@@H](' + Q2[15:len(Q2)] + ')'

    SM2 = SM2 +'C(=O)O'
    return SM2
