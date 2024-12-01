def sort_sum_diff(nums1, nums2):
    pass

def read_input(filename):
    nums1, nums2 = [], []
    with open(filename, "r") as file:
        for line in file:
            a, b = map(int, line.split("   "))
            nums1.append(a)
            nums2.append(b)
    
    return nums1, nums2