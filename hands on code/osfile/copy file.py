import shutil

original = r'F:\BLOCKCHAIN\Quarter 01\Javascript\practice projects.txt'
target = r'F:\BLOCKCHAIN\Quarter 01\Type script\practice projects.txt'
path = 'practice projects.txt'
if shutil.copyfile(original, target) :
    print(f'file {path} copied successfully')
