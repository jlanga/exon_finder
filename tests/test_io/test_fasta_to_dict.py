#!/usr/bin/env python3

"""Unittests for exfi.io.fasta_to_dict"""

import unittest

from exfi.io.fasta_to_dict import \
    fasta_to_dict

from tests.test_data import \
    EXONS_EMPTY_FN, EXONS_SIMPLE_FN, EXONS_COMPLEX_FN, \
    EXONS_EMPTY_DICT, EXONS_SIMPLE_DICT, EXONS_COMPLEX_DICT


class TestFastaToDict(unittest.TestCase):
    """Tests for fasta_to_dict"""

    def test_empty(self):
        """exfi.io.fasta_to_dict: process an empty fasta"""
        actual = fasta_to_dict(EXONS_EMPTY_FN)
        expected = EXONS_EMPTY_DICT
        self.assertEqual(actual, expected)

    def test_simple(self):
        """exfi.io.fasta_to_dict: process a simple fasta"""
        actual = fasta_to_dict(EXONS_SIMPLE_FN)
        expected = EXONS_SIMPLE_DICT
        self.assertEqual(actual, expected)

    def test_complex(self):
        """exfi.io.fasta_to_dict: process a complex fasta"""
        actual = fasta_to_dict(EXONS_COMPLEX_FN)
        expected = EXONS_COMPLEX_DICT
        self.assertEqual(actual, expected)
