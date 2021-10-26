import os

# print(dir(os))  # prints all functions
print("Current Directory : ", os.getcwd())
# os.chdir("E:\Programming\Python\python_gui")
print("List Directory : ", os.listdir("ex5"))
# os.mkdir("lol")   # makes a new folder
# os.makedirs("lol\lmao\Rolf")   # makes multiple folders
# os.rename("goodmorning.py","1_hello.py",)
# os.rmdir("lol")  # removes empty directory
# os.removedirs("lol")  # removes all directory, including all inside
# print("Env variable : ",os.environ.get('path'))  # displays all evn var
# print(os.path.join("c://","\python"))  # joins 2 paths
# tells if a path exists or not
print("Path exists ? : ", os.path.exists("c:\\"))
print("Is Dir ? : ", os.path.isdir("E:\Programming\Python"))
print("Is file ? : ", os.path.isfile("E:\Programming\Python"))
