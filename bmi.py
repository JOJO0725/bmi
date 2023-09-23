wight = input('請輸入體重:')
wight = float(wight)
tall = input('請輸入身高:')
tall = float(tall)
high = tall / 100
bmi = wight / high / high
print('你的身高:',high,'你的體重:',wight,'你的BMI:',bmi)
if bmi < 18.5:
    print('你的體重過輕')
elif bmi >= 18.5 and bmi< 24:
    print('你的體態良好!')
elif bmi >= 24 and bmi < 27:
    print('你過重了!!')
elif bmi >=27 and bmi < 30:
    print('你有輕度肥胖!!!')
elif bmi >= 30 and bmi < 35:
    print('你有中度肥胖!!!!')
else:
    print('你重度肥胖!太肥了!!趕快減肥!!!') 