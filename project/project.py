import sys
import requests
import bs4
import re
import wikipedia


def main():
    # usage
    if sys.argv[1] == "-h":
        print("This program helps you sort key words by number of google results.")
        print("Usage: project.py INPUT_FILE OUTPUT_FILE [-w]")
        print("-h  help")
        print("-w  output links for wikipedia pages into the file")
        sys.exit(0)
    elif len(sys.argv) == 3:
        w = False
    elif len(sys.argv) == 4 and sys.argv[-1] == '-w':
        w = True
    else:
        print("Usage: project.py INPUT_FILE OUTPUT_FILE [-w]")
        print("Use -h for the help page")
        sys.exit(1)

    # google search
    try:
        f1 = open(sys.argv[1])
    except FileNotFoundError:
        print("Invalid input file")
        sys.exit(1)
    else:
        results = google(f1.readlines())
        f1.close()

        if w:
            f1 = open(sys.argv[1])
            wikipages = wiki(f1.readlines())
            f1.close()
        else:
            wikipages = {}

    # output file
    output(results, wikipages, sys.argv[2])


def google(file):
    '''
    Input a file with key words in each line.
    Output a dictionary with key words as keys, numbers of google search results as values.
    '''
    results = {}

    for line in file:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"}
        response = requests.get("https://www.google.com/search?q=" + line.strip(), headers=headers)
        soup = bs4.BeautifulSoup(response.content, features="lxml")
        stats = soup.find(id="result-stats")
        if stats:
            matches = re.search(r"About ([0-9,]+) results", stats.text)
            n = matches.group(1)
        else:
            n = '0'
        results[line.strip()] = int(n.replace(',', ''))

    return results


def wiki(file):
    '''
    Input a file with key words in each line.
    Output a dictionary with key words as keys, wikipedia links as values.
    '''
    wikipages = {}

    for line in file:
        # search the key word on wikipedia
        try:
            word = wikipedia.search(line.strip())[0]
        except IndexError:
            continue

        # get the wikipage
        try:
            page = wikipedia.page(word, auto_suggest=False)
        except wikipedia.exceptions.DisambiguationError as e:
            word = e.options[0]
            page = wikipedia.page(word, auto_suggest=False)

        wikipages[line.strip()] = page.url

    return wikipages


def output(results, wikipages, outfile="output.tsv"):
    '''
    Input dictionaries with key words and their numbers of google search results or wikipedia links.
    Input a filename.
    Output the key words in a descending order based on numbers of google search results, together with wikipedia links (if exist).
    '''
    sort_results = dict(sorted(results.items(), key=lambda x: x[1], reverse=True))

    with open(outfile, 'w') as f2:
        for key, value in sort_results.items():
            f2.write(key + "\t" + str('{:,}'.format(value)))
            if key in wikipages:
                f2.write("\t" + wikipages[key] + "\n")
            else:
                f2.write("\n")


if __name__ == "__main__":
    main()