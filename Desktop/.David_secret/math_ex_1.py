lst1 = [11, 21, 18, 12, 9, 67]
lst2 = [32, 54, 25, 86, 72]

print('Hi, please answer this 5 math exercises')

i=0
length1 = len(lst1)
length2 = len(lst2)
correct = 0
incorrect = 0

while i< min(length1, length2):
	print('How much is', lst1[i], '+', lst2[i], '= ?')
	answer =  int(input())
	if answer == (lst1[i] + lst2[i]):
		print('Well done!')
		correct += 1
	else:
		print('Well no...')
		incorrect += 1
	i += 1

print('Thank you!')
print('You have got',correct,'correct answers')
print('You have got',incorrect,'incorrect answers')
print('Yoyr mark is',(correct/(correct+incorrect)*100),'%')

















