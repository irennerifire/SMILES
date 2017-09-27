from Bio import SeqIO
from rdkit import Chem
from rdkit.Chem import AllChem
import numpy as np
import chirSM
from rdkit import DataStructs
from rdkit import rdBase
from rdkit.Chem.Fingerprints import FingerprintMols
from rdkit.Chem import Draw
from prody import *

# m1 = Chem.MolFromSmiles('Cc1ccccc1')
# fp1 = AllChem.GetMorganFingerprint(m1,2)
# print(fp1)

# out_file = open("out_pro3.fasta", "w")
# with open("one_pro3.fa", "rU") as handle:
#     #mas.append([])
#     #for e in range(count):
#         for record in SeqIO.parse(handle, "fasta"):
#             new_sequence = chirSM.SM2(record.seq)
#             #mas[e]=chirSM.SM2(record.seq)
#             out_file.write(">")
#             out_file.write(record.id)
#             out_file.write("\n")
#             out_file.write('%s\n'%new_sequence)

bi = {}
#m = Chem.MolFromSmiles("C(NC(=O)[C@@H](N)CCC(=O)(N))C(=O)N[C@@H](CCC(=O)(N))C(=O)N[C@@H](CO)C(=O)N[C@@H](Cc1c2ccccc2N(H)c1)C(=O)O")
#Draw.MolToFile(m, 'mol.png', size=(600,400), kekulize=True, wedgeBonds=True, imageType=None, fitImage=True)
#fp1 = AllChem.GetMorganFingerprintAsBitVect(m,radius = 2, nBits = 1024, useBondTypes=False)
#print(fp1)

# def sliding_window(aminoacids, width=20):
#     """
#     iterates over residues in given chain, returns iterator
#     with arrays containing each width elements (as a sliding window)
#     """
#     index = 1 # prody starts iteration from 1, or at least it seems
#     aa_list = [ aminoacids[index + offset] for offset in range(width) ]
#     yield aa_list
#     offset = 0
#     while width+offset < len(aminoacids):
#         aa_list.pop(0)
#         aa_list.append(aminoacids[width + offset])
#         yield aa_list
#         offset += 1
#
# def get_aminoacid_sequence(fragment):
#     """
#     gets list of Aminoacid elements as an input
#     returns aminoacid sequence as a string containing 1-letter IUPAC codes
#     """
#     get = prody.atomic.chain.AAMAP.get
#     return ''.join([get(res.getResname(), 'X') for res in fragment])


def slidingWindow(sequence,winSize,step=3):
    """Returns a generator that will iterate through
    the defined chunks of input sequence.  Input sequence
    must be iterable."""

    # Verify the inputs
    try: it = iter(sequence)
    except TypeError:
        raise Exception("**ERROR** sequence must be iterable.")
    if not ((type(winSize) == type(0)) and (type(step) == type(0))):
        raise Exception("**ERROR** type(winSize) and type(step) must be int.")
    if step > winSize:
        raise Exception("**ERROR** step must not be larger than winSize.")
    if winSize > len(sequence):
        raise Exception("**ERROR** winSize must not be larger than sequence length.")

    # Pre-compute number of chunks to emit
    print(len(sequence))
    print(len(sequence)-winSize)
    print((len(sequence)-winSize)/step)
    numOfChunks = int(((len(sequence)-winSize)/step)+1)

    # Do the work
    for i in range(0,numOfChunks*step,step):
        yield sequence[i:i+winSize]

i = 0
out_file = open("fingerprints.fasta", "w")
#with open("out_pro.fasta", "rU") as handle:
with open("one_pro.fa", "rU") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            print("seq  ", record.seq)
            chunks = slidingWindow(str(record.seq), int(5) )
            for chunk in chunks:
                i = i+1
                print("chunk= ", chunk)
                SM = chirSM.SM2(chunk)
                m = Chem.MolFromSmiles(SM)
                print("m    ", m)
                fp = AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=1024, useBondTypes=False)
                print("fp       ",   fp)
                out_file.write("chunk №")
                out_file.write(str(i))
                out_file.write("\n")
                out_file.write(chunk)
                out_file.write("\n")
                out_file.write("chunk_smiles")
                out_file.write("\n")
                out_file.write(SM)
                out_file.write("\n")
                out_file.write("fp")
                out_file.write("\n")
                out_file.write('%s\n'%fp)


# j = 0
# out_file = open("fingerprints_PDB-part.fasta", "w")
# #with open("out_pro.fasta", "rU") as handle:
# with open("PDB-part.fa", "rU") as handle:
#         for record in SeqIO.parse(handle, "fasta"):
#             print("seq  ", record.seq)
#             chunks = slidingWindow(str(record.seq), int(5) )
#             for chunk in chunks:
#                 j = j+1
#                 SM = chirSM.SM2(chunk)
#                 m = Chem.MolFromSmiles(SM)
#                 print("m    ", m)
#                 fp = AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=1024)
#                 print("fp       ",   fp)
#                 out_file.write("chunk №")
#                 out_file.write(str(j))
#                 out_file.write("\n")
#                 out_file.write(chunk)
#                 out_file.write("\n")
#                 out_file.write("chunk_smiles")
#                 out_file.write("\n")
#                 out_file.write(SM)
#                 out_file.write("\n")
#                 out_file.write("fp")
#                 out_file.write("\n")
#                 out_file.write('%s\n'%fp)

# out_file = open("fingerprints.fasta", "w")
# bi = {}
# with open("one_pro.fa", "rU") as handle:
#         for record in SeqIO.parse(handle, "fasta"):
#             print("seq  ", record.seq)
#             for frag in sliding_window(record.seq):
#                 #m = Chem.MolFromSmiles(record.seq, isomericSmiles=True, kekuleSmiles=True)
#                 #s = str(record.seq)
#                 #print(s)
#                 #get_aminoacid_sequence(frag)
#                 print("fragment         ", frag)
#                 m = Chem.MolFromSmiles(str(frag))
#                 #Draw.MolToFile(m, 'mol.png', size=(600,400), kekulize=True, wedgeBonds=True, imageType=None, fitImage=True)
#                 print("m    ", m)
                #fp = AllChem.GetMorganFingerprintAsBitVect(m,radius = 2, nBits = 2048, bitInfo=bi)
                #fp = AllChem.GetMorganFingerprintAsBitVect(m, 2, nBits=1024)
                # out_file.write(frag)
                # print("frag:    ", frag)
                # out_file.write("\n")
                # out_file.write('%s\n'%fp)
                # print("fp       ",   fp)
