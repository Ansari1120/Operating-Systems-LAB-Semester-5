import os.path

path = "F:\\bootcamp.txt"
path_to_file = 'bootcamp.txt'
if (os.path.exists(path)) :
    print(f'The File {path_to_file} exist !')
else :
    print(f'The file {path_to_file} does not exist !')

