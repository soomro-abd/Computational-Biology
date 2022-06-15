#include <iostream>
#include <fstream>

using namespace std;

string read_fasta(string filename);
string reverse_sequence (string sequence);
string complement_sequence (string sequence);
string* get_orfs(string sequence);
bool is_stop_codon (string codon);

int main()
{
    string covid_sequence = read_fasta("COVID_Sequence.fasta");
    // cout << covid_sequence.length() << endl;
    string* orfs = get_orfs(covid_sequence);

    string best_orf = "";

    for (int i = 0; i < 6; i++)
    {
        bool inside_orf = false;
        string temp_orf = "";
        for (int j = 0; j < orfs[i].length(); j+=3)
        {
            string current_codon = orfs[i].substr(j,3);

            if (current_codon == "ATG" && inside_orf == false)
            { 
                    inside_orf = true;
            }
            else if (is_stop_codon(current_codon) && inside_orf)
            {
                temp_orf += "*";

                if (temp_orf.length() > best_orf.length()) { best_orf = temp_orf; }
                
                temp_orf = "";
                inside_orf = false;

            }
            else if (inside_orf)
            {
                if (current_codon == "TTT" || current_codon == "TTC") { temp_orf += "F"; }
                else if (current_codon == "TTA"|| current_codon == "TTG"|| current_codon == "CTT"|| current_codon == "CTC"|| current_codon == "CTA"|| current_codon == "CTG") { temp_orf += "L"; }
                else if (current_codon == "ATT"|| current_codon == "ATC"|| current_codon == "ATA") { temp_orf += "I"; }
                else if (current_codon == "ATG") { temp_orf += "M"; }
                else if (current_codon == "GTT"|| current_codon == "GTC"|| current_codon == "GTA"|| current_codon == "GTG") { temp_orf += "V"; }
                else if (current_codon == "TCT" || current_codon ==  "TCC"|| current_codon ==  "TCA"|| current_codon ==  "TCG"|| current_codon ==  "AGT"|| current_codon ==  "AGC") { temp_orf += "S"; }
                else if ( current_codon == "CCT" || current_codon == "CCC" || current_codon == "CCA" || current_codon == "CCG") { temp_orf += "P"; }
                else if ("ACT", "ACC", "ACA",  current_codon == "ACG") { temp_orf += "T"; }
                else if ("GCT", "GCC", "GCA",  current_codon == "GCG") { temp_orf += "A"; }
                else if ( current_codon == "TAT" || current_codon == "TAC") { temp_orf += "Y"; }
                else if ( current_codon == "CAT" || current_codon == "CAC") { temp_orf += "H"; }
                else if ( current_codon == "CAA" || current_codon == "CAG") { temp_orf += "Q"; }
                else if ( current_codon == "AAT" || current_codon == "AAC") { temp_orf += "N"; }
                else if ( current_codon == "AAA" || current_codon == "AAG") { temp_orf += "K"; }
                else if ( current_codon == "GAT" || current_codon == "GAC") { temp_orf += "D"; }
                else if ( current_codon == "GAA" || current_codon == "GAG") { temp_orf += "E"; }
                else if ( current_codon == "TGT" || current_codon == "TGC") { temp_orf += "C"; }
                else if ( current_codon == "TGG") { temp_orf += "W"; }
                else if ( current_codon == "CGT" || current_codon == "CGC" || current_codon == "CGA" || current_codon == "CGG" || current_codon == "AGA" || current_codon == "AGG") { temp_orf += "R"; }
                else if ( current_codon == "GGT" || current_codon == "GGC" || current_codon == "GGA" || current_codon == "GGG") { temp_orf += "G"; }
            }
        }
    }

    cout << best_orf << endl;


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

bool is_stop_codon (string codon) { return ((codon == "TAA") || (codon == "TAG") || (codon == "TGA")); }




