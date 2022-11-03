XML_FILE = open("shedule.xml", "r", encoding="utf-8")
STRING_XML_FILE = XML_FILE.read().replace("\n", "").replace(" ", "")


class Tag:
    def __init__(self, name, index_in_string, string):
        self.name = name
        self.index_in_string = index_in_string + len(name)
        self.ending_index = string.find(f"</{str(self)}>", self.index_in_string)+1
        self.data = string[self.index_in_string:self.ending_index-1]

    def __str__(self):
        return self.name[1:-1:1]


class Parser:
    number_levels = 0

    def __init__(self, string, in_container = False):
        self.data = string
        self.output = ""

    def first_tag_in_data(self):
        end_tag = self.data.find(">") +1
        tag = Tag(self.data[0:end_tag], 0, self.data)
        return tag

    def parse(self):
        current_tag = self.first_tag_in_data()
        if self.check(current_tag.data):
            Parser.number_levels += 1
        new_parser = Parser(current_tag.data, True)

        if self.check(current_tag.data):
            self.output += str(current_tag) + ":\n" + " "*self.number_levels
            new_parser.parse()
            self.output += new_parser.output
        else:
            self.output += str(current_tag) + ": " + current_tag.data
            Parser.number_levels -= 1

    def check(self, string):
        if string.count("<") > 0:
            return True
        return False


def main():
    tests_string = STRING_XML_FILE
    parser = Parser(tests_string)
    parser.parse()
    print(parser.output)

if __name__ == "__main__":
    main()




