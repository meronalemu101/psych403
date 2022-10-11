1) #"sub_str" is used to get the answer 'sub2' because using the "sub_int" 
#variable will just give the answer 'subsub' because the integer is
#adding the previous variable by 2. 

2) print(sub_code + " " + sub_str)
#answer is 'sub 2'
print(sub_code + " " + sub_str + sub_str + sub_str)
#answer is 'sub 222'
print((sub_code + sub_str)*3)
#answer is sub2sub2sub2
print(sub_code + sub_code + sub_code + sub_str + sub_str + sub_str)
#answer is subsubsub222
