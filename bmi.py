wight = input('請輸入體重:')
wight = float(wight)
tall = input('請輸入身高:')
tall = float(tall)
high = tall / 100
bmi = wight / high / high
print('你的身高:',high,'你的體重:',wight,'你的BMI:',bmi)