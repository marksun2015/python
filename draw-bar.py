import matplotlib.pyplot as plt
sales = [7125,12753,13143,8635]

plt.rcParams['font.sans-serif'] =['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = ['Apple','banana','nop','nop']
plt.barh(range(4), sales, 0.4,color='r', alpha = 0.8)
plt.ylabel('sale')
plt.title('fruit 2018 sale')
plt.yticks(range(4),['apple','banana','nop','nop'])
plt.xlim([5000,15000])

for x,y in enumerate(sales):
    plt.text(y+0.2,x,'%s' %y,va='center')

plt.show()
