class Elem:
    class ValidationError(Exception):
        def __init__(self, message="Validation error"):
            super().__init__(message)

    def __init__(self, tag, attr={}, content=None, tag_type="double"):
        self.tag = tag
        self.attr = attr
        self.content = [] if content is None else [content]
        self.tag_type = tag_type

    def __str__(self):
        html = f"<{self.tag}{self.format_attributes()}>"
        if self.content:
            html += self.format_content()
        if self.tag_type == "double":
            html += f"</{self.tag}>"
        return html

    def format_attributes(self):
        if not self.attr:
            return ""
        return " " + " ".join([f'{key}="{value}"' for key, value in self.attr.items()])

    def format_content(self):
        content_html = ""
        for item in self.content:
            if isinstance(item, Elem):
                content_html += str(item)
            else:
                content_html += item
        return content_html

    def add_content(self, content):
        if isinstance(content, Elem):
            self.content.append(content)
        else:
            self.content.append(str(content))
   

# Test the Elem class and replicate the HTML structure
if __name__ == '__main__':
    html = Elem("html")
    head = Elem("head")
    title = Elem("title", content="Hello ground!")
    head.add_content(title)
    body = Elem("body")
    h1 = Elem("h1", content="Oh no, not again!")
    body.add_content(h1)
    img = Elem("img", attr={"src": "http://i.imgur.com/pfp3T.jpg"}, tag_type="simple")
    body.add_content(img)
    html.add_content(head)
    html.add_content(body)

    print(html)

