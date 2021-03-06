# Program TRANSFORM in Python
# Figure 5.2 from the book "Computational Thinking: First Algorithms, Then Code"
# Authors: Paolo Ferragina and Fabrizio Luccio
# Published by Springer


def transform(k, c):
    """
    Transforms the input character into the output encrypted character t by applying
    a sum module 26 of k positions in the alphabet, 
    where k is the cypher key.
    :param k: cipher k
    :param c: input c character
    :return: t output trnsformed character
    """

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    i = 0
    while alphabet[i] != c:
        i = i + 1

    j = (i + k) % 26
    t = alphabet[j]

    return t


def main():

    print transform(0, 'D')
    print transform(3, 'D')
    print transform(3, 'X')


if __name__ == "__main__":
    main()
