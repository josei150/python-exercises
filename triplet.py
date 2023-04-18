def triplets_with_sum(number):
    half_number = number//2
    triplets = []

    for i in range(1, half_number):
        for j in range(i + 1, half_number):
            for k in range(j + 1, half_number):
                if i + j + k == number and i**2 + j**2 == k**2:
                    triplets.append([i, j, k])
                    break
    return triplets



def triplets_two(number):
    half_number = number//2
    triplets = []
    
    
    for i in range(1, half_number//2 + 1):
        for j in range(half_number//2 + 1, half_number):
            k_2 = i**2 + j**2
            k = int(k_2 ** (1/2))
            if i + j + k == number and i**2 + j**2 == k**2:
                triplets.append([i, j, k])
                break
    return triplets


if __name__ == "__main__":
    #print(triplets_with_sum(30000))
    print(triplets_two(840))