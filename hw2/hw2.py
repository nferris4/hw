import requests

## For this homework, you'll be learning how to consume an API using Python. We
## found an API that provides Philadelphia property tax records in JSON format
## for public consumption.
##
## Use comprehensions where appropriate to make your code more concise and
## readable.
##
## Be sure to take advantage of built in string functions such as join, split,
## title and replace (look at the string documentation for more).
##
## Read the doctests to understand how we want your implementations to behave.

BASE_URL = "http://api.phillyaddress.com/"


class ApiException(Exception):
    """Exception thrown when the API returns an error"""
    pass


## PROBLEM 1 ##
## Implement the following helper functions

def convert_arg(arg):
    """Convert the argument into the expected '+' separated string format

    If given a non-string, convert it to a string first.

    The API expects that strings are separated like this, so let's write a
    quick helper function for it.

    >>> convert_arg("spruce")
    'spruce'
    >>> convert_arg("spruce st")
    'spruce+st'
    >>> convert_arg("van pelt st")
    'van+pelt+st'
    """
    raise NotImplementedError()


def make_url(*args):
    """Join a URL with the '/' symbol

    This function should join the arguments it receives using the '/' symbol,
    and append those to the end of the BASE_URL defined above. It will allow us
    to easily create URLs in the format expected by the API.

    You probably want to start by playing around with printing the received
    arguments, so you get a feel for what the *args does in the function
    declaration.

    >>> make_url()
    'http://api.phillyaddress.com/'
    >>> make_url("account", 1234567)
    'http://api.phillyaddress.com/account/1234567'
    >>> make_url("block", 4000, "spruce st")
    'http://api.phillyaddress.com/block/4000/spruce+st'
    """
    raise NotImplementedError()


def get_json(*args):
    """GET some JSON, raising an HTTPError if we don't get a 200 status.

    First calls make_url using the arguments, then makes the web requests and
    returns the JSON. If the received JSON is empty, throw a ValueError.

    Remember to check out the requests documentation, as requests makes raising
    the error on non-200 status a one-liner:
    http://docs.python-requests.org/en/latest/user/quickstart/

    First calls make_url with the arguments.
    Returns the JSON decoded as a dictionary.

    >>> get_json("account", 4321)
    Traceback (most recent call last):
    ...
    ApiException: Invalid Account Number

    >>> get_json("blah")
    Traceback (most recent call last):
    ...
    ApiException: Welcome to the OPA Property Search...

    >>> get_json("block", 4000, "spruce st")
    {u'properties': [...]}

    """
    raise NotImplementedError()


## PROBLEM 2 ##
## Build the Block, Property and Owner classes. You will probably have to
## complete both Block and Property together before you can get the tests to
## pass for either. You can build Owner after that.
##
## Make sure you define __repr__ methods for each class that are consistent
## with the provided doctests


class Block(object):
    """A block entity. Holds many Properties

    Your constructor should take a street number and street name, retrieve the
    data, and create a list of property objects. The street name should be
    converted to title case if it isn't already.

    >>> b = Block(4100, "spruce st")
    >>> b
    4100 block of Spruce St (12 properties)
    >>> b.street_name
    'Spruce St'
    >>> b.street_number
    4100
    >>> b.properties
    [4100 Spruce St, 4101-03 Spruce St, 4102 Spruce St, 4104 Spruce St,
    4105-07 Spruce St, 4106 Spruce St, 4108 Spruce St, 4110 Spruce St,
    4112 Spruce St, 4114 Spruce St, 4116 Spruce St, 4141 Spruce St]
    """
    pass


class Property(object):
    """A property entity. Holds the information for a single address.

    The easiest way to implement this is probably to have the constructor take
    a dictionary (since the Block lookup will return a dictionary for each
    Property on the block). The object should store the address string
    (converted to title case), value (from the 'proposed_value' item), and
    owner names (title case).

    Notice that the API returns property values as strings like '$314,000'.
    Please convert these to ints.

    The Property object should lazily load the Owner objects (see the lecture
    notes for an example of lazy loading something using a property). Use the
    @property annotation and a method called owners.


    >>> details = dict(address="1234 main st", proposed_value="$314,000",
    ...     owners=["WAWA INC"])
    >>> p = Property(details)
    >>> p
    1234 Main St
    >>> p.address
    '1234 Main St'
    >>> p.value
    314000
    >>> p.owner_names
    ['Wawa Inc']


    >>> b = Block(4400, "pine st")
    >>> b.properties[0]
    4400 Pine St
    >>> b.properties[0].address
    u'4400 Pine St'
    >>> b.properties[0].value
    375400
    >>> b.properties[0].owner_names
    [u'Ethyle Herman Irrevocable']
    >>> b.properties[0].owners
    [Ethyle Herman Irrevocable (5 properties)]

    """
    pass


class Owner(object):
    """An owner entity. Similar to Block, mostly a container for properties.

    Your constructor should take the owner name, and retrieve the list of owned
    properties (creating Property objects). The name should be converted to
    title case.

    >>> o = Owner("wawa")
    >>> o
    Wawa (18 properties)
    >>> o.name
    'Wawa'
    >>> o.properties
    [6400 Bustleton Ave, 6460 Bustleton Ave, 151 Byberry Rd, 4510 Castor Ave,
    6925-35 Castor Ave, 8140 Castor Ave, 9213-19 Frankford Ave, 2600L Grant
    Ave, 6001 Harbison Ave, 10550 Knights Rd, 7913-29 Oxford Ave, 2401
    Pennsylvania Ave Unit: 14C48, 3222-48 Richmond St, 4371 Richmond St, 7301
    Rockwell Ave, 8000 E Roosevelt Blv, 9440 State Rd, 6400-22 Torresdale Ave]
    >>> o.properties[0].owners
    [Wawa Inc (15 properties)]

    """
    pass


## PROBLEM 3 ##
## Now that we've built a wrapper around the API, let's do some useful stuff

def mean_value(block_or_owner):
    """Find the mean value of properties, rounded to the cents place.

    >>> block = Block(4000, "spruce st")
    >>> mean_value(block)
    413686.05
    """
    raise NotImplementedError()


def median_value(block_or_owner):
    """Find the median value of properties, rounded to the cents place.

    http://mathworld.wolfram.com/StatisticalMedian.html

    >>> block = Block(4000, "spruce st")
    >>> median_value(block)
    396100.0
    >>> owner = Owner("wawa")
    >>> median_value(owner)
    594550.0
    """
    raise NotImplementedError()


def max_block_or_owner(*entities):
    """Find the block/owner with the maximum mean property value

    Remember that with the * above, the arguments are packed into a tuple

    >>> o1 = Owner("Wawa")
    >>> o1
    Wawa (18 properties)
    >>> o2 = Owner("citibank")
    >>> o2
    Citibank (8 properties)
    >>> max_block_or_owner(o1, o2)
    Wawa (18 properties)
    """
    raise NotImplementedError()


def main():
    """Our main function. Runs doc and nose tests."""
    print "Running doctests...\n"
    import doctest

    # this sets our doctests to:
    # a) ignore the messages associated with exceptions. Just ensure they're
    # thrown.
    # b) ignore whitespace
    # c) allow us to use '...' when we don't care what something is
    options = (doctest.IGNORE_EXCEPTION_DETAIL | doctest.NORMALIZE_WHITESPACE |
               doctest.ELLIPSIS)
    doctest_results = doctest.testmod(optionflags=options, verbose=True)
    print doctest_results

    print "\n\nRunning unit tests...\n"
    # You will need to 'pip install nose' for this line to work
    # You will need to 'pip install coverage' to get coverage information
    import nose
    if nose.run(argv=["--with-coverage", "hw2.py"]):
        print "\nPassed all unit tests"

    print "\n\nRepeating doctest results:"
    print str(doctest_results)


if __name__ == "__main__":
    # calls main() if we have run this with 'python hw2.py'
    main()
