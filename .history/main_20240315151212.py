print ("hello world")

with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.lower().split()
    n_words = len(words)
    print(n_words)