def parseInput(string):
    try:
        return [float(i) for i in string.split(",")]
    except:
        return []

def main():
    # Take User Input as elements of groups (A, B, C, ...)
    print("Welcome to the F-score Computer!")
    groups = []
    for i in range(0, 4):
        ugroup = []
        while parseInput(ugroup) == []:
            ugroup = input(f"Group {chr(i + 65)} = ")
            print("\033[F", end="\r")
            if ugroup == "": break
        if ugroup != "": groups.append(parseInput(ugroup))
        print()
    print()

    # Take significance level
    α = input("α = ")
    print()

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
    print(f"N = {N}")
    print(f"k = {k}")
    print(f"dfn = {k-1}")
    print(f"dfd = {N-k}")
    print(f"x̄ = {x̄:.2f}")

    # Caculate SSB
    SSB = 0
    for i in range(k):
        SSB += n[i] * ((x[i] - x̄) ** 2)
    print(f"SSB = {SSB:.2f}")

    SSW = 0
    for i in range(k):
        for j in groups[i]:
            SSW += (j - x[i]) ** 2
    print(f"SSW = {SSW:.2f}")

    F = (SSB / (k - 1)) / (SSW / (N - k))
    print(f"F = {F:.2f}")
    print()

if __name__ == "__main__":
    main()