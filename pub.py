import sys
import io

if len(sys.argv) < 3:
    print("Usage example: python pub.py 1,3,4 20")
    exit(1)

# 1st argument is a comma delimited list of possible moves - e.g. "1,2,3"
move_set_strings = sys.argv[1].split(',')
move_set = list(map(lambda s: int(s), move_set_strings))

# 2nd argument is the sequence length
seq_length = int(sys.argv[2])

nimber_cache = {}


def print_nimber_sequence(sequence):
    """Prints the nimber sequence of a pick up bricks game.
    """
    table = get_sequence_table(sequence)
    print(table)


def get_sequence_table(sequence):
    """Returns the nimber sequence as a table string
    """
    output = io.StringIO()
    output.write("| position | nimber |\n")
    output.write("+----------+--------+\n")
    for position, nimber in enumerate(sequence):
        output.write(f"| {position:<8} | {nimber:>6} |\n")
    return output.getvalue()


def write_nimber_sequence(sequence):
    """Writes the nimber sequence of a pick up bricks game to a csv file.
    """
    csv = get_sequence_csv(sequence)

    filename = f"sequence_{'-'.join(move_set_strings)}_{seq_length}.csv"
    f = open(filename, "w+")
    f.write(csv)


def get_sequence_csv(sequence):
    """Returns the nimber sequence as csv string
    """
    output = io.StringIO()
    output.write("position,nimber\n")
    for position, nimber in enumerate(sequence):
        output.write(f"{position},{nimber}\n")
    return output.getvalue()


def get_nimber_sequence():
    """Computes the nimber sequence of a pick-up-bricks position up to a specified length.
    """
    sequence = []
    for i in range(seq_length):
        sequence.append(get_nimber(i))
    return sequence


def get_nimber(num_bricks):
    """Retrieves the nimber equivalent of a pick-up-bricks position.
    """
    # TODO

    # Instead of computing the same nimbers repeatedly, we should use nimber_cache to store them
    global nimber_cache

    return 0


def compute_nimber(num_bricks):
    """Computes the nimber equivalent of a pick-up-bricks position.
    """
    # TODO
    return 0


def mex(int_list):
    """Returns the MEX of a list of integers.
    """
    # TODO
    return 0


seq = get_nimber_sequence()
print_nimber_sequence(seq)
write_nimber_sequence(seq)
