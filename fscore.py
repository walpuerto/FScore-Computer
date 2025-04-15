def fscore(groups, α):
    # Solve N and k
    N = 0
    k = len(groups)
    n = []
    x = []
    x̄ = 0
    for group in groups:
        N += len(group)
        n.append(len(group))
        x.append(sum(group) / len(group))
        x̄ += sum(group)
    x̄ /= N

    # Caculate SSB
    SSB = 0
    for i in range(k):
        SSB += n[i] * ((x[i] - x̄) ** 2)

    SSW = 0
    for i in range(k):
        for j in groups[i]:
            SSW += (j - x[i]) ** 2

    F = (SSB / (k - 1)) / (SSW / (N - k))

    return F, N, k, n, x, x̄, SSB, SSW