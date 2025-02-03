from enum import Enum
from leafnode import *

TextType = Enum('TextType',["NORMAL","BOLD","ITALIC","CODE","LINK","IMAGE"])

class TextNode:
    def __init__(self,text,text_type,url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self,other):
        return (self.text == other.text and
                self.text_type == other.text_type and
                self.url == other.url)

    def __repr__(self):
        text = f"\"{self.text}\""
        value = self.text_type
        url = f"\"{self.url}\""
        return f"TextNode({text},{value},{url})"

    def text_node_to_html_node(self):
        match self.text_type:
            case TextType.NORMAL:
                return LeafNode(None,self.text)
            case TextType.BOLD:
                return LeafNode("b",self.text)
            case TextType.ITALIC:
                return LeafNode("i",self.text)
            case TextType.CODE:
                return LeafNode("code",self.text)
            case TextType.LINK:
                return LeafNode("a",self.text,{"href": self.url})
            case TextType.IMAGE:
                return LeafNode("img","",{"src": self.url, "alt" : self.text})
            case _:
                return ""

