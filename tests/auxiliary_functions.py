#!/usr/bin/env python3

"""
Auxiliary functions and classes for testing
"""


import tempfile
import shutil
from subprocess import \
    Popen, PIPE

import numpy as np
import pandas as pd

from Bio.SeqIO.FastaIO import SimpleFastaParser

from exfi.find_exons import \
    process_output, \
    get_fasta, \
    find_exons

from exfi.build_baited_bloom_filter import \
    _get_build_bf_command

def _command_to_list(command):
    """Execute command and return output as list of strings"""
    process = Popen(command, stdout=PIPE, shell=False)
    results = process_output(process)
    return results



def _fasta_to_list(filename):
    """fasta to list with SimpleFastaParser"""
    with open(filename, "r") as handle:
        return [record for record in SimpleFastaParser(handle)]



def _getfasta_to_list(transcriptome_dict, iterable_of_bed):
    """Convert to a list the generator from getfasta"""
    return list(get_fasta(transcriptome_dict, iterable_of_bed))



def _silent_popen(command):
    """Create a Popen with no stderr and stdout"""
    return Popen(
        command,
        stdout=open("/dev/null", 'w'),
        stderr=open("/dev/null", 'w'),
        shell=False
    )



def _bf_and_process(reads_fns, transcriptome_fn):
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
    results = find_exons(args)
    shutil.rmtree(tmp_dir)
    bed3 = pd.DataFrame(
        data=results,
        columns=["chrom", "chromStart", "chromEnd"]
    )

    bed3.chromStart.astype(np.int64)
    bed3.chromEnd.astype(np.int64)
    return bed3
