
import FrequentWords
from tqdm import tqdm

def main():

    file = 'Ecoli_Genome.txt'
    genome = get_params(file)
    
    # PRE-DEFINED PARAMETERS FOR THE EXERCISE
    kmer_size = 9
    subregion_length = 500
    min_counts = 3
    
    all_frequent_kmers = set()
    for i in tqdm( range(len(genome) - subregion_length + 1) ):
        # START BY PERFORMING KMER-COUNTS FOR THE ENTIRE SUBREGION, ONLY FOR THE FIRST POSITION
        if i == 0:
            subregion = genome[i:i+subregion_length]
            kmer_counts = FrequentWords.calc_kmer_counts(subregion, kmer_size)
        # FOR ALL POSITIONS AFTER THE FIRST, SIMPLY MODIFY THE kmer_counts DICTIONARY
        # BY CONSIDERING ONLY THE KMER THAT IS LOST AT THE BEGINNING OF THE SUBREGION AND
        # THE KMER THAT IS GAINED AT THE END OF THE SUBREGION WHEN THE SLIDING WINDOW
        # IS MOVED BY ONE POSITION.
        else:
            subtracted_kmer = genome[i-1:i-1+kmer_size]
            added_kmer = genome[i+subregion_length-kmer_size:i+subregion_length]
            kmer_counts = update_kmer_dict(kmer_counts, added_kmer, subtracted_kmer)
            
        frequent_kmers = FrequentWords.find_frequent_kmers(kmer_counts, min_counts)
        for kmer in frequent_kmers:
            all_frequent_kmers.add(kmer)
    
    print(all_frequent_kmers)
    print(' '.join(list(all_frequent_kmers)))
    print('total number:', len(all_frequent_kmers))
    
    
def update_kmer_dict(kmer_counts, added_kmer, subtracted_kmer):
    """Modify the kmer_count dictionary by only considering the new kmer that is 
    encountered in the next sliding window and by subtracting 1 from the count for
    the kmer that is no longer part of the next sliding window.
    
    Also removes the old kmer from the dictionary if its kmer count dropped to zero.
    
    This function is essential for computational efficiency (time and memory) on whole genomes,
    as kmer counts do not need to be recalculated from scratch each time the sliding window is
    moved by one position.
    """
    
    kmer_counts[added_kmer] = kmer_counts.get(added_kmer, 0) + 1
    kmer_counts[subtracted_kmer] -= 1
    if kmer_counts[subtracted_kmer] == 0:
        kmer_counts.pop(subtracted_kmer)
    
    return kmer_counts
    
    
def get_params(file):
    """Get parameters from test file.
    Returns:
        genome = string --> represents a genome sequence
    """
    
    h = open(file)
    genome = h.readline().rstrip()
    
    h.close()
    
    return genome
    

if __name__ == '__main__':
    main()