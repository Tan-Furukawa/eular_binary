#%%
import unittest
import numpy as np
from scipy.linalg import toeplitz
from scipy.sparse import csr_matrix, eye, kron
from logging import info

def laplacian (nx: int, ny: int, dx: float, dy: float, eta: float) -> csr_matrix:
  nxny: int = ny * ny
  r: np.ndarray = np.zeros(nx, dtype=np.float64)
  r[0] = 2.0
  r[1] = -1.0

  t = toeplitz(r)
  t_sprs: csr_matrix = csr_matrix(t)
  e_sprs: csr_matrix = eye(nx)

  grad: csr_matrix = -(kron(t_sprs, e_sprs) + kron(e_sprs, t_sprs) * eta)

  for i in range(0, nx):
    for j in range(0, ny):
      ii: int = i * nx
      jj: int = ii + nx - 1
      grad[ii, jj] = 1.0 * eta
      grad[jj, ii] = 1.0 * eta
      kk = nxny - nx + i
      grad[i, kk] = 1.0
      grad[kk, i] = 1.0
  
  print(grad.toarray())
  return grad


class Test(unittest.TestCase):
  def test_laplacian(self) -> None:
    res = laplacian(3, 3, 1.0, 1.0, 2.0)
    expected = np.array(
      [[-6,  2,  2,  1,  0,  0,  1,  0,  0],
      [ 2, -6,  2,  0,  1,  0,  0,  1,  0],
      [ 2,  2, -6,  0,  0,  1,  0,  0,  1],
      [ 1,  0,  0, -6,  2,  2,  1,  0,  0],
      [ 0,  1,  0,  2, -6,  2,  0,  1,  0],
      [ 0,  0,  1,  2,  2, -6,  0,  0,  1],
      [ 1,  0,  0,  1,  0,  0, -6,  2,  2],
      [ 0,  1,  0,  0,  1,  0,  2, -6,  2],
      [ 0,  0,  1,  0,  0,  1,  2,  2, -6]]
    )
    self.assertTrue((expected == res.toarray()).all())

if __name__ == '__main__':
  unittest.main(argv=[''], exit=False)
# %%

