[![Build Status](https://travis-ci.org/jlanga/exfi.svg?branch=master)](https://travis-ci.org/jlanga/exfi)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/e3200fef4f7549d78c2cf85364f1c602)](https://www.codacy.com/app/jorge.langa.arranz/exfi?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=jlanga/exfi&amp;utm_campaign=Badge_Grade)
[![Codacy Badge](https://api.codacy.com/project/badge/Coverage/e3200fef4f7549d78c2cf85364f1c602)](https://www.codacy.com/app/jorge.langa.arranz/exfi?utm_source=github.com&utm_medium=referral&utm_content=jlanga/exfi&utm_campaign=Badge_Coverage)
# exfi
Get exons from a transcriptome and raw genomic reads using abyss-bloom and bedtools

## Citation

exfi was published on Ecology and Evolution

> Langa J, Estonba A, Conklin D. EXFI: Exon and splice graph prediction without a reference genome.
> Ecol Evol. 2020;00:1–14. https://doi.org/10.1002/ece3.6587

## Requirements

Docker or different apt and conda packages (see installation guide).

## How to install

To install other dependencies, follow the instructions from the travis files:

1. Install packages with `apt`:

```sh
sudo apt install \
    autoconf build-essential bzip2 cmake curl gcc git libboost-dev libsdsl3 \
    libz-dev zlib1g
```

2. Install conda, then configure channels and install

```sh
conda config --add channels conda-forge
conda config --add channels defaults
conda config --add channels r
conda config --add channels bioconda
conda install --yes abyss=2.0.1 bedtools biopython pandas pip
```

3. Install `biobloomtools`

You may need to use `sudo` in the last command:

```sh
# Install biobloomtools
git clone --recursive https://github.com/bcgsc/biobloom.git && \
cd biobloom/ && \
git submodule update --init && \
git checkout 0a42916922d42611a087d4df871e424a8907896e && \
./autogen.sh && \
./configure --prefix=/usr/local/ && \
make -j 4 && \
make install
```

4. Copy this repo and install it with `pip`:

```sh
pip install https://github.com/jlanga/exfi/archive/v1.5.6.zip
```

If you have access to Docker, you can create a Debian container with the following command:

```sh
docker build --rm --tag exfi:v1.5.6 github.com/jlanga/exfi-docker
```

[More info](https://github.com/jlanga/exfi-docker)



## Required data

- A transcriptome in fasta format (take it from Ensembl for example, or the result of a _de novo_ transcriptome assembler like trinity, trans-abyss or oases)

- A set of genomic reads in fastq format, paired end or not. `.gz` files are allowed.

## Running the pipeline

1. Make a baited Bloom filter of the genomic reads with `build_baited_bloom_filter`:
- `genome.fa.gz` is the set of genomic reads and
- `genome_k25_m100M_l1.bf` is the resulting Bloom filter, made of kmers of length 25, a size of 100 MB and the number of times of a kmer must be in the reads is 1 (levels).

```sh
# Assuming that you are in the exfi folder:
build_baited_bloom_filter \
    --input-fasta data/transcript.fa \
    --kmer 25 \
    --bloom-size 100M \
    --levels 1 \
    --threads 4 \
    --output-bloom genome_k25_m100M_l1.bf \
    data/genome.fa.gz
```

2. Run `build_splice_graph` to get putative exons in the transcriptome.
- `data/transcript.fa` is the input transcriptome,
- `genome_k25_m500M_l1.bf` is the Bloom filter generated above
- kmer length has to be the same
- `test.gfa` is the resulting splice graph in [GFA1 format](https://github.com/GFA-spec/GFA-spec/blob/master/GFA1.md).

```sh
build_splicegraph \
    --input-fasta data/transcript.fa \
    --input-bloom genome_k25_m100M_l1.bloom \
    --kmer 25 \
    --max-fp-bases 5 \
    --output-gfa test.gfa
```

This splice graph can be visualized with [Bandage](https://rrwick.github.io/Bandage/)

Example:

```
H	VN:Z:1.0
S	ENSDART00000033574.5:0-216	GTAAGCCGCGGCGGTGTGTGTGTGTGTGTGTGTTCTCCGTCATCTGTGTTCTGCTGAATGATGAGGACAGACGTGTTTCTCCAGCGGAGGAAGCGTAGAGATGTTCTGCTCTCCATCATCGCTCTTCTTCTGCTCATCTTCGCCATCGTTCATCTCGTCTTCTGCGCTGGACTGAGTTTCCAGGGTTCGAGTTCTGCTCGCGTCCGCCGAGACCTC
S	ENSDART00000033574.5:216-398	GAGAATGCGAGTGAGTGTGTGCAGCCACAGTCGTCTGAGTTTCCTGAAGGATTCTTCACGGTGCAGGAGAGGAAAGATGGAGGAATCCTGATTTACTTCATGATCATCTTCTACATGCTGCTGTCCGTCTCCATCGTGTGTGATGAATATTTTCTGCCATCTCTGGAGGTCATCAGCGAGCG
S	ENSDART00000033574.5:397-482	GTCTTGGTCTCTCGCAGGATGTTGCTGGAGCCACGTTTATGGCTGCGGGGAGTTCGGCTCCAGAGCTCGTCACTGCATTTCTGGG
S	ENSDART00000033574.5:480-586	GGTGTGTTTGTGACGAAGGGCGACATCGGCGTCAGCACCATCATGGGTTCTGCTGTCTATAACCTGCTGTGCATCTGTGCAGCGTGCGGCCTGCTGTCCTCTGCAG
S	ENSDART00000033574.5:585-687	GTTGGTCGTCTGAGCTGCTGGCCGTTGTTCAGAGATTGTGTTGCGTACTCCATCAGTGTCGCCGCCGTCATCGCCATCATCTCAGATAACAGAGTTTACTGG
S	ENSDART00000033574.5:685-969	GGTATGATGGCGCGTGTCTCCTGCTGGTGTACGGTGTGTATGTAGCTGTACTGTGTTTCGATCTGAAGATCAGCGAGTACGTGATGCAGCGCTTCAGTCCATGCTGCTGGTGTCTGAAACCTCGCGATCGTGACTCAGGCGAGCAGCAGCCTCTAGTGGGCTGGAGTGACGACAGCAGCCTGCGGGTCCAGCGCCGTTCCAGAAATGACAGCGGAATATTCCAGGATGATTCTGGATATTCACATCTATCGCTCAGCCTGCACGGACTCAACGAAATCAGCGAC
S	ENSDART00000033574.5:969-1177	GAGCACAAGAGTGTGTTCTCCATGCCGGATCACGATCTGAAGCGAATCCTGTGGGTTTTGTCTCTTCCGGTCAGCACTCTGCTGTTTGTGAGCGTTCCCGACTGCAGGAGACCCTTCTGGAAGAACTTCTACATGCTGACCTTCCTGATGTCCGCCGTCTGGATTTCTGCATTCACTTATGTGCTGGTCTGGATGGTCACAATCGTGG
S	ENSDART00000033574.5:1176-1283	GGGGAGACTCTGGGAATCCCGGACACAGTGATGGGAATGACTCTTCTGGCTGCAGGAACCAGTATCCCCGACACCGTGGCCAGTGTGATGGTGGCACGAGAAGGTAA
S	ENSDART00000033574.5:1277-2002	AGGTAAATCTGATATGGCCATGTCCAACATCGTGGGCTCTAACGTGTTCGATATGCTGTGTCTGGGCCTGCCGTGGTTCATCCAGACGGTGTTTGTTGACGTGGGCTCCCCGGTGGATGTCAACAGCTCGGGGCTGGTCTTCATGTCCTGCACGCTGCTGCTCTCCATCATCTTCCTCTTCCTCGCCGTGCACATCAACGGCTGGAAGCTGGACTGGAAGCTGGGTCTGGTGTGTTTGGCGTGTTACATTCTGTTCGCAACACTCTCCATCCTGTACGAGCTCGGCATCATCGGGAACAATCCCATACGCTCCTGCAGCGACTGAACACTGCTCTACAGCGCCCCCTTATGGACAACACAAGGACGTGACTCTTTATAACCCTCTAAAGTGCACAGGTTCATTACTGAATACAAGAAAATAGAACTGCGAGACGTCAACTCAAAATACAAGAGAAGTCAAAGTGCGAGATGTAAAAAATATATGCACATAAATGAGGATAAACTTTTTATTTAATAAGACAAAACTGCATAAAGTCTGATGTGAACACTGCTCAACAGCGCCCTCTCATGGACAACACATGGATCTGACTCTTATTAACCCTCCAGAGTGCAAATACACTAACACAACGTAATATAACCAAGTTAAAATGGCAAGATGTGAACTCAAAATACAAGAAAGCAGTCAAGATGCCCGACATAACAAATGTGCATTAAAATGTAAGCCC
L	ENSDART00000033574.5:0-216	+	ENSDART00000033574.5:216-398	+	0M
L	ENSDART00000033574.5:216-398	+	ENSDART00000033574.5:397-482	+	1M
L	ENSDART00000033574.5:397-482	+	ENSDART00000033574.5:480-586	+	2M
L	ENSDART00000033574.5:480-586	+	ENSDART00000033574.5:585-687	+	1M
L	ENSDART00000033574.5:585-687	+	ENSDART00000033574.5:685-969	+	2M
L	ENSDART00000033574.5:685-969	+	ENSDART00000033574.5:969-1177	+	0M
L	ENSDART00000033574.5:969-1177	+	ENSDART00000033574.5:1176-1283	+	1M
L	ENSDART00000033574.5:1176-1283	+	ENSDART00000033574.5:1277-2002	+	6M
C	ENSDART00000033574.5	+	ENSDART00000033574.5:0-216	+	0	216M
C	ENSDART00000033574.5	+	ENSDART00000033574.5:216-398	+	216	182M
C	ENSDART00000033574.5	+	ENSDART00000033574.5:397-482	+	397	85M
C	ENSDART00000033574.5	+	ENSDART00000033574.5:480-586	+	480	106M
C	ENSDART00000033574.5	+	ENSDART00000033574.5:585-687	+	585	102M
C	ENSDART00000033574.5	+	ENSDART00000033574.5:685-969	+	685	284M
C	ENSDART00000033574.5	+	ENSDART00000033574.5:969-1177	+	969	208M
C	ENSDART00000033574.5	+	ENSDART00000033574.5:1176-1283	+	1176	107M
C	ENSDART00000033574.5	+	ENSDART00000033574.5:1277-2002	+	1277	725M
P	ENSDART00000033574.5	ENSDART00000033574.5:0-216+,ENSDART00000033574.5:216-398+,ENSDART00000033574.5:397-482+,ENSDART00000033574.5:480-586+,ENSDART00000033574.5:585-687+,ENSDART00000033574.5:685-969+,ENSDART00000033574.5:969-1177+,ENSDART00000033574.5:1176-1283+,ENSDART00000033574.5:1277-2002+	*
```

3.  Get exonic sequences

To extract meaningful information from the GFA file, we provide two scripts:

- `gfa_to_exons`: which returns the predicted exons in FASTA format. For each record, each sequence comes with a unique identifier (`EXON[0-9]+`), a description indicating the coordinates of this exon with respect to the different transcripts (`TR1:0-200 TR2:105-305`), and the sequence of nucleotides. It is possible to hard and soft mask nucleotides that may not be correct. Example (soft masked):

```
>EXON00000000003 ENSDART00000033574.5:397-482
gTCTTGGTCTCTCGCAGGATGTTGCTGGAGCCACGTTTATGGCTGCGGGGAGTTCGGCTC
CAGAGCTCGTCACTGCATTTCTGgg
>EXON00000000004 ENSDART00000033574.5:480-586
ggTGTGTTTGTGACGAAGGGCGACATCGGCGTCAGCACCATCATGGGTTCTGCTGTCTAT
AACCTGCTGTGCATCTGTGCAGCGTGCGGCCTGCTGTCCTCTGCAg
```

- `gfa_to_gapped_transcript`: which returns the transcript with interleaved `N`s where it is predicted to be an intron. Example (hard masked):
```
>ENSDART00000033574.5 EXON00000000001,EXON00000000002,EXON00000000003,EXON00000000004,EXON00000000005,EXON00000000006,EXON00000000007,EXON00000000008,EXON00000000009
GTAAGCCGCGGCGGTGTGTGTGTGTGTGTGTGTTCTCCGTCATCTGTGTTCTGCTGAATG
ATGAGGACAGACGTGTTTCTCCAGCGGAGGAAGCGTAGAGATGTTCTGCTCTCCATCATC
GCTCTTCTTCTGCTCATCTTCGCCATCGTTCATCTCGTCTTCTGCGCTGGACTGAGTTTC
CAGGGTTCGAGTTCTGCTCGCGTCCGCCGAGACCTCNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNGAGAATGCGAGTGAGTGTGTGCAGCCACAGTCGTCTGAGTTTCC
TGAAGGATTCTTCACGGTGCAGGAGAGGAAAGATGGAGGAATCCTGATTTACTTCATGAT
CATCTTCTACATGCTGCTGTCCGTCTCCATCGTGTGTGATGAATATTTTCTGCCATCTCT
GGAGGTCATCAGCGAGCNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNT
CTTGGTCTCTCGCAGGATGTTGCTGGAGCCACGTTTATGGCTGCGGGGAGTTCGGCTCCA
GAGCTCGTCACTGCATTTCTGNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNTGTGTTTGTGACGAAGGGCGACATCGGCGTCAGCACCATCATGGGTTCTGCTGTC
TATAACCTGCTGTGCATCTGTGCAGCGTGCGGCCTGCTGTCCTCTGCANNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNTTGGTCGTCTGAGCTGCTGGCCGTTGTTCA
GAGATTGTGTTGCGTACTCCATCAGTGTCGCCGCCGTCATCGCCATCATCTCAGATAACA
GAGTTTACTNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNTATGATG
GCGCGTGTCTCCTGCTGGTGTACGGTGTGTATGTAGCTGTACTGTGTTTCGATCTGAAGA
TCAGCGAGTACGTGATGCAGCGCTTCAGTCCATGCTGCTGGTGTCTGAAACCTCGCGATC
GTGACTCAGGCGAGCAGCAGCCTCTAGTGGGCTGGAGTGACGACAGCAGCCTGCGGGTCC
AGCGCCGTTCCAGAAATGACAGCGGAATATTCCAGGATGATTCTGGATATTCACATCTAT
CGCTCAGCCTGCACGGACTCAACGAAATCAGCGACNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNGAGCACAAGAGTGTGTTCTCCATGCCGGATCACGATCTGAAGCGA
ATCCTGTGGGTTTTGTCTCTTCCGGTCAGCACTCTGCTGTTTGTGAGCGTTCCCGACTGC
AGGAGACCCTTCTGGAAGAACTTCTACATGCTGACCTTCCTGATGTCCGCCGTCTGGATT
TCTGCATTCACTTATGTGCTGGTCTGGATGGTCACAATCGTGNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNGGGAGACTCTGGGAATCCCGGACACAGTGATGGGAA
TGACTCTTCTGGCTGCAGGAACCAGTATCCCCGACACCGTGGCCAGTGTGATGGTGGCAC
GAGANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNATCT
GATATGGCCATGTCCAACATCGTGGGCTCTAACGTGTTCGATATGCTGTGTCTGGGCCTG
CCGTGGTTCATCCAGACGGTGTTTGTTGACGTGGGCTCCCCGGTGGATGTCAACAGCTCG
GGGCTGGTCTTCATGTCCTGCACGCTGCTGCTCTCCATCATCTTCCTCTTCCTCGCCGTG
CACATCAACGGCTGGAAGCTGGACTGGAAGCTGGGTCTGGTGTGTTTGGCGTGTTACATT
CTGTTCGCAACACTCTCCATCCTGTACGAGCTCGGCATCATCGGGAACAATCCCATACGC
TCCTGCAGCGACTGAACACTGCTCTACAGCGCCCCCTTATGGACAACACAAGGACGTGAC
TCTTTATAACCCTCTAAAGTGCACAGGTTCATTACTGAATACAAGAAAATAGAACTGCGA
GACGTCAACTCAAAATACAAGAGAAGTCAAAGTGCGAGATGTAAAAAATATATGCACATA
AATGAGGATAAACTTTTTATTTAATAAGACAAAACTGCATAAAGTCTGATGTGAACACTG
CTCAACAGCGCCCTCTCATGGACAACACATGGATCTGACTCTTATTAACCCTCCAGAGTG
CAAATACACTAACACAACGTAATATAACCAAGTTAAAATGGCAAGATGTGAACTCAAAAT
ACAAGAAAGCAGTCAAGATGCCCGACATAACAAATGTGCATTAAAATGTAAGCCC
```


## Attributions

Written by Jorge Langa

## Bibliography

- [abyss](https://github.com/bcgsc/abyss/)

- [bandage](https://rrwick.github.io/Bandage/)

- [bedtools](https://bedtools.readthedocs.io/)

- [biobloomtools](https://github.com/bcgsc/biobloom)

- [biopython](http://biopython.org/)

- [networkx](https://networkx.github.io/)

- [pandas](http://pandas.pydata.org/)

- [funniest](https://pypi.python.org/pypi/funniest/0.1)

- [sphinx](www.sphinx-doc.org)

- [unittest](https://docs.python.org/3/library/unittest.html)
