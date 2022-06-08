# Google search counter
#### Video Demo: https://youtu.be/7jk9Uzj8HM0
#### Description:
This project is a final project for CS50P course. When working on large datasets, for example, thousands of microorganisms in microbiome,
it is important to find out the most well-studied species as the target for research. This project can help people to sort key words
in the order of numbers of google search results, and also provide links to wikipedia pages automatically. This will help to understand
what is more well-studied, versus what is relatively unknown.
#### Component:
This project contains four documments:
1. project.py contains major Python code for the program.
2. test_project.py contains codes for pytest.
3. requirements.txt contains Python modules needed for project.py. Install by "pip install" + module name.
4. README.md is a Markdown file with instructions.
#### Design:
project.py has four functions:
1. main() function accepts input and output files via sys arguments. It then calls google() and wiki() (if "-w" is provided) to get numbers
of google search results and links to wikipedia pages. Finally, it calls output() to list results by a descending order into output file.
2. google() function accepts input file, with a key word on each line. For each key word, it uses "reqeusts" to scrape the google search
results, and then uses "BeautifulSoup" to extract the div with the id of "result-stats", from the HTML content. Then, it uses "re",
regular expression, to extract the number of google search results from the div, and converts the string into an integer. Finally, the numbers
are stored into a dictionary which is returned at the end of the function.
3. wiki() function is called when "-w" is provided. It accepts the same input file as google(), and search through wikipedia for the closest
key words. Then it gets the wikipedia page and its associated url (if exists). Finally it stores all links into a dictionary which is then returned.
4. output() function accepts dictionaries from google() and wiki(). It puts key words into a descending order by numbers of google search results,
and writes them into the output file. If requested, the wikipedia links will also be added to the same file.
#### User instruction:
##### Usage: python + project.py INPUT_FILE OUTPUT_FILE \[-w\]
-h  show help page.\
-w  \[optional\] show wikipedia links in the output file.
##### Example: $ python project.py input.txt output.tsv -w
##### input.txt:
Ecoli\
cats\
New York\
CS50
##### output.tsv:
|          |               |                                                |
| -------- | ------------- | ---------------------------------------------- |
| New York | 8,360,000,000 | https://en.wikipedia.org/wiki/New_York_City    |
|   cats   | 4,270,000,000 | https://en.wikipedia.org/wiki/Cat              |
|   Ecoli	 | 2,360,000,000 | https://en.wikipedia.org/wiki/Escherichia_coli |
|   CS50	 |    10,700,000 | https://en.wikipedia.org/wiki/CS50             |

##### Looks like New York City is the most googled item!
