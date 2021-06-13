temp = input('請輸入攝氏溫度:')
temp = float(temp)
if temp >= 28:
	print('好熱喔!開個冷氣吧~')
elif temp <= 16:
	print('好冷~暖氣呢!!') 
else:
	print('溫度適中')