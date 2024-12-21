import os

path = 'practice projects.txt'
if os.path.exists('F:\BLOCKCHAIN\Quarter 01\Type script\practice projects.txt') :
   os.remove('F:\BLOCKCHAIN\Quarter 01\Type script\practice projects.txt')
   print(f'file {path} removed successfully')
else : 
    print(f'file {path} not found !')
