def kthTerm(n, k):
    result = 0
    bin_k = bin(k)[2:]
    for i in range (len(bin_k)-1,-1,-1):
        result += (n**i)*int(bin_k[(len(bin_k)-1)-i])
    return result

print (kthTerm(3,4))