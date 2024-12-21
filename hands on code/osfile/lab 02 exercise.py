import os.path

#taking input of a path to create a file 
file_name = input ("enter file name : ")

file_path = input("enter file path to save it : ")

# writing to file

with open(file_path, 'w') as f:
 f.write('Create a new text file!')
   
#check if file created or not 

if(os.path.exists(file_path)):
    print(f'the file {file_name} created sucessfully !')
else:
    print('something went wrong !')


wnna_see = input("wanna see content inside a file ?")
L = ["this is the file content , this is created through python os system call"]
wnna_see.lower()
if(wnna_see == "yes"):
# writing to file
 file1 = open(file_path, 'w')
file1.writelines(L)
file1.close()

# Using readlines()
file1 = open(file_path, 'r')
contents = file1.read()
print(contents)
