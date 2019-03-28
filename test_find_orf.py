#! /usr/bin/env python3

import unittest

import test_util
import find_orf


class TestFindOrfBaseClass(test_util.TestBaseClass):
    def run_find_first_orf(self, sequence,
            expected_result,
            start_codons = ['AUG'],
            stop_codons = ['UAA', 'UAG', 'UGA']):
        key_word_args = {
                "sequence" : sequence,
                "start_codons" : start_codons,
                "stop_codons" : stop_codons,
                }
        self.run_test_of_function(
                function = find_orf.find_first_orf,
                key_word_args = key_word_args,
                expected_result = expected_result)

    def run_vet_nucleotide_sequence(self, sequence,
            raises_exception = False):
        if not raises_exception:
            self.run_test_of_function(
                    function = find_orf.vet_nucleotide_sequence,
                    key_word_args = {"sequence": sequence},
                    expected_result = None)
            return
        self.run_test_of_function_raise(
                function = find_orf.vet_nucleotide_sequence,
                key_word_args = {"sequence": sequence},
                expected_exception = Exception)

    def run_vet_codon(self, codon,
            raises_exception = False):
        if not raises_exception:
            self.run_test_of_function(
                    function = find_orf.vet_codon,
                    key_word_args = {"codon": codon},
                    expected_result = None)
            return
        self.run_test_of_function_raise(
                function = find_orf.vet_codon,
                key_word_args = {"codon": codon},
                expected_exception = Exception)


class TestVetNucleotideSequence(TestFindOrfBaseClass):
    def test_rna_lower(self):
        seq = "acugauagcugacugaug"
        self.run_vet_nucleotide_sequence(seq, False)

    def test_rna_upper(self):
        seq = "ACUGAUAGCUGACUGAUG"
        self.run_vet_nucleotide_sequence(seq, False)

    def test_dna_lower(self):
        seq = "actgatagctgactgatg"
        self.run_vet_nucleotide_sequence(seq, False)

    def test_dna_upper(self):
        seq = "ACTGATAGCTGACTGATG"
        self.run_vet_nucleotide_sequence(seq, False)

    def test_rna_dna_mix(self):
        seq = "ACGUT"
        self.run_vet_nucleotide_sequence(seq, True)

    def test_empty_string(self):
        seq = ""
        self.run_vet_nucleotide_sequence(seq, False)


class TestVetCodon(TestFindOrfBaseClass):
    def test_codon_lower(self):
        codon = "aug"
        self.run_vet_codon(codon, False)

    def test_codon_upper(self):
        codon = "AUU"
        self.run_vet_codon(codon, False)

    def test_short_codon(self):
        codon = "AU"
        self.run_vet_codon(codon, True)

    def test_long_codon(self):
        codon = "AUGG"
        self.run_vet_codon(codon, True)

    def test_dna_codon(self):
        codon = "ATG"
        self.run_vet_codon(codon, True)


class TestFindFirstOrf(TestFindOrfBaseClass):
    def test_empty_sequence(self):
        seq = ""
        expected_result = ""
        self.run_find_first_orf(seq, expected_result)

    def test_full_rna_orf_upper(self):
        seq = 'AUGGUAGUAUAA'
        expected_result = 'AUGGUAGUAUAA'
        self.run_find_first_orf(seq, expected_result)

    def test_full_rna_orf_lower(self):
        seq = 'augguaguauaa'
        expected_result = 'AUGGUAGUAUAA'
        self.run_find_first_orf(seq, expected_result)

    def test_full_dna_orf_upper(self):
        seq = 'ATGGTAGTATAA'
        expected_result = 'AUGGUAGUAUAA'
        self.run_find_first_orf(seq, expected_result)

    def test_full_dna_orf_lower(self):
        seq = 'atggtagtataa'
        expected_result = 'AUGGUAGUAUAA'
        self.run_find_first_orf(seq, expected_result)

    def test_no_start(self):
        seq = 'ACGGUAGUAUAA'
        expected_result = ''
        self.run_find_first_orf(seq, expected_result)

    def test_no_stop(self):
        seq = 'AUGGUAGUAUAC'
        expected_result = ''
        self.run_find_first_orf(seq, expected_result)

    def test_frame_shift(self):
        seq = 'AUGGUAGUAGUAA'
        expected_result = ''
        self.run_find_first_orf(seq, expected_result)

    def test_embedded_orf(self):
        seq = 'CCACCAUGGUAGUAUAACCACC'
        expected_result = 'AUGGUAGUAUAA'
        self.run_find_first_orf(seq, expected_result)

    def test_nonoverlapping_orfs(self):
        seq = 'CCACCAUGGUAGUAUAACCACCAUGGUGGUGUAACCACC'
        expected_result = 'AUGGUAGUAUAA' # should only find the first
        self.run_find_first_orf(seq, expected_result)

    def test_overlapping_orfs(self):
        seq = 'CCACCAUGGUAAUGGUAGUAUAACCACC'
        expected_result = 'AUGGUAAUGGUAGUAUAA' # should only find the first
        self.run_find_first_orf(seq, expected_result)

    def test_other_start_stop_no_match(self):
        seq = 'CCACCAUGGUAAUGGUAGUAUAACCACC'
        expected_result = ''
        self.run_find_first_orf(seq, expected_result,
                start_codons = ['AAA'],
                stop_codons = ['UUU'])

    def test_other_start_stop_match(self):
        seq = 'CAAACACCAUGGUAGUAGGUAAUUUAACCACC'
        expected_result = 'AAACACCAUGGUAGUAGGUAAUUU'
        self.run_find_first_orf(seq, expected_result,
                start_codons = ['AAA'],
                stop_codons = ['UUU'])


if __name__ == '__main__':
    unittest.main() 
