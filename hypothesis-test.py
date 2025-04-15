import fscore
import precomputed

def parseInput(string):
    try:
        return [float(i) for i in string.split(",")]
    except:
        return []

def main():
    # Take User Input as elements of groups (A, B, C, ...)
    print("Welcome to the ANOVA Computer!")
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

    if groups == []:   
        print("No groups were entered. Exiting...")
        return

    # Take significance level
    α = input("α = ")
    if α != "0.05" and α != "0.01":
        α = 0.01
        print(f"\033[Fα = 0.01")
    else:
        α = float(α)
    print()

    # Step 1: State the Hypothesis
    print(f"(1) H0: All groups have the same mean.")
    print(f"    H1: At least one group has a different mean.")

    # Step 2: State the significance level
    print(f"(2) α = {α}")
    
    # Step 3: Calculate the test statistic
    fscoreResults = fscore.fscore(groups)
    print(f"(3) F = {fscoreResults[0]}")

    # Step 4: Find the critical value
    s2df = f"{fscoreResults[1]},{fscoreResults[2]}"
    CV = precomputed.getCV(s2df, α)
    print(f"(4) Fα = {CV}")
    if fscoreResults[0] < CV: print(f"    F < Fα, fail to reject H0")
    else: print(f"    F > Fα, reject H0")
    
    # Step 5: Conclusion
    if fscoreResults[0] < CV:
        print(f"(5) Conclusion: All groups have the same mean.")
    else:
        print(f"(5) Conclusion: At least one group has a different mean.")

    # Ask for another test
    again = input("Do you want to do another test? (y/n) ")
    if again.lower() == "y":
        print("\033[F\033[K", end="\r")
        main()
    else:
        print("thank you for using this calculator! Goodbye! =D")

if __name__ == "__main__":
    main()