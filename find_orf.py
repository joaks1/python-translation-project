#! /usr/bin/env python3

import sys
import re

def vet_nucleotide_sequence(sequence):
    """
    Return None if `sequence` is a valid RNA or DNA sequence, else raise exception. 

    Parameters
    ----------
    sequence : str
        A string representing a DNA or RNA sequence (upper or lower-case)

    Returns
    -------
    None
        Return nothing (None) if sequence is valid, otherwise raise an
        exception.

    Examples
    --------
    >>> vet_nucleotide_sequence('ACGTACGT') == None
    True

    >>> vet_nucleotide_sequence('not a valid sequence')
    Traceback (most recent call last):
        ...
    Exception: Invalid sequence: 'not a valid sequence'

    Don't allow mixing of DNA and RNA!
    >>> vet_nucleotide_sequence('AUTGC')
    Traceback (most recent call last):
        ...
    Exception: Invalid sequence: 'AUTGC'

    Don't allow whitespace (or other characters) before, within, or after!
    >>> vet_nucleotide_sequence(' ACGT ACGT ')
    Traceback (most recent call last):
        ...
    Exception: Invalid sequence: ' ACGT ACGT '

    But, an empty string should be deemed valid
    >>> vet_nucleotide_sequence('') == None
    True
    """
    ##########################################################################
    ############################ EDIT CODE BELOW #############################
    # `rna_pattern_str` and `dna_pattern_str` need to be regular expressions
    # that will match any string of zero or more RNA and DNA bases,
    # respectively (and only strings of zero or more RNA and DNA bases).
    # Currently, `rna_pattern_str` and `dna_pattern_str` are strings of literal
    # characters.
    # These are valid regular expressions, but they will only match their
    # respective strings exactly.
    # Change `rna_pattern_str` and `dna_pattern_str` so that they will match
    # any valid RNA and DNA sequence strings, respectively (and only strings of
    # RNA and DNA bases).
    # Read the docstring above for additional clues.
    rna_pattern_str = r'AUCG'
    dna_pattern_str = r'ATCG'
    ##########################################################################

    rna_pattern = re.compile(rna_pattern_str)
    dna_pattern = re.compile(dna_pattern_str)

    if rna_pattern.match(sequence):
        return
    if dna_pattern.match(sequence):
        return
    else:
        raise Exception("Invalid sequence: {0!r}".format(sequence))



def vet_codon(codon):
    """
    Return None if `codon` is a valid RNA codon, else raise an exception. 

    Parameters
    ----------
    codon : str
        A string representing a codon (upper or lower-case)

    Returns
    -------
    None
        Return nothing (None) if codon is valid, otherwise raise an
        exception.

    Examples
    --------
    Valid codon
    >>> vet_codon('AUG') == None
    True

    lower-case is also vaild 
    >>> vet_codon('aug') == None
    True

    DNA is not valid
    >>> vet_codon('ATG')
    Traceback (most recent call last):
        ...
    Exception: Invalid codon: 'ATG'

    A codon must be exactly 3 RNA bases long
    >>> vet_codon('AUGG')
    Traceback (most recent call last):
        ...
    Exception: Invalid codon: 'AUGG'
    """
    ##########################################################################
    ############################ EDIT CODE BELOW #############################
    # `codon_pattern_str` needs to be a regular expression that will match any
    # codon (but only a string that is one codon).
    # Currently, `codon_pattern_str` is only a string of literal characters.
    # This is a valid regular expression, but it will only match 'AUG' exactly.
    # Change `codon_pattern_str` so that it will match any valid codons, and
    # only valid codons.
    # Read the docstring above for additional clues.
    codon_pattern_str = r'AUG'
    ##########################################################################

    codon_pattern = re.compile(codon_pattern_str)

    if codon_pattern.match(codon):
        return
    else:
        raise Exception("Invalid codon: {0!r}".format(codon))


def find_first_orf(sequence,
        start_codons = ['AUG'],
        stop_codons = ['UAA', 'UAG', 'UGA']):
    """
    Return the first open-reading frame in the DNA or RNA `sequence`.

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

    Returns
    -------
    str
        An uppercase string of the first ORF found in the `sequence` that
        starts with any one of the `start_codons` and ends with any one of the
        `stop_codons`. If no ORF is found an empty string is returned.

    Examples
    --------
    When the whole RNA sequence is an ORF:
    >>> find_first_orf('AUGGUAUAA', ['AUG'], ['UAA'])
    'AUGGUAUAA'

    When the whole DNA sequence is an ORF:
    >>> find_first_orf('ATGGTATAA', ['AUG'], ['UAA'])
    'AUGGUAUAA'

    When there is no ORF:
    >>> find_first_orf('CUGGUAUAA', ['AUG'], ['UAA'])
    ''

    When there is are bases before and after ORF:
    >>> find_first_orf('CCAUGGUAUAACC', ['AUG'], ['UAA'])
    'AUGGUAUAA'
    """
    # Make sure the sequence is valid
    vet_nucleotide_sequence(sequence)

    # Make sure the codons are valid
    for codon in start_codons:
        vet_codon(codon)
    for codon in stop_codons:
        vet_codon(codon)

    # Get copies of everything in uppercase
    seq = sequence.upper()
    starts = [c.upper() for c in start_codons]
    stops = [c.upper() for c in stop_codons]
    # Make sure seq is RNA
    seq = seq.replace('T', 'U')

    ##########################################################################
    ############################ EDIT CODE BELOW #############################
    # `orf_pattern_str` needs to be a regular expression that will match an
    # open reading frame within a string of RNA bases. At this point we know
    # the string only contains uppercase A, C, G, and U.
    # I recommend starting by hardcoding the standard start and stop codons
    # (the ones listed as defaults for this function) into the regular
    # expression. After you get that working, then try generalizing it to work
    # for any start/stop codons.
    # Currently, `orf_pattern_str` is only a string of literal characters. This
    # is a valid regular expression, but it will only match 'AUGGUAUAA'
    # exactly. Change `orf_pattern_str` so that it will match any open reading
    # frame.
    # Read the docstring above for additional clues.
    orf_pattern_str = r'AUGGUAUAA'
    ##########################################################################

    # Create the regular expression object
    orf_pattern = re.compile(orf_pattern_str)
    # Search the sequence
    match_object = orf_pattern.search(seq)
    if match_object:
        return match_object.group()
    return ''


def parse_sequence_from_path(path):
    # Try to open the path to read from it, and handle exceptions if they
    # arrise
    try:
        file_stream = open(path, 'r')
    except FileNotFoundError as e:
        sys.stderr.write("Sorry, couldn't find path {}".format(path))
        raise e
    except IsADirectoryError as e:
        sys.stderr.write("Sorry, path {} appears to be a directory".format(
                path))
        raise e
    except:
        sys.stderr.write("Sorry, something went wrong when trying to open {}".format(
                path))
        raise
    # If we've reached here, the file is open and ready to read
    sequence = ''
    # A for loop to visit each line in the file
    for line in file_stream:
        # Strip whitespace from the line and concatenate it to the end of the
        # sequence
        sequence += line.strip()
    return sequence


def main():
    import argparse

    # Create a command-line parser object
    parser = argparse.ArgumentParser(
            formatter_class = argparse.ArgumentDefaultsHelpFormatter)

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
    parser.add_argument('-s', '--start-codons',
            type = str,
            nargs = '+', # one or more arguments
            default = ['AUG'],
            help = ('One or more possible start codons.'))
    parser.add_argument('-x', '--stop-codons',
            type = str,
            nargs = '+', # one or more arguments
            default = ['UAA', 'UAG', 'UGA'],
            help = ('One or more possible stop codons.'))

    # Parse the command-line arguments into a 'dict'-like container
    args = parser.parse_args()

    # Check to see if the path option was set to True by the caller. If so, parse
    # the sequence from the path
    if args.path:
        sequence = parse_sequence_from_path(args.sequence)
    else:
        sequence = args.sequence

    orf = find_first_orf(sequence = sequence,
            start_codons = args.start_codons,
            stop_codons = args.stop_codons)
    sys.stdout.write('{}\n'.format(orf))


if __name__ == '__main__':
    main()

