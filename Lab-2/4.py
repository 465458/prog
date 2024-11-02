import xml.dom.minidom as minidom

xml_file = open('currency.xml','r')
xml_data = xml_file.read()

dom = minidom.parseString(xml_data)
dom.normalize()

elements = dom.getElementsByTagName('Valute')
currency_dict={}

for node in elements:
    for child in node.childNodes:
        if child.nodeType == 1:
            if child.tagName == "CharCode":
                if child.firstChild.nodeType == 3:
                    char_code = child.firstChild.data
            if child.tagName == 'Nominal':
                if child.firstChild.nodeType == 3:
                    value = child.firstChild.data.replace(',','.')
    currency_dict[char_code] = value

print(currency_dict)
