import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p","This is a paragraph",None,{"class":"testclass testclass2","id":"my_id"})
        node2 = HTMLNode("p","This is a paragraph",None,{"class":"testclass testclass2","id":"my_id"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())



if __name__ == "__main__":
    unittest.main()

