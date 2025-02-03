import unittest

from textnode import TextNode, TextType
from leafnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("This is a link node", TextType.LINK, "https://yahoo.com")
        node2 = TextNode("This is a link node", TextType.LINK, "https://yahoo.com")
        self.assertEqual(node, node2)

    def test_url_is_none(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        self.assertIsNone(node.url)

    def test_text_diff(self):
        node = TextNode("This is a link node", TextType.LINK)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node,node2)

    def test_text_to_leaf(self):
        node = TextNode("This is a text node", TextType.NORMAL)
        node2 = LeafNode(None,"This is a text node")
        ln1 = node.text_node_to_html_node()
        n1_html = ln1.to_html()
        n2_html = node2.to_html()
        self.assertEqual(n1_html,n2_html)

if __name__ == "__main__":
    unittest.main()

