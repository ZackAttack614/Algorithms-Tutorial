def binary_search(array, target):
  left_bound = 0
  right_bound = len(array) - 1

  while left_bound < right_bound:
    check_index = (left_bound + right_bound) // 2
    
    if array[check_index] == target:
      return True
    elif array[check_index] > target:
      right_bound = check_index
    elif left_bound != check_index:
      left_bound = check_index
    else:
      return False

  if array[left_bound] == target:
    return True
  else:
    return False
