#! /usr/bin/env python3

import sys
import translate
import find_orf

def translate_first_orf(sequence,
        start_codons = ['AUG'],
        stop_codons = ['UAA', 'UAG', 'UGA'],
        genetic_code = {
            'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T',
            'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I',
            'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'GUU': 'V', 'CAC': 'H',
            'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P',
            'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C',
            'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S',
            'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': '*',
            'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'UAG': '*', 'AUA': 'I',
            'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'CUG': 'L',
            'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A',
            'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R',
            'CGC': 'R', 'CGA': 'R', 'GCU': 'A', 'GAA': 'E', 'AUU': 'I',
            'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'
            },
        ):
    """
    Translate the first open-reading frame in the DNA or RNA `sequence`.

    An open-reading frame (ORF) is the part of an RNA sequence that is
    translated into a peptide. It must begin with a start codon, followed by
    zero or more codons (triplets of nucleotides), and end with a stop codon.
    If there are no ORFs in the sequence, an empty string is returned.

    Parameters
    ----------
    sequence : str
        A string representing a DNA or RNA sequence (upper or lower-case)
    start_codons : list of strings
        All possible start codons. Each codon must be a string of 3 RNA bases,
        upper or lower-case.
    stop_codons : list of strings
        All possible stop codons. Each codon must be a string of 3 RNA bases,
        upper or lower-case.
    genetic_code : dict
        A dictionary of the genetic code, mapping codons to single-letter
        abbreviations for amino acids.

    Returns
    -------
    str
        An uppercase string of the amino acid encoded by the first ORF found in
        the `sequence` that starts with any one of the `start_codons` and ends
        with any one of the `stop_codons`. If no ORF is found an empty string
        is returned.

    Examples
    --------
    When the whole RNA sequence is an ORF:
    >>> translate_first_orf('AUGGUAUAA', ['AUG'], ['UAA'])
    'MV'

    When the whole DNA sequence is an ORF:
    >>> translate_first_orf('ATGGTATAA', ['AUG'], ['UAA'])
    'MV'

    When there is no ORF:
    >>> translate_first_orf('CUGGUAUAA', ['AUG'], ['UAA'])
    ''

    When there are bases before and after ORF:
    >>> translate_first_orf('CCAUGGUAUAACC', ['AUG'], ['UAA'])
    'MV'
    """
    orf = find_orf.find_first_orf(sequence,
            start_codons = start_codons,
            stop_codons = stop_codons)
    aa_seq = translate.translate_sequence(orf, genetic_code)
    return aa_seq

def main():
    import argparse

    # Create a command-line parser object
    parser = argparse.ArgumentParser()

    default_start_codons = ['AUG']
    default_stop_codons = ['UAA', 'UAG', 'UGA']

    # Tell the parser what command-line arguments this script can receive
    parser.add_argument('sequence',
            metavar = 'SEQUENCE',
            type = str,
            help = ('The sequence to search for an open-reading frame. '
                    'If the path flag (\'-p\'/\'--path\') is specified, '
                    'then this should be a path to a file containing the '
                    'sequence to be searched.'))
    parser.add_argument('-p', '--path',
            action = 'store_true',
            help = ('The sequence argument should be treated as a path to a '
                    'containing the sequence to be searched.'))
    parser.add_argument('-s', '--start-codon',
            type = str,
            action = 'append', # append each argument to a list
            default = None,
            help = ('A start codon. This option can be used multiple times '
                    'if there are multiple start codons. '
                    'Default: {0}.'.format(" ".join(default_start_codons))))
    parser.add_argument('-x', '--stop-codon',
            type = str,
            action = 'append', # append each argument to a list
            default = None,
            help = ('A stop codon. This option can be used multiple times '
                    'if there are multiple stop codons. '
                    'Default: {0}.'.format(" ".join(default_stop_codons))))

    # Parse the command-line arguments into a 'dict'-like container
    args = parser.parse_args()

    # Check to see if the path option was set to True by the caller. If so, parse
    # the sequence from the path
    if args.path:
        sequence = find_orf.parse_sequence_from_path(args.sequence)
    else:
        sequence = args.sequence

    # Check to see if start/stop codons were provided by the caller. If not,
    # use the defaults.
    if not args.start_codon:
        args.start_codon = default_start_codons
    if not args.stop_codon:
        args.stop_codon = default_stop_codons

    aa_seq = translate_first_orf(sequence = sequence,
            start_codons = args.start_codon,
            stop_codons = args.stop_codon)
    sys.stdout.write('{0}\n'.format(aa_seq))


if __name__ == '__main__':
    main()
