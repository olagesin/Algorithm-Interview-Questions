#Problem: Create a fucntion that finds the sum pairs of two integers in a list


def pair_sum(list_of_integers, sum_total):
    if len(list_of_integers) < 2:
        return "list too short, must have more than one element"
    else:
        seen = set()
        output = set()
        for number in list_of_integers:
            target = sum_total - number
            if target not in seen:
                seen.add(number)
            else:
                output.add(((min(number, target)), max(number, target)))

        print("\n".join(map(str, list(output))))


pair_sum([1, 3, 2, 2], 4)
