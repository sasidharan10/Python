nums = [1, 2, 3, 4, 5]
print("nums :", nums)
print("nums[1] :", nums[1])
print("nums[2:] :", nums[2:])
print("nums[-1] :", nums[-1])
names = ['sasi', 'kane', 'smith']
print("names :", names)
mixed = [1, 'bob', 9.5]
print("mixed :", mixed)
twoArray = [nums, names]
print("2D list :", twoArray)

# add 1 element in last
nums.append(6)
print("nums.append(6) :", nums)

# add 1 element in specified location
nums.insert(2, 2.5)
print("nums.insert(2,2.5) :", nums)

# add multiple element in last
nums.extend([7, 7.5, 8, 9])
print("nums.extend([7,7.5,8,9]) :", nums)

# remove 1 element using value
nums.remove(2.5)

# remove 1 element from last
nums.pop()

# remove 1 element using index
nums.pop(7)
print("nums(deleted) :", nums)

# remove multiple element using slicing
del nums[5:]
nums.append(0)
print("nums.append(0) :", nums)

# sorting
nums.sort()
print("nums.sort() :", nums)

print("sum : ", sum(nums))
print("max : ", max(nums))
print("min : ", min(nums))
print("count(5) : ", nums.count(5))
print("index(5) : ", nums.index(5))
nums.clear()
print("nums.clear() : ", nums)
