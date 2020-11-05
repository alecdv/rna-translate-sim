"""
orf module implements a function to generate all amino acid sequences from open
reading frames of an input RNA or DNA base sequence.
"""
import SequenceReader
from collections import deque
import sys


def orf(sequence):
    """Produces all amino acid strings possible from an open
    reading frame of the passed in sequenceself.

    Sequence may be any iterable object, and should be a valid RNA or DNA sequence
    containing only the characters 'A', 'T', 'G', 'C', or 'U'
    """
    reads = []
    rev_comp = deque()
    seq_reader = SequenceReader.OrfReader()
    #Read characters in order, and build reverse comliment
    for char in sequence:
        rev_comp.appendleft(complement(char))
        seq_reader.read_in(char)
    #Get complete reads and flush incomplete reads
    for read in seq_reader.get_reads():
        reads.append(read)
    seq_reader.flush_reads()
    #Now read reverse compliment
    for char in rev_comp:
        seq_reader.read_in(char)
    for read in seq_reader.get_reads():
        reads.append(read)
    return reads

def complement(char):
    """Retern complimentary DNA base for character
    """
    if char == 'A':
        return 'T'
    elif char == 'T':
        return 'A'
    elif char == 'G':
        return 'C'
    elif char == 'C':
        return 'G'

def orf_file(file_name):
    """
    Reads in input file 1 line at a time and passes lines to orf(). Returns a
    generator that yields a touple containing the sequence that was read and
    the list of open reading frames returned by orf().
    """
    with open(file_name) as file:
        for line in file:
            yield (line, orf(line))

if __name__ == "__main__":
    """Main testing routine.

    Enter either file path/name as command line argument, or 'S' followed by
    second command line argument containing typed in sequence.

    File path can have multiple lines, they will each be treated as separate se-
    quences and read separately.
    Examples:
    File:
    $ python3 orf.py test_file.txt
    Direct sequence:
    $ python3 orf.py S AUGGCCAUGGC
    """
    try:
        #Direct sequence
        if sys.argv[1].upper() == 'S':
            try:
                for sequence in orf(sys.argv[2]):
                    print(sequence)
            except IndexError:
                print("No second command line argument entered")
        #File path
        else:
            for sequence_list in orf_file(sys.argv[1]):
                print("Sequence: ", sequence_list[0])
                print("Reads: ")
                for sequence in sequence_list[1]:
                    print(sequence)
    except KeyError:
        print("Invalid character foud. This could be due to file format (e.g. RTF)")
        print("File should be plain text and contain only A, U, C, and G")
    except IndexError:
        print("No command line argument entered")
