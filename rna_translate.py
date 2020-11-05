"""
rna_translate module contains function to translate RNA sequences into amino
acid sequences.
"""
from SequenceReader import ReadingFrame
import sys

def rna_translate(rna_seq):
    """Translates passed in RNA sequence into amino acid sequenceself.

    Translation will begin at the first codon and end at the first stop codon
    ecountered. If the end of the string is reached before a stop codon, then
    the trailing characters (if any) are ignored and the existing amino acid
    sequence returned.
    """
    reading_frame  = ReadingFrame()
    for char in rna_seq:
        reading_frame.read(char)
        if not reading_frame.is_open:
            break
    return reading_frame.get_sequence()

def translate_file(file_name):
    """
    Reads in input file 1 line at a time and passes lines to rna_translate
    """
    with open(file_name) as file:
        for line in file:
            yield rna_translate(line)


if __name__ == "__main__":
    """Main testing routine.

    Enter either file path/name as command line argument, or 'S' followed by
    second command line argument containing typed in sequence.
    Examples:
    File:
    $ python3 rna_translate.py test_file.txt
    Direct sequence:
    $ python3 rna_translate.py S AUGGCCAUGGC
    """
    try:
        if sys.argv[1].upper() == 'S':
            try:
                print(rna_translate(sys.argv[2]))
            except IndexError:
                print("No second command line argument entered")
        else:
            for sequence in translate_file(sys.argv[1]):
                print(sequence)
    except KeyError:
        print("Invalid character foud. This could be due to file format (e.g. RTF)")
        print("File should be plain text and contain only A, U, C, and G")
    except IndexError:
        print("No command line argument entered")
