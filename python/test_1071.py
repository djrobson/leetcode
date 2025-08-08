def gcdOfStrings(str1: str, str2: str) -> str:
    longest = ""

    for span in range(1, min(len(str1), len(str2)) + 1):
        # filter out all the offsets that don't divide into the full strings
        if len(str1) % span != 0 or len(str2) % span != 0:
            continue

        # check if the prefix matches
        if str1[:span] == str2[:span]:
            # check if the prefix repeats for the rest of the first string
            print(f"{len(str1)} {span}")
            fullstr1 = str1[:span] * (len(str1) // span)
            if fullstr1 == str1:
                # check is the prefix repeats for the rest of the second string
                fullstr2 = str2[:span] * (len(str2) // span)
                if fullstr2 == str2:
                    longest = str1[:span]

    return longest


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
