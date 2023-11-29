import mappy as mp
from marvin.tools import tool


@tool
def reverse_compliment(seq: str) -> str:
    """Return the reverse complement of a DNA sequence.
    This function recognizes IUB code and preserves the letter cases. Uracil U is complemented to A.

    Args:
    seq (str): The DNA sequence to reverse

    Returns:
    rev_seq (srt): The reversed DNS sequence
    """
    print(f"reversing: {seq}")
    return mp.revcomp(seq)
