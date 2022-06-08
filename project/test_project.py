from project import wiki, output
import requests
import re


def test_google():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
    response = requests.get("https://www.google.com/search?q=Ecoli", headers=headers)
    match = re.search(r"About [0-9,]+ results", response.text)
    assert match != None


def test_wiki():
    file = ['Ecoli\n', 'cats\n']
    assert wiki(file) == {
        'Ecoli': 'https://en.wikipedia.org/wiki/Escherichia_coli',
        'cats': 'https://en.wikipedia.org/wiki/Cat',
        }


def test_output():
    results = {'Ecoli': 2240000000, 'cats': 5780000000}
    wikipages = {
        'Ecoli': 'https://en.wikipedia.org/wiki/Escherichia_coli',
        'cats': 'https://en.wikipedia.org/wiki/Cat',
        }
    outfile = 'out.tsv'

    output(results, wikipages, outfile)

    with open(outfile) as f:
       assert f.readlines() == [
           'cats\t5,780,000,000\thttps://en.wikipedia.org/wiki/Cat\n',
           'Ecoli\t2,240,000,000\thttps://en.wikipedia.org/wiki/Escherichia_coli\n'
           ]