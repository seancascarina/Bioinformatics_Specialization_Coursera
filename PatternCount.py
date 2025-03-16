

def main():
    
    file = 'PatternCount_TestData.txt'
    seq, pattern = get_params(file)
    
    count = 0
    for i in range(len(seq)-len(pattern)+1):
        kmer = seq[i:i+len(pattern)]
        if kmer == pattern:
            count += 1
            
    print(count)
    
    
def get_params(file):
    """Get parameters from test file.
    Returns:
        seq = string --> represents a DNA sequence
        k = int --> represents the size of kmer that we are interested in examining
    """
    
    h = open(file)
    seq = h.readline().rstrip()
    pattern = h.readline().rstrip()
    
    h.close()
    
    return seq, pattern


if __name__ == '__main__':
    main()