import os
name=0
for i in os.listdir("/Users/banshee/Downloads/target"):
    if int(i)%2==0:
        os.rename("/Users/banshee/Downloads/target/"+i, "/Users/banshee/Downloads/target/"+"banshee"+str(name))
