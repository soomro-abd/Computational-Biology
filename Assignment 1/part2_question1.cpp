#include <iostream>
#include <fstream>

using namespace std;

string read_fasta(string filename);
string reverse_sequence (string sequence);
string complement_sequence (string sequence);
string* get_orfs(string sequence);

int main()
{
    string covid_sequence = read_fasta("COVID_Sequence.fasta");
    // cout << covid_sequence.length() << endl;
    string* orfs = get_orfs(covid_sequence);

    for (int i = 0; i < 6; i++)
    { 
        cout << "Index of Start Codons in ORF " << i + 1 << ": "; 
        for (int j = 0; j < orfs[i].length(); j+=3)
        {
            if (orfs[i].substr(j,3) == "ATG") { cout << j << "\t"; }
        } 

        cout << endl << endl;
    }
    
    delete[] orfs;
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

string reverse_sequence(string sequence)
{
    //takes a string and reverse it
    string rev_seq = "";

    for (int i = sequence.length() - 1; i >= 0 ; i--) { rev_seq += sequence[i]; }

    return rev_seq;
}

string complement_sequence(string sequence)
{
    //takes a DNA sequence and complements it
    string comp_seq = "";
    
    for (int i= 0; i < sequence.length(); i++)
    {
        switch (sequence[i])
        {
        case 'A':
            comp_seq += 'T';
            break;
        case 'C':
            comp_seq += 'G';
            break;
        case 'G':
            comp_seq += 'C';
            break;
        case 'T':
            comp_seq += 'A';
            break;
        default:
            break;
        }
    }

    return comp_seq;
}

string *get_orfs(string sequence)
{
    string *orfs = new string[6];
    int length = sequence.length();
    string rev_comp_sequence = complement_sequence(reverse_sequence(sequence));

    orfs[0] = sequence;
    orfs[1] = sequence.substr(1, length - 1);
    orfs[2] = sequence.substr(2, length - 2);
    orfs[3] = rev_comp_sequence;
    orfs[4] = rev_comp_sequence.substr(1, length - 1);
    orfs[5] = rev_comp_sequence.substr(2, length - 2);

    return orfs; 
}
