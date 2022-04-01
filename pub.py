import sys

nimber_cache = {}

#========================================================================================
# Input/Output
#========================================================================================
def output_sequence():
    if len(sys.argv) < 3:
        print("Usage example: python pub.py 1,3,4 20")
        exit(1)

    # 1st argument is a comma delimited list of possible moves - e.g. "1,2,3"
    move_set_strings = sys.argv[1].split(',')
    move_set = list(map(lambda s: int(s), move_set_strings))

    # 2nd argument is the sequence length
    seq_length = int(sys.argv[2])

    seq = get_nimber_sequence(move_set, seq_length)
    print_nimber_sequence(seq)

    filename = f"sequence_{'-'.join(move_set_strings)}_{seq_length}.csv"
    write_nimber_sequence(seq, filename)


def print_nimber_sequence(sequence):
    """Prints the nimber sequence of a pick up bricks game."""
    output_sequence_table(sequence, sys.stdout)


def output_sequence_table(sequence, output):
    """Outputs the nimber sequence as a table string"""
    output.write("| position | nimber |\n")
    output.write("+----------+--------+\n")
    for position, nimber in enumerate(sequence):
        output.write(f"| {position:<8} | {nimber:>6} |\n")


def write_nimber_sequence(sequence, filename):
    """Writes the nimber sequence of a pick up bricks game to a csv file."""
    file = open(filename, "w+")
    output_sequence_csv(sequence, file)


def output_sequence_csv(sequence, output):
    """Outputs the nimber sequence as csv string"""
    output.write("position,nimber\n")
    for position, nimber in enumerate(sequence):
        output.write(f"{position},{nimber}\n")


#========================================================================================
# Nimber Sequences
#========================================================================================
def get_nimber_sequence(move_set, seq_length):
    """Computes the nimber sequence of a pick-up-bricks position up to a specified length."""
    nimber_cache.clear()
    sequence = []
    for i in range(seq_length):
        sequence.append(get_nimber(move_set, i))
    return sequence


def get_nimber(move_set, num_bricks):
    """Retrieves the nimber equivalent of a pick-up-bricks position."""
    global nimber_cache

    if num_bricks in nimber_cache:
        return nimber_cache[num_bricks]
    else:
        nimber = compute_nimber(move_set, num_bricks)
        nimber_cache[num_bricks] = nimber
        return nimber


def compute_nimber(move_set, num_bricks):
    """Computes the nimber equivalent of a pick-up-bricks position."""
    nimber_list = []
    for move in move_set:
        position = num_bricks - move
        if position >= 0:
            nimber_list.append(get_nimber(move_set, position))

    if len(nimber_list) == 0:
        return 0
    return mex(nimber_list)


def mex(int_list):
    """Returns the MEX of a list of integers."""
    mex = max(int_list) + 1
    for i in range (max(int_list)):
        if i not in int_list:
            mex = i
            break
    return mex


#========================================================================================
# Main Function
#========================================================================================
def main():
    output_sequence()


main()
