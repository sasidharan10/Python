import time
from functools import lru_cache

# @lru_cache(maxsize=int(input("Enter the no of cache you want : ")))


@lru_cache(maxsize=5)  # maxsize is the no of function results you want to save
def working(n):
    time.sleep(n)
    return n


if __name__ == "__main__":
    print(f"Work Done in {working(3)} seconds")
    print(f"Work Done in {working(2)} seconds")
    print(f"Work Done in {working(1)} seconds")
    print(f"Work Done in {working(3)} seconds")
    print(f"Work Done in {working(2)} seconds")
    print(f"Work Done in {working(3)} seconds")


"""
- Using lru_cache, we can save some previous function calll results so that when
  the function is called again, it can fetch the data from previous results
  saves the time of operation.
"""
