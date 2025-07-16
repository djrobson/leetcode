import pytest

def convert(s: str, numRows: int) -> str:
    return s

def test_convert_1():
    assert convert("PAYPALISHIRING", 1) == "PAYPALISHIRING", "Failed with 1 row"

def test_convert_2():
    assert convert("PAYPALISHIRING", 2) == "PYAIHRNAPLSIIG", "Failed with 2 row"
def test_convert_3():
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR", "Failed with 3 row"

def test_convert_4():
    assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI", "Failed with 4 row"
    assert convert("0123456789ABCD", 4) == "06C157BD248A39", "Failed with 4 row"
