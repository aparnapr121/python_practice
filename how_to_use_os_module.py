#os.walk
import os
dir= os.getcwd()
for root,sub,files in os.walk(dir):
    print("curr_dir: ",root)
    for file in files:
        print(file)

print("trying bottom up approach")
#change the way the directory is traversed
for root,sub,files in os.walk(dir, topdown=False):
    print("curr_dir: ",root)
    for file in files:
        print(file)

#selectively recursing into subdirectories


#printing the path
print("printing the basename")
print(os.path.basename(os.path.join(dir,"myfile.txt")))


