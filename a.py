def solve():
    n = int(input())
    pieces = input().split()

    from itertools import permutations

    all_possible_numbers = []
    for p in permutations(pieces):
        num_str = "".join(p)
        try:
            num = int(num_str)
            if 100 <= num <= 1999:
                all_possible_numbers.append(num)
        except ValueError:
            pass

    if not all_possible_numbers:
        print("UNKNOWN")
        return

    centuries = set()
    for num in all_possible_numbers:
        centuries.add(num // 100)

    if len(centuries) == 1:
        print(list(centuries)[0])
    else:
        print("UNKNOWN")

solve()

