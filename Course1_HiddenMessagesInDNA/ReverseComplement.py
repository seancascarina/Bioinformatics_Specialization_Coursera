

def main():

    complement_df = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    file = 'ReverseComplement_TestData.txt'
    seq = get_seq(file)
    rev_comp = ''
    for i in range(len(seq)-1, -1, -1):
        nt = seq[i]
        comp_nt = complement_df[nt]
        rev_comp += comp_nt
        
    print(seq)
    print(rev_comp)
    
    print(len(seq), len(rev_comp))
    

def get_seq(file):
    """Get sequence from test file.
    Returns:
        seq = string --> represents a DNA sequence
    """
    
    h = open(file)
    seq = h.readline().rstrip()
    h.close()
    
    return seq
    
    
if __name__ == '__main__':
    main()