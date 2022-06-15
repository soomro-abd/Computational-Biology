""" 
Write a program that takes any PDB file as input
and output the following details 
    • Amino acid sequence
    • Number of hydrophobic residues
    • Number of protein chains
    • Number of helices
    • Number of sheets
"""


def readPDB(filename):
    """

    Arguments: 
    filename - String

    Returns:
    residues - List
    """

    myFile = open(filename, 'r')
    lines = myFile.readlines()

    residues = []

    for line in lines:

        if (line[0:6] == 'SEQRES'):
            temp = line[18:]
            temp = temp.split()

            residues += temp

    return residues

def aminoAcidSequence(residues):
    """
    
    Arguments:
    residues - List

    Return:
    String - A string of residues
    """

    return " ".join(residues)

def countHydrophobic(residues):
    """
    Arguments:
    residues - List

    Return:
    Int - The number of hydrophobic residues
    """

    """
    The nine amino acids that have hydrophobic side chains are
    glycine (Gly), alanine (Ala), valine (Val), leucine (Leu),
    isoleucine (Ile), proline (Pro), phenylalanine (Phe),
    methionine (Met), and tryptophan (Trp).
    """

    hpResidues = ["GLY", "ALA", "VAL", "LEU", "ILE", "PRO", "PHE", "MET", "TRP"]
    hpCount = 0

    for residue in residues:
        if residue in hpResidues:
            hpCount += 1

    return hpCount

def countHelices(filename):
    """
      
      Arguments:
      filename - String

      Returns:
      Int - Number of helices in the protein
    """

    myFile = open(filename, 'r')
    lines = myFile.readlines()

    temp = []

    for line in lines:
        if (line[0:5] == 'HELIX'):
            temp += line[11:14]

    return temp[-1]

def countSheets(filename):
    """
      
      Arguments:
      filename - String

      Returns:
      Int - Number of sheets in the protein
    """

    myFile = open(filename, 'r')
    lines = myFile.readlines()

    temp = []

    for line in lines:
        if (line[0:5] == 'SHEET'):
            temp += line[11:14]

    return temp[-1]

def countChains(filename):
    """
    
    Arguments: 
    filename - String

    Returns:
    Int - Number of chains in the protein
    """

    myFile = open(filename, 'r')
    lines = myFile.readlines()

    temp = []

    for line in lines:
        if (line[0:6] == 'SEQRES'):

            #the elevent character is the chain name, ex: 'A'
            temp += line[11]

    #type casting the list of chains to set removes duplicates
    temp = set(temp)

    #the length of the temp set is the number of chains
    return len(temp)


if __name__ == "__main__":

    residues = readPDB('5chb.pdb')
    print(len(residues))
    # print("Residues: ", aminoAcidSequence(residues))
    # print("Hydrophobic Residues: ", countHydrophobic(residues))
    # print("Chains: ", countChains('5chb.pdb'))
    # print("Helices: ", countHelices('5chb.pdb'))
    # print("Sheets: ", countSheets('5chb.pdb'))


