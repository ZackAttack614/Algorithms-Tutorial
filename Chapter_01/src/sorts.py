def selection_sort(C):
  S = []

  while any(C):
    min_index = C.index(min(C))
    S.append(C[min_index])
    C.pop(min_index)

  return S

def bitmap_sort(C, max_val):
  B = [0 for i in range(max_val + 1)]

  for val in C:
    B[val] = 1

  S = []

  for i in range(len(B)):
    if B[i] == 1:
      S.append(i)

  return S