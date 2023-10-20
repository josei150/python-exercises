def sum_of_multiples(limit, multiples):
    multi = []
    for multiplo in multiples:
        for counter in range(limit):
            if counter * multiplo >= limit:
                break
            multi.append(counter * multiplo)
    
    print(multi)

    return sum(set(multi))

if __name__ == "__main__":
    print(sum_of_multiples(10, [3, 5])) #23