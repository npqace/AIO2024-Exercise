def max_kernel(num_list, k):
    """
    This function efficiently finds the maximum value in every window of size k
    within the given list.
    Args:
        num_list: A list of numerical values.
        k: The window size to use for finding maximums.
    Returns:
        A new list containing the maximum value found in each window of size k.
    """

    result = []
    for i in range(len(num_list) - k + 1):
        # Find the maximum in the current window
        result.append(max(num_list[i:i+k]))
    return result


if __name__ == '__main__':
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    print(max_kernel(num_list, 3))