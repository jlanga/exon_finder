#!/usr/bin/env python3

import unittest
from exfi.build_splice_graph import \
    _bed3_to_str, \
    bed3_records_to_bed6df, \
    bed6df_to_path2node, \
    bed6df_to_node2coordinates, \
    compute_edge_overlaps, \
    build_splice_graph

import networkx as nx
import pandas as pd

from tests.test_data import *

bed3_cols = ['chrom', 'start', 'end']
bed6_cols = ['chrom', 'start', 'end', 'name', 'score', 'strand']


def _prepare_overlaps(bed3_records):
    """Compute splicegraph prior the computation of overlaps"""
    splice_graph = nx.DiGraph()
    bed6df = bed3_records_to_bed6df(bed3_records)
    splice_graph.add_nodes_from(bed6df["name"].tolist())
    node2coords = bed6df_to_node2coordinates(bed6df)
    nx.set_node_attributes(
        G=splice_graph,
        name="coordinates",
        values=node2coords
    )
    transcript2path = bed6df_to_path2node(bed6df)
    for path in transcript2path.values():
        splice_graph.add_path(path)
    return splice_graph


class TestBed3ToStr(unittest.TestCase):

    def test_empty(self):
        """_bed3_to_str: empty record"""
        with self.assertRaises(IndexError):
            _bed3_to_str([])

    def test_malformed1(self):
        """_bed3_to_str: record of 2 elements"""
        with self.assertRaises(IndexError):
            _bed3_to_str((0,1))

    def test_malformed2(self):
        """_bed3_to_str: record of 4 elements"""
        with self.assertRaises(IndexError):
            _bed3_to_str((0,1,2,3))

    def test_record(self):
        """_bed3_to_str: correct record"""
        self.assertEqual(
            _bed3_to_str(("tr", 10, 15)),
            "tr:10-15"
        )


class TestBed3RecordsToBed6DF(unittest.TestCase):

    def test_empty_index(self):
        """bed3_records_to_bed6df: empty exome"""
        actual = bed3_records_to_bed6df([])
        expected = bed6df_empty
        self.assertTrue(
            actual.equals(expected)
        )

    def test_one_entry(self):
        """bed3_records_to_bed6df: single exon"""
        actual = bed3_records_to_bed6df(bed3records_simple)
        expected = bed6df_simple
        self.assertTrue(
            actual.equals(expected)
        )

    def test_multiple(self):
        """bed3_records_to_bed6df: multiple transcripts - multiple exons"""
        actual = bed3_records_to_bed6df(bed3records_complex)
        expected = bed6df_complex
        self.assertTrue(
            actual.equals(expected)
        )


class TestBed6DFToPath2Node(unittest.TestCase):

    def test_empty(self):
        """bed6df_to_path2node: convert an empty exome to path"""
        self.assertEqual(
            bed6df_to_path2node(bed6df_empty),
            path_empty
        )


    def test_single(self):
        """bed6df_to_path2node: convert an single exon transcript to path"""
        self.assertEqual(
            bed6df_to_path2node(bed6df_simple),
            path_simple
        )

    def test_multiple(self):
        """bed6df_to_path2node: convert an single exon transcript to path"""
        self.assertEqual(
            bed6df_to_path2node(bed6df_complex),
            path_complex
        )


class TestBed6ToNode2Coord(unittest.TestCase):

    def test_empty(self):
        """bed6df_to_node2coordinates: empty records"""
        self.assertEqual(
            node2coords_empty,
            bed6df_to_node2coordinates(bed6df_empty)
        )

    def test_simple(self):
        """bed6df_to_node2coordinates: single node"""
        self.assertEqual(
            bed6df_to_node2coordinates(bed6df_simple),
            node2coords_simple
        )

    def test_complex(self):
        """bed6df_to_node2coordinates: complex case"""
        self.assertEqual(
            bed6df_to_node2coordinates(bed6df_complex),
            node2coords_complex
        )


class TestComputeEdgeOverlaps(unittest.TestCase):

    def test_empty_exome(self):
        """compute_overlaps: compute the overlaps of an empty exome"""
        splice_graph = _prepare_overlaps({})
        overlaps = compute_edge_overlaps(splice_graph)
        self.assertEqual(overlaps, {})

    def test_single_exon(self):
        """compute_overlaps: compute the overlaps of a single exon exome"""
        splice_graph = _prepare_overlaps(bed3records_simple)
        overlaps = compute_edge_overlaps(splice_graph)
        self.assertEqual(overlaps, overlaps_simple)

    def test_multiple_exons(self):
        """compute_overlaps: compute the overlaps of a simple exome"""
        splice_graph = _prepare_overlaps(bed3records_complex)
        overlaps = compute_edge_overlaps(splice_graph)
        self.assertEqual(
            overlaps, overlaps_complex
        )


class TestBuildSpliceGraph(unittest.TestCase):

    def test_empty(self):
        """build_splice_graph: compute the splice graph of an empty set of exons"""
        actual = build_splice_graph(bed3records_empty)
        self.assertTrue(
            nx.is_isomorphic(
                actual,
                splice_graph_empty
            )
        )
        self.assertEqual(
            nx.get_node_attributes(G=actual, name="coordinates"),
            nx.get_node_attributes(G=splice_graph_empty, name="coordinates"),
        )
        self.assertEqual(
            nx.get_edge_attributes(G=actual, name="overlaps"),
            nx.get_edge_attributes(G=splice_graph_empty, name="overlaps"),
        )

    def test_simple(self):
        """build_splice_graph: compute the splice graph of a singe exon"""
        actual = build_splice_graph(bed3records_simple)
        self.assertTrue(
            nx.is_isomorphic(
                actual,
                splice_graph_simple
            )
        )
        self.assertEqual(
            nx.get_node_attributes(G=actual, name="coordinates"),
            nx.get_node_attributes(G=splice_graph_simple, name="coordinates"),
        )
        self.assertEqual(
            nx.get_edge_attributes(G=actual, name="overlaps"),
            nx.get_edge_attributes(G=splice_graph_simple, name="overlaps"),
        )

    def test_multiple(self):
        """build_splice_graph: compute the splice graph of a set of exons"""
        actual = build_splice_graph(bed3records_complex)
        self.assertTrue(
            nx.is_isomorphic(
                actual,
                splice_graph_complex
            )
        )
        self.assertEqual(
            nx.get_node_attributes(G=actual, name="coordinates"),
            nx.get_node_attributes(G=splice_graph_complex, name="coordinates"),
        )
        print(nx.get_edge_attributes(G=actual, name="overlaps"))
        print(nx.get_edge_attributes(G=splice_graph_complex, name="overlaps"))
        self.assertEqual(
            nx.get_edge_attributes(G=actual, name="overlaps"),
            nx.get_edge_attributes(G=splice_graph_complex, name="overlaps"),
        )


if __name__ == '__main__':
    unittest.main()
