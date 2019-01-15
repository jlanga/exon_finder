#!/usr/bin/env python3

"""tests.io.gfa1.py: Fragments of GFA1 files"""

import pandas as pd

HEADER = pd.DataFrame(
    data=[["H", "VN:Z:1.0"]],
    columns=["RecordType", "Version"]
)



SEGMENTS_EMPTY = pd.DataFrame(
    columns=["RecordType", "name", "sequence", "SegmentLength"]
)

SEGMENTS_SIMPLE = pd.DataFrame(
    data=[[
        "S",
        "ENSDART00000161035.1:0-326",
        "TGCACGGGTTTATTGTTCACAAAGAGATCGACAATGTGCGCAACTAAAATAAACATAGTACATTTTGATT"
        "ATACACGAACTTAAACTAAAGTCCAATCACACCTCCGCCCCGTTTCCACAGCAGCCTGTCAGGGTGGAGG"
        "AAAAGCGCGGCGGTCATGTGAGGCTCGAGCATCTCTCTCTCTCTCTCTCTCTCTCTCTCTACAGAATGAT"
        "AGAGGGAGCTCGTGAATCACATCATAGTCGTCCTCCCCTCATTCGTCCTCTCCAGCAGACACCGAAAAAC"
        "TGCGTTCATGCCAAAATGGGATGTGGAAATTCCTCCGCCACGAGCA",
        "LN:i:326"
        ]],
    columns=["RecordType", "name", "sequence", "SegmentLength"]
)

SEGMENTS_COMPLEX = pd.DataFrame(
    data=[[
        "S",
        "ENSDART00000161035.1:0-326",
        "TGCACGGGTTTATTGTTCACAAAGAGATCGACAATGTGCGCAACTAAAATAAACATAGTACATTTTGATT"
        "ATACACGAACTTAAACTAAAGTCCAATCACACCTCCGCCCCGTTTCCACAGCAGCCTGTCAGGGTGGAGG"
        "AAAAGCGCGGCGGTCATGTGAGGCTCGAGCATCTCTCTCTCTCTCTCTCTCTCTCTCTCTACAGAATGAT"
        "AGAGGGAGCTCGTGAATCACATCATAGTCGTCCTCCCCTCATTCGTCCTCTCCAGCAGACACCGAAAAAC"
        "TGCGTTCATGCCAAAATGGGATGTGGAAATTCCTCCGCCACGAGCA",
        "LN:i:326",
    ], [
        "S",
        "ENSDART00000161035.1:397-472",
        "AGGAACTACGGTGGAGTGTATGTGGGTCTTCCTGCTGATCTGACTGCAGTCGCTGCCAGTCAGTCCAAAT"
        "CAACA",
        "LN:i:75",
    ], [
        "S",
        "ENSDART00000161035.1:477-523",
        "AGTCAACAGATGTTTATTGCAGACCTTCAGATAAAACAACATAGAA", "LN:i:46"
    ], [
        "S",
        "ENSDART00000165342.1:5-127",
        "TGGAGCTGAAGCCGAGTATCTTGGTATTGGACTGGAACAGAAATCCAGCAAAAACTTTAAGGGAAATCAC"
        "TTTCATTTCATGATCGAAAAACTCCCGCAGATCATAAAAGAGTGGAAGGAAG", "LN:i:122"
    ], [
        "S",
        "ENSDART00000165342.1:125-304",
        "AGGACCTGTAGTAGAAACAAAACTAGGATCTCTGAGAGGTGCCTTCTTGACTGTGAAGGGCAAGGACACA"
        "ATAGTCAATAGTTATCTAGGTGTGCCGTTCGCCAAGCCGCCTGTAGGACCCCTGAGACTTGCTCGACCAC"
        "AGGCTGCAGAGAAATGGCAAGGAGTTAGAGATGCCACCA", "LN:i:179"
    ], [
        "S",
        "ENSDART00000165342.1:317-460",
        "GTGCCTCCAGGAAAGGCAAATGACTGTAACTGAACTGGAGTTTCTATCGATGGATGTGGAGGTTCCTGAG"
        "GTCTCGGAGGATTGCCTGTATCTTAACATCTACACCCCAGTTAAACCTGGACAAGGAGACAAGAAGTTAC"
        "CAG", "LN:i:143"
    ], [
        "S",
        "ENSDART00000165342.1:459-592",
        "GTCATGGTTTGGATTCATGGTGGAGGACTCTCTCTTGGATCGGCTTCAATGTATGATGGCTCTGTTCTGG"
        "CTGCGTATCAGGATGTGGTCGTGGTGCTCATTCAGTACAGATTGGGTCTTCTGGGGTTCTTAA",
        "LN:i:133"
    ], [
        "S",
        "ENSDART00000165342.1:591-650",
        "AGCACCGGAGACGAGCATGCGCCAGGAAACTATGGTTTTCTGGATCAAGTAGCTGCCCT",
        "LN:i:59"
    ], [
        "S",
        "ENSDART00000165342.1:645-746",
        "GCCCTTCAGTGGGTTCAGGAGAACATCCACAGCTTCGGTGGAGATCCTGGATCAGTGACCATCTTTGGAG"
        "AGTCTGCTGGAGGAATCAGTGTATCCACGCT",
        "LN:i:101",
    ], [
        "S",
        "ENSDART00000165342.1:746-851",
        "GATTCTTTCCCCGCTGGCGTCTGGACTGTTTCATCGCGCCATTGCAGAAAGTGGAACTGCCTTCTGGGAT"
        "GGTTTAGTCATGGCTGATCCTTTTCAGAGAGCCCA", "LN:i:105",
    ], [
        "S",
        "ENSDART00000165342.1:854-886",
        "TGCAGCCAAACAATGCAACTGTGACAGCAGCA",
        "LN:i:32"
    ], [
        "S",
        "ENSDART00000165342.1:899-953",
        "TGTCGACTGCATTATGCACTGGTCTGAAGAGGAGGCTCTGGAATGTGCTAAAAA", "LN:i:54"
    ], [
        "S",
        "ENSDART00000165342.1:974-1097",
        "CGTTGCTGTAGATTCTTATTTCCTTCCCAAACCCATCGAGGAGATTGTTGAGAAACAAGAGTTTAGTAAA"
        "GTTCCTCTCATCAACGGCATTAACAATGATGAGTTTGGCTTCTTGTTGGCTGA",
        "LN:i:123"
    ], [
        "S",
        "ENSDART00000165342.1:1098-1175",
        "TATTTCTTGGGTCCTGAATGGATGAATGGGTTGAAAAGAGAGCAAATCGCTGAAGCCTTGACGCTCACAT"
        "ATCCTGA",
        "LN:i:77",
    ], [
        "S",
        "ENSDART00000165342.1:1176-1324",
        "CCCAAGGATCGATGGATCATTGATCTGGTGGCGAAGGAATATCTGGGCGACACACACGACCCCATTGAAA"
        "TCCGTGAAGTTTATCGGGAGATGATGGGAGACGTGCTGTTTAACATCCCTGCCCTGCAACTGGCAAAACA"
        "CCACAGCG",
        "LN:i:148"
    ]],
    columns=["RecordType", "name", "sequence", "SegmentLength"]
)



LINKS_EMPTY = pd.DataFrame(
    columns=["RecordType", "From", "FromOrient", "To", "ToOrient", "Overlap"]
)

LINKS_SIMPLE = pd.DataFrame(
    columns=["RecordType", "From", "FromOrient", "To", "ToOrient", "Overlap"]
)

LINKS_COMPLEX = pd.DataFrame(
    data=[[
        "L", "ENSDART00000161035.1:0-326", "+",
        "ENSDART00000161035.1:397-472", "+", "71N"
    ], [
        "L", "ENSDART00000161035.1:397-472", "+",
        "ENSDART00000161035.1:477-523", "+", "5N"
    ], [
        "L", "ENSDART00000165342.1:5-127", "+",
        "ENSDART00000165342.1:125-304", "+", "2M"
    ], [
        "L", "ENSDART00000165342.1:125-304", "+",
        "ENSDART00000165342.1:317-460", "+", "13N"
    ], [
        "L", "ENSDART00000165342.1:317-460", "+",
        "ENSDART00000165342.1:459-592", "+", "1M"
    ], [
        "L", "ENSDART00000165342.1:459-592", "+",
        "ENSDART00000165342.1:591-650", "+", "1M"
    ], [
        "L", "ENSDART00000165342.1:591-650", "+",
        "ENSDART00000165342.1:645-746", "+", "5M"
    ], [
        "L", "ENSDART00000165342.1:645-746", "+",
        "ENSDART00000165342.1:746-851", "+", "0M"
    ], [
        "L", "ENSDART00000165342.1:746-851", "+",
        "ENSDART00000165342.1:854-886", "+", "3N"
    ], [
        "L", "ENSDART00000165342.1:854-886", "+",
        "ENSDART00000165342.1:899-953", "+", "13N"
    ], [
        "L", "ENSDART00000165342.1:899-953", "+",
        "ENSDART00000165342.1:974-1097", "+", "21N"
    ], [
        "L", "ENSDART00000165342.1:974-1097", "+",
        "ENSDART00000165342.1:1098-1175", "+", "1N"
    ], [
        "L", "ENSDART00000165342.1:1098-1175", "+",
        "ENSDART00000165342.1:1176-1324", "+", "1N"
    ]],
    columns=["RecordType", "From", "FromOrient", "To", "ToOrient", "Overlap"]
)



CONTAINMENTS_EMPTY = pd.DataFrame(
    columns=["RecordType", "Container", "ContainerOrient", "Contained",
             "ContainedOrient", "Pos", "Overlap"]
)

CONTAINMENTS_SIMPLE = pd.DataFrame(
    data=[[
        "C", "ENSDART00000161035.1", "+", "ENSDART00000161035.1:0-326", "+",
        0, "326M"
    ]],
    columns=["RecordType", "Container", "ContainerOrient", "Contained",
             "ContainedOrient", "Pos", "Overlap"]
)
CONTAINMENTS_COMPLEX = pd.DataFrame(
    data=[[
        "C", "ENSDART00000161035.1", "+", "ENSDART00000161035.1:0-326", "+",
        0, "326M"
    ], [
        "C", "ENSDART00000161035.1", "+", "ENSDART00000161035.1:397-472", "+",
        397, "75M"
    ], [
        "C", "ENSDART00000161035.1", "+", "ENSDART00000161035.1:477-523", "+",
        477, "46M"
    ], [
        "C", "ENSDART00000165342.1", "+", "ENSDART00000165342.1:5-127", "+",
        5, "122M"
    ], [
        "C", "ENSDART00000165342.1", "+", "ENSDART00000165342.1:125-304", "+",
        125, "179M"
    ], [
        "C", "ENSDART00000165342.1", "+", "ENSDART00000165342.1:317-460", "+",
        317, "143M"
    ], [
        "C", "ENSDART00000165342.1", "+", "ENSDART00000165342.1:459-592", "+",
        459, "133M"
    ], [
        "C", "ENSDART00000165342.1", "+", "ENSDART00000165342.1:591-650", "+",
        591, "59M"
    ], [
        "C", "ENSDART00000165342.1", "+", "ENSDART00000165342.1:645-746", "+",
        645, "101M"
    ], [
        "C", "ENSDART00000165342.1", "+", "ENSDART00000165342.1:746-851", "+",
        746, "105M"
    ], [
        "C", "ENSDART00000165342.1", "+", "ENSDART00000165342.1:854-886", "+",
        854, "32M"
    ], [
        "C", "ENSDART00000165342.1", "+", "ENSDART00000165342.1:899-953", "+",
        899, "54M"
    ], [
        "C", "ENSDART00000165342.1", "+", "ENSDART00000165342.1:974-1097", "+",
        974, "123M"
    ], [
        "C", "ENSDART00000165342.1", "+", "ENSDART00000165342.1:1098-1175",
        "+", 1098, "77M"
    ], [
        "C", "ENSDART00000165342.1", "+", "ENSDART00000165342.1:1176-1324",
        "+", 1176, "148M"
    ]],
    columns=["RecordType", "Container", "ContainerOrient", "Contained",
             "ContainedOrient", "Pos", "Overlap"]
)


PATHS_EMPTY = pd.DataFrame(
    columns=["RecordType", "PathName", "SegmentNames", "Overlaps"]
)
PATHS_SIMPLE = pd.DataFrame(
    data=[["P", "ENSDART00000161035.1", "ENSDART00000161035.1:0-326+", "*"]],
    columns=["RecordType", "PathName", "SegmentNames", "Overlaps"]
)
PATHS_COMPLEX = pd.DataFrame(
    data=[[
        "P", "ENSDART00000161035.1",
        "ENSDART00000161035.1:0-326+,"
        "ENSDART00000161035.1:397-472+,"
        "ENSDART00000161035.1:477-523+",
        "*"
    ], [
        "P", "ENSDART00000165342.1",
        "ENSDART00000165342.1:5-127+,ENSDART00000165342.1:125-304+,"
        "ENSDART00000165342.1:317-460+,ENSDART00000165342.1:459-592+,"
        "ENSDART00000165342.1:591-650+,ENSDART00000165342.1:645-746+,"
        "ENSDART00000165342.1:746-851+,ENSDART00000165342.1:854-886+,"
        "ENSDART00000165342.1:899-953+,ENSDART00000165342.1:974-1097+,"
        "ENSDART00000165342.1:1098-1175+,ENSDART00000165342.1:1176-1324+",
        "*"
    ]],
    columns=["RecordType", "PathName", "SegmentNames", "Overlaps"]
)

GFA1_EMPTY_FN = "tests/io/empty.gfa"
GFA1_SIMPLE_FN = "tests/io/simple.gfa"
GFA1_COMPLEX_FN = "tests/io/complex.gfa"
