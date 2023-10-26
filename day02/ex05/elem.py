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
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            file.write(str(self))

class Html(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class Head(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class Body(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class Title(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class Meta(Elem):
    def __init__(self, content=None):
        super().__init__(content)
        self.tag_type = "simple"

class Img(Elem):
    def __init__(self, src, content=None):
        super().__init__(content)
        self.attr = {"src": src}

class Table(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class Th(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class Tr(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class Td(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class Ul(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class Ol(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class Li(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class H1(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class H2(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class P(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class Div(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class Span(Elem):
    def __init__(self, content=None):
        super().__init__(content)

class Hr(Elem):
    def __init__(self, content=None):
        super().__init__(content)
        self.tag_type = "simple"

class Br(Elem):
    def __init__(self, content=None):
        super().__init__(content)
        self.tag_type = "simple"

# Test the derived classes and replicate the HTML structure
if __name__ == '__main__':
    # Create a Body element without attributes and with content
    html = Body([
        H1("Oh no, not again!"),
        Img(src="http://i.imgur.com/pfp3T.jpg")
    ])


    print(html)
    
    # Create and save the HTML file
    html.save_to_file("index.html")
