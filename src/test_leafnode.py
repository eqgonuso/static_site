import unittest

from leafnode import *


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p","This is a paragraph",{"class":"testclass testclass2","id":"my_id"})
        node2 = LeafNode("p","This is a paragraph",{"class":"testclass testclass2","id":"my_id"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())



if __name__ == "__main__":
    unittest.main()

