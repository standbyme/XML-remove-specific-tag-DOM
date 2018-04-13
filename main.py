from bs4 import BeautifulSoup, element


def no_nl(s):
    return str(s).replace("\r", "").replace("\n", "")


soup = BeautifulSoup(open("document.xml"), "xml")
[s.extract() for s in soup(["mc:AlternateContent", "w:drawing"])]

for e in soup.find_all():
    for x in e.children:
        if isinstance(x, element.Comment):
            x.replace_with("")

for e in soup.find_all():
    name = e.name
    if ((not len(no_nl(e.text).strip())) and (name != 'sz') and (name != 'szCs') and (name != 'pPr') and (name != 'rPr') and (name != 'vanish')):
        e.extract()

f = open('output.xml', 'w')
f.write(soup.prettify())
f.close()
