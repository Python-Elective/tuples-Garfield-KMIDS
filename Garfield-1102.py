def skip_tuples(tuple):
    """
    It has a tuple as input.

    It returns a new tuple as output,such as
    every second element of the input tuple is
    skipped, starting with the first one.
    """
    new_tuple = ()
    for i in range(len(tuple)):
        if i % 2 == 0:
            new_tuple += (tuple[i],)
    return new_tuple

def main():
    print("Test skip_tuples -----------")
    print(skip_tuples((1, 2, 3, 4, 5)))
    print(skip_tuples((1, 2, 3, 4, 5, 6, 7, 8)))
    print(skip_tuples(('I', 'am', 'a', 'test', 'tuple')))
    print(skip_tuples((1, True, 3, False, 5, False, 'Hi', 8, True)))

if __name__ == "__main__":
    main()