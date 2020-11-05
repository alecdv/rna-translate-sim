README for SequenceReader

This module implements 2 classes to assist with translating RNA and DNA sequences. At a high level, OrfReader processes sequences one character at a time and opens ReadingFrames when start (AUG) codons are encountered. Characters are passed to all currently open ReadingFrames stored within the OrfReader, and their sequences can be retrieved at any time.


OrfReader:

This class implements an OrfReader which processes RNA/DNA sequences one character at a time. The current window of the last 3 bases processed is stored and each time a start codon is encountered, OrfReader will open a new reading frame (implemented as a ReadingFrame object, see below) and begin passing characters from the sequence to it. Each character is passed to all currently open reading frames stored within the OrfReader reading_frames list. The individual reading frames handle translating codons and closing themselves when stop codons are encountered. OrfReader also includes a method for retrieving sequences from all currently closed reading frames, useful for retrieving all protein sequences at the end of orf translation of a nucleic acid sequence. Finally there are helper methods to flush the reading_frames list (clearing out any existing ReadingFrames if the OrfReader is being reused on a new sequence) and to translate 'T' characters to 'U' to allow handling of DNA as well as RNA sequences.

ReadingFrame:

This is the primary translating class. ReadingFrame reads in characters and translates every three characters passed in to an amino acid which is appended to the stored protein sequence. Translation is done with an RNA codon tree implemented as a class level nested dictionary. ReadingFrame objects also stored a boolean indicating whether they are currently open or closed, allowing other objects (like OrfReader) to determine whether that ReadingFrame's particular read is complete.


See code documentation for specific method and attribute descriptions.


