def reverseVowels(s: str) -> str:
    vowels = "aeiouAEIOU"
    input_str = list(s)

    front = 0
    back = len(input_str) - 1

    while True:
        # scan the front for a vowel, stop if you reach the end
        while (front <= back) and (input_str[front] not in vowels):
            front += 1

        while (back > front) and (input_str[back] not in vowels):
            back -= 1

        if back <= front:
            break
        else:
            tmp = input_str[front]
            input_str[front] = input_str[back]
            input_str[back] = tmp
            front += 1
            back -= 1

    return "".join(input_str)


# Assuming reverseVowels is defined in the same file, otherwise import it
# from reverseVowels import reverseVowels


def test_reverseVowels_single_vowel():
    assert reverseVowels("apple") == "eppla", "Failed to reverse a single vowel"


def test_reverseVowels_multiple_vowels():
    assert reverseVowels("leetcode") == "leotcede", "Failed to reverse multiple vowels"


def test_reverseVowels_no_vowel_changes():
    assert reverseVowels("xyz") == "xyz", "Failed with no vowel changes"


def test_reverseVowels_no_vowels():
    assert reverseVowels("bcdfg") == "bcdfg", "Failed when no vowels are present"


def test_reverseVowels_all_vowels():
    assert reverseVowels("aeiou") == "uoiea", "Failed when the string is all vowels"


def test_reverseVowels_mixed_case():
    assert reverseVowels("Hello") == "Holle", "Failed to handle mixed case vowels"


def test_reverseVowels_empty_string():
    assert reverseVowels("") == "", "Failed with an empty string"


def test_reverseVowels_special_characters():
    assert (
        reverseVowels("h@llo! w&rld") == "h@llo! w&rld"
    ), "Failed with special characters and no vowel changes"
