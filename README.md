# AI for Programming

Small Python utilities for working with DNA sequences in FASTA files.

## Requirements

Python 3; the scripts use only the standard library.

## Scripts

- `scripts/gc_content.py <fasta>` prints the GC-content percentage for each
  non-empty record in a FASTA file.
- `scripts/reverse_complement.py <fasta>` prints the reverse complement of a
  single-record FASTA file. It accepts the DNA bases `A`, `C`, `G`, and `T`.
- `scripts/translate_dna.py` defines `translate(seq)`, which translates a DNA
  sequence into amino acids using the standard genetic code and stops at the
  first stop codon. Running the file prints its built-in example.

## Examples

```bash
python scripts/gc_content.py input/multi_seq.fasta
python scripts/reverse_complement.py input/test_seq.fasta
python scripts/translate_dna.py
```
