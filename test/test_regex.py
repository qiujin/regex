from nose2.compat import unittest
from nose2.tools import params
import re

class TestBasicReFunction(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_001_match_something_at_the_beginning(self):
        print "re.match only works at the beginning of string \n re.match(r'^abc', 'abcdefabc') = ", re.match(r"^abc", "abcdefabc")

        print "So string in the middle doesn't work \n re.match(r'abc', 'xabc') = ", re.match(r'abc', 'xabc')

    def test_002_search_for_one_match(self):
        match = re.search(r'(?:abc)adf', 'abcadfasdfadfabcasdfasdfabc')
        print "Search for multiple matches using search \n re.search(r'(?:abc)adf', 'abcadfasdfadfabcasdfasdfabc')", match.group(0), match.groups()

    def test_003_search_for_multiple_match(self):
        print "Search for multiple matches using search \n re.findall(r'abc', 'abcadfasdfadfabcasdfasdfabc')", re.findall(r'abc', 'abcadfasdfadfabcasdfasdfabc')

    def test_004_print_debug_expression(self):
        print "Debug expression by printing more informationsearch \n re.findall(r'abc', 'abcadfasdfadfabcasdfasdfabc', re.DEBUG)", re.findall(r'abc', 'abcadfasdfadfabcasdfasdfabc', re.DEBUG)

    def test_005_match_ignorecase(self):
        print "We can ignore case \n re.findall(r'abc', 'ABC', re.I)", re.findall(r'abc', 'ABC', re.I)

    def test_006_match_multiline(self):
        multiline_text = """
        some Varying TEXT

        DSJFKDAFJKDAFJDSAKFJADSFLKDLAFKDSAF
        [more of the above, ending with a newline]
        [yep, there is a variable number of lines here]

        some Varying TEXT

        DSJFKDAFJKDAFJDSAKFJADSFLKDLAFKDSAF
        [more of the above, ending with a newline]
        [yep, there is a variable number of lines here]

        """
        regex = re.compile(r'^(.+)(?:\n|\r\n?)((?:(?:\n|\r\n?).+)+)', re.MULTILINE)
        match = regex.search(multiline_text)
        print "We can search multiline \n re.compile(r'^(.+)(?:\\n|\\r\\n?)((?:(?:\\n|\\r\\n?).+)+) = ', re.MULTILINE)", match.groups()

    def test_007_match_dotall(self):
        fancy_text = """
        <div>I'm some
               fancy text that needs
               to be found</div>
               """
        regex = re.compile('some\s*fancy', re.DOTALL)
        match = regex.search(fancy_text)
        print "DOTALL can be used to match pattern on multiline\n re.compile('some\\s*fancy', re.DOTALL)", match.group()

    def test_010_print_verbose_expression(self):
        print "Debug expression by printing more informationsearch\n re.findall(r'abc', 'abcadfasdfadfabcasdfasdfabc', re.VERBOSE)", re.findall(r'abc', 'abcadfasdfadfabcasdfasdfabc', re.VERBOSE)
        pass

    def test_011_split_string(self):
        print "Split string is easy\n re.split(r',', 'hello,the,world')", re.split(r',', 'hello,the,world')

    def test_012_substitute(self):
        print "Substitute string is easy\n re.sub(r'hello', 'hi', 'hello,the,world')", re.sub(r'hello', 'hi', 'hello,the,world')

    def test_013_escape(self):
        print "Regex can escape string\n", re.escape('A$^a|string-*.withmetacharacters')
