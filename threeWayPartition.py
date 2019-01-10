import random


def test_model(nums=[], pivot=0):
    """
    :param nums: on default, we do not provide test data, it's an random generated array.
    If you like, you can provide your own
    """
    if not nums:
        for i in range(10):
            nums.append(random.randint(1, 100))
        pivot = nums[0]
    print("Input:", nums)
    print("Pivot:", pivot)
    print("Result:", three_way_partition(nums, pivot))


def swap(a, b, nums):
    temp = nums[a]
    nums[a] = nums[b]
    nums[b] = temp


def three_way_partition(nums, pivot):
    """
    Description:
        Give an unsorted array, and a pivot,
        split the split to three part:
            the middle part includes the num which equal to the pivot
            the left part includes the num which smaller than pivot
            the right part includes the num which bigger than pivot
    e.g. input:  [44, 17, 42, 68, 44, 28, 75, 68, 96, 19, 57]
         output: [17, 42, 19, 28, |44, 44| 68, 96, 75, 57, 68]
    This algorithm is very useful in many places.
    e.g., find the median of number arrays,
          find the kth largest number of arrays.
    IDEA: use two pointers,
          the indexes before start pointer are smaller than pivot
          the indexes after end pointer are bigger than pivot
          we scan the array from head to end pointer.
              when current scanned value is smaller than pivot,
                swap it to start pointer
                start pointer++
                Go next position
              when current scanned value is bigger than pivot,
                swap it to start pointer;
                end pointer--
                maybe you swap a smaller one back, "so current position is not changed"
              when current scanned value is equal to pivot,
                skip it,
                Go next position

    :param nums: you know it, skip!
    :param pivot: the split pivot
    :return:
    """

    sp, ep = 0, len(nums) - 1
    i = 0
    while i <= ep:
        if nums[i] > pivot:
            swap(i, ep, nums)
            ep -= 1
        elif nums[i] < pivot:
            swap(i, sp, nums)
            sp += 1
            i += 1
        else:
            i += 1
    return nums


if __name__ == '__main__':
    # test_model([1,53,6,765,3,5456,564,64],53)
    test_model()


