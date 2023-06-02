#%%
import file_operator

def delete_all () -> None:
  file_operator.delete_directory_contents("result/", ["README.md"])
  file_operator.delete_directory_contents("make_plot/png", ["README.md"])
  file_operator.delete_directory_contents("make_plot/gif", ["README.md"])


#%%
