
import FrequentWords

def main():

    file = 'KmerDensity_TestData.txt'
    genome, kmer_size, subregion_length, min_counts = get_params(file)

    all_frequent_kmers = set()
    for i in range(len(genome) - subregion_length + 1):
        subregion = genome[i:i+subregion_length]
        kmer_counts = FrequentWords.calc_kmer_counts(subregion, kmer_size)
        frequent_kmers = FrequentWords.find_frequent_kmers(kmer_counts, min_counts)
        for kmer in frequent_kmers:
            all_frequent_kmers.add(kmer)
    
    print(all_frequent_kmers)
    print(' '.join(list(all_frequent_kmers)))
    
    
def get_params(file):
    """Get parameters from test file.
    Returns:
        genome = string --> represents a genome sequence
        kmer_size = int --> represents the size of kmer that we are interested in examining
        subregion_length = int --> represents the length of a subregion within which you want 
                                    to measure the kmer density
        min_counts = int --> represents the minimum counts of the kmer in subregion_length
                                to be saved as a kmer with high density
    """
    
    h = open(file)
    genome = h.readline().rstrip()
    kmer_size, subregion_length, min_counts = h.readline().rstrip().split(' ')
    kmer_size, subregion_length, min_counts = int(kmer_size), int(subregion_length), int(min_counts)
    
    h.close()
    
    return genome, kmer_size, subregion_length, min_counts
    

if __name__ == '__main__':
    main()