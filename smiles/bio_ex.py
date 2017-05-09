from Bio import SeqIO
import numpy as np
import chirSM

count = 0
for record in  SeqIO.parse("PDB-part.fa", "fasta"):
    #print(record.id)
    #print(record.seq)
    count = count+1
print("count", count)

#
# print("")
# #
#mas = []

out_file = open("out_file.fasta", "w")
with open("PDB-part.fa", "rU") as handle:
    #mas.append([])
    #for e in range(count):
        for record in SeqIO.parse(handle, "fasta"):
            new_sequence = chirSM.SM2(record.seq)
            #mas[e]=chirSM.SM2(record.seq)
            out_file.write(record.id)
            out_file.write("\n")
            out_file.write('%s\n'%new_sequence)
            # print("Seq: ", record.seq)
            # print("SMILES: ", new_sequence)
            # print("")

# for i in mas:
#     out_file.write(str(i))
# out_file.close()
