#include <iostream>
#include <fstream>

using namespace std;


string read_fasta(string filename);
bool find_restriction_site(string seqeunce, string restriction_site);

int main()
{
    string sequence = read_fasta("COVID_Sequence.fasta");

    string restriction_sites[10] = {"AACGTT", "AAGCTT", "AATATT", "ACATGT", "CCTCAGC", "GAATTC", "GCGC", "GCGCGC", "GCGGCCGC", "TACGTA"};
    string restriction_names[10] = {"AclI", "HindIII", "SspI", "PciI", "BbvCI", "EcoRI", "HhaI", "BssHII", "NotI", "SnaBI"};

    cout << "Checking for patterns of splicing...." << endl;
    cout << "The following sites were checked: ";

    for (int i = 0; i < 10; i++)
    {
        cout << restriction_names[i] << "\t";
    }
    
    cout << endl << "The following restriction sites for found in the provided sequence..." << endl;

    for (int i = 0; i < 10; i++)
    {
        if (find_restriction_site(sequence, restriction_sites[i]))
        {
            cout << restriction_names[i] << " site was found..." << endl;
        }
    }

}

string read_fasta(string filename)
{
    //reads a fasta file and returns the sequence as a string
    string sequence;
    string line;

    fstream fastaFile(filename);

    //skips the first line
    getline(fastaFile, line);

    while (!fastaFile.eof())
    {
        getline(fastaFile, line);
        sequence += line;
    }

    return sequence;
}

bool find_restriction_site(string seqeunce, string restriction_site)
{
    int length = restriction_site.length();
    bool found = false;

    for (int i = 0; i < seqeunce.length() - length; i++)
    {
        if (seqeunce.substr(i, length) == restriction_site)
        {
            found = true;
        }

        if (found) { break; } 
    }
    return found;
}


