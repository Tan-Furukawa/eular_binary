# %%
from scipy.sparse import csr_matrix
import numpy as np
from typing import Tuple

def fix_zero_csr_matrix(input: csr_matrix, range: Tuple[float, float], to: float) -> csr_matrix:
  arr = input.toarray()
  arr[np.logical_and(range[0] < arr, arr < range[1])] = to
  return csr_matrix(arr)

# input = csr_matrix(np.array(
#     [[-6.0,  2,  2,  1,  0,  0,  1,  0,  0],
#     [ 2, -6,  2,  0,  1,  0,  0,  1,  0],
#     [ 2,  2, -6,  0,  0,  1,  0,  0,  1],
#     [ 1,  0,  0, -6,  2,  2,  1,  0,  0],
#     [ 0,  1,  0,  2, -6,  2,  0,  1,  0],
#     [ 0,  0,  1,  2,  2, -6,  0,  0,  1],
#     [ 1,  0,  0,  1,  0,  0, -6,  2,  2],
#     [ 0,  1,  0,  0,  1,  0,  2, -6,  2],
#     [ 0,  0,  1,  0,  0,  1,  2,  2, -6]]
# ))

# res = fix_zero_csr_matrix(input, (-0.001, 0.001), 0.1)
# print(res.toarray())

# class Test(unittest.TestCase):
#   def test_fix_zero_csr_matrix(self) -> None:
#     input = np.array(
#       [[-6,  2,  2,  1,  0,  0,  1,  0,  0],
#       [ 2, -6,  2,  0,  1,  0,  0,  1,  0],
#       [ 2,  2, -6,  0,  0,  1,  0,  0,  1],
#       [ 1,  0,  0, -6,  2,  2,  1,  0,  0],
#       [ 0,  1,  0,  2, -6,  2,  0,  1,  0],
#       [ 0,  0,  1,  2,  2, -6,  0,  0,  1],
#       [ 1,  0,  0,  1,  0,  0, -6,  2,  2],
#       [ 0,  1,  0,  0,  1,  0,  2, -6,  2],
#       [ 0,  0,  1,  0,  0,  1,  2,  2, -6]]
#     )
#     res = fix_zero_csr_matrix(csr_matrix(input), (-0.01, 0.01), 0.01)
#     print(res.toarray())

# if __name__ == '__main__':
#   unittest.main(argv=[''], exit=False)
# %%