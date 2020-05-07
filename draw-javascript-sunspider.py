import matplotlib.pyplot as plt
sales = [1725.8,226.6,488.8]

plt.rcParams['font.sans-serif'] =['SimHei']
plt.rcParams['axes.unicode_minus'] = False

x = ['PX30 webkit2gtk','PC webkit2gtk','PC chromium']
plt.barh(range(3),sales, 0.4, color="#000088" , alpha = 0.8)
#plt.ylabel('sale')
plt.title('javascript sunspider    m/s(lower is better)',fontsize=16)
plt.yticks(range(3),['PX30 webkit2gtk','PC webkit2gtk','PC chromium'],fontsize=16)
plt.xlim([0,2000])

for x,y in enumerate(sales):
	plt.text(y+0.2,x+0.1,'  %s m/s ' %y,fontsize=16, va='center')

plt.show()
