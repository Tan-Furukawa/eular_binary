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

nstep: int = 10000
nprint:int = 100
dtime: float = 0.01
ttime: float = 0.0

c0: float = 0.5
mobility: float = 1.0
grad_coef: float = 0.5

seed: int = 1
noise: float = 0.002

eta: float = 5.0

ncon = initial_concentration (nx, ny, c0, seed, noise)
con: csr_matrix = csr_matrix(ncon).transpose()
grad = laplacian(nx, ny, dx, dy, eta)

# make save environment
save_dir_name: str = f"{file_operator.format_current_datetime()}"
file_operator.mkdir(f"result/{save_dir_name}")

# make parameter_info
param_info:str = file_operator.to_str_from_dir_variables(
   [{'date': save_dir_name}, {'nx': nx}, {'ny': ny}, {'dx': dx}, {'dy': dy},
    {'nstep': nstep}, {'nprint': nprint}, {'dtime': dtime}, {'ttime': ttime},
    {'c0': c0}, {'mobility': mobility}, {'grad_coef': grad_coef},{'seed': seed}, {'noise': noise} ]
)
file_operator.save_as_txt(param_info, f"result/{save_dir_name}/info.txt")
file_operator.add_data_to_json({"file": save_dir_name, "done": False}, "result/done.json")

np.random.seed(seed + 1)

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
    file_operator.save_as_csv(res.reshape((nx,ny)), f"result/{save_dir_name}/res_{istep}.csv")
    print(f'done step {istep}')

# test


#%%