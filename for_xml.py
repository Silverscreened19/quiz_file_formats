import xml.etree.ElementTree as ET
import collections


def read_xml(parser, max_len_word=6, top_words=10):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    my_list = []
    top_10_list = []
    descriptions_list = root.findall("channel/item/description")
    for desc in descriptions_list:
        my_list.append(desc.text)
    for element in my_list:
        description = [word for word in element.split(' ') if len(word) > max_len_word]
        top_10_list.extend(description)
    counter_words = collections.Counter(top_10_list)
    print(counter_words.most_common(top_words))

if __name__ == '__main__':
    read_xml('newsafr.xml')

# [('туристов', 40), ('компании', 26), ('Wilderness', 23), ('странах', 21),
# ('туризма', 19), ('которые', 16), ('африканских', 16), ('туристы', 15),
# ('является', 14), ('природы', 13)]
