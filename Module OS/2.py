import os
name=0
os.mkdir("/Users/banshee/Downloads/target")
for i in range(1, 11):
    name+=1
    os.mkdir("/Users/banshee/Downloads/target/"+str(name))
