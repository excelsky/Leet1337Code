import collections

def countTriplets(arr, r):
    # stores number of tuples with two elements that can be formed if we find the key
    potential_2_tuples_dict = collections.defaultdict(int) 
    # stores number of tuples with three elements that can be formed if we find the key
    potential_3_tuples_dict = collections.defaultdict(int)
    count = 0
    for i in arr:
        # i completes the three tuples given we have already found i/(r^2) and i/r
        count += potential_3_tuples_dict[i]
        # For any element of array we can form three element tuples if we find i*r given i / r is already found. Also i forms the second element.
        potential_3_tuples_dict[i*r] += potential_2_tuples_dict[i]
        # For any element of array we can form two element tuples if we find i*r. Also i forms the first element.
        potential_2_tuples_dict[i*r] += 1
    return count



def countTriplets(arr, r):
    r2 = {}
    r3 = {}
    count = 0
    for k in arr:
        # if k in r3 indicates the triplet already completed,
        # the count need be incremented
        if k in r3:
            count += r3[k]
        # if k in r2, it is the secound number of the triplet,
        # your successor (3rd element k*r) need be added or incremented in the r3
        # because is a potencial triplet 
        if k in r2:
            if k*r in r3:
                r3[k*r] += r2[k]
            else:
                r3[k*r] = r2[k]
        # if k is the first element of the triplet,
        # your seccessor (2nd element k*r) need be added or incremented in the r2 
        # because is a potencial triplet
        if k*r in r2:
            r2[k*r] += 1
        else:
            r2[k*r] = 1
    return count

arr = [1,3,9,9,27,81]
r = 3

countTriplets(arr,r)