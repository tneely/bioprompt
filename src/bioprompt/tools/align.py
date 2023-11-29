import subprocess

from marvin.tools import tool


@tool
def align_sequence(seq_file: str, ref_file: str, out_file: str) -> str:
    """A versatile sequence alignment program that aligns DNA or mRNA sequences against a large reference database.
    Typical use cases include:
     (1) mapping PacBio or Oxford Nanopore genomic reads to the human genome;
     (2) finding overlaps between long reads with error rate up to ~15%;
     (3) splice-aware alignment of PacBio Iso-Seq or Nanopore cDNA or Direct RNA reads against a reference genome;
     (4) aligning Illumina single- or paired-end reads;
     (5) assembly-to-assembly alignment;
     (6) full-genome alignment between two closely related species with divergence below ~15%.

    Args:
    seq_file (str): A path representing a FASTQ or FASTA sequence file
    ref_file (str): A path representing a FASTQ or FASTA reference file
    out_file (str): A path representing the SAM file that should be written to.
     This is often the same name as seq_file, but with the extension replaced by ".sam"

    Returns:
    out_file (str): A path representing the SAM file that is generated as output
    """
    # a = mp.Aligner(ref_file)
    # if not a:
    #     raise Exception(f"ERROR: failed to load/build index from {ref_file}")
    #
    # a.map(seq_file)
    # minimap2 -a ref.fa query.fq > alignment.sam
    f = open(out_file, "w")
    print(f"Aligning {seq_file} to {ref_file} and outputting to {out_file}")
    subprocess.run(["/Users/tneely/dev/minimap2/minimap2", "-a", ref_file, seq_file], stdout=f)
    return out_file
