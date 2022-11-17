# Write your solution for algorithm 5 below

def find_pair(lst, target):
    sorted_lst = sorted(lst)
    left = 0
    right = len(sorted_lst) -1

    while left < right:
        if sorted_lst[left] + sorted_lst[right] == target:
            return(f"Pair that matches target: {sorted_lst[left]}, {sorted_lst[right]}")

        if sorted_lst[left] + sorted_lst[right] < target:
            left += 1
        else:
            right -= 1

    return "Pair not found"

if __name__ == '__main__':
    test_list = [2, 3, 1, 4, 3, 4, 5, 3]
    target = 6
    print(find_pair(test_list, target))