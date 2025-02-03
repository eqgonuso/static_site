from htmlnode import *

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super().__init__(tag,value,None,props)
        del self.children

    def to_html(self):
        if self.value == None:
            raise ValueError("leafnode that does not have value")
        if self.tag == None:
            return self.value
        l_props = self.props_to_html()
        if l_props is None:
            l_props = ""
        open_tag = f"<{self.tag} {l_props}>"
        close_tag = f"</{self.tag}>"
        return f"{open_tag}{self.value}{close_tag}"

    def props_to_html(self):
        if self.props is not None:
            return " ".join(map(lambda x: f"{x[0]}=\"{x[1]}\"",list(self.props.items())))
        return None
    
    def __repr__(self):
        return f"<{self.tag} {self.props_to_html}>{self.value}</{self.tag}>"
