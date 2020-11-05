"""
Nested dictionary tree for codon - amino acid lookupself.

Returns a dictionary with nexted dictionaries that can be
used to retrieve the amino acid coded by an RNA codonself.

Examples:

codon_tree['U']['C']['U'] = 'S'
codon_tree['A']['U']['G'] = 'M'
codon_tree['U']['G']['A'] = '*STOP*'
"""

def RNA_codon_tree():
    """Return dictionary for RNA codon translation.

    Example usage:
    codon_tree['A']['U']['G'] = 'M'
    """
    codon_tree = {
        'U' : {
            'U' : {
                'U' : 'F',
                'C' : 'F',
                'A' : 'L',
                'G' : 'L',
                },
            'C' : {
                'U' : 'S',
                'C' : 'S',
                'A' : 'S',
                'G' : 'S',
                },
            'A' : {
                'U' : 'Y',
                'C' : 'Y',
                'A' : '*STOP*',
                'G' : '*STOP*',
                },
            'G' : {
                'U' : 'C',
                'C' : 'C',
                'A' : '*STOP*',
                'G' : 'W',
                },
            },
        'C' : {
            'U' : {
                'U' : 'L',
                'C' : 'L',
                'A' : 'L',
                'G' : 'L',
                },
            'C' : {
                'U' : 'P',
                'C' : 'P',
                'A' : 'P',
                'G' : 'P',
                },
            'A' : {
                'U' : 'H',
                'C' : 'H',
                'A' : 'Q',
                'G' : 'Q',
                },
            'G' : {
                'U' : 'R',
                'C' : 'R',
                'A' : 'R',
                'G' : 'R',
                },
            },
        'A' : {
            'U' : {
                'U' : 'I',
                'C' : 'I',
                'A' : 'I',
                'G' : 'M',
                },
            'C' : {
                'U' : 'T',
                'C' : 'T',
                'A' : 'T',
                'G' : 'T'
                },
            'A' : {
                'U' : 'N',
                'C' : 'N',
                'A' : 'K',
                'G' : 'K',
                },
            'G' : {
                'U' : 'S',
                'C' : 'S',
                'A' : 'R',
                'G' : 'R',
                },
            },
        'G' : {
            'U' : {
                'U' : 'V',
                'C' : 'V',
                'A' : 'V',
                'G' : 'V',
                },
            'C' : {
                'U' : 'A',
                'C' : 'A',
                'A' : 'A',
                'G' : 'A',
                },
            'A' : {
                'U' : 'D',
                'C' : 'D',
                'A' : 'E',
                'G' : 'E',
                },
            'G' : {
                'U' : 'G',
                'C' : 'G',
                'A' : 'G',
                'G' : 'G',
                },
            },
        }
    return codon_tree
