"""Module with classes for open reading frame prossessing of DNA/RNA sequences.

This module contains two classes that work togeather to translate sequences of
RNA or DNA nucleotides into all open reading frame amino-acid sequences.

Classes:
OrfReader - processes one character of the nucleotide sequence at a time. Will
intiate a new ReadingFrame opject every time a start codon "AUG" is encountered.
Stores all reading frames in a list to be retrieved at the end of sequence
processing.

ReadingFrame - ReadingFrame objects are passed sequence characters once they are
open and will translate every 3 characters into an amino acid. Once a stop codon
is encountered the ReadingFrame frame_open attribute will be set to False.
"""

from rna_codon_tree import RNA_codon_tree

class OrfReader:
    """Processes a DNA/RNA sequence and stores all reading frames.

    Attributes:
    reading_frames - this is a list of reading frames generated by the OrfReader.
    Each time a start codon is encountered, OrfReader will open a new reading
    frame (implemented as a ReadingFrame, see below) and begin passing
    characters from the sequence to it.
    start_read - current 3 nucleotide window being viewed by the OrfReader. New
    bases are added at position 2 and a base is removed from position 0. When
    an "AUG" sequence is encountered a new reading frame is opened.
    """

    def __init__(self):
        self.reading_frames = []
        self.start_read = ['*', '*', '*']

    def read_in(self, char):
        """Process one nucleotide base

        Passes base to all currently open reading frames for translation. Also
        shifts start_read window one character and checks for start_codon. If
        start_codon is found, instantiates new ReadingFrame and adds to
        reading_frames.
        """
        char = self.dna_to_rna(char)
        for frame in self.reading_frames:
            if frame.is_open:
                frame.read(char)
        self.start_read.pop(0)
        self.start_read.append(char)
        if self.start_read == ['A', 'U', 'G']:
            self.reading_frames.append(ReadingFrame(['A','U','G']))

    def get_reads(self):
        """Generater for sequences stored in reading_frames.

        Used to retrieve protein sequences after conclusion of DNA/RNA sequence
        processing.
        """
        for frame in self.reading_frames:
            if frame.is_open == False:
                yield frame.get_sequence()

    def flush_reads(self):
        """Clear reading frames.

        This should generally be called at the end of sequence to clear out any
        un-closed frames before using the same OrfReader to continue reading a
        new sequence.
        """
        self.reading_frames = []

    def dna_to_rna(self, char):
        """Translates DNA 'T' to RNA 'U'.
        """
        if char == 'T':
            return 'U'
        else:
            return char


class ReadingFrame:
    """Reads in RNA bases and translates into an amino acid sequence.

    Attributes:
    codon_tree: class level RNA - Amino Acid mapping tree used for translation.
    is_open: Boolean that indicates whether the reading frame is open or closed.
    creation and will close (frame_open = False) when a stop codon is encounter-
    ed.
    curr_codon: The current codon being red. Once len(curr_codon) = 3 it is tra-
    nslated into an amino acid and cleared to continue processing.
    sequence: current amino acid sequence for the reading frame.
    start_codon: initiation codon
    """
    codon_tree = RNA_codon_tree()

    def __init__(self, start_codon=None):
        self.is_open = True
        self.sequence = []
        self.curr_codon = []
        self.start_codon = start_codon
        if start_codon:
            for char in start_codon:
                self.read(char)


    def read(self, char):
        """Reads next RNA base.

        RNA base character is appended to curr_codon. If len(curr_codon) = 3
        the codon will be translated into an additional amino acid character
        added to sequence and cudd_codon cleared.
        """
        self.curr_codon.append(char)
        if len(self.curr_codon) == 3:
            new_amino = self.translate(self.curr_codon)
            if new_amino == '*STOP*':
                self.is_open = False
            else:
                self.sequence.append(new_amino)
            self.curr_codon = []

    def translate(self, codon):
        """Translate RNA codon into amino acid character.
        """
        return ReadingFrame.codon_tree[codon[0]][codon[1]][codon[2]]

    def get_sequence(self):
        """Return amino acid sequence formatted as string.
        """
        return ''.join(self.sequence)