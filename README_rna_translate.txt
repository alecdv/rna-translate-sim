README for rna_translate

Testing
To test the rna_translate function, sequences can be passed in either as lines in a text file and the file name provided as a command line argument, or as a direct sequence entered in as a command line argument. If sequences are provided in a file, it should be a plain text file with separate sequences separated by newline characters. If entering a sequence directly, first enter 'S' as the first command line argument and then the sequence as the second command line argument. Sequences should only contain the characters A T G or C (U is allowed as will in place of T). Protein strings will be output to the command line.


Examples:
file:           
$ python3 orf.py file_name.txt
direct sequence:
$ python3 S AUGCUCGUAGC


Implementation summary
The rna_translate function creates a ReadingFrame object and processes the passed in RNA sequence into an amino acid sequence. For details on ReadingFrame object implementation, see the SequenceReader module README. At a high level, every 3 RNA base characters passed to the ReadingFrame object will be translated into the codon's corresponding amino acid and that amino acid character is appended to the ReadingFrame protein sequence. When a stop codon is encountered, the ReadingFrame will switch from open to closed. In the rna_translate function, the characters are translated starting at the beggining of the sequence, at translation is terminated when a stop codon is reached. Characters after a stop codon, or trailing 1 or 2 characters will be ignored. If no stop codon is encountered, the current protein sequence will be returned.