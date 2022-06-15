""" Write a program that takes a DNA sequence as input and output six reading frames, and their amino acid sequence """



def reverse(sequence):
    """
    
    Arguments:
    sequence : String

    Returns:
    Reversed DNA Sequence : String
    """

    return sequence[::-1]

def complement(sequence):
    """

    Arguments:
    sequence : String

    Returns:
    Complement of the DNA Sequence : String
    """

    result = "" #the variable that will store the complemented seqeunce
    complements = {'A':'T', 'T':'A', 'C':'G', 'G':'C'} #a dictionary that helps us find the complement of every nucleotide


    #iterating through the sequence and appending the complement in the "result"
    for nucleotide in sequence:
        result += complements[nucleotide]

    return result


def find_orfs(sequence):
    """
    
    Arguments: 
    sequence : String

    Returns:
    A List of Six Strings (ORFs) - List of Type String
    """
    
    orfs = [] #the list that will store the six orfs

    orfs.append(sequence) #append the first orf to the empty list
    orfs.append(sequence[1:])  #append the second orf (one nucleotide shift) to the list containing first orf
    orfs.append(sequence[2:]) #append the third orf (two nucleotide shift)

    reverse_complement = complement(reverse(sequence)) #stores the second strand in a variable for ease

    orfs.append(reverse_complement) #append the fourth orf (the secondary strand, from the 5' end)
    orfs.append(reverse_complement[1:]) #append the fifth orf (secondary orf with 1 nucleotide shift)
    orfs.append(reverse_complement[2:]) #append the sixth orf (secondary orf with 2 nucleotide shift)

    return orfs


def transcription(sequence):
    """

    Arguments:
    sequence - String

    Returns:
    Residues - A list containing six amino acid sequences (List of Type String)
    """

    orfs = find_orfs(sequence)

    residues = [] #the list that will contain the residues
    codon_to_aa = {
        "ATG" : 'M',
        "TTT" : 'F', "TTC" : 'F',
        "TTA" : 'L', "TTG" : 'L', "CTT" : 'L', "CTC" : 'L', "CTA" : 'L', "CTG" : 'L',
        "ATT" : 'I', "ATC" : 'I', "ATA" : 'I',
        "GTT" : 'V', "GTC" : 'V', "GTA" : 'V', "GTG" : 'V',
        "TCT" : 'S', "TCC" : 'S', "TCA" : 'S', "TCG" : 'S', "AGT" : 'S', "AGC" : 'S',
        "CCT" : 'P', "CCC" : 'P', "CCA" : 'P', "CCG" : 'P',
        "ACT" : 'T', "ACC" : 'T', "ACA" : 'T', "ACG" : 'T',
        "GCT" : 'A', "GCC" : 'A', "GCA" : 'A', "GCG" : 'A',
        "TAT" : 'Y', "TAC" : 'Y',
        "CAT" : 'H', "CAC" : 'H',
        "CAA" : 'Q', "CAG" : 'Q',
        "AAT" : 'N', "AAC" : 'N',
        "AAA" : 'K', "AAG" : 'K',
        "GAT" : 'D', "GAC" : 'D',
        "GAA" : 'E', "GAG" : 'E',
        "TGT" : 'C', "TGC" : 'C',
        "TGG" : 'W',
        "CGT" : 'R', "CGC" : 'R', "CGA" : 'R', "CGG" : 'R', "AGA" : 'R', "AGG" : 'R',
        "GGT" : 'G', "GGC" : 'G', "GGA" : 'G', "GGG" : 'G',
        "TAA" : '*', "TAG" : '*', "TGA" : '*'
        }

    for orf in orfs:
        residue = "" #the string that will contain the aa sequence of a particular orf

        #this loop iterates through every orf with a step of 3
        for i in range(0, len(orf), 3):
            if orf[i+2:]:
                codon = orf[i:i+3]
                residue += codon_to_aa[codon]
        
        #when the loop finished, add the residue to the list of residues
        residues.append(residue)

    return residues

def print_dna(sequence):
    """
    
    Arguments:
    sequence - String

    Returns:
    Nothing
    """

    for index, char in enumerate(sequence):
        
        if (index % 3 == 0):
            print(" ", end = "")
        
        print(char, end = "")
            

def master(sequence):
    """

    Arguments:
    sequence - String

    Returns:
    Nothing
    """

    orfs = find_orfs(sequence)
    residues = transcription(sequence)

    for index, orf in enumerate(orfs):
        print(f"ORF # {index + 1}:")
        print(f"Nucleotide Length : {len(orf)}, \t Amino Acid Length: {len(residues[index])}")
        print("Sequence : ", end = "") ; print_dna(orf) ; print("")
        print(f"Amino Acid Sequence : {residues[index]} \n\n\n")





if __name__ == "__main__":
    
    test_seq = 'accttgggttagtgcatgctctgattctctcactcaccaacatgtgcgagcataaggctatcggaccttgccgatcggggctaaaacatttaggtcggag'
    test_seq = test_seq.upper()
    
    master(test_seq)