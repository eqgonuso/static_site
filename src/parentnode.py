from htmlnode import *
from leafnode import *

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super().__init__(tag,None,children,props)
        del self.value

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode that does not have tag")
        if self.children == None:
            raise ValueError("ParentNode that does not have children")
        l_props = self.props_to_html()
        if l_props is None:
            l_props = ""
        retval = f"<{self.tag} {l_props}>"
        for child in self.children:
            retval += child.to_html()

        retval += f"</{self.tag}>"
        return retval

    def props_to_html(self):
        if self.props is not None:
            return " ".join(map(lambda x: f"{x[0]}=\"{x[1]}\"",list(self.props.items())))
        return ""
    
    def __repr__(self):
        return f"<{self.tag} {self.props_to_html}>{self.value}</{self.tag}>"
