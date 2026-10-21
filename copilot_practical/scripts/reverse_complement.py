# reverse_complement.py
# Reads a single-record DNA sequence from a FASTA file and prints its
# reverse complement.

COMPLEMENT = {"A": "T", "T": "A", "C": "G", "G": "C"}


def read_fasta_sequence(path):
    """Return the sequence from a single-record FASTA file."""
    sequence = []
    header_seen = False

    with open(path) as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header_seen:
                    raise ValueError("Expected a single-record FASTA file")
                header_seen = True
                continue
            if not header_seen:
                raise ValueError(
                    f"Sequence data found before FASTA header on line {line_number}"
                )
            sequence.append(line)

    return "".join(sequence)


def reverse_complement(seq):
    """Return the reverse complement of a DNA sequence."""
    seq = seq.upper()
    try:
        return "".join(COMPLEMENT[base] for base in reversed(seq))
    except KeyError as error:
        raise ValueError(f"Invalid DNA base: {error.args[0]}") from error


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Print the reverse complement of a single-record FASTA file."
    )
    parser.add_argument("fasta", help="path to the FASTA file")
    args = parser.parse_args()

    seq = read_fasta_sequence(args.fasta)
    print(reverse_complement(seq))
