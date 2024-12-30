import unittest

from textnode import TextNode, TextType


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


if __name__ == "__main__":
    unittest.main()

