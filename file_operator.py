#%%
import os
import numpy as np
import csv

def mkdir(name: str) -> None:
  current_directory = os.getcwd()
  folder_path = os.path.join(current_directory, name)

  if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print(f"{name}: made folder")
    return
  else:
    # do nothing
    return

def save_as_csv(data: np.ndarray, file_path: str) -> None:
    # if not isinstance(data, np.ndarray):
    #     print("data must be 2 dimensional ndarray")
    #     return

    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print(f"{file_path} :save as csv")

# # test
# data: np.ndarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# file_path: str = "data_example.csv"
# save_as_csv(data, file_path)

#%%
