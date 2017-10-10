#!/usr/bin/env python3

import networkx as nx
import pandas as pd

def _process_index(exons_index):
    """(dict of SeqRecords) -> list

    Convert a indexed_exons to a list of tuples with the info in the header
    Note: assumes that the description is clean (the id is removed. By default
    biopython doesn't)
    """
    for exon in exons_index.values():
        exon_id = exon.id
        transcript_coords = exon.description.split(" ")
        for transcript_coord in transcript_coords:
            transcript_id, coords = transcript_coord.split(":")
            start, end = coords.split("-")
            start = int(start)
            end = int(end)
            yield [transcript_id, start, end, exon_id]


def exons_to_df(exons_index):
    """Convert an indexed fasta (exons) into a dataframe (~BED6)"""
    # Add mock values
    results = (line + ["+", 0] for line in _process_index(exons_index))
    return pd.DataFrame(
            data=results,
            columns=['transcript_id', 'start', 'end', 'exon_id', 'score', 'strand']
        )\
        .sort_values(
            by=['transcript_id', 'start','end']
        )


def exon_to_coordinates(exons_index):
    """Convert an indexed fasta (SeqIO.index) into a dict {exon_id : (transcript_id, start,
    end)} (str, int, int)"""
    exon_to_coord = {exon_id: [] for exon_id in exons_index.keys()}  # Fill
    results = _process_index(exons_index)
    for line in results:
        transcript_id, start, end, exon_id = line
        exon_to_coord[exon_id].append((transcript_id, start, end))
    return exon_to_coord


def transcript_to_path(exon_df):
    """Get a dict containing transcript_id to list of exons, indicating the path"""
    return exon_df\
        .sort_values(['transcript_id', 'start', 'end'])\
        .drop(['start','end','score','strand'], axis=1)\
        .groupby('transcript_id')\
        .agg(lambda exon: exon.tolist())\
        .rename(columns={'exon_id':'path'})\
        .to_dict()["path"]


def compute_edge_overlaps(splice_graph):
    """Get the overlap between connected exons:
    - Positive overlap means that they overlap that number of bases,
    - Zero that they occur next to each other
    - Negative that there is a gap in the transcriptome of that number of bases (one or multiple exons of length < kmer)

    Note: the splice graph must have already the nodes written with coordinates, and the edges alredy entered too.
    """
    #Init
    edge_overlaps = {edge: None for edge in splice_graph.edges()}
    exon2coord = nx.get_node_attributes(
        G=splice_graph,
        name='coordinates'
    )

    for (node1, node2) in sorted(edge_overlaps.keys()):

        # Get the list of transcripts that they belong
        node1_transcripts = set(coordinate[0] for coordinate  in exon2coord[node1])
        node2_transcripts = set(coordinate[0] for coordinate  in exon2coord[node2])
        intersection = node1_transcripts & node2_transcripts
        a_common_transcript = intersection.pop()

        # Get the end the first
        node1_coords = exon2coord[node1]
        node1_coords_in_transcript = [x for x in node1_coords if x[0] == a_common_transcript][0]
        node1_end = node1_coords_in_transcript[2]

        # Get the start of the next
        node2_coords = exon2coord[node2]
        node2_coords_in_transcript = [x for x in node2_coords if x[0] == a_common_transcript][0]
        node2_start = node2_coords_in_transcript[1]

        # Overlap in bases, 0 means one next to the other, negative numbers a gap
        overlap = node1_end - node2_start
        edge_overlaps[(node1, node2)] = overlap

    return edge_overlaps



def build_splicegraph(exon_index):
    """Build the splicegraph from a dict of SeqRecords

    Splicegraph is a directed graph, whose nodes
        - are exon_ids,
        - attributes are
            - coordinates [(transcript1, start, end), ..., (transcriptN, start, end)]
            - sequence in str format
    and whose edges
        - are connected exons in any way
        - attributes are the overlap between them:
            - positive means there is an overlap of that number of bases
            - zero means no overlap
            - negative means a gap of that number of bases
    """
    # Initialize grpah
    splice_graph = nx.DiGraph()

    # Add nodes
    splice_graph.add_nodes_from(exon_index.keys())
    nx.set_node_attributes(
        G=splice_graph,
        name='coordinates',
        values= exon_to_coordinates(exon_index)
    )
    nx.set_node_attributes(
        G=splice_graph,
        name='sequence',
        values={exon.id : str(exon.seq) for exon in exon_index.values()}
    )

    # Edges
    transcript2path = transcript_to_path(exons_to_df(exon_index))
    for path in transcript2path.values():
        splice_graph.add_path(path)

    nx.set_edge_attributes(
        G=splice_graph,
        name='overlap',
        values = compute_edge_overlaps(splice_graph)
    )

    return splice_graph
