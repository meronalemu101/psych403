1)
list100 = (range(101))
print(list(list100))
#answer shows a list of numbers from 0 to 100.
2)
print(list(list100[:10]))
#*if we include 0 as a number* answer given:[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
3)
print(list(list100[1::2])[::-1])
#answer shows all numbers backward from 99-1
4)print(list(list100[::-1])[97:])
#*if we include 0 as a number* answer given: [3, 2, 1, 0]
5)
list100 = (range(101))
print(list(list100))
print(list(list100[39:44] and ['39', '40', '41', '42', '43']))
#could not create script with understand if values were identical 
#to their positon on list. Will ask this question during office hours please.
