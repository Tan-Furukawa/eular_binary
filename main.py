#%%
from initial_state import initial_concentration
from laplacian import laplacian
from free_energy import get_free_energy
from scipy.sparse import csr_matrix
import file_operator
import numpy as np

nx: int = 64
ny: int = 64
nxny: int = nx * ny
dx: float = 1.0
dy: float = 1.0

nstep: int = 40000
nprint:int = 100
dtime: float = 0.01
ttime: float = 0.0

c0: float = 0.50
mobility: float = 1.0
grad_coef: float = 0.5

seed: int = 1
noise: float = 0.02

ncon = initial_concentration (nx, ny, c0, seed, noise)
con: csr_matrix = csr_matrix(ncon).transpose()
grad = laplacian(nx, ny, dx, dy)

file_operator.mkdir("result")
for istep in range(0, nstep):
  ttime = ttime + dtime
  dfdconf = get_free_energy(con, 1.0)

  lap_con = grad.dot(con)
  lap_con2 = lap_con.multiply(grad_coef)
  lap_con2.data = dfdconf.data - lap_con2.data
  lap_con2 = grad.dot(lap_con2)

  con = csr_matrix(con.data + dtime * mobility * lap_con2.data).transpose()

  # add random noise for each step
  con.data = con.data + (0.5 - np.random.rand(nxny)) * noise

  if (istep % nprint == 0) or (istep == 1):
    res = con.toarray()
    file_operator.save_as_csv(res.reshape((nx,ny)), f"result/res_{istep}.csv")
    print(f'done step {istep}')

# test


#%%