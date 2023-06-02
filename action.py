#%%
import file_operator

def clear_tmp_data () -> None:
  file_operator.delete_directory_contents("result/", ["README.md"])
  file_operator.delete_directory_contents("make_plot/png", ["README.md"])

clear_tmp_data()

#%%
