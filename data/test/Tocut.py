import os

def Tocut(path1,path2):

    files1 = os.listdir(path1)
    files2 = os.listdir(path2)		
    for file in files1:
        #read file in files    
        file1_path = os.path.join(path1, file)

        #detect if file in files have corresonding file in files2
        file1name = file.partition('.')
        file1b = file1name[0] + '_mask.png'
        flag = 0
        for file2 in files2:
            if file2 == file1b:
                flag = 1
        if flag == 0:
            patht = os.path.join(path1, file)
            os.unlink(patht)                
            print(file)
        flag = 0


Tocut(r'../imgs',r'../masks')
