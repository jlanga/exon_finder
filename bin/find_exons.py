#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
    usage = 'python3 fill_indels.py -t treseq.tsv -i bloom.filter -k 27 ',
    description='Fix small indels within introns with help of abyss-sealer',
    epilog = 'Jorge Langa. Send issues and pull requests to github.com/jlanga/'
        'exon_finder'
)

parser.add_argument(
    '--input-fasta',
    '-t',
    type = str,
    required = True,
    help = 'Input transcriptome in FASTA format',
    dest = 'input_fasta',
    metavar = 'FASTA'
)

parser.add_argument(
    '--input-bloom',
    '-i',
    type = str,
    required = True,
    help = 'Bloom filter with genomic sequences (from abyss-bloom)',
    dest = 'bloom_filter',
    metavar = 'BLOOM'
)

parser.add_argument(
    '--kmer',
    '-k',
    type = int,
    required = True,
    help = 'The size of the k-mer (enter the same as in the bloom filter)',
    dest = 'kmer',
    metavar = 'KMER'
)

parser.add_argument(
    '--output-fasta',
    '-o',
    type = str,
    required = False,
    help = 'Path to output fasta file',
    dest = "output_fasta",
    metavar = "FILE"
)

args = parser.parse_args()


def run_pipeline(transcriptome_fn, kmer, bloom_filter_fn, output_fasta):
    """(str, int, str) -> str
    Run the find exons pipeline:
        - abyss-bloom kmers: Test all kmers in the transcriptome
        - bedtools merge: Check overlap and merge
        - bedtools getfasta: convert bed to fasta
    """
    from subprocess import Popen, PIPE
    from sys import stdin, stdout, stderr
    from exfi.read_fasta_from_bedtools_getfasta import read_fasta_from_bedtools_getfasta
    from exfi.write_fasta import write_fasta
    from exfi.read_fasta import read_fasta

    abyss_bloom_kmers = [  # Run abyss-bloom kmers
    "abyss-bloom", "kmers",
        "--kmer", str(kmer),
        "--verbose",
        "--bed",
        bloom_filter_fn,
        transcriptome_fn
    ]

    bedtools_merge = [  # Merge overlapping kmers
    "bedtools", "merge",
        "-d", str(- kmer + 2)
    ]

    bedtools_getfasta = [  # Get transcriptid:coordinates TAB sequence
        "bedtools", "getfasta",
            "-fi", transcriptome_fn,
            "-bed", "-",
            #"-tab"
    ]
    
    # Run the pipeline
    process_abyss_bloom_kmers = Popen(
        abyss_bloom_kmers,
        stdout= PIPE,
    )
    
    process_bedtools_merge = Popen(
        bedtools_merge,
        stdin= process_abyss_bloom_kmers.stdout,
        stdout= PIPE
    )

    process_bedtools_getfasta = Popen(
        bedtools_getfasta,
        stdin= process_bedtools_merge.stdout,
        stdout= PIPE,
    )
    
    process_abyss_bloom_kmers.stdout.close()
    process_bedtools_merge.stdout.close()
    output = process_bedtools_getfasta.communicate()[0]
    process_abyss_bloom_kmers.wait()
    process_bedtools_merge.wait()

    with open(output_fasta, "w") as f_out:
        for line in output.decode().split("\n"):
            if line.startswith(">"):
                line = line.rsplit(":")[0]
            f_out.write(line + "\n")


if __name__ == "__main__":
    
    import sys
    
    args = vars(parser.parse_args())
    transcriptome = args["input_fasta"]
    bloom_filter = args["bloom_filter"]
    kmer = args["kmer"]
    output_fasta = args["output_fasta"]

    run_pipeline(transcriptome, kmer, bloom_filter, output_fasta)
