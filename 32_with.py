with open("demo.txt") as f:
    print(f.readlines())
    print(f.readline())

# by using 'with' we dont need to close the file as the compiler will do the job for us
