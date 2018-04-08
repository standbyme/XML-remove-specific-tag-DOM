from bs4 import BeautifulSoup
soup = BeautifulSoup(open("document.xml"), "xml")
[s.extract() for s in soup(["mc:AlternateContent","w:drawing"])]

f = open('output.xml', 'w')
f.write(soup.prettify())
f.close()
