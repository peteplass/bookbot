print ("hello world")

count_lib = {}
with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.lower().split()
    n_words = len(words)
    print(n_words)
    for f in file_contents:
        if file_contents.isalpha() == False:
            file_contents.remove(f)

    for i in file_contents.lower():
        if i in count_lib:
            count_lib[i] += 1
        else:
            count_lib[i] = 1
    for n in count_lib:
        print(f"The {n} character was found {count_lib[n]} times")
    print (count_lib)

