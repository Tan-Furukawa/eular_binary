#%%
from datetime import datetime
import os
import numpy as np
import csv
import shutil
from typing import List, Dict, Any
import json

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

def delete_directory_contents(path: str, exclude_files: List[str]) -> None:
    for root, dirs, files in os.walk(path):
        # delete file
        for file in files:
            if exclude_files and file in exclude_files:
                continue
            file_path = os.path.join(root, file)
            os.remove(file_path)

        # delete directoryを削除
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            shutil.rmtree(dir_path)


def format_current_datetime() -> str:
    now = datetime.now()
    formatted_datetime = now.strftime("%Y_%m_%d_%H_%M_%S")
    return formatted_datetime

def to_str_from_dir_variables(variables_list: List[Dict[str, Any]]) -> str:
    """Returns a formatted string that combines variable names and values for a list of variables.

    Args:
        variables_list (list): List of variables (in dictionary format).

    Returns:
        str: Formatted string combining variable names and values.
    """
    result = ""
    for variables in variables_list:
        for var_name, value in variables.items():
            result += f"{var_name}: {value}\n"
    return result

def save_as_txt(input_text: str, filename: str) -> None:
    with open(filename, 'w') as file:
        file.write(input_text)

def add_data_to_json(data: Dict[str,Any],json_file: str) -> None:
    if os.path.exists(json_file):
          with open(json_file, 'r', encoding='utf-8') as file:
              json_data = json.load(file)
    else:
        json_data = []

    json_data.append(data)

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(json_data, file, indent=4)


# input_string = "# Heading\n\nThis is a paragraph."
# save_as_md(input_string, "output.md")
# # test
# data: np.ndarray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# file_path: str = "data_example.csv"
# save_as_csv(data, file_path)

#%%
