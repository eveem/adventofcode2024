from collections import defaultdict

def sort_sum_diff(nums1, nums2):
    nums1.sort()
    nums2.sort()

    total = 0

    for a, b in zip(nums1, nums2):
        total += abs(a - b)
    
    return total

def read_input(filename):
    nums1, nums2 = [], []
    with open(filename, "r") as file:
        for line in file:
            a, b = map(int, line.split("   "))
            nums1.append(a)
            nums2.append(b)
    
    return nums1, nums2

def count_freq(nums):
    freq = defaultdict(int)
    for num in nums:
        freq[num] += 1
    return freq

def find_similarity_score(nums1, nums2):
    memo = defaultdict(int)
    freq = count_freq(nums2)
    total = 0

    for num in nums1:
        if num not in memo:
            temp = num * freq[num]
            memo[num] = temp
        
        total += memo[num]
    
    return total

def first_star():
    # filename = "small_input.txt"
    filename = "input.txt"
    nums1, nums2 = read_input(filename)
    print(f"first star result: {sort_sum_diff(nums1, nums2)}")

def second_star():
    # filename = "small_input.txt"
    filename = "input.txt"
    nums1, nums2 = read_input(filename)
    print(f"second star result: {find_similarity_score(nums1, nums2)}")

if __name__ == "__main__":
    first_star()
    second_star()