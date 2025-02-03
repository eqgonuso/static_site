import unittest

from parentnode import *


class TestParentNode(unittest.TestCase):
    def test_eq(self):
        node = ParentNode("p",[LeafNode("b","Bold Text"), LeafNode(None,"Normal Text")],{"class":"testclass testclass2","id":"my_id"})
        node2 = ParentNode("p",[LeafNode("b","Bold Text"), LeafNode(None,"Normal Text")],{"class":"testclass testclass2","id":"my_id"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())



if __name__ == "__main__":
    unittest.main()

