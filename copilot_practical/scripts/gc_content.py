"""Print GC content percentages for records in a FASTA file."""

import argparse
import sys


def read_fasta(path):
    """Yield each FASTA header and its concatenated sequence."""
    header = None
    sequence = []

    with open(path) as fasta:
        for line in fasta:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                if header is not None:
                    yield header, "".join(sequence)
                header = line[1:]
                sequence = []
            elif header is not None:
                sequence.append(line)

    if header is not None:
        yield header, "".join(sequence)


def main():
    parser = argparse.ArgumentParser(
        description="Print GC content percentages for FASTA records."
    )
    parser.add_argument("fasta", help="path to the FASTA file")
    args = parser.parse_args()

    for header, sequence in read_fasta(args.fasta):
        if not sequence:
            print(f"Warning: skipping empty sequence for >{header}", file=sys.stderr)
            continue
        gc_count = sum(base in "GCgc" for base in sequence)
        percentage = gc_count / len(sequence) * 100
        print(f">{header}\t{percentage:.3f}%")


if __name__ == "__main__":
    main()
