# %%
import numpy as np
import unittest
from scipy.sparse import csr_matrix

def free_energy_ch_v2 (con: csr_matrix, a: float) -> csr_matrix:
  dfdcon = con.copy()

  dfdcon.data = a * (2.0 * con.data * (1.0 - con.data) ** 2 \
    - 2.0 * con.data ** 2 * (1.0 - con.data))
  return dfdcon

class Test(unittest.TestCase):

  def test_free_energy_ch_v2 (self) -> None:
    con = csr_matrix(np.array([0.3, 0, 1, 0.5]))
    result = free_energy_ch_v2(con, 1.0).toarray()
    expected = np.array([0.168, 0, 0, 0])
    print(result)
    self.assertTrue((abs(result - expected) < 1e-5).all())

if __name__ == '__main__':
  unittest.main(argv=[''], exit=False)
# %%
