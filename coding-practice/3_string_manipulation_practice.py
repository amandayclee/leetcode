class StringManipulationPractice:

    # Exercise 1: Progressive Substrings
    # Given a string s, print the string progressively by adding one character at a time.
    # Example: For input "abcde", output:
    # a
    # ab
    # abc
    # abcd
    # abcde
    @staticmethod
    def progressive_substrings(s):
        # TODO: Fill in the logic
        pass

    # Exercise 2: Sliding Window Substrings
    # Given a string s and a window size n, print all substrings of length n using a sliding window approach.
    # Example: For input "abcde" and window size 3, output:
    # abc
    # bcd
    # cde
    @staticmethod
    def sliding_window_substrings(s, window_size):
        # TODO: Fill in the logic
        pass

    # Exercise 3: Reverse Progressive Substrings
    # Given a string s, print the string progressively in reverse, removing one character at a time from the end.
    # Example: For input "abcde", output:
    # abcde
    # abcd
    # abc
    # ab
    # a
    @staticmethod
    def reverse_substrings(s):
        # TODO: Fill in the logic
        pass

    # Exercise 4: Substring in Reverse Order
    # Given a string s, print each character in reverse order one by one.
    # Example: For input "abcde", output:
    # e
    # d
    # c
    # b
    # a
    @staticmethod
    def reverse_characters(s):
        # TODO: Fill in the logic
        pass

    # Exercise 5: Palindromic Substrings
    # Given a string s, find and print all substrings that are palindromes.
    # Example: For input "abcba", output:
    # a
    # b
    # c
    # b
    # a
    # bcb
    # abcba
    @staticmethod
    def palindromic_substrings(s):
        # TODO: Fill in the logic
        pass

    # Exercise 6: String Rotation
    # Given a string s, rotate the string by 1 position to the right and print the result repeatedly until it returns to its original form.
    # Example: For input "abcde", output:
    # abcde
    # eabcd
    # deabc
    # cdeab
    # bcdea
    @staticmethod
    def rotate_string(s):
        # TODO: Fill in the logic
        pass

    # Exercise 7: Character Frequency
    # Given a string s, count and print the frequency of each character in the string.
    # Example: For input "apple", output:
    # a: 1
    # p: 2
    # l: 1
    # e: 1
    @staticmethod
    def character_frequency(s):
        # TODO: Fill in the logic
        pass

    # Exercise 8: Vowel and Consonant Count
    # Given a string s, count the number of vowels and consonants separately, and print the result.
    # Example: For input "hello world", output:
    # Vowels: 3
    # Consonants: 7
    @staticmethod
    def vowel_consonant_count(s):
        # TODO: Fill in the logic
        pass

    # Exercise 9: Alternate Character Printing
    # Given a string s, print every alternate character in the string, starting from the first character.
    # Example: For input "abcdefg", output:
    # aceg
    @staticmethod
    def alternate_characters(s):
        # TODO: Fill in the logic
        pass

    # Exercise 10: Check for Anagrams
    # Given two strings s1 and s2, check whether they are anagrams of each other.
    # Print True if they are, and False if they are not.
    # Example: For input "listen" and "silent", output:
    # True
    @staticmethod
    def are_anagrams(s1, s2):
        # TODO: Fill in the logic
        return False

    # Exercise 11: Remove Vowels
    # Given a string s, remove all vowels from the string and print the result.
    # Example: For input "beautiful", output:
    # btf
    @staticmethod
    def remove_vowels(s):
        # TODO: Fill in the logic
        return s

    # Exercise 12: Longest Repeated Character Substring
    # Given a string s, find and print the longest substring that consists of the same character repeated.
    # Example: For input "aaabbcdddd", output:
    # dddd
    @staticmethod
    def longest_repeated_character_substring(s):
        # TODO: Fill in the logic
        return s

    # Exercise 13: Character Case Inversion
    # Given a string s, invert the case of all characters (i.e., convert uppercase to lowercase and vice versa).
    # Example: For input "Hello World", output:
    # hELLO wORLD
    @staticmethod
    def invert_case(s):
        # TODO: Fill in the logic
        return s

    # Exercise 14: String Reversal
    # Given a string s, reverse the entire string and print it.
    # Example: For input "abcdefg", output:
    # gfedcba
    @staticmethod
    def reverse_string(s):
        # TODO: Fill in the logic
        return s

    # Exercise 15: Replace Spaces with Underscores
    # Given a string s, replace all spaces with underscores and print the result.
    # Example: For input "hello world", output:
    # hello_world
    @staticmethod
    def replace_spaces(s):
        # TODO: Fill in the logic
        return s

    # Exercise 16: First Non-Repeating Character
    # Given a string s, find and print the first character that does not repeat.
    # Example: For input "swiss", output:
    # w
    @staticmethod
    def first_non_repeating_character(s):
        # TODO: Fill in the logic
        return ' '

    # Exercise 17: Count Substring Occurrences
    # Given a string s and a substring sub, count how many times sub appears in s.
    # Example: For input "hellohello" and "hello", output:
    # 2
    @staticmethod
    def count_substrings(s, sub):
        # TODO: Fill in the logic
        return 0

    # Exercise 18: Check for Rotation
    # Given two strings s1 and s2, check if s2 is a rotation of s1. Print True if it is, and False if it is not.
    # Example: For input "waterbottle" and "erbottlewat", output:
    # True
    @staticmethod
    def is_rotation(s1, s2):
        # TODO: Fill in the logic
        return False

    # Exercise 19: Capitalize First Letter of Each Word
    # Given a string s, capitalize the first letter of each word and print the result.
    # Example: For input "hello world", output:
    # Hello World
    @staticmethod
    def capitalize_words(s):
        # TODO: Fill in the logic
        return s

    # Exercise 20: Check for Subsequence
    # Given two strings s1 and s2, check if s2 is a subsequence of s1. Print True if it is, and False if it is not.
    # Example: For input "abcde" and "ace", output:
    # True
    @staticmethod
    def is_subsequence(s1, s2):
        # TODO: Fill in the logic
        return False

# Test Cases for each Exercise

def test_exercises():
    # Exercise 1:
    assert StringManipulationPractice.progressive_substrings("abcde") == ['a', 'ab', 'abc', 'abcd', 'abcde']

    # Exercise 2:
    assert StringManipulationPractice.sliding_window_substrings("abcde", 3) == ['abc', 'bcd', 'cde']

    # Exercise 3:
    assert StringManipulationPractice.reverse_substrings("abcde") == ['abcde', 'abcd', 'abc', 'ab', 'a']

    # Exercise 4:
    assert StringManipulationPractice.reverse_characters("abcde") == ['e', 'd', 'c', 'b', 'a']

    # Exercise 5:
    assert StringManipulationPractice.palindromic_substrings("abcba") == ['a', 'b', 'c', 'b', 'a', 'bcb', 'abcba']

    # Exercise 6:
    assert StringManipulationPractice.rotate_string("abcde") == ['abcde', 'eabcd', 'deabc', 'cdeab', 'bcdea']

    # Exercise 7:
    assert StringManipulationPractice.character_frequency("apple") == {'a': 1, 'p': 2, 'l': 1, 'e': 1}

    # Exercise 8:
    assert StringManipulationPractice.vowel_consonant_count("hello world") == {'Vowels': 3, 'Consonants': 7}

    # Exercise 9:
    assert StringManipulationPractice.alternate_characters("abcdefg") == 'aceg'

    # Exercise 10:
    assert StringManipulationPractice.are_anagrams("listen", "silent") == True

    # Exercise 11:
    assert StringManipulationPractice.remove_vowels("beautiful") == 'btfl'

    # Exercise 12:
    assert StringManipulationPractice.longest_repeated_character_substring("aaabbcdddd") == 'dddd'

    # Exercise 13:
    assert StringManipulationPractice.invert_case("Hello World") == 'hELLO wORLD'

    # Exercise 14:
    assert StringManipulationPractice.reverse_string("abcdefg") == 'gfedcba'

    # Exercise 15:
    assert StringManipulationPractice.replace_spaces("hello world") == 'hello_world'

    # Exercise 16:
    assert StringManipulationPractice.first_non_repeating_character("swiss") == 'w'

    # Exercise 17:
    assert StringManipulationPractice.count_substrings("hellohello", "hello") == 2

    # Exercise 18:
    assert StringManipulationPractice.is_rotation("waterbottle", "erbottlewat") == True

    # Exercise 19:
    assert StringManipulationPractice.capitalize_words("hello world") == 'Hello World'

    # Exercise 20:
    assert StringManipulationPractice.is_subsequence("abcde", "ace") == True

test_exercises()