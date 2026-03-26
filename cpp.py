from itertools import permutations

def solve_cryptarithm(puzzle):
   
    puzzle = puzzle.replace(" ", "")
    
    left, right = puzzle.split("=")
    words = left.split("+")
    words.append(right)

    letters = set("".join(words))
    
    if len(letters) > 10:
        print("Too many unique letters (max 10 allowed).")
        return

    letters = list(letters)
    digits = range(10)

    first_letters = set(word[0] for word in words)

    for perm in permutations(digits, len(letters)):
        assign = dict(zip(letters, perm))

        # small improvement: use all() instead of any()
        if not all(assign[ch] != 0 for ch in first_letters):
            continue

        nums = []
        for word in words:
            # small improvement: store string once
            num_str = "".join(str(assign[ch]) for ch in word)
            nums.append(int(num_str))

        if sum(nums[:-1]) == nums[-1]:
            print("Solution Found!")
            for k in sorted(assign):
                print(f"{k} = {assign[k]}")
            print("\nVerification:")
            print(" + ".join(str(n) for n in nums[:-1]), "=", nums[-1])
            return

    print("No solution found.")


if __name__ == "__main__":
    puzzle = input("Enter puzzle (e.g., SEND + MORE = MONEY): ")
    solve_cryptarithm(puzzle)