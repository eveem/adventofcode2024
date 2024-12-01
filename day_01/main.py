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

def main():
    # filename = "small_input.txt"
    filename = "input.txt"
    nums1, nums2 = read_input(filename)
    print(sort_sum_diff(nums1, nums2))

if __name__ == "__main__":
    main()