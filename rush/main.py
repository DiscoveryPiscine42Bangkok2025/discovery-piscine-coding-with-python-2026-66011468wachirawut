from checkmate import checkmate

def main():
    # Example 1
    board = """\
....
....
....
....
\
"""
    checkmate(board)

    # Example 2
    board = """\
R...
.K.....
..P.
....
\
"""
    checkmate(board)

if __name__ == "__main__":
    main()