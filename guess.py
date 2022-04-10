import random
r = random.randint(1,100)
while True:
	num = input('請輸入數字')
	num = int(num)
	if num == r :
		print('你猜中了')
		break 
	elif num > r :
		print('答案要在小點')
	elif num < r :
		print('答案要較大點')
