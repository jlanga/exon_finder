#!/usr/bin/env python3

"""
Constant values for testing
"""

import pandas as pd
import networkx as nx

from exfi.io import index_fasta

BED6_COLS = ["chrom", "start", "end", "name", "score", "strand"]


BED3RECORDS_EMPTY_FN = "tests/find_exons/empty.bed"
BED3RECORDS_SIMPLE_FN = "tests/find_exons/simple.bed"
BED3RECORDS_COMPLEX_FN = "tests/find_exons/complex.bed"

BED3RECORDS_EMPTY = []
BED3RECORDS_SIMPLE = [
    ("ENSDART00000161035.1", 0, 326)
]
BED3RECORDS_COMPLEX = [
    ("ENSDART00000161035.1", 397, 472,),
    ("ENSDART00000165342.1", 1176, 1324),
    ("ENSDART00000161035.1", 0, 326),
    ("ENSDART00000165342.1", 125, 304),
    ("ENSDART00000165342.1", 746, 851),
    ("ENSDART00000165342.1", 974, 1097),
    ("ENSDART00000165342.1", 854, 886),
    ("ENSDART00000165342.1", 1098, 1175),
    ("ENSDART00000165342.1", 5, 127),
    ("ENSDART00000165342.1", 645, 746),
    ("ENSDART00000165342.1", 317, 460),
    ("ENSDART00000165342.1", 591, 650),
    ("ENSDART00000165342.1", 459, 592),
    ("ENSDART00000165342.1", 899, 953),
    ("ENSDART00000161035.1", 477, 523)
]

BED6DF_EMPTY = pd.DataFrame(columns=BED6_COLS)
BED6DF_SIMPLE = pd.DataFrame(
    data=[("ENSDART00000161035.1", 0, 326, "ENSDART00000161035.1:0-326", 0, "+")],
    columns=BED6_COLS
)
BED6DF_COMPLEX = pd.DataFrame(
    data=[
        ["ENSDART00000161035.1", 397, 472, "ENSDART00000161035.1:397-472", 0, "+"],
        ["ENSDART00000165342.1", 1176, 1324, "ENSDART00000165342.1:1176-1324", 0, "+"],
        ["ENSDART00000161035.1", 0, 326, "ENSDART00000161035.1:0-326", 0, "+"],
        ["ENSDART00000165342.1", 125, 304, "ENSDART00000165342.1:125-304", 0, "+"],
        ["ENSDART00000165342.1", 746, 851, "ENSDART00000165342.1:746-851", 0, "+"],
        ["ENSDART00000165342.1", 974, 1097, "ENSDART00000165342.1:974-1097", 0, "+"],
        ["ENSDART00000165342.1", 854, 886, "ENSDART00000165342.1:854-886", 0, "+"],
        ["ENSDART00000165342.1", 1098, 1175, "ENSDART00000165342.1:1098-1175", 0, "+"],
        ["ENSDART00000165342.1", 5, 127, "ENSDART00000165342.1:5-127", 0, "+"],
        ["ENSDART00000165342.1", 645, 746, "ENSDART00000165342.1:645-746", 0, "+"],
        ["ENSDART00000165342.1", 317, 460, "ENSDART00000165342.1:317-460", 0, "+"],
        ["ENSDART00000165342.1", 591, 650, "ENSDART00000165342.1:591-650", 0, "+"],
        ["ENSDART00000165342.1", 459, 592, "ENSDART00000165342.1:459-592", 0, "+"],
        ["ENSDART00000165342.1", 899, 953, "ENSDART00000165342.1:899-953", 0, "+"],
        ["ENSDART00000161035.1", 477, 523, "ENSDART00000161035.1:477-523", 0, "+"],
    ],
    columns=BED6_COLS
)\
.sort_values(BED6_COLS[0:3])

NODE2COORDS_EMPTY = {}
NODE2COORDS_SIMPLE = {
    "ENSDART00000161035.1:0-326": (("ENSDART00000161035.1", 0, 326), )
}
NODE2COORDS_COMPLEX = {
    "ENSDART00000161035.1:0-326": (("ENSDART00000161035.1", 0, 326), ),
    "ENSDART00000161035.1:397-472": (("ENSDART00000161035.1", 397, 472), ),
    "ENSDART00000161035.1:477-523": (("ENSDART00000161035.1", 477, 523), ),
    "ENSDART00000165342.1:5-127": (("ENSDART00000165342.1", 5, 127), ),
    "ENSDART00000165342.1:125-304": (("ENSDART00000165342.1", 125, 304), ),
    "ENSDART00000165342.1:317-460": (("ENSDART00000165342.1", 317, 460), ),
    "ENSDART00000165342.1:459-592": (("ENSDART00000165342.1", 459, 592), ),
    "ENSDART00000165342.1:591-650": (("ENSDART00000165342.1", 591, 650), ),
    "ENSDART00000165342.1:645-746": (("ENSDART00000165342.1", 645, 746), ),
    "ENSDART00000165342.1:746-851": (("ENSDART00000165342.1", 746, 851), ),
    "ENSDART00000165342.1:854-886": (("ENSDART00000165342.1", 854, 886), ),
    "ENSDART00000165342.1:899-953": (("ENSDART00000165342.1", 899, 953), ),
    "ENSDART00000165342.1:974-1097": (("ENSDART00000165342.1", 974, 1097), ),
    "ENSDART00000165342.1:1098-1175": (("ENSDART00000165342.1", 1098, 1175), ),
    "ENSDART00000165342.1:1176-1324": (("ENSDART00000165342.1", 1176, 1324),)
}

PATH_EMPTY = {}
PATH_SIMPLE = {"ENSDART00000161035.1": ("ENSDART00000161035.1:0-326",)}
PATH_COMPLEX = {
    "ENSDART00000161035.1": (
        "ENSDART00000161035.1:0-326",
        "ENSDART00000161035.1:397-472",
        "ENSDART00000161035.1:477-523",
    ),
    "ENSDART00000165342.1": (
        "ENSDART00000165342.1:5-127",
        "ENSDART00000165342.1:125-304",
        "ENSDART00000165342.1:317-460",
        "ENSDART00000165342.1:459-592",
        "ENSDART00000165342.1:591-650",
        "ENSDART00000165342.1:645-746",
        "ENSDART00000165342.1:746-851",
        "ENSDART00000165342.1:854-886",
        "ENSDART00000165342.1:899-953",
        "ENSDART00000165342.1:974-1097",
        "ENSDART00000165342.1:1098-1175",
        "ENSDART00000165342.1:1176-1324",
    )
}

OVERLAPS_EMPTY = {}
OVERLAPS_SIMPLE = {}
OVERLAPS_COMPLEX = {
    ("ENSDART00000161035.1:0-326", "ENSDART00000161035.1:397-472"): -71,
    ("ENSDART00000161035.1:397-472", "ENSDART00000161035.1:477-523"): -5,
    ("ENSDART00000165342.1:5-127", "ENSDART00000165342.1:125-304"): 2,
    ("ENSDART00000165342.1:125-304", "ENSDART00000165342.1:317-460"): -13,
    ("ENSDART00000165342.1:317-460", "ENSDART00000165342.1:459-592"): 1,
    ("ENSDART00000165342.1:459-592", "ENSDART00000165342.1:591-650"): 1,
    ("ENSDART00000165342.1:591-650", "ENSDART00000165342.1:645-746"): 5,
    ("ENSDART00000165342.1:645-746", "ENSDART00000165342.1:746-851"): 0,
    ("ENSDART00000165342.1:746-851", "ENSDART00000165342.1:854-886"): -3,
    ("ENSDART00000165342.1:854-886", "ENSDART00000165342.1:899-953"): -13,
    ("ENSDART00000165342.1:899-953", "ENSDART00000165342.1:974-1097"): -21,
    ("ENSDART00000165342.1:974-1097", "ENSDART00000165342.1:1098-1175"): -1,
    ("ENSDART00000165342.1:1098-1175", "ENSDART00000165342.1:1176-1324"): -1
}

SPLICE_GRAPH_EMPTY = nx.DiGraph()

SPLICE_GRAPH_SIMPLE = nx.DiGraph()
SPLICE_GRAPH_SIMPLE.add_nodes_from(BED6DF_SIMPLE["name"].tolist())
nx.set_node_attributes(
    G=SPLICE_GRAPH_SIMPLE,
    name="coordinates",
    values=NODE2COORDS_SIMPLE
)
for PATH in PATH_SIMPLE.values():
    SPLICE_GRAPH_SIMPLE.add_path(PATH)
nx.set_edge_attributes(
    G=SPLICE_GRAPH_SIMPLE,
    name="overlap",
    values=OVERLAPS_SIMPLE
)

SPLICE_GRAPH_COMPLEX = nx.DiGraph()
SPLICE_GRAPH_COMPLEX.add_nodes_from(BED6DF_COMPLEX["name"].tolist())
nx.set_node_attributes(
    G=SPLICE_GRAPH_COMPLEX, name="coordinates", values=NODE2COORDS_COMPLEX
)
for PATH in PATH_COMPLEX.values():
    SPLICE_GRAPH_COMPLEX.add_path(PATH)
nx.set_edge_attributes(
    G=SPLICE_GRAPH_COMPLEX, name="overlaps", values=OVERLAPS_COMPLEX
)

TRANSCRIPTOME_EMPTY_FN = "tests/build_splice_graph/transcriptome_empty.fa"
TRANSCRIPTOME_SIMPLE_FN = "tests/build_splice_graph/transcriptome_simple.fa"
TRANSCRIPTOME_COMPLEX_FN = "tests/build_splice_graph/transcriptome_complex.fa"

TRANSCRIPTOME_EMPTY = index_fasta(TRANSCRIPTOME_EMPTY_FN)
TRANSCRIPTOME_SIMPLE = index_fasta(TRANSCRIPTOME_SIMPLE_FN)
TRANSCRIPTOME_COMPLEX = index_fasta(TRANSCRIPTOME_COMPLEX_FN)

SEGMENTS_EMPTY = []
SEGMENTS_SIMPLE = [
    "S\t"
    "ENSDART00000161035.1:0-326\t"
    "TGCACGGGTTTATTGTTCACAAAGAGATCGACAATGTGCGCAACTAAAATAAACATAGTACATTTTGATTATACACGAACTTAAACTAAAGTCC"
    "AATCACACCTCCGCCCCGTTTCCACAGCAGCCTGTCAGGGTGGAGGAAAAGCGCGGCGGTCATGTGAGGCTCGAGCATCTCTCTCTCTCTCTCT"
    "CTCTCTCTCTCTACAGAATGATAGAGGGAGCTCGTGAATCACATCATAGTCGTCCTCCCCTCATTCGTCCTCTCCAGCAGACACCGAAAAACTG"
    "CGTTCATGCCAAAATGGGATGTGGAAATTCCTCCGCCACGAGCA\t"
    "LN:i:326\n"
]
SEGMENTS_COMPLEX = [
    "S\tENSDART00000161035.1:0-326\tTGCACGGGTTTATTGTTCACAAAGAGATCGACAATGTGCGCAACTAAAATAAACATAGTACAT"
    "TTTGATTATACACGAACTTAAACTAAAGTCCAATCACACCTCCGCCCCGTTTCCACAGCAGCCTGTCAGGGTGGAGGAAAAGCGCGGCGGTCAT"
    "GTGAGGCTCGAGCATCTCTCTCTCTCTCTCTCTCTCTCTCTCTACAGAATGATAGAGGGAGCTCGTGAATCACATCATAGTCGTCCTCCCCTCA"
    "TTCGTCCTCTCCAGCAGACACCGAAAAACTGCGTTCATGCCAAAATGGGATGTGGAAATTCCTCCGCCACGAGCA\tLN:i:326\n",
    "S\tENSDART00000161035.1:397-472\tAGGAACTACGGTGGAGTGTATGTGGGTCTTCCTGCTGATCTGACTGCAGTCGCTGCCAGTC"
    "AGTCCAAATCAACA\tLN:i:75\n",
    "S\tENSDART00000161035.1:477-523\tAGTCAACAGATGTTTATTGCAGACCTTCAGATAAAACAACATAGAA\tLN:i:46\n",
    "S\tENSDART00000165342.1:5-127\tTGGAGCTGAAGCCGAGTATCTTGGTATTGGACTGGAACAGAAATCCAGCAAAAACTTTAAGGG"
    "AAATCACTTTCATTTCATGATCGAAAAACTCCCGCAGATCATAAAAGAGTGGAAGGAAG\tLN:i:122\n",
    "S\tENSDART00000165342.1:125-304\tAGGACCTGTAGTAGAAACAAAACTAGGATCTCTGAGAGGTGCCTTCTTGACTGTGAAGGGC"
    "AAGGACACAATAGTCAATAGTTATCTAGGTGTGCCGTTCGCCAAGCCGCCTGTAGGACCCCTGAGACTTGCTCGACCACAGGCTGCAGAGAAAT"
    "GGCAAGGAGTTAGAGATGCCACCA\tLN:i:179\n",
    "S\tENSDART00000165342.1:317-460\tGTGCCTCCAGGAAAGGCAAATGACTGTAACTGAACTGGAGTTTCTATCGATGGATGTGGAG"
    "GTTCCTGAGGTCTCGGAGGATTGCCTGTATCTTAACATCTACACCCCAGTTAAACCTGGACAAGGAGACAAGAAGTTACCAG\tLN:i:143\n"
    ,
    "S\tENSDART00000165342.1:459-592\tGTCATGGTTTGGATTCATGGTGGAGGACTCTCTCTTGGATCGGCTTCAATGTATGATGGCT"
    "CTGTTCTGGCTGCGTATCAGGATGTGGTCGTGGTGCTCATTCAGTACAGATTGGGTCTTCTGGGGTTCTTAA\tLN:i:133\n",
    "S\tENSDART00000165342.1:591-650\tAGCACCGGAGACGAGCATGCGCCAGGAAACTATGGTTTTCTGGATCAAGTAGCTGCCCT\t"
    "LN:i:59\n",
    "S\tENSDART00000165342.1:645-746\tGCCCTTCAGTGGGTTCAGGAGAACATCCACAGCTTCGGTGGAGATCCTGGATCAGTGACCA"
    "TCTTTGGAGAGTCTGCTGGAGGAATCAGTGTATCCACGCT\tLN:i:101\n",
    "S\tENSDART00000165342.1:746-851\tGATTCTTTCCCCGCTGGCGTCTGGACTGTTTCATCGCGCCATTGCAGAAAGTGGAACTGCC"
    "TTCTGGGATGGTTTAGTCATGGCTGATCCTTTTCAGAGAGCCCA\tLN:i:105\n",
    "S\tENSDART00000165342.1:854-886\tTGCAGCCAAACAATGCAACTGTGACAGCAGCA\tLN:i:32\n",
    "S\tENSDART00000165342.1:899-953\tTGTCGACTGCATTATGCACTGGTCTGAAGAGGAGGCTCTGGAATGTGCTAAAAA\tLN:i:"
    "54\n",
    "S\tENSDART00000165342.1:974-1097\tCGTTGCTGTAGATTCTTATTTCCTTCCCAAACCCATCGAGGAGATTGTTGAGAAACAAGA"
    "GTTTAGTAAAGTTCCTCTCATCAACGGCATTAACAATGATGAGTTTGGCTTCTTGTTGGCTGA\tLN:i:123\n",
    "S\tENSDART00000165342.1:1098-1175\tTATTTCTTGGGTCCTGAATGGATGAATGGGTTGAAAAGAGAGCAAATCGCTGAAGCCTT"
    "GACGCTCACATATCCTGA\tLN:i:77\n",
    "S\tENSDART00000165342.1:1176-1324\tCCCAAGGATCGATGGATCATTGATCTGGTGGCGAAGGAATATCTGGGCGACACACACGA"
    "CCCCATTGAAATCCGTGAAGTTTATCGGGAGATGATGGGAGACGTGCTGTTTAACATCCCTGCCCTGCAACTGGCAAAACACCACAGCG\tLN:"
    "i:148\n"
]

LINKS_EMPTY = []
LINKS_SIMPLE = []
LINKS_COMPLEX = [
    "L\tENSDART00000161035.1:0-326\t+\tENSDART00000161035.1:397-472\t+\t71G\n",
    "L\tENSDART00000161035.1:397-472\t+\tENSDART00000161035.1:477-523\t+\t5G\n",
    "L\tENSDART00000165342.1:5-127\t+\tENSDART00000165342.1:125-304\t+\t2M\n",
    "L\tENSDART00000165342.1:125-304\t+\tENSDART00000165342.1:317-460\t+\t13G\n",
    "L\tENSDART00000165342.1:317-460\t+\tENSDART00000165342.1:459-592\t+\t1M\n",
    "L\tENSDART00000165342.1:459-592\t+\tENSDART00000165342.1:591-650\t+\t1M\n",
    "L\tENSDART00000165342.1:591-650\t+\tENSDART00000165342.1:645-746\t+\t5M\n",
    "L\tENSDART00000165342.1:645-746\t+\tENSDART00000165342.1:746-851\t+\t0M\n",
    "L\tENSDART00000165342.1:746-851\t+\tENSDART00000165342.1:854-886\t+\t3G\n",
    "L\tENSDART00000165342.1:854-886\t+\tENSDART00000165342.1:899-953\t+\t13G\n",
    "L\tENSDART00000165342.1:899-953\t+\tENSDART00000165342.1:974-1097\t+\t21G\n",
    "L\tENSDART00000165342.1:974-1097\t+\tENSDART00000165342.1:1098-1175\t+\t1G\n",
    "L\tENSDART00000165342.1:1098-1175\t+\tENSDART00000165342.1:1176-1324\t+\t1G\n"
]

CONTAINMENTS_EMPTY = []
CONTAINMENTS_SIMPLE = [
    "C\tENSDART00000161035.1\t+\tENSDART00000161035.1:0-326\t+\t0\t326M\n"
]
CONTAINMENTS_COMPLEX = [
    "C\tENSDART00000161035.1\t+\tENSDART00000161035.1:0-326\t+\t0\t326M\n",
    "C\tENSDART00000161035.1\t+\tENSDART00000161035.1:397-472\t+\t397\t75M\n",
    "C\tENSDART00000161035.1\t+\tENSDART00000161035.1:477-523\t+\t477\t46M\n",
    "C\tENSDART00000165342.1\t+\tENSDART00000165342.1:5-127\t+\t5\t122M\n",
    "C\tENSDART00000165342.1\t+\tENSDART00000165342.1:125-304\t+\t125\t179M\n",
    "C\tENSDART00000165342.1\t+\tENSDART00000165342.1:317-460\t+\t317\t143M\n",
    "C\tENSDART00000165342.1\t+\tENSDART00000165342.1:459-592\t+\t459\t133M\n",
    "C\tENSDART00000165342.1\t+\tENSDART00000165342.1:591-650\t+\t591\t59M\n",
    "C\tENSDART00000165342.1\t+\tENSDART00000165342.1:645-746\t+\t645\t101M\n",
    "C\tENSDART00000165342.1\t+\tENSDART00000165342.1:746-851\t+\t746\t105M\n",
    "C\tENSDART00000165342.1\t+\tENSDART00000165342.1:854-886\t+\t854\t32M\n",
    "C\tENSDART00000165342.1\t+\tENSDART00000165342.1:899-953\t+\t899\t54M\n",
    "C\tENSDART00000165342.1\t+\tENSDART00000165342.1:974-1097\t+\t974\t123M\n",
    "C\tENSDART00000165342.1\t+\tENSDART00000165342.1:1098-1175\t+\t1098\t77M\n",
    "C\tENSDART00000165342.1\t+\tENSDART00000165342.1:1176-1324\t+\t1176\t148M\n"
]

PATHS_EMPTY = []
PATHS_SIMPLE = [
    "P\tENSDART00000161035.1\tENSDART00000161035.1:0-326+\n"
]
PATHS_COMPLEX = [
    "P\tENSDART00000161035.1\tENSDART00000161035.1:0-326+,ENSDART00000161035.1:397-472+,ENSDART0000"
    "0161035.1:477-523+\n",
    "P\tENSDART00000165342.1\tENSDART00000165342.1:5-127+,ENSDART00000165342.1:125-304+,ENSDART0000"
    "0165342.1:317-460+,ENSDART00000165342.1:459-592+,ENSDART00000165342.1:591-650+,ENSDART00000165"
    "342.1:645-746+,ENSDART00000165342.1:746-851+,ENSDART00000165342.1:854-886+,ENSDART00000165342."
    "1:899-953+,ENSDART00000165342.1:974-1097+,ENSDART00000165342.1:1098-1175+,ENSDART00000165342.1"
    ":1176-1324+\n"
]



SEGMENTS_EMPTY_DICT = {}
SEGMENTS_SIMPLE_DICT = {
    "ENSDART00000161035.1:0-326" :
    "TGCACGGGTTTATTGTTCACAAAGAGATCGACAATGTGCGCAACTAAAATAAACATAGTACATTTTGATTATACACGAACTTAAACTAAAGTCC"
    "AATCACACCTCCGCCCCGTTTCCACAGCAGCCTGTCAGGGTGGAGGAAAAGCGCGGCGGTCATGTGAGGCTCGAGCATCTCTCTCTCTCTCTCT"
    "CTCTCTCTCTCTACAGAATGATAGAGGGAGCTCGTGAATCACATCATAGTCGTCCTCCCCTCATTCGTCCTCTCCAGCAGACACCGAAAAACTG"
    "CGTTCATGCCAAAATGGGATGTGGAAATTCCTCCGCCACGAGCA"
}
SEGMENTS_COMPLEX_DICT = {
    "ENSDART00000161035.1:0-326":
    "TGCACGGGTTTATTGTTCACAAAGAGATCGACAATGTGCGCAACTAAAATAAACATAGTACATTTTGATTATACACGAACTTAAACTAAAGTCC"
    "AATCACACCTCCGCCCCGTTTCCACAGCAGCCTGTCAGGGTGGAGGAAAAGCGCGGCGGTCATGTGAGGCTCGAGCATCTCTCTCTCTCTCTCT"
    "CTCTCTCTCTCTACAGAATGATAGAGGGAGCTCGTGAATCACATCATAGTCGTCCTCCCCTCATTCGTCCTCTCCAGCAGACACCGAAAAACTG"
    "CGTTCATGCCAAAATGGGATGTGGAAATTCCTCCGCCACGAGCA",
    "ENSDART00000161035.1:397-472":
    "AGGAACTACGGTGGAGTGTATGTGGGTCTTCCTGCTGATCTGACTGCAGTCGCTGCCAGTCAGTCCAAATCAACA",
    "ENSDART00000161035.1:477-523":
    "AGTCAACAGATGTTTATTGCAGACCTTCAGATAAAACAACATAGAA",
    "ENSDART00000165342.1:5-127":
    "TGGAGCTGAAGCCGAGTATCTTGGTATTGGACTGGAACAGAAATCCAGCAAAAACTTTAAGGGAAATCACTTTCATTTCATGATCGAAAA"
    "ACTCCCGCAGATCATAAAAGAGTGGAAGGAAG",
    "ENSDART00000165342.1:125-304":
    "AGGACCTGTAGTAGAAACAAAACTAGGATCTCTGAGAGGTGCCTTCTTGACTGTGAAGGGCAAGGACACAATAGTCAATAGTTATCTAGG"
    "TGTGCCGTTCGCCAAGCCGCCTGTAGGACCCCTGAGACTTGCTCGACCACAGGCTGCAGAGAAATGGCAAGGAGTTAGAGATGCCACCA",
    "ENSDART00000165342.1:317-460":
    "GTGCCTCCAGGAAAGGCAAATGACTGTAACTGAACTGGAGTTTCTATCGATGGATGTGGAGGTTCCTGAGGTCTCGGAGGATTGCCTGTA"
    "TCTTAACATCTACACCCCAGTTAAACCTGGACAAGGAGACAAGAAGTTACCAG",
    "ENSDART00000165342.1:459-592":
    "GTCATGGTTTGGATTCATGGTGGAGGACTCTCTCTTGGATCGGCTTCAATGTATGATGGCTCTGTTCTGGCTGCGTATCAGGATGTGGTC"
    "GTGGTGCTCATTCAGTACAGATTGGGTCTTCTGGGGTTCTTAA",
    "ENSDART00000165342.1:591-650":
    "AGCACCGGAGACGAGCATGCGCCAGGAAACTATGGTTTTCTGGATCAAGTAGCTGCCCT",
    "ENSDART00000165342.1:645-746":
    "GCCCTTCAGTGGGTTCAGGAGAACATCCACAGCTTCGGTGGAGATCCTGGATCAGTGACCATCTTTGGAGAGTCTGCTGGAGGAATCAGT"
    "GTATCCACGCT",
    "ENSDART00000165342.1:746-851":
    "GATTCTTTCCCCGCTGGCGTCTGGACTGTTTCATCGCGCCATTGCAGAAAGTGGAACTGCCTTCTGGGATGGTTTAGTCATGGCTGATCC"
    "TTTTCAGAGAGCCCA",
    "ENSDART00000165342.1:854-886":
    "TGCAGCCAAACAATGCAACTGTGACAGCAGCA",
    "ENSDART00000165342.1:899-953":
    "TGTCGACTGCATTATGCACTGGTCTGAAGAGGAGGCTCTGGAATGTGCTAAAAA",
    "ENSDART00000165342.1:974-1097":
    "CGTTGCTGTAGATTCTTATTTCCTTCCCAAACCCATCGAGGAGATTGTTGAGAAACAAGAGTTTAGTAAAGTTCCTCTCATCAACGGCAT"
    "TAACAATGATGAGTTTGGCTTCTTGTTGGCTGA",
    "ENSDART00000165342.1:1098-1175":
    "TATTTCTTGGGTCCTGAATGGATGAATGGGTTGAAAAGAGAGCAAATCGCTGAAGCCTTGACGCTCACATATCCTGA",
    "ENSDART00000165342.1:1176-1324":
    "CCCAAGGATCGATGGATCATTGATCTGGTGGCGAAGGAATATCTGGGCGACACACACGACCCCATTGAAATCCGTGAAGTTTATCGGGAG"
    "ATGATGGGAGACGTGCTGTTTAACATCCCTGCCCTGCAACTGGCAAAACACCACAGCG"
}


LINKS_EMPTY_DICT = OVERLAPS_EMPTY
LINKS_SIMPLE_DICT = OVERLAPS_SIMPLE
LINKS_COMPLEX_DICT = OVERLAPS_COMPLEX

CONTAINMENTS_EMPTY_DICT = NODE2COORDS_EMPTY
CONTAINMENTS_SIMPLE_DICT = NODE2COORDS_SIMPLE
CONTAINMENTS_COMPLEX_DICT = NODE2COORDS_COMPLEX

PATHS_EMPTY_DICT = PATH_EMPTY
PATHS_SIMPLE_DICT = PATH_SIMPLE
PATHS_COMPLEX_DICT = PATH_COMPLEX



GFA_EMPTY_FN = "tests/io/empty.gfa"
GFA_SIMPLE_FN = "tests/io/simple.gfa"
GFA_COMPLEX_FN = "tests/io/complex.gfa"

EXONS_EMPTY_FN = "tests/io/exons_empty.fa"
EXONS_SIMPLE_FN = "tests/io/exons_simple.fa"
EXONS_COMPLEX_FN = "tests/io/exons_complex.fa"
EXONS_COMPLEX_SOFT_FN = "tests/io/exons_complex_soft.fa"
EXONS_COMPLEX_HARD_FN = "tests/io/exons_complex_hard.fa"

GAPPED_EMPTY_FN = "tests/io/gapped_empty.fa"
GAPPED_SIMPLE_FN = "tests/io/gapped_simple.fa"
GAPPED_COMPLEX_FN = "tests/io/gapped_complex.fa"
GAPPED_COMPLEX_SOFT_FN = "tests/io/gapped_complex_soft.fa"
GAPPED_COMPLEX_HARD_FN = "tests/io/gapped_complex_hard.fa"
