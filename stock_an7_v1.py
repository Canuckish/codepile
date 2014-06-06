#1dOHLC the conversions here only work if starting from YYYYMMDD
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import matplotlib.dates as mdates
import numpy as np
import time
import datetime
import matplotlib
matplotlib.rcParams.update({'font.size': 9})

eachStock = 'TSLA','AAPL'

def graphData(stock):
	try:
		stockFile = stock+'.txt'

		date, closep, highp, lowp, openp, volume = np.loadtxt(stockFile,delimiter=',',unpack=True,
			converters={ 0: mdates.strpdate2num('%Y%m%d')})

		fig = plt.figure()
		# ax1 = plt.subplot(2,1,1) #spot 1 in a 2x1 pair array of graphs
		ax1 = plt.subplot2grid((5,4), (0,0), rowspan=4, colspan=4)
		ax1.plot(date, openp)
		ax1.plot(date, highp)
		ax1.plot(date, lowp)
		ax1.plot(date, closep)
		plt.ylabel('Stock price')
		ax1.grid(True)


		# ax2 = plt.subplot(2,1,2, sharex=ax1) #spot 2 in a 2x1 pair array of graphs
		ax2 = plt.subplot2grid((5,4), (4,0), sharex = ax1, rowspan = 1, colspan = 4)
		ax2.bar(date,volume)
		ax2.axes.yaxis.set_ticklabels([]) #empty array to get rid of the axis labels on y
		plt.ylabel('Volume')
		ax2.grid(True)

		ax1.xaxis.set_major_locator(mticker.MaxNLocator(10)) 
		ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

		for label in ax1.xaxis.get_ticklabels():
			label.set_rotation(90)

		for label in ax2.xaxis.get_ticklabels():
			label.set_rotation(45)

		plt.subplots_adjust(left=.1, bottom = .19, right = .93, top = .95, wspace =.2, hspace = .07)

		plt.xlabel('Date')

		plt.suptitle(stock+' Stock Price')

		# ax1.axes.yaxis.set_visible(False)
		# ax1.axes.xaxis.set_ticklabels([])

		plt.setp(ax1.get_xticklabels(), visible = False) #get rid of xlabels on top, but not bottom, graph

		plt.subplots_adjust(left =.09, bottom = .18, right = .94, top = .94, wspace = .2, hspace = 0)
		plt.show()
		fig.savefig('example.png')    

	except Exception, e:
		print 'failed main loop', str(e)
	
for stock in eachStock:
	graphData(stock)
	time.sleep(1)

