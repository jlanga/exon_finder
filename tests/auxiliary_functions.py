#!/usr/bin/env python3

"""
Auxiliary functions and classes for testing
"""

from typing import Iterable, List, Tuple

import tempfile
import shutil
from subprocess import \
    Popen, PIPE

from Bio.SeqIO.FastaIO import SimpleFastaParser

from exfi.find_exons import \
    _process_output, \
    _get_fasta, \
    _find_exons_pipeline

from exfi.build_baited_bloom_filter import \
    _get_build_bf_command

from exfi.classes import FastaDict, Coordinate

def _command_to_list(command: List[str]) -> List[Coordinate]:
    """Execute command and return output as list of strings"""
    process = Popen(command, stdout=PIPE, shell=False)
    results = list(_process_output(process))
    return results



def _fasta_to_list(filename: str) -> List[Tuple[str, str]]:
    """fasta to list with SimpleFastaParser"""
    with open(filename, "r") as handle:
        return [record for record in SimpleFastaParser(handle)]



def _getfasta_to_list(
        transcriptome_dict: FastaDict, iterable_of_bed: Iterable[Coordinate]) \
        -> List[Tuple[str, str]]:
    """Convert to a list the generator from getfasta"""
    return list(_get_fasta(transcriptome_dict, iterable_of_bed))



def _silent_popen(command: List[str]) -> Popen:
    """Create a Popen with no stderr and stdout"""
    return Popen(
        command,
        stdout=open("/dev/null", 'w'),
        stderr=open("/dev/null", 'w'),
        shell=False
    )



def _bf_and_process(reads_fns: List[str], transcriptome_fn: str) -> List[Coordinate]:
    """(list of str, str) -> list

    Build the BF and process the reads
    """
    tmp_dir = tempfile.mkdtemp()
    tmp_bf = tmp_dir + "/transcriptome_noreads.bf"
    args = {
        "kmer": 30,
        "bloom_size": "100M",
        "levels": 1,
        "threads": 1,
        "bloom": tmp_bf,
        "reads": reads_fns,
        "fasta": transcriptome_fn,
        "max_fp_bases": 5,
        "max_overlap": 10
    }
    command = _get_build_bf_command(args, reads_fns)
    process = _silent_popen(command)
    process.wait()
    results = _find_exons_pipeline(args)
    shutil.rmtree(tmp_dir)
    return list(results)
