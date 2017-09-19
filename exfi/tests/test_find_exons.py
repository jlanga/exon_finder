#!/usr/bin/env python3

from unittest import TestCase
from exfi.find_exons import \
    _process_output, \
    _get_fasta, \
    _find_exons_pipeline
    #find_exons
from subprocess import Popen, PIPE
from Bio import SeqIO
from exfi.tests.auxiliary_functions import CustomAssertions
import os

class TestProcessOutput(TestCase):

    def test_empty_process(self):
        """find_exons.py: process an empty stream"""
        command = ["cat", "/dev/null"]
        process = Popen(command, stdout=PIPE)
        results = list(_process_output(process))
        self.assertEqual(results, [])

    def test_simple_process(self):
        """find_exons.py: process an simple stream"""
        command = ["cat", "exfi/tests/files/find_exons/simple.bed"]
        process = Popen(command, stdout=PIPE)
        results = list(_process_output(process))
        self.assertEqual(results, [("test", 4, 27)])

    def test_big_process(self):
        """find_exons.py: process an big stream"""
        command = ["cat", "exfi/tests/files/find_exons/big.bed"]
        process = Popen(command, stdout=PIPE)
        results = list(_process_output(process))
        self.assertEqual(
            results,
            [("test1", 14, 27), ("test2", 15, 19),
            ("test2", 17, 21), ("test3", 19, 25)]
        )


class TestGetFasta(TestCase, CustomAssertions):

    def test_empty_sequence_empty_bed(self):
        """find_exons.py: process an empty fasta and an empty bed"""
        results = _get_fasta(
            transcriptome_dict={},
            iterable_of_bed = []
        )
        expected = []
        self.assertEqual(
            list(results), expected
        )

    def test_empty_sequence_one_bed(self):
        """find_exons.py: process an empty fasta and an empty bed"""
        results = _get_fasta(
            transcriptome_dict={},
            iterable_of_bed = [("test1", 14, 27)]
        )
        expected = []
        self.assertEqual(
            list(results), expected
        )

    def test_one_sequence_empty_bed(self):
        """find_exons.py: process a simple fasta and an empty bed"""
        results = _get_fasta(
            transcriptome_dict= SeqIO.index(
                filename="exfi/tests/files/find_exons/single_sequence.fa",
                format="fasta"),
            iterable_of_bed = []
        )
        expected = []
        self.assertEqual(
            list(results), expected
        )

    def test_one_sequence_one_bed(self):
        """find_exons.py: process an single fasta and a single bed record"""
        record_dict = SeqIO.index(
            filename="exfi/tests/files/find_exons/one_sequence_one_bed_input.fa",
            format="fasta"
        )
        bed = [("test1", 0, 60)]
        results = [x for x in _get_fasta(record_dict, bed)]
        expected = list(SeqIO.parse(
            handle="exfi/tests/files/find_exons/one_sequence_one_bed_output.fa",
            format="fasta"
        ))
        #print(record_dict)
        self.assertEqualListOfSeqrecords(results, expected)

    def test_multiple_sequences_multiple_beds(self):
        """find_exons.py: process an multiline fasta and multple bed"""
        record_dict = SeqIO.index(
            filename="exfi/tests/files/find_exons/multiple_sequences_multiple_beds_input.fa",
            format="fasta"
        )
        bed = [("test1", 0, 60), ("test2", 0, 40), ("test3", 10, 20)]
        results = [x for x in _get_fasta(record_dict, bed)]
        expected = list(SeqIO.parse(
            handle="exfi/tests/files/find_exons/multiple_sequences_multiple_beds_output.fa",
            format="fasta"
        ))
        #print(record_dict)
        self.assertEqualListOfSeqrecords(results, expected)


class TestFindExonsPipeline(TestCase):

    def test_notranscriptome_noreads(self):
        """find_exons.py: Process an empty transcriptome and an empty BF"""
        process = Popen(['abyss-bloom', 'build',
                '--kmer', "30",
                '--bloom-size', "100M",
                '--levels', "1",
                '--threads', "1",
                "/tmp/test_bloom.bf",
                '/dev/null'],
            stdout=open("/dev/null", 'w'),
            stderr=open("/dev/null", "w")
        )
        process.wait()
        results = _find_exons_pipeline(
            kmer=30,
            bloom_filter_fn="/tmp/test_bloom.bf",
            transcriptome_fn="/dev/null",
            max_fp_bases=5
        )
        results = list(results)
        os.remove("/tmp/test_bloom.bf")
        self.assertEqual(results, [])


    def test_transcriptome_noreads(self):
        """find_exons.py: Process a small transcriptome and an empty BF"""
        process = Popen(['abyss-bloom', 'build',
                '--kmer', "30",
                '--bloom-size', "100M",
                '--levels', "1",
                '--threads', "1",
                "/tmp/test_bloom.bf",
                '/dev/null'],
            stdout=open('/dev/null', 'w'),
            stderr=open('/dev/null', 'w')
        )
        process.wait()
        results = _find_exons_pipeline(
            kmer=30,
            bloom_filter_fn='/tmp/test_bloom.bf',
            transcriptome_fn='exfi/tests/files/find_exons/small_transcriptome.fa',
            max_fp_bases=5
        )
        results = list(results)
        os.remove('/tmp/test_bloom.bf')
        self.assertEqual(results, [])

    def test_small_data(self):
        """find_exons.py: Process an empty transcriptome and a small BF"""
        process = Popen(['abyss-bloom', 'build',
                '--kmer', "30",
                '--bloom-size', "100M",
                '--levels', "1",
                '--threads', "1",
                "/tmp/test_bloom.bf",
                'exfi/tests/files/find_exons/reads_1.fq',
                'exfi/tests/files/find_exons/reads_2.fq'],
            stdout=open('/dev/null', 'w'),
            stderr=open('/dev/null', 'w')
        )
        process.wait()
        results = _find_exons_pipeline(
            kmer=30,
            bloom_filter_fn='/tmp/test_bloom.bf',
            transcriptome_fn='exfi/tests/files/find_exons/small_transcriptome.fa',
            max_fp_bases=5
        )
        results = list(results)
        os.remove('/tmp/test_bloom.bf')
        self.assertEqual(results, [])