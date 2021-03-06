#!/usr/bin/env python3

"""
Tests form the find_exons submodule
"""


import unittest

from exfi.io.fasta_to_dict import \
    fasta_to_dict

from tests.auxiliary_functions import \
    _command_to_list, \
    _fasta_to_list, \
    _getfasta_to_list, \
    _bf_and_process

from tests.custom_assertions import \
    CustomAssertions

from tests.io.bed import \
    BED3_EMPTY, BED3_SIMPLE, BED3_COMPLEX, \
    BED3_EMPTY_FN, BED3_SIMPLE_FN, BED3_COMPLEX_FN



class TestProcessOutput(unittest.TestCase):
    """Tests for _command_to_list"""

    def test_empty_process(self):
        """exfi.find_exons._command_to_list: process an empty stream"""
        results = _command_to_list(["cat", BED3_EMPTY_FN])
        self.assertTrue(results.shape == (0, 3))


    def test_simple_process(self):
        """exfi.find_exons._command_to_list: process an simple stream"""
        results = _command_to_list(["cat", BED3_SIMPLE_FN])
        print("Observed:\n", results)
        print("Expected:\n", BED3_SIMPLE)
        self.assertTrue(results.equals(BED3_SIMPLE))

    def test_big_process(self):
        """exfi.find_exons._command_to_list: process an big stream"""
        results = _command_to_list(["cat", BED3_COMPLEX_FN])
        print("Observed:\n", results, results.dtypes)
        print("Expected:\n", BED3_COMPLEX, BED3_COMPLEX.dtypes)
        self.assertTrue(results.equals(BED3_COMPLEX))



class TestGetFastaToList(unittest.TestCase, CustomAssertions):
    """Tests for _get_fasta_to_list"""

    def test_empty_sequence_empty_bed(self):
        """exfi.find_exons._getfasta_to_list: process an empty fasta and an
        empty bed"""
        transcriptome_dict = {}
        iterable_of_bed = []
        self.assertEqual(
            _getfasta_to_list(transcriptome_dict, iterable_of_bed),
            []
        )

    def test_empty_sequence_one_bed(self):
        """exfi.find_exons._getfasta_to_list: process an empty fasta and an
        empty bed"""
        transcriptome_dict = {}
        iterable_of_bed = [("test1", 14, 27)]
        self.assertEqual(
            _getfasta_to_list(transcriptome_dict, iterable_of_bed),
            []
        )

    def test_one_sequence_empty_bed(self):
        """exfi.find_exons._getfasta_to_list: process a simple fasta and an
        empty bed"""
        transcriptome_dict = fasta_to_dict(
            "tests/find_exons/single_sequence.fa"
        )
        iterable_of_bed = []
        self.assertEqual(
            _getfasta_to_list(transcriptome_dict, iterable_of_bed),
            []
        )

    def test_one_sequence_one_bed(self):
        """exfi.find_exons._getfasta_to_list: process an single fasta and a
        single bed record"""
        transcriptome_dict = fasta_to_dict(
            "tests/find_exons/one_sequence_one_bed_input.fa"
        )
        iterable_of_bed = [("test1", 0, 60)]
        self.assertEqual(
            _getfasta_to_list(transcriptome_dict, iterable_of_bed),
            _fasta_to_list(
                "tests/find_exons/one_sequence_one_bed_output.fa"
            )
        )

    def test_multi_seqs_multi_beds(self):
        """exfi.find_exons._getfasta_to_list: process an multiline fasta and multple bed"""
        transcriptome_dict = fasta_to_dict(
            "tests/find_exons/multiple_sequences_multiple_beds_input.fa",
        )
        iterable_of_bed = [
            ("test1", 0, 60), ("test2", 0, 40), ("test3", 10, 20)
        ]
        self.assertEqual(
            _getfasta_to_list(transcriptome_dict, iterable_of_bed),
            _fasta_to_list(
                "tests/find_exons/multiple_sequences_multiple_beds_output.fa",
            )
        )



class TestFindExonsPipeline(unittest.TestCase):
    """Tests for find_exons_pipeline"""

    def test_notranscriptome_noreads(self):
        """exfi.find_exons._bf_and_process: Process an empty transcriptome and
        an empty BF"""
        reads_fns = ["/dev/null"]
        transcriptome_fn = "/dev/null"
        results = _bf_and_process(reads_fns, transcriptome_fn)
        print("Observed:\n", results)
        print("Expected:\n", BED3_EMPTY)
        self.assertEqual(results.shape, (0, 3))

    def test_transcriptome_noreads(self):
        """exfi.find_exons._bf_and_process: Process a small transcriptome and
        an empty BF"""
        reads_fns = ["/dev/null"]
        transcriptome_fn = 'tests/find_exons/small_transcriptome.fa'
        results = _bf_and_process(reads_fns, transcriptome_fn)
        self.assertEqual(results.shape, (0, 3))

    def test_small_data(self):
        """exfi.find_exons._bf_and_process: Process an empty transcriptome and
        a small BF"""
        reads_fns = [
            'tests/find_exons/reads_1.fq',
            'tests/find_exons/reads_2.fq'
        ]
        transcriptome_fn = 'tests/find_exons/small_transcriptome.fa'
        results = _bf_and_process(reads_fns, transcriptome_fn)
        self.assertEqual(results.shape, (0, 3))



if __name__ == "__main__":
    unittest.main()
