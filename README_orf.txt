README for orf

Testing
To test the orf function, sequences can be passed in either as lines in a text file and the file name provided as a command line argument, or as a direct sequence entered in as a command line argument. If sequences are provided in a file, it should be a plain text file with separate sequences separated by newline characters. If entering a sequence directly, first enter 'S' as the first command line argument and then the sequence as the second command line argument. Sequences should only contain the characters A T G or C (U is allowed as will in place of T). Protein strings will be output to the command line, with reads listed under the corresponding sequence.

Input Examples:
file:           
$ python3 orf.py file_name.txt
direct sequence:
$ python3 S AUGCUCGUAGC

Output example:
Sequence:  AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG

Reads: 
M
MGMTPRLGLESLLE
MTPRLGLESLLE
MLLGSFRLIPKETLIQVAGSSPCNLS
M



Implementation summary
The orf function returns every amino acid sequence that can be translated from an open reading frame of the input DNA string. Two helper classes are used to implement the orf function, OrfReader and ReadingFrame. Further details on each class are stored in the SequenceReader module README.

At a high level, the OrfReader object reads the sequence 1 character at a time, checking at each character for a start codon. When a start codon is encountered, OrfReader will create a new ReadingFrame object. OrfReader passes each new character to all currently open ReadingFrame objects. ReadingFrame objects accept the characters passed in, and after every 3 characters translate the codon into an amino acid and append that character to that ReadingFrame's amino acid sequence. When a stop codon is encountered, the ReadingFrame changes it's status to closed.

The orf function creates an OrfReader and begins processing the passed in sequence. In addition, as it processes the sequence it transcribes each character into it's complement (A - T, G - C) and appends those to the left of the reverse compliment sequence. Once the end of the initial sequence is reached, the OrfReader is then used to read the reverse compliment, and finally the reads from orf reader are returned as a list of amino acid sequences.