def gcdOfStrings(str1: str, str2: str) -> str:
    def gcd(a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    # Handle empty strings
    if not str1 or not str2:
        return ""

    # If str1 + str2 != str2 + str1, no common divisor exists
    if str1 + str2 != str2 + str1:
        return ""

    # The GCD length is the GCD of the two string lengths
    gcd_length = gcd(len(str1), len(str2))

    # Return the prefix of that length
    return str1[:gcd_length]


# Test cases
def test_gcdOfStrings_same_strings():
    assert gcdOfStrings("ABC", "ABC") == "ABC", "Test failed for identical strings"


def test_gcdOfStrings_no_common_gcd():
    assert (
        gcdOfStrings("ABC", "DEF") == ""
    ), "Test failed for strings with no common GCD"


def test_gcdOfStrings_common_gcd():
    assert (
        gcdOfStrings("ABABAB", "ABAB") == "AB"
    ), "Test failed for strings with a common GCD"


def test_gcdOfStrings_empty_string():
    assert gcdOfStrings("", "ABC") == "", "Test failed for one empty string"
    assert gcdOfStrings("ABC", "") == "", "Test failed for the other empty string"
