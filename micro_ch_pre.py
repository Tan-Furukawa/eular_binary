#%%
import numpy as np
import unittest

def micro_ch_pre (nx: int, ny: int, c0: float, seed: int, noise: float) -> np.ndarray:
  np.random.seed(seed) 
  nxny: int = nx * ny
  c0_vec = np.zeros(nxny) + c0
  res = c0_vec + (0.5 - np.random.rand(nxny)) * noise
  return res

class Test(unittest.TestCase):

  def test_micro_ch_pre(self) -> None:
    result = micro_ch_pre(10, 10, 0.4, 1, 0.02)
    print(result)
    # self.assertEqual(result, c0)

# テストを実行する
if __name__ == '__main__':
  unittest.main(argv=[''], exit=False)


# %%
