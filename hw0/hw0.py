# CIS 192 Homework 0
# by: <your_name> <your_pennkey>

# Please fill in the following functions according to their docstrings

# Try to be as "Pythonic" as possible. Take advantage of Python's online
# documentation: http://docs.python.org/2/


def fizzbuzz(n):
    """We'll start with the classic warmup, FizzBuzz

    Create a list of strings with the numbers from 1 to n (inclusive), with the
    following conditions:
    If the number is divisible by 3, output "fizz"
    If the number is divisible by 5, output "buzz"
    If the number is divisible by 3 and 5, output "fizzbuzz"

    Remember, the output should be strings (how do we convert an int to a
    string?). If n < 1 you should raise a ValueError. The mod function in
    Python is '%'.

    Below we provide sample inputs/outputs. You will be able to use these to
    test the correctness of your work.

    >>> fizzbuzz(1)
    ['1']

    >>> fizzbuzz(0)
    Traceback (most recent call last):
    ...
    ValueError: message

    >>> fizzbuzz(7)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7']

    >>> fizzbuzz(17)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11',
    'fizz', '13', '14', 'fizzbuzz', '16', '17']

    """
    pass


def encode_text(text, codefile="code.txt"):
    """Encode a string of text according to the mappings in codefile

    codefile will contain mappings, one per line, of one character to another:
    a,b means that 'a' should be mapped to 'b' in the encoded string. If a
    character is not mapped in the codefile, it should not be changed in the
    output.

    If any line in the input file doesn't match this format, raise an
    InvalidFormatException (create that class).

    If you get multiple mappings for the same character, raise a
    DuplicateException (create that class).

    Remember, we have a fundamental data structure that helps us remember
    key/value mappings. Strings can be treated similar to lists, with random
    access using the string[index] notation, and for loops.

    Note that while appending to a list in Python takes constant time, strings
    are immutable, and appending takes O(n) time. Full style points will be
    awarded to solutions that take this into account and use a list for
    efficiency (hint: experiment with "".join(a_list)).

    >>> encode_text("aabbccdd", codefile="simple.txt")
    'bbccaadd'

    >>> encode_text("cat", codefile="hw0.py")
    Traceback (most recent call last):
    ...
    InvalidFormatException: message

    >>> encode_text("cat", codefile="bad1.txt")
    Traceback (most recent call last):
    ...
    InvalidFormatException: message

    >>> encode_text("cat", codefile="bad2.txt")
    Traceback (most recent call last):
    ...
    DuplicateException: message

    >>> encode_text("the quick brown fox jumped over the lazy dog.")
    'mrz hjfwl vkdxi edy tjgqzs duzk mrz bocp sdn.'

    """
    pass


def decode_text(text, codefile="code.txt"):
    """Decode a string encoded with encode_text

    This function should decode a string that was encoded with the given
    codefile. Keep your code DRY (Don't Repeat Yourself). How can you factor
    the encode_text function so that you can reuse code from that (without
    copying it).

    Again, full style points will be rewarded for using strings and lists in
    the efficient way described above.

    >>> decode_text('bbccaadd', codefile="simple.txt")
    'aabbccdd'

    >>> decode_text("cat", codefile="hw0.py")
    Traceback (most recent call last):
    ...
    InvalidFormatException: message

    >>> decode_text("cat", codefile="bad1.txt")
    Traceback (most recent call last):
    ...
    InvalidFormatException: message

    >>> decode_text("cat", codefile="bad2.txt")
    Traceback (most recent call last):
    ...
    DuplicateException: message

    >>> decode_text('mrz hjfwl vkdxi edy tjgqzs duzk mrz bocp sdn.')
    'the quick brown fox jumped over the lazy dog.'

    """
    pass


def hamming_distance(dna1, dna2):
    """The following is a  problem from computational biology.

    First, a brief overview of the structure of DNA. DNA can be represented
    as a sequence of nucleotide bases, each of which is one of guanine,
    adenine, cytosine, or thymine (in reality DNA is two strands -- one given
    by its representation and one given by that helix's complement, in which
    guanine is mapped to cytosine and adenine is mapped to cytosine).

    In Python, we'll represent a DNA strand as a string. For example, "GAC"
    would represent DNA with guanine, then adenine, then cytosine.

    Now, to the problem: in computational biology, it is often important to
    know how much two strands of DNA differ. One measure of this is Hamming
    distance. Hamming distance is defined as the number of character where
    two strings of equal length differ.

    This function, given two strings representing DNA, should return the
    Hamming distance of the two strings. If the strings are of unequal length,
    it should raise an UnequalDNAException (which you should create).

    Hint: take a look at the builtin zip function's documentation.

    >>> hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT")
    7

    >>> hamming_distance("CAT", "CAT")
    0

    >>> hamming_distance("CAT", "CATCAT")
    Traceback (most recent call last):
    ...
    UnequalDNAException: message

    """
    pass


def main():
    """Our main function. Runs the doctests."""
    import doctest
    options = (doctest.IGNORE_EXCEPTION_DETAIL | doctest.NORMALIZE_WHITESPACE |
               doctest.ELLIPSIS)
    doctest.testmod(optionflags=options)


if __name__ == "__main__":
    # calls main() if we have run this with 'python hw0.py'
    main()
