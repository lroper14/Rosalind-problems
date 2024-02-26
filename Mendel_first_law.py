# Rosalind problem 7
# Mendel's First Law

def probability(k,m,n):

    total = k + m + n
    totalMinusOne = total - 1

    kk = (k / total) * ((k - 1) / totalMinusOne)
    km = (k / total) * (m / totalMinusOne)
    kn = (k / total) * (n / totalMinusOne)
    mk = (m / total) * (k / totalMinusOne)
    mm = (m / total) * ((m-1) / totalMinusOne) * 0.75
    mn = (m / total) * (n / totalMinusOne) * 0.5
    nk = (n / total) * (k / totalMinusOne)
    nm = (n / total) * (m / totalMinusOne) * 0.5

    final_prob = (kk + km + kn + mk + mm + mn + nk + nm)
    print(kk)
    print(final_prob)



probability(26,15,25)

