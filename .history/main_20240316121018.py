print ("hello world")

count_lib = {}
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.lower().split()
    n_words = len(words)
    print(n_words)

    for i in file_contents.lower():
        if i in count_lib:
            count_lib[i] += 1
        else:
            count_lib[i] = 1
    for n in count_lib:
        print(f"The {n.values()} character was found {n.keys()} times")
    print (count_lib)

