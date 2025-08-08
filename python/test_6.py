from typing import List

import pytest


def convert(s: str, numRows: int) -> str:
    output = ""
    stride_size = get_stride(numRows)
    offset_lists = get_offsets_in_stride(stride_size)
    for offset_list in offset_lists:
        chunk = 0
        while chunk < len(s):
            for offset in offset_list:
                if chunk + offset < len(s):
                    output += s[chunk + offset]
            chunk += stride_size

    return output

def get_stride(numRows:int) -> int:
    if numRows <= 2:
        return numRows

    return 2+((numRows -2)*2)

def get_offsets_in_stride(stride_size:int) -> List[List[int]]:
    # the first one in the stride
    output = []
    for sequence in range((stride_size//2) +1):
        if sequence == 0:
            # the top row
            output.append([0])
        elif sequence == ((stride_size // 2)):
            # the bottom row
            output.append([sequence])
        else:
            # some middle row
            output.append([sequence,stride_size - sequence])

    return output

def test_convert_1():
    assert convert("PAYPALISHIRING", 1) == "PAYPALISHIRING", "Failed with 1 row"

def test_convert_2():
    assert convert("PAYPALISHIRING", 2) == "PYAIHRNAPLSIIG", "Failed with 2 row"

def test_convert_3():
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR", "Failed with 3 row"

def test_convert_4():
    assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI", "Failed with 4 row"
    assert convert("0123456789ABCD", 4) == "06C157BD248A39", "Failed with 4 row"

def test_stride_1():
    assert get_stride(1) == 1, "Failed stride 1"

def test_stride_2():
    assert get_stride(2) == 2, "Failed stride 2"

def test_stride_3():
    assert get_stride(3) == 4, "Failed stride 3"

def test_stride_4():
    assert get_stride(4) == 6, "Failed stride 4"

def test_get_offsets_in_stride_1():
    assert get_offsets_in_stride(get_stride(1)) == [[0]], "Failed get_offsets 1"
def test_get_offsets_in_stride_2():
    assert get_offsets_in_stride(get_stride(2)) == [[0],[1]], "Failed get_offsets 2"
def test_get_offsets_in_stride_3():
    assert get_offsets_in_stride(get_stride(3)) == [[0],[1,3],[2]], "Failed get_offsets 3"
def test_get_offsets_in_stride_4():
    assert get_offsets_in_stride(get_stride(4)) == [[0],[1,5],[2,4],[3]], "Failed get_offsets 4"
