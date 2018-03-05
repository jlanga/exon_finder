#!/usr/bin/env bash
set -euxo pipefail

mkdir -p results/

k=31
m=4G
l=1

if [ ! -f results/drer25sim_k${k}_m${m}_l${l}.bloom ]; then
build_baited_bloom_filter \
    --input-fasta data/Danio_rerio.GRCz10.cdna.25.fa \
    --kmer $k \
    --bloom-size $m \
    --levels $l \
    --threads 4 \
    --output-bloom results/drer25sim_k${k}_m${m}_l${l}.bloom \
    data/drer25.1_1.fq.gz \
    data/drer25.1_2.fq.gz \
    data/drer25.2_1.fq.gz \
    data/drer25.2_2.fq.gz
fi

if [ ! -f results/drer25real_k${k}_m${m}_l1.bloom ]; then
build_baited_bloom_filter \
    --input-fasta data/Danio_rerio.GRCz10.cdna.25.fa \
    --kmer $k \
    --bloom-size $m \
    --levels 1 \
    --threads 4 \
    --output-bloom results/drer25real_k${k}_m${m}_l1.bloom \
    data/Danio_rerio.GRCz10.dna.25.fa.gz
fi

build_splice_graph \
    --input-fasta data/Danio_rerio.GRCz10.cdna.25.fa \
    --input-bloom results/drer25sim_k${k}_m${m}_l${l}.bloom \
    --kmer $k \
    --max-fp-bases 3 \
    --output-gfa results/drer25sim.gfa \
    --verbose \
    --threads 4

build_splice_graph \
    --input-fasta data/Danio_rerio.GRCz10.cdna.25.fa \
    --input-bloom results/drer25sim_k${k}_m${m}_l${l}.bloom \
    --kmer $k \
    --max-fp-bases 3 \
    --correct \
    --output-gfa results/drer25sim_correct.gfa \
    --verbose \
    --threads 4

build_splice_graph \
    --input-fasta data/Danio_rerio.GRCz10.cdna.25.fa \
    --input-bloom results/drer25sim_k${k}_m${m}_l${l}.bloom \
    --kmer $k \
    --max-fp-bases 3 \
    --correct \
    --polish \
    --output-gfa results/drer25sim_correct_polish.gfa \
    --verbose \
    --threads 4

build_splice_graph \
    --input-fasta data/Danio_rerio.GRCz10.cdna.25.fa \
    --input-bloom results/drer25sim_k${k}_m${m}_l${l}.bloom \
    --kmer $k \
    --max-fp-bases 3 \
    --correct \
    --polish \
    --collapse \
    --output-gfa results/drer25sim_correct_polish_collapse.gfa \
    --verbose \
    --threads 4

build_splice_graph \
    --input-fasta data/Danio_rerio.GRCz10.cdna.25.fa \
    --input-bloom results/drer25real_k${k}_m${m}_l1.bloom \
    --kmer $k \
    --max-fp-bases 3 \
    --correct \
    --output-gfa results/drer25real.gfa \
    --verbose \
    --threads 4 \
    --debug

gfa1_to_exons \
    --input-gfa results/drer25sim.gfa \
    --output-fasta results/drer25sim_exons.fa \
    --soft-mask-overlaps \
    --debug

gfa1_to_exons \
    --input-gfa results/drer25real.gfa \
    --output-fasta results/drer25real_exons.fa \
    --soft-mask-overlaps \
    --debug

bash src/pr_chr25.sh
