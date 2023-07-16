import argparse
from Bio import Entrez, SeqIO

def get_genome(id):
    """Fetch a genome from NCBI and return as a SeqRecord."""
    print(f"Fetching genome {id} from NCBI...")
    Entrez.email = args.email
    handle = Entrez.efetch(db="nucleotide", id=id, retype="gb", retmode="text")
    return SeqIO.read(handle, "genbank")

def count_nucleotides(seq_record):
    """Count the nucleotides in a SeqRecord and return as a dictionary."""
    print(f"Counting nucleotides in {seq_record.id}...")
    nucleotide_counts = {
        "A": 0,
        "C": 0,
        "G": 0,
        "T": 0
    }

    for nucleotide in seq_record.seq:
        if nucleotide in nucleotide_counts:
            nucleotide_counts[nucleotide] += 1

    return nucleotide_counts

parser = argparse.ArgumentParser(description='Count the nucleotides in a genome from NCBI.')
parser.add_argument('genome_id', type=str, help='The genome ID to fetch from NCBI.')
parser.add_argument('email', type=str, help='Your email address to provide to NCBI.')

args = parser.parse_args()

genome = get_genome(args.genome_id)
counts = count_nucleotides(genome)

for nucleotide, count in counts.items():
    print(f"{nucleotide}: {count}")
