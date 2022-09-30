1)
print(1==1.0)
## script printed 'True' so these equal eachother. 
print("1"=="1.0")
## scripted printed 'False', so number presented aren't equal to eachother. 
## Adding "" makes python recgonizes the numbers as its own string and 
## not identical values.

2)
print(5 == (3+2))
## script printed True. These values are the same.

3)
print(1 == 1.0) and ("1" == "1.0") and (5 == (3+2))
## scripts prints 'True'.
print(1 == 1.0) or ("1" == "1.0") or (5 == (3+2))
## script prints 'True'.
print(1 == 1.0) and not ("1" == "1.0") and not (5 == (3+2))
## script prints 'True'.
