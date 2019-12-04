def count_words(filename):
    """compute how many words a file contains"""

    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
              " words.")


filename = '40623.txt'
count_words(filename)

filenames = ['40623.txt', 'fk.txt', '42075.txt']
for fname in filenames:
    count_words(fname)
