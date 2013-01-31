# CIS 192 Homework 1
# by: <your_name>

# Please fill in the following functions according to their docstrings

# Try to be as "Pythonic" as possible. Take advantage of Python's online
# documentation: http://docs.python.org/2/

from StringIO import StringIO
from urllib import urlopen
import random

# This will cause an error until you install nose
# 'pip install nose'
from nose.tools import eq_


#### PROBLEM 1 ####

def checksum(handle):
    """Calculate the checksum for the data read from this handle.

    When dealing with data sent from an untrusted or insecure source, it is
    necessary to verify what you received was what you expected and not somehow
    modified or corrupted. To do this, hash functions that with high likelihood
    uniquely fingerprint the data can also be computed and sent with the data,
    which you can compare to your own computation of the same hash function to
    verify you received an unmodified version of the data. This is particularly
    useful in the distribution of software -- software that is modified due to
    disk corruption on a server, network issues, or malicious intent can
    be detected and rejected before installation, preventing errors or harm
    to the installing computer.

    One very simple hashing algorithm is Fletcher's checksum
    (http://en.wikipedia.org/wiki/Fletcher's_checksum).
    Here is Java-flavored pseudocode for an implementation:

    public short fletcher(byte[] data) {
      short sum1 = 0;
      short sum2 = 0;
      for(int i = 0; i < data.length; i++) {
        sum1 = (sum1 + data[i]) % 255;
        sum2 = (sum2 + sum1) % 255;
      }

      return (sum2 << 8) | sum1;
    }

    Notice that the above code, if translated literally to Python, would not be
    very Pythonic. We ask you to come up with a more idiomatic implementation
    that is equivalent.

    Your function, given a handle to a file-like object (something that has a
    read() method like a file), will read its contents and return a Fletcher
    checksum from the contents as a string.

    The power of treating our input as file-like and not exactly as a file
    lies in duck-typing: if we write our code with this level of abstraction,
    we can accept anything that acts like a file as input. This means we can
    accept a string wrapped in StringIO (which is equivalent to a StringBuffer
    in Java), something loaded over the network like a web page retrieved using
    HTTP, stdin, a socket, or a multitude of other options.

    In Java, we would achieve this kind of polymorphism using interfaces; but,
    because the purpose of formal interfaces in Java is to allow programs to be
    typechecked, and there is no typechecking in Python before runtime, formal
    interfaces are unnecessary. This is an example of a place where Python
    trusts the user (you) to make the right choice. Another example would be
    with attribute access -- there is no public or private in Python, just
    naming conventions that are intended to discourage but not prevent access
    without good cause. This trust trades foolproofness for flexibility when
    it is needed.

    Hint: calling read will, in some cases such as reading from a file not
    opened with a binary flag or an instance of StringIO, return a string. Use
    the built-in function ord() to convert a 1-byte string into binary data.
    This isn't a safe approach for unicode (why?), but works fine for our
    purposes.


    >>> checksum(open('good.txt'))
    34533

    >>> checksum(StringIO(open('corrupted.txt').read()))
    51974

    >>> checksum(urlopen('http://git.to/easteregg')) # get it?
    31665

    """
    raise NotImplementedError()


class Node(object):
    """Node class for a binary tree

    Used in HW1 problems 2+"""
    def __init__(self, value, left=None, right=None):
        """Constructor. Expects the value stored at the node"""
        self.value, self.left, self.right = value, left, right

    def __repr__(self):
        return "Node(%s)" % self.value


# Note that the next two problems could be implemented either as standalone
# functions, using the Tree/Node classes as merely containers for the value and
# left/right pointers, or you could implement these as methods on the Node
# class. If you choose to implement them as methods on the Node class, please
# have these functions call the appropriate method on the object they are
# passed.

#### PROBLEM 2 ####

def insert(node, element):
    """Insert an element into a binary search tree rooted at this Node.

    (http://en.wikipedia.org/wiki/Binary_search_tree)

    After insertion, return the modified node.

    Inserting into None should return a new node with the element:

    >>> insert(None, 2)
    Node(2)

    Our implementation will allow duplicate nodes. The left subtree should
    contain all elements <= to the current element, and the right subtree
    will contain all elements > the current element.

    Note that due to duck-typing, your implementation should work for any
    objects that implement the comparison methods
    (http://www.rafekettler.com/magicmethods.html#comparisons). This
    includes by default ints, strings, floats, and any other data type you
    might implement the comparison operators for.

    You should write your own unit tests with doctest or nose for this
    function.
    """
    raise NotImplementedError()


#### PROBLEM 3 ####

def inorder(node, elements=None):
    """Return a list of the elements visited in an inorder traversal

    Note that this should be the sorted order if you've inserted all
    elements using your previously defined insert function.

    You should write your own unit tests for this function.
    """
    raise NotImplementedError()


# Now we're going to write a randomized test for our insert and inorder
# functions.

#### PROBLEM 4 ####

def random_list(length, min_int, max_int):
    """Return a list of random integers in the given range

    You should look at python's 'random' module for random number generation.

    Even though this function doesn't have deterministic results, it should
    still be possible to write tests for it.

    """
    raise NotImplementedError()


#### PROBLEM 5 ####

def check_sorted(l):
    """Assert that the given list is sorted

    You may want to use the eq_ function provided by nose, which will
    automatically create an assertion with a good error message for you. We've
    already added it as an import at the top of this file.
    (https://nose.readthedocs.org/en/latest/testing_tools.html#nose.tools.eq_)

    eq_(something, something_else)

    There are many ways to approach this problem. One simple way might make use
    of the 'sorted' function.

    >>> check_sorted(None)
    Traceback (most recent call last):
    AssertionError: ...

    >>> check_sorted([2,1])
    Traceback (most recent call last):
    AssertionError: ...

    >>> check_sorted([1,2,3])

    """
    raise NotImplementedError()


#### PROBLEM 6 ####

def check_sorting(list_length):
    """Run random tests to verify insert and inorder work correctly.

    You should run 'trials' number of tests using random lists verifying that
    your insert and inorder functions work correctly. Use your random_list and
    check_sorted functions to assist with this.

    Things to verify include:

    Every element in the original list should still be in the list generated by
    inserting all elements, then running an inorder traversal on the root.

    After inserting all elements, running the inorder traversal should result
    in a sorted list.

    Make sure you are using Python's 'assert' keyword somewhere in here.

    """
    raise NotImplementedError()


# This function runs our check_sorting function defined above for multiple
# trials. You can leave it as is. It uses a more advanced concept (generators)
# that we will talk about soon.
# You can change the number of trials if you'd like.
def test_sorting(trials=10):
    """Run our check_sorting function for the given number of trials.

    Uses a bigger list on each trial"""
    for i in range(1, trials + 1):
        yield check_sorting, i


def main():
    """Our main function"""
    print "Running doctests...\n"
    import doctest
    options = (doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS)
    doctest.testmod(optionflags=options, verbose=True)

    print "\n\nRunning unit tests...\n"
    # You will need to 'pip install nose' for this line to work
    # You will need to 'pip install coverage' to get coverage information
    import nose
    if nose.run(argv=["--with-coverage", "hw1.py"]):
        print "\nPassed all unit tests"


if __name__ == "__main__":
    # calls main() if we have run this with 'python hw0.py'
    main()
