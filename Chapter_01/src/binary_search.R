binary_search = function(array, target) {
  left_bound = 1
  right_bound = length(array)

  while(left_bound < right_bound) {
    check_index = as.integer((left_bound + right_bound) / 2)

    if(array[check_index] == target) {
      return(TRUE) }
    else if(array[check_index] > target) {
      right_bound = check_index }
    else if(left_bound != check_index) {
      left_bound = check_index }
    else {
      return(FALSE) } }

  if(array[left_bound] == target) {
    return(TRUE) }
  else {
    return(FALSE) } }
