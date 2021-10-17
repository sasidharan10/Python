def div(a, b):
    try:
        print("Div :", (a/b))
    except Exception as e:
        print("Exception Occured :", e)
        return
    else:
        print("Operation done Successfully")
        return
    # return
    finally:
        print("This is Finally")
    print("this is normal print")


a = 5
b = 0

div(a, b)

"""

- Exception will execute only if any logical exception occurs
- else will execute if no exception occured and try block executed successfully.
- Finally will always execute, nomatter what happens in the try,excep block
- Even if we return from the program, finally will execute.
- finLally is usedd to close files, etc, which should be done for the
  proper working if the program

"""
