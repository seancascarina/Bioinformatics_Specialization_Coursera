

def main():
    
    file = 'Vibrio_cholerae_genome.txt'
    motif = 'CTTGATCAT'     # PRE-DEFINED IN THE EXERCISE
    genome = get_params(file)
    
    locations = []
    for i in range(len(genome)-len(motif)+1):
        kmer = genome[i:i+len(motif)]
        if kmer == motif:
            locations.append(i)
            
    print(locations)
    print(' '.join([str(x) for x in locations]))
    
    
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