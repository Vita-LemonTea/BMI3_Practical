import textdistance

def KmerFreq(sequence, kmer):
    n = len(kmer)
    l = list(sequence)
    frequency = 0
    for i in range(0,len(l)-n+1):
        check = l[i:i+n]
        check = ''.join(check)
        if check == kmer:
            frequency += 1
    return frequency

def MostFreqKmer(sequence, n):
    l = list(sequence)
    dict1 = {}
    for i in range(0, len(l)-n+1):
        kmer = l[i:i+n]
        kmer = ''.join(kmer)
        if kmer in dict1.keys():
            dict1[kmer] += 1
        else:
            dict1[kmer] = 1
    best = []
    max_value = max(dict1.values())
    for key,value in dict1.items():
        if value == max_value:
            best.append(key)
    return best

def miniBLAST(align, genome):
    result ={'forward': [], 'reverse': []}
    n = len(align)
    l = list(genome)
    rl = []
    for f in range(0,len(l)-n+1):
        check = l[f:f+n]
        check = ''.join(check)
        if check == align:
            result['forward'].append(f)
    for i in range(0,len(l)):
        nu = l.pop()
        if nu == "A":
            nu = "T"
            rl.append(nu)
        elif nu == "T":
            nu = "A"
            rl.append(nu)
        elif nu =="C":
            nu = "G"
            rl.append(nu)
        else:
            nu = "C"
            rl.append(nu)
    for r in range(0,len(rl)-n+1):
        check = rl[r:r+n]
        check = ''.join(check)
        if check == align:
            result['reverse'].append(r)
    return result


def miniBLASTwithMismatch(align, genome,d):
    result = {'forward': [], 'reverse': []}
    n = len(align)
    l = list(genome)
    rl = []
    for i in range(0, len(l) - n + 1):
        check = l[i:i + n]
        check = ''.join(check)
        if textdistance.hamming.distance(check,align) <= d:
            result['forward'].append(i)
    for i in range(0,len(l)):
        nu = l.pop()
        if nu == "A":
            nu = "T"
            rl.append(nu)
        elif nu == "T":
            nu = "A"
            rl.append(nu)
        elif nu =="C":
            nu = "G"
            rl.append(nu)
        else:
            nu = "C"
            rl.append(nu)
    for r in range(0,len(rl)-n+1):
        check = rl[r:r+n]
        check = ''.join(check)
        if check == align:
            result['reverse'].append(r)
    return result

print(miniBLAST("GTGAG", "GATATATGGAGTGAGTGCATATACTT"))
print(miniBLASTwithMismatch("GTGAG", "GATATATGGAGTGAGTGCATATACTT",2))
