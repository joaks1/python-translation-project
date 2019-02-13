#! /usr/bin/env python3

import unittest

import translate

class TestTranslateBaseClass(unittest.TestCase):
    def setUp(self):
        self.genetic_code = {'GUC': 'V', 'ACC': 'T', 'GUA': 'V', 'GUG': 'V', 'ACU': 'T', 'AAC': 'N', 'CCU': 'P', 'UGG': 'W', 'AGC': 'S', 'AUC': 'I', 'CAU': 'H', 'AAU': 'N', 'AGU': 'S', 'GUU': 'V', 'CAC': 'H', 'ACG': 'T', 'CCG': 'P', 'CCA': 'P', 'ACA': 'T', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'GCG': 'A', 'UGC': 'C', 'CAG': 'Q', 'GAU': 'D', 'UAU': 'Y', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': '*', 'GGA': 'G', 'UAC': 'Y', 'GAC': 'D', 'UAG': '*', 'AUA': 'I', 'GCA': 'A', 'CUU': 'L', 'GGC': 'G', 'AUG': 'M', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AAA': 'K', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'GCU': 'A', 'GAA': 'E', 'AUU': 'I', 'UUG': 'L', 'UUA': 'L', 'UGA': '*', 'UUC': 'F'}

    def run_translate_sequence(self, rna_seq,
            expected_amino_acid_seq,
            gen_code = None):
        if gen_code is None:
            gen_code = self.genetic_code
        amino_acid_seq = translate.translate_sequence(
                rna_sequence = rna_seq,
                genetic_code = gen_code)
        message = (
                "\n\n"
                "Calling `translate_sequence` with `rna_sequence` '{0}'.\n"
                "Expecting '{1}', but '{2}' was returned".format(
                        rna_seq,
                        expected_amino_acid_seq,
                        amino_acid_seq))
        self.assertEqual(amino_acid_seq, expected_amino_acid_seq, message)

class TestTranslateSequence(TestTranslateBaseClass):

    def test_empty_rna_sequence(self):
        rna_seq = ""
        expected_amino_acid_seq = ""
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_rna_sequence_with_one_base(self):
        rna_seq = "A"
        expected_amino_acid_seq = ""
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_rna_sequence_with_two_bases(self):
        rna_seq = "AG"
        expected_amino_acid_seq = ""
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_only_stop_codon(self):
        rna_seq = "UGA"
        expected_amino_acid_seq = ""
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_one_codon(self):
        rna_seq = "GUC"
        expected_amino_acid_seq = "V"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

        rna_seq = "GAA"
        expected_amino_acid_seq = "E"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_one_codon_lower_case(self):
        rna_seq = "guc"
        expected_amino_acid_seq = "V"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

        rna_seq = "gaa"
        expected_amino_acid_seq = "E"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_no_stop_to_end(self):
        rna_seq = "GUCGAACGA"
        expected_amino_acid_seq = "VER"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_no_stop_with_extra_base(self):
        rna_seq = "GUCGAACGAA"
        expected_amino_acid_seq = "VER"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_stop_codon_at_end(self):
        rna_seq = "GUCGAACGAUAA"
        expected_amino_acid_seq = "VER"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)

    def test_stop_codon_within(self):
        rna_seq = "GUCGAAUAACGA"
        expected_amino_acid_seq = "VE"
        self.run_translate_sequence(
                rna_seq = rna_seq,
                expected_amino_acid_seq = expected_amino_acid_seq)


if __name__ == '__main__':
    unittest.main() 
