

def main():

    file = 'FrequentWords_TestData.txt'
    seq, k = get_params(file)
    
    kmer_counts = calc_kmer_counts(seq, k)
    max_kmer_count = max(list(kmer_counts.values()))
    frequent_kmers = find_frequent_kmers(kmer_counts, max_kmer_count)

    print(frequent_kmers)
    print(' '.join(frequent_kmers))
    
    
def find_frequent_kmers(kmer_counts, min_counts):
    """Collect the most frequent kmers from the kmer_counts dictionary.
    Returns:
        frequent_kmers = list --> contains all kmers that had a frequency matching the 
        maximum kmer frequency (of the same kmer size) in the sequence.
    """

    frequent_kmers = [kmer for kmer in kmer_counts if kmer_counts[kmer] >= min_counts]
    
    return frequent_kmers
    
    
def calc_kmer_counts(seq, k):
    """Calculate kmer counts for the given kmer size (k).
    Returns:
        kmer_counts = dict --> keys are kmer sequences, values are the corresponding frequency of the kmer in the sequence
    """
    
    kmer_counts = {}
    for i in range(len(seq)-k+1):
        kmer = seq[i:i+k]
        if kmer not in kmer_counts:
            kmer_counts[kmer] = seq.count(kmer)
            
    return kmer_counts
    
    
def get_params(file):
    """Get parameters from test file.
    Returns:
        seq = string --> represents a DNA sequence
        k = int --> represents the size of kmer that we are interested in examining
    """
    
    h = open(file)
    seq = h.readline().rstrip()
    k = int(h.readline().rstrip())
    
    h.close()
    
    return seq, k

if __name__ == '__main__':
    main()