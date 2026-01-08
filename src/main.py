# Genomic Sequence Analysis Tool
# This script reads a FASTA file and performs basic bioinformatics analysis

def read_fasta(file_path):
    """
    Reads a FASTA file and returns the header and DNA sequence
    """
    header = ""
    sequence = ""

    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                header = line
            else:
                sequence += line.upper()

    return header, sequence


def calculate_gc_content(sequence):
    """
    Calculates GC content percentage of a DNA sequence
    """
    g_count = sequence.count("G")
    c_count = sequence.count("C")

    gc_content = ((g_count + c_count) / len(sequence)) * 100
    return gc_content


def nucleotide_frequency(sequence):
    """
    Calculates frequency of A, T, G, C nucleotides
    """
    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }


def save_results(header, sequence, gc_content, freq):
    """
    Saves analysis results to a file
    """
    with open("results/analysis.txt", "w") as file:
        file.write("Genomic Sequence Analysis Results\n")
        file.write("--------------------------------\n")
        file.write(f"Header: {header}\n")
        file.write(f"Sequence Length: {len(sequence)}\n")
        file.write(f"GC Content: {gc_content:.2f}%\n\n")
        file.write("Nucleotide Frequency:\n")

        for nucleotide, count in freq.items():
            file.write(f"{nucleotide}: {count}\n")


if __name__ == "__main__":
    fasta_file = "data/sample.fasta"

    header, sequence = read_fasta(fasta_file)

    gc = calculate_gc_content(sequence)
    freq = nucleotide_frequency(sequence)

    print("FASTA Header:")
    print(header)
    print("\nSequence Length:", len(sequence))
    print("GC Content: {:.2f}%".format(gc))
    print("Nucleotide Frequency:", freq)

    save_results(header, sequence, gc, freq)

    print("\nResults saved to results/analysis.txt")

