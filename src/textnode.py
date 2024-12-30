from enum import Enum

TextType = Enum('TextType',["NORMAL","BOLD","ITALIC","CODE","LINK","IMAGE"])

class TextNode:
    def __init__(self,text,text_type,url):
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