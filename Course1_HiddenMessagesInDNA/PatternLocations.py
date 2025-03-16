

def main():
    
    file = 'PatternLocations_TestData.txt'
    motif, genome = get_params(file)
    
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
        motif = string --> represents a kmer sequence that we are looking for in a genome sequence
        genome = string --> represents a genome sequence
    """
    
    h = open(file)
    motif = h.readline().rstrip()
    genome = h.readline().rstrip()
    
    h.close()
    
    return motif, genome


if __name__ == '__main__':
    main()