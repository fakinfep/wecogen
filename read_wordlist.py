# Read Wordlist from file
def read_wordlist(file_name):
    wordlist = []
    with open(file_name, 'r') as f:
        for line in f:
            wordlist.append(line.strip())
    return wordlist