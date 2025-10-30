import re

'regular regression sequence of characters that form search patterns'
"""
[arn] Returns a match where one of the specified characters (a, r or n) is present
[a-n] Return a match for any lower case character, aphabetically between a and n
[^arn] Return a match for any character EXCEPT a, r and n
[0123] Return a match where any of the specified digit  (0, 1, 2, 3) are present
[0-9] Return a match for any digit between 0 and 9
[0-5][0-9] Return a match for any two-digit number from 00 and 59
[a-zA-Z] Returns a match for any character alphabetically between a and z, lower case or upper case
[+] In sets  +, *, ., |, (), $, {} has no special meaning, so [+] means: return a match for any + characters in the string
"""

def demo_re_match():
    pattern = r'^Hello'
    text = 'Hello, World!'
    match = re.match(pattern, text)
    if match:
        print('Match found: ', match.group())
    else:
        print('No match found :(')

def demo_re_search():
    pattern= r"world"
    text = "Hello, world!"
    search = re.search(pattern, text)
    if search:
        print('Search Found: ', search.group())
    else:
        print('Search not found.')

def demo_re_findall():
    pattern = r'\d+'
    text = 'There are 24 apples and 13 oranges.'
    numbers = re.findall(pattern, text)
    print('Numbers found: ', numbers)

def demo_re_finditer():
    pattern = r'\d+'
    text = 'There are 24 apples and 13 oranges.'
    for match in re.finditer(pattern, text):
        print('Found number: ', match.group())

def demo_re_sub():
    pattern = r'\d+'
    text = 'There are 24 apples and 13 oranges.'
    new_text = re.sub(pattern, 'NUMBER', text)
    print('Substituted text: ', new_text)

def demo_re_split():
    pattern = r'\W+'
    text = 'Hello, world! How are you?'
    parts = re.split(pattern, text)
    print('Split Parts: ', parts)


def main():
    print("Demo of re.match:")
    demo_re_match()
    print("\nDemo of re.search:")
    demo_re_search()
    print("\nDemo of re.findall:")
    demo_re_findall()
    print("\nDemo of re.finditer:")
    demo_re_finditer()
    print("\nDemo of re.sub:")
    demo_re_sub()
    print("\nDemo of re.split:")
    demo_re_split()

if __name__ == "__main__":
    main()

## Core regular expression function

"""
re.compile(pattern, flags=0) → compiled regex object (faster reuse)

re.match(pattern, string, flags=0) → match at start of string

re.fullmatch(pattern, string, flags=0) → match entire string

re.search(pattern, string, flags=0) → first match anywhere

re.findall(pattern, string, flags=0) → list of matched substrings (or tuples if groups)

re.finditer(pattern, string, flags=0) → iterator of Match objects

re.sub(pattern, repl, string, count=0, flags=0) → replace; repl is str or function

re.subn(pattern, repl, string, count=0, flags=0) → like sub + returns (new_string, nsubs)

re.split(pattern, string, maxsplit=0, flags=0) → split by regex; capturing groups are kept

re.escape(string) → escape all regex metacharacters

re.purge() → clear internal caches

re.error → exception type raised on bad patterns
"""