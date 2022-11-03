
class Tag:
    def __init__(self, name, index_in_string, string):
        self.name = name
        self.index_in_string = index_in_string + len(name)
        self.ending_index = string.find(f"</{str(self)}>", self.index_in_string)
        self.data = string[self.index_in_string:self.ending_index]
        self.depth = None
        self.is_united_without_tags = False
        self.is_united_with_tags = False
        self.add = []
        self.skip = False

    def __eq__(self, other):
        if isinstance(other, Tag):
            return self.name == other.name and self.depth == other.depth
        return NotImplemented

    def __str__(self):
        return self.name[1:-1:1]


class Parser:
    def __init__(self, string):
        self.data = string
        self.tags = []
        self.output = ""

    def __find_tags(self):
        current_string = ""
        start = 0
        for i in range(len(self.data)):
            if self.data[i] == "<":
                start = i
                current_string = self.data[i]
            elif self.data[i] == ">":
                current_string += self.data[i]
                tag = Tag(current_string, start, self.data)
                if "/" not in current_string:
                    self.tags.append(tag)
            else:
                current_string += self.data[i]

    def __calc_depth(self):
        for i in range(len(self.tags)):
            number_all_tags = self.data.count("<", 0, self.tags[i].index_in_string)
            number_closed_tags = self.data.count("/", 0, self.tags[i].index_in_string)
            self.tags[i].depth = number_all_tags - 2 * number_closed_tags - 1

    def check_change_unit(self, start, end):
        start_depth = self.tags[start].depth
        for i in range(start, end):
            if self.tags[i].depth != start_depth:
                return False
        return True

    def __unite_tags(self):
        for i in range(len(self.tags)):
            if self.tags[i].skip:
                continue
            j = i
            flag = True
            while flag:
                j += 1
                if j >= len(self.tags):
                    flag = False
                while j < len(self.tags) and self.tags[j].depth > self.tags[i].depth:
                    j += 1
                if j >= len(self.tags):
                    continue
                if self.tags[i] == self.tags[j]:
                    if j == i + 1 + self.calc_skip_tags(i, j) and self.check_change_unit(i, j):
                        self.tags[j].skip = True
                        if not self.tags[i].is_united_without_tags:
                            self.tags[i].is_united_without_tags = True
                            self.tags[i].data = "- "+self.tags[i].data + "\n" + "  "*(self.tags[i].depth+1)
                            self.tags[i].data += "- " + self.tags[j].data
                        else:
                            self.tags[i].data += "\n" + "  " * (self.tags[i].depth + 1)
                            self.tags[i].data += "- " + self.tags[j].data
                    else:
                        self.tags[i].add.append([])
                        self.tags[i].is_united_with_tags = True
                        self.tags[j].skip = True
                        k = j+1
                        while k < len(self.tags) and self.tags[k].depth > self.tags[j].depth:
                            self.tags[k].skip = True
                            self.tags[i].add[-1].append(Tag(self.tags[k].name,
                                                            self.tags[k].index_in_string-len(self.tags[k].name),
                                                            self.data))
                            self.tags[i].add[-1][-1].depth = self.tags[k].depth
                            k += 1

    def calc_skip_tags(self, start, end):
        ans = 0
        for i in range(start, end):
            if self.tags[i].skip:
                ans += 1
        return ans

    def calc_output(self):
        self.__find_tags()
        self.__calc_depth()
        self.__unite_tags()
        i = 0
        while i < len(self.tags):
            if self.tags[i].skip:
                i += 1
                continue
            if self.tags[i].is_united_without_tags:
                self.output += str(self.tags[i]) + ":\n" + "  " * (self.tags[i].depth+1)
                self.output += self.tags[i].data + "\n" + "  " * self.tags[i + 1].depth
            elif self.tags[i].is_united_with_tags:
                self.output += str(self.tags[i]) + ":\n" + "  " * self.tags[i + 1].depth
                self.output += "- "
                j = i+1
                while j < len(self.tags) and self.tags[j].depth > self.tags[i].depth:
                    if j == len(self.tags) - 1:
                        self.output += str(self.tags[j]) + ": " + self.tags[j].data
                    elif self.tags[j].depth >= self.tags[j + 1].depth:
                        self.output += str(self.tags[j]) + ": " + self.tags[j].data + "\n"
                        self.output += "  " * (self.tags[j + 1].depth+1)
                    else:
                        self.output += str(self.tags[j]) + ":\n" + "  " * (self.tags[j + 1].depth+1)
                    j += 1
                t = j
                for k in range(len(self.tags[i].add)):
                    self.output += "- "
                    for z in range(len(self.tags[i].add[k])):
                        if z == len(self.tags[i].add[k]) - 1:
                            self.output += str(self.tags[i].add[k][z]) + ": " + self.tags[i].add[k][z].data
                            if t != len(self.tags):
                                if k < len(self.tags[i].add)-1:
                                    self.output += "\n" + "  " * self.tags[i].add[k][z].depth
                                else:
                                    next_tag = t
                                    while next_tag < len(self.tags) and self.tags[next_tag].skip:
                                        next_tag += 1
                                    if next_tag < len(self.tags):
                                        self.output += "\n" + "  " * self.tags[next_tag].depth
                        elif self.tags[i].add[k][z].depth >= self.tags[i].add[k][z+1].depth:
                            self.output += str(self.tags[i].add[k][z]) + ": " + self.tags[i].add[k][z].data
                            self.output += "\n" + "  " * (self.tags[i].add[k][z+1].depth + 1)
                        else:
                            self.output += str(self.tags[i].add[k][z]) + ":\n"
                            self.output += "  " * (self.tags[i].add[k][z+1].depth + 1)
                        t += 1
                i = t
            elif i == len(self.tags) - 1:
                self.output += str(self.tags[i]) + ": " + self.tags[i].data
            elif self.tags[i].depth >= self.tags[i + 1].depth:
                self.output += str(self.tags[i]) + ": " + self.tags[i].data + "\n" + "  " * self.tags[i + 1].depth
            else:
                self.output += str(self.tags[i]) + ":\n" + "  " * self.tags[i + 1].depth
            i += 1


def main():
    xml_file = open("shedule.xml", "r", encoding="utf-8")
    string_xml_file = xml_file.read().replace("\n", "").replace(" ", "")
    out_yaml_file = open("shedule.yaml", "w")
    parser = Parser(string_xml_file)
    parser.calc_output()
    out_yaml_file.write(parser.output)
    xml_file.close()
    out_yaml_file.close()

if __name__ == "__main__":
    main()
