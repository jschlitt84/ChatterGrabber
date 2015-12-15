import operator
import urllib
import datetime

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np
import os

from random import shuffle, sample
from datetime import timedelta
from dateutil import parser
from matplotlib.dates import DateFormatter, date2num, num2date
from copy import deepcopy
from time import sleep
from geopy.distance import vincenty
from math import pow

from mpl_toolkits.basemap import Basemap
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.animation as animation

import warnings
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)

#from IPython.display import HTML


weekList = ['zero','Mon','Tue','Wed','Thu','Fri','Sat','Sun','null']
weekNum = [-1,0,1,2,3,4,5,6,7]

#Wordcloud dependencies
import unicodedata

from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from wordcloud import WordCloud


blockKeys = ['$!','$?','$...','#yesallwomen']
stopWords = stopwords.words('english')
lmtzr = WordNetLemmatizer()


#Timeline dependencies
import subprocess

def cleanSave(content,directory,mode,**kwargs):
    try:
        os.remove(directory)
    except OSError:
        pass
    try:
        if mode == 'fig':
            content.savefig(directory,**kwargs)
        elif mode == 'anim':
            content.save(directory,**kwargs)
        content.close()
    except Exception as e:
        print "Figure",directory,'save failed, error:', e
        directory = 'null'
    del content
    return directory

def printSample(data,title,length):
    characters = 100
    indexed = list(data.index)
    shuffle(indexed)
    for pos in indexed[:length]:
        print '\t',data.ix[pos]['text'][:characters]+(len(data.ix[pos]['text'])>characters)*'...'
    print '\n'
    
    
def getGeoSub(dataIn,box,prefix):
    dataOut = deepcopy(dataIn)
    if prefix != '':
        dataOut['name'] = prefix + ' ' + dataOut['name']

    data = dataOut['data']
    data = data[(data.lat > box['lat1']) & (data.lat < box['lat2']) & (data.lon > box['lon1']) & (data.lon < box['lon2'])]
    dataOut['data'] = data
    return dataOut
    
    
def getCatSub(dataIn,cat,categories, catCol = 'NLPCat'):
    dataOut = deepcopy(dataIn)
    if type(categories) is dict:
        dataOut['name'] = categories[cat] + ' ' + dataOut['name']
    elif categories == '' or categories == 'null':
        dataOut['name'] = dataOut['name']
    else:
        dataOut['name'] = str(categories) + ' ' + dataOut['name']
    data = dataOut['data']
    data = data[data[catCol] == cat]
    dataOut['data'] = data
    return dataOut
    
    
def getLocSub(dataIn,locNames,exclusions,prefix):
    return getFieldSub(dataIn,locNames,exclusions,prefix,'place')
    """dataOut = deepcopy(dataIn)
    dataOut['name'] = prefix + ' ' + dataOut['name']
    data = dataOut['data']
    data = data[data.apply(lambda x: sum([1 for place in locNames if place.lower() in str(x['place']).lower()]) > 0, axis=1)]
    if exclusions != []:
        data = data[data.apply(lambda x: sum([1 for place in exclusions if place.lower() in x['place'].lower()]) == 0, axis=1)]
    dataOut['data'] = data
    return dataOut"""
    
    
def getFieldSub(dataIn,sought,exclusions,prefix,field):
    dataOut = deepcopy(dataIn)
    dataOut['name'] = prefix + ' ' + dataOut['name']
    data = dataOut['data']
    data = data[data.apply(lambda x: sum([1 for place in sought if str(place).lower() in str(x[str(field)]).lower()]) > 0, axis=1)]
    if exclusions != [] and len(data) > 0:
        data = data[data.apply(lambda x: sum([1 for place in exclusions if str(place).lower() in str(x[str(field)]).lower()]) == 0, axis=1)]
    dataOut['data'] = data
    return dataOut
    
def getFieldItem(dataIn,sought,prefix,field):
    dataOut = deepcopy(dataIn)
    #sought = [str(item) for item in sought]
    dataOut['name'] = prefix + ' ' + dataOut['name']
    data = dataOut['data']
    data = data[data[field].isin(sought)]
    dataOut['data'] = data
    return dataOut
    
    
def trimRange(start,end,collected,mode='text'):
    if mode == 'text':
        start = parser.parse(start)
        end = parser.parse(end)
    if start > end:
        start,end = end,start
    holder = deepcopy(collected)
    #start = start.replace(tzinfo=None)
    #end = end.replace(tzinfo=None)
    holder['data']['timeStamp'] = [parser.parse(point).replace(tzinfo=None) for point in holder['data']['created_at']]
    data = holder['data'][(holder['data']['timeStamp'] >= start) & (holder['data']['timeStamp'] <= end)]
    holder['data'] = data
    return holder
    
    
def getTime(time):
    hour =  int(time.split(':')[0])
    minute = int(time.split(':')[1])
    return hour + minute/100.


def truncData(dataIn,mode):
    data = deepcopy(dataIn)
    firstDay = data.iloc[0]['day']
    firstTime = getTime(data.iloc[0]['time'])
    limit = len(data)
    pos = limit-1
    if mode == "hour":
        while getTime(data.iloc[pos]['time']) > firstTime or getTime(data.iloc[pos-1]['time']) < firstTime and pos > 0 :
            pos -= 1
    elif mode == "day":
        while getTime(data.iloc[pos]['time']) > firstTime or getTime(data.iloc[pos-1]['time']) < firstTime or firstDay !=data.iloc[pos-1]['day'] and pos > 0:
                pos -= 1
    if pos == -1:
        pos = limit
            
                
    dayDiff = parser.parse(data.iloc[pos]['created_at']).timetuple().tm_yday - parser.parse(data.iloc[0]['created_at']).timetuple().tm_yday
    timeLim = 7*(mode=='day')+1*(mode=='hour')
    if dayDiff < timeLim:
        print "Cannot truncate to %s*n complete days, using full data range instead" % timeLim
        pos =  limit
        
    return data[:pos]
    

def chartHourly(dataIn, timeShift,show=True):
    plt.gca()
    data = truncData(dataIn['data'],"hour")
    dates = data['created_at']
    dates = [parser.parse(date) for date in dates]
    hour_list = [(t+timedelta(hours=timeShift)).hour for t in dates]
    numbers=[x for x in xrange(0,25)]
    labels=map(lambda x: str(x), numbers)
    plt.xticks(numbers, labels)
    plt.title(dataIn['name'],size = 12)
    plt.xlabel("Hour (GMT %s)" % timeShift)
    plt.ylabel("Tweets")
    plt.hist(hour_list,bins=numbers, alpha=0.5, align='mid')
    if show:
        plt.show()
    return plt
    
    
def groupHourly(dataGroup, names, title, timeShift, stacked=True, show=True ,truncate=True):
    plt.gca()
    toPlot = []
    namesShown = []
    for pos in range(len(dataGroup)):
        if len(dataGroup[pos]['data']) > 0:
            if truncate:
                data = truncData(dataGroup[pos]['data'],"hour")
            else:
                data = dataGroup[pos]['data']
            dates = data['created_at']
            dates = [parser.parse(date) for date in dates]
            hour_list = [(t+timedelta(hours=timeShift)).hour for t in dates]
            toPlot.append(hour_list)
            namesShown.append(names[pos])
            numbers=[x for x in xrange(0,25)]
            labels=map(lambda x: str(x), numbers)
            plt.xticks(numbers, labels)
            plt.xlabel("Hour (GMT %s)" % timeShift)
            plt.ylabel("Tweets")
    if len(namesShown) != 0:
        plt.title(title,size = 12)
        plt.hist(toPlot,bins=numbers,stacked=stacked, alpha=0.5, label=names, align='mid')
        plt.legend([str(entry) for entry in namesShown],loc="best")
        if show:
            plt.show()
    return plt
    
    
    
def chartDaily(dataIn, timeShift, show=True):
    plt.gca()
    data = truncData(dataIn['data'],"day")
    dates = data['created_at']
    dates = [parser.parse(date) for date in dates]
    dayList = [(t+timedelta(hours=timeShift)).weekday() for t in dates]
    plt.xticks(weekNum, weekList)
    plt.title(dataIn['name'],size = 12)
    plt.xlabel("Day (GMT %s)" % timeShift)
    plt.ylabel("Tweets")
    plt.hist(dayList,bins=weekNum,align='left',alpha=0.5)
    if show:
        plt.show()
    return plt
    
    
def groupDaily(dataGroup, names, title, timeShift, stacked=True, show=True, truncate = True):
    plt.gca()
    toPlot = []
    namesShown = []
    for pos in range(len(dataGroup)):
    #for dataIn in dataGroup:
        if len(dataGroup[pos]['data']) > 0:
            if truncate:
                data = truncData(dataGroup[pos]['data'],"day")
            else:
                data = dataGroup[pos]['data']
            dates = data['created_at']
            dates = [parser.parse(date) for date in dates]
            dayList = [(t+timedelta(hours=timeShift)).weekday() for t in dates]
            toPlot.append(dayList)
            namesShown.append(names[pos])
            plt.xticks(weekNum, weekList)
            plt.title(dataGroup[pos],size = 12)
            plt.xlabel("Day (GMT %s)" % timeShift)
            plt.ylabel("Tweets")
    if len(namesShown) != 0:
        plt.title(title,size = 12)
        plt.hist(toPlot,bins=weekNum,stacked=stacked, alpha=0.5, label=names, align='left')
        plt.legend([str(entry) for entry in namesShown],loc="best")
        if show:
            plt.show()
    return plt
    

def dailyDistributionPlot(dataIn,titles,bigTitle,timeShift,divFactor=24,overlay = False, show = True):
    """ draw the histogram of the daily distribution """
    #ax = plt.figure(figsize=(18,6)).gca()
    ax = plt.figure(figsize=(11,5)).gca()
    merged = []
    prepped = [] 
    
    collected = deepcopy(dataIn)
    for pos in range(len(collected)):
        collected[pos] = collected[pos]['data']['created_at']
        collected[pos] = [parser.parse(date)+timedelta(hours=timeShift)for date in collected[pos]]
        
    for ytime in collected:
        numtime = [date2num(t) for t in list(ytime)] 
        merged += numtime
        prepped.append(numtime)
        
    first = num2date(min(merged))
    last = num2date(max(merged))
    
    hour = timedelta(hours=1) 
    minute = timedelta(minutes=1)
    
    firstRounded = first.replace(second=0,minute=0)
    lastRounded = last.replace(second=0,minute=0) + hour
    plotMin = date2num(firstRounded)
    plotMax = date2num(lastRounded)
    dateFirst = first.strftime("%a %m/%d/%y")
    dateLast = last.strftime("%a %m/%d/%y")
    timeSuffix = " from %s to %s" % (dateFirst,dateLast)
    
    difference = (lastRounded-firstRounded)
    hourBlocks = difference.days*24 + difference.seconds//3600
    if hourBlocks%2 != 0:
        plotMax = date2num(lastRounded + hour)
        hourBlocks += 1

    while (hourBlocks/divFactor) <= 1 and divFactor > 1:
	divFactor = divFactor/4
    
    plotTitle = titles[0]
    for i in range(len(prepped)):
        if overlay:
            numtime = prepped[i]
            _, _, patches = plt.hist(numtime, bins=(hourBlocks)/divFactor, alpha=0.5, 
                                    stacked=False, range=(plotMin,plotMax))
    if not overlay:
        _, _, patches = plt.hist(prepped, bins=(hourBlocks)/divFactor, alpha=0.5, 
                                    stacked=True, range=(plotMin,plotMax))
    
        
    #tks = [num2date(p.get_x())+minute for p in patches] 
    #plt.xticks(tks,rotation=90,size = 8)
    plt.xlabel("Date/time (GMT %s)" % timeShift)
    plt.gca().set_xlim([plotMin,plotMax])
    plt.ylabel("Number of tweets")
    plt.legend([str(entry) for entry in titles],loc="best")
    plt.title(bigTitle+timeSuffix,size=16)
    ax.xaxis.set_major_formatter(DateFormatter('%m/%d %H'))
    
    if show:
        for pos in range(len(prepped)):
            print "%s: %s entries found" % (titles[pos],len(prepped[pos]))
            countHashTags(dataIn[pos]['data'],5)
            printSample(dataIn[pos]['data'],"",5)
        plt.show()
    return plt
        
        
def countHashTags(data,number='all',freq=1):
    entries = data['text']
    counts = dict()
    for entry in entries:
        words = entry.split(' ')
        for word in words:
            if word.startswith('#'):
                wordL = word.lower()
                if wordL not in counts.keys():
                    counts[wordL] = 1
                else:
                    counts[wordL] += 1
    if type(freq) is int and freq != 1:
        counts = {key: value for key, value in counts.iteritems() if value >= freq}
    sortedCounts= sorted(counts.iteritems(), key=operator.itemgetter(-1))
    if number == 'all':
        number = len(sortedCounts)
    for count in reversed(sortedCounts[-number:]):
        print count
        
        
def checkLinks(data,n='all',shown='all',linkfreq=2, imagefreq=1, cfg = 'null'):
    entries = data['text']
    output = ''
    links = []
    counts = dict()
    domainCounts = dict()
    row = 0
    for entry in entries:
        words = entry.split(' ')
        for word in words:
            if word.startswith('http'):
                links.append(word)
    total = len(links)
    if type(n) is int:
        if n < len(links):
            links = sample(links,n)
        else:
            n = len(links)
    else:
        n = len(links)
    temp = "%s shortened URLs found, testing sample of size = %s\n\n" % (total,n)
    print temp; output+=temp
    for link in links:
        row += 1
        if row % 300 == 0:
            print "Entry",row,"out of",n,"complete,",len(counts),"destination links found with",len(domainCounts),'unique domains'
        sleep(0.1)
        try:
            linked = urllib.urlopen(link)
            if linked.getcode() == 200:
                word = str(linked.url)
                if word not in counts.keys():
                    counts[word] = 1
                    domain = '/'.join(word.split('/')[:3])+'/'
                    if domain not in domainCounts.keys():
                        domainCounts[domain] = 1
                    else:
                        domainCounts[domain] += 1
                else:
                    counts[word] += 1
                #print word
        except:
            None
    photos = {key: value for key, value in counts.iteritems() if '/photo/' in key or 'instagram' in key}
    
    temp = "%s destination URLs found\n" % len(counts.keys())
    temp += "%s destination domains found\n" % len(domainCounts.keys())
    temp += "%s images found\n" % len(photos.keys())
    print temp; output+=temp+'\n\n'
    
    if type(linkfreq) is int and linkfreq != 1:
        counts = {key: value for key, value in counts.iteritems() if value >= linkfreq}
        domainCounts = {key: value for key, value in domainCounts.iteritems() if value >= linkfreq}
    if type(imagefreq) is int and imagefreq != 1:
        photos = {key: value for key, value in photos.iteritems() if value >= imagefreq}
    sortedCounts= sorted(counts.iteritems(), key=operator.itemgetter(-1))
    sortedDomainCounts= sorted(domainCounts.iteritems(), key=operator.itemgetter(-1))
    sortedPhotoCounts= sorted(photos.iteritems(), key=operator.itemgetter(-1))
    
    outStyle = lambda x: '\t' + str(x).replace("'"," ").replace('(','[').replace(')',']') + '\n'
    

    if shown == 'all':
        if len(sortedCounts) != 0:
            temp = "Highest Ranked Links:\n"
            for count in reversed(sortedCounts):
                temp += outStyle(count)
        if len(sortedDomainCounts) != 0:
            temp += "Highest Ranked Domains:\n"
            for count in reversed(sortedDomainCounts):
                temp += outStyle(count)
        if len(sortedPhotoCounts) != 0:
            temp += "Most Shared Images:\n"
            for count in reversed(sortedPhotoCounts):
                temp += outStyle(count)
    else:
        if len(sortedCounts) != 0:
            temp = "Highest Ranked Links:\n"
            for count in reversed(sortedCounts[-shown:]):
                temp += outStyle(count)
        if len(sortedDomainCounts) != 0:
            temp += "Highest Ranked Domains:\n"
            for count in reversed(sortedDomainCounts[-shown:]):
                temp += outStyle(count)
        if len(sortedPhotoCounts) != 0:
            temp += "Most Shared Images:\n"
            for count in reversed(sortedPhotoCounts[-shown:]):
                temp += outStyle(count)
    print temp; output += temp
    return output
    
    
def fixBox(dataSet,box):
    if box == 'tight':
        return {'lat1':min(dataSet['data']['lat'])-1.5,
               'lat2':max(dataSet['data']['lat']+1.5),
               'lon1':min(dataSet['data']['lon']-1.5),
               'lon2':max(dataSet['data']['lon']+1.5)}
    elif box == 'very tight':
        return {'lat1':min(dataSet['data']['lat'])-0.5,
               'lat2':max(dataSet['data']['lat']+0.5),
               'lon1':min(dataSet['data']['lon']-0.5),
               'lon2':max(dataSet['data']['lon']+0.5)}
    else:
        return box
    
    
def setWidth(box,longest):
    if (box['lon2'] - box['lon1']) >  (box['lat2'] - box['lat1']):
        lonWidth = longest
        latWidth = longest*((box['lat2'] - box['lat1'])/(box['lon2'] - box['lon1']))
    else:
        latWidth = longest
        lonWidth = longest*((box['lon2'] - box['lon1'])/(box['lat2'] - box['lat1']))
    return lonWidth,latWidth


def getData(dataSet,offset):
    dataSet['data'] = dataSet['data'].dropna(subset=['lat','lon','created_at']) 
    lats = list(dataSet['data']['lat']); lons = list(dataSet['data']['lon'])
    times =  [(parser.parse(entry) + datetime.timedelta(hours=int(offset))) for entry in list(dataSet['data']['created_at'])]
    return lats, lons, times

def getDensity(box,lats,lons,longest):
    lonWidth, latWidth = setWidth(box,longest)
    lon_bins = np.linspace(box['lon1'], box['lon2'], lonWidth+1)
    lat_bins = np.linspace(box['lat1'], box['lat2'], latWidth+1)
    density, _, _ = np.histogram2d(lats, lons, [lat_bins, lon_bins])
    return density, lon_bins, lat_bins


def fixDensity(density,xs,ys):
    if np.sum(density) == 0.:
        print "Adjusting density of empty sequence"
      	density == deepcopy(xs)
	density.fill(0.00000001)
    return density


def mapTransparency(grid,coloredGrid,level):
    #coloredGrid = cm.hsv(grid)
    temp = deepcopy(coloredGrid)
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            temp[i][j][3] = pow((float(grid[i][j])/level),.333)
    return temp


def mapColors(grid,level,cmap):
	cNorm  = colors.Normalize(vmin=0, vmax=level)
	scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=cmap)
	temp = grid.tolist()
	for x in range(len(grid)):
	    for y in range(len(grid[0])):
		temp[x][y] = list(scalarMap.to_rgba(float(grid[x][y])))
	return temp
	

def mapSubject(dataset,subject,box='tight',level='auto',
               longest=20,call='default',highlight=False,
               heatmap=True, mark = 'r', cmap='YlOrRd',
               show = True, offset = 0, subtitle = '', geobox = 'null',
	       important = 'null',background = 'none'):

    if call == 'animate':
        plt.clf()
    else:
        fig = plt.figure(figsize=(9,9))
    
    if geobox == 'null' or (type(box) is str and type(geobox) is str):
    	box = fixBox(dataset,box)
    else:
        box = geobox
    	
    lats, lons, times = getData(dataset,offset)
    
    mapped = Basemap(projection='mill', 
                     llcrnrlon=box['lon1'],
                     llcrnrlat=box['lat1'],
                     urcrnrlon=box['lon2'],
                     urcrnrlat=box['lat2'])

    mapOpacity = 0.75
    if background == 'etopo':
	mapped.etopo(zorder=0, alpha=mapOpacity)
    elif background == 'shaded relief':
	mapped.shadedrelief(zorder=0, alpha=mapOpacity)
    elif background == 'blue marble':
        mapped.bluemarble(zorder=0, alpha=mapOpacity)
    elif '/' in background or '.' in background:
        try:
            mapped.warpimage(image='maps/'+background, scale=None, zorder=0, alpha=mapOpacity)
        except:
            mapped.warpimage(image=background, scale=None, zorder=0, alpha=mapOpacity)
    else:
	background = 'null'
	
    smallest = min(box['lat2']-box['lat1'],box['lon2']-box['lon1'])

    mapped.drawcoastlines(zorder=3,linewidth = 1.5)
    
    if smallest < 5:
        mapped.drawcountries(zorder=3,linewidth = 2)
        mapped.drawstates(zorder=3, linewidth = 1.5)
        mapped.drawcounties(zorder=3,linewidth = 1)
    else:
        mapped.drawcountries(zorder=3,linewidth = 1.5)
        mapped.drawstates(zorder=3, linewidth = 1)
    
    if heatmap:
        # ######################################################################
        # http://stackoverflow.com/questions/11507575/basemap-and-density-plots)
        density, lon_bins, lat_bins = getDensity(box,lats,lons,longest)
        lon_bins_2d, lat_bins_2d = np.meshgrid(lon_bins, lat_bins)
        xs, ys = mapped(lon_bins_2d, lat_bins_2d) # will be plotted using pcolormesh
        # ######################################################################
        
        if level == 'auto':
            level = np.amax(density)

	density = fixDensity(density,xs,ys)
	
  	if background == 'null':
        	plt.pcolormesh(xs, ys, density, cmap = cmap,zorder=2, alpha = 1, vmin =1)
	else:
		extent = (xs[0][0],xs[0][-1],ys[0][0],ys[-1][0]) 
		colorized = mapColors(density,level,cmap)
		colorized = mapTransparency(density,colorized,level)
		plt.imshow(colorized, extent=extent,cmap=cmap,origin='lower',interpolation='nearest',zorder=2)


    smallest = min(box['lat2']-box['lat1'],box['lon2']-box['lon1'])
    
    if smallest < 1.0:
        gridIncrement = 0.1
    if smallest < 2.5:
	gridIncrement = 0.5
    elif smallest < 5:
	gridIncrement = 1.0
    elif smallest < 10:
	gridIncrement = 2.5
    else:
	gridIncrement = 5.0

    parallels = np.arange(-90.,90.,gridIncrement)
    mapped.drawparallels(parallels,labels=[1,0,0,0],fontsize=10, alpha = .75)
    meridians = np.arange(-180.,180.,gridIncrement)
    mapped.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10, alpha = .75)

    if important != 'null':
	xI,yI = mapped(important[0],important[1])
	xM,yM = mapped(np.mean(lons),np.mean(lats))
	mapped.plot(xI,yI,'o',markersize=15, zorder=6, markerfacecolor = "white", markeredgecolor=mark, alpha = 1.0)
	mapped.plot(xM,yM,'x',markersize=15, zorder=6, markerfacecolor = "white", markeredgecolor=mark, alpha = 1.0)

    x, y = mapped(lons, lats) # compute map proj coordinates.
    mapped.plot(x, y, 'o', markersize=4,zorder=6, markerfacecolor=mark,markeredgecolor="none", alpha=0.30)
    if highlight != False:
        mapped.plot(x, y, 'o', markersize=4,zorder=6, markerfacecolor=highlight,markeredgecolor="none", alpha=0.03)

    
    title = '%s search for "%s",\n%s Related Tweets Found from\n%s to %s' % (dataset['name'],
                                                                            subject,
                                                                            len(dataset['data']),
                                                                            times[0],
                                                                            times[-1])
    plt.title(title)
    if subtitle != '':
   	 plt.xlabel(subtitle)

    if heatmap:
        divider = make_axes_locatable(plt.gca())
        cax = divider.append_axes("right", "5%", pad="3%")
        cbar = plt.colorbar(orientation='vertical',cax=cax)
        if level != 'full':
            plt.clim([0,level])
        cbar.set_label('Number of Tweets')
    
    if call != 'animate' and show:
        plt.show()
    return plt
    
    
def getDays(dataSet):
    days = dataSet['data']['date']
    return days.unique()


def findCenter(dataSet):
	mlat = np.mean(dataSet['data']['lat'])
	mlon = np.mean(dataSet['data']['lon'])
	minDist = 999999999999
	lowest = 'null'
	for pos in range(len(dataSet['data'])):
		lat = dataSet['data'].iloc[pos]['lat']
		lon = dataSet['data'].iloc[pos]['lon']
		distance = vincenty((mlon,mlat),(lon,lat))
		if distance < minDist:
			lowest = pos
			minDist = distance
	return dataSet['data'].iloc[lowest]
		

def animateMap(dataSet,subject,box='tight',level='auto',longest=20,
               timeStamp=False,highlight=False,heatmap=True,mark='r',
               cmap='YlOrRd',makeVideo=True,makeGif=True,show=True,
               offset=0, showCluster = True, background = 'none'):
    #print "HERE AND NOW"
    days = getDays(dataSet)
    length = len(days)
    plots = []; daySubs = []
    
    daySubs = [getFieldSub(dataSet,[day],[],day,'date') for day in days]
    
    if box == 'tight':
    	geoBox = fixBox(dataSet,box)
     
    extraFig = 'null'   
              
    if level == 'auto' and heatmap:
        maxVal = 0
        for daySub in daySubs:
            lats, lons, times = getData(daySub,offset)
            density, lon_bins, lat_bins = getDensity(geoBox,lats,lons,longest)
            maxVal = max(maxVal, float(np.amax(density)))
        level = maxVal    
        maxVal = 0
        if showCluster:
            for daySub in daySubs:
                lats, lons, times = getData(daySub,offset)
                density, lon_bins, lat_bins = getDensity(geoBox,lats,lons,longest)
                maxVal = max(maxVal, float(np.amax(density)))
                if maxVal == level:
                    maxCluster = deepcopy(daySub)
                    break 
                    
            row,col = np.unravel_index(np.argmax(density), density.shape)
            
            cols = len(density[0])
            rows = len(density)
            rowInc = (geoBox['lat2']-geoBox['lat1'])/rows
            colInc = (geoBox['lon2']-geoBox['lon1'])/cols
            
            clusterBox = {'lat1':-0.5+geoBox['lat1']+row*rowInc,
               'lat2':0.5+geoBox['lat1']+(row+1)*rowInc,
               'lon1':-0.5+geoBox['lon1']+col*colInc,
               'lon2':0.5+geoBox['lon1']+(col+1)*colInc}
            
            
            clusterData = getGeoSub(daySub,clusterBox,'')
            clusterBox = fixBox(clusterData,'tight')
            clusterData = getGeoSub(daySub,clusterBox,'')
            clusterBox = fixBox(clusterData,'very tight')

	    temp = findCenter(clusterData)
	    subtitle = "\n\nCentral Point: %s {%s,%s}" % (temp['place'],
							str(temp['lon'])[:5],
							str(temp['lat'])[:5])
	    important = [[temp['lon']],[temp['lat']]]
            
            extraFig = mapSubject(clusterData,subject+' Cluster Analysis',box=clusterBox,level='auto',longest=longest,
                   highlight=highlight, heatmap=heatmap, show=show,
                   mark=mark, cmap=cmap, offset=offset,
		   subtitle = subtitle, important = important, background = background)
            
            
            
        
    fig = plt.figure(figsize=(10,10))
    
    
    def animate(i):
        mapSubject(daySubs[i],subject,box=box,level=level,longest=longest,
                   call='animate',highlight=highlight,heatmap=heatmap,
                   mark=mark,cmap=cmap,offset=offset, geobox = geoBox,
		   background=background)
    
    anim = animation.FuncAnimation(fig,animate, frames=length, interval=1500, blit=False)
    
    if timeStamp:
        timeStamp = datetime.datetime.now().strftime('%Y%m%d%H%M-%S')
    else:
        timeStamp = ''
    
    fileName = (dataSet['name'][0:15]+subject[0:15]).replace(' ','').replace(',','').replace(':','')+timeStamp
    
    if makeGif:
        print "Generating", fileName, "gif animation"
        anim.save(fileName+'.gif', writer='imagemagick', fps=1)
        sleep(3)
    if makeVideo:
        print "Generating", fileName, "mp4 video"
        writer = animation.writers['ffmpeg'](fps=1)
        anim.save(fileName+'.mp4',writer=writer,dpi=80)
        sleep(5)
        del writer
        del anim
        anim = 'null'
    
    plt.close()    
    return anim,fileName,extraFig
    
    
    
    
def makeTimeLine(inFile,
                name='default',
                embed='media',
                sort='place',
                placeLevel = 1,
                keep = 'null',
                keepStyle = 'direct',
                directory = ''):
    
    outFile = 'timeLineTemp.csv'
    
    if embed == 'media':
        contentCol = 'media1_display_url'
        mediaCol = 'media1_media_url_https'
    else:
        contentCol = 'link1'
        mediaCol = 'link1'

    
    if type(inFile) is str:
        data =  pd.DataFrame.from_csv(inFile,index_col='id')
    elif type(inFile) is dict:
        data = inFile['data']
    else:
        data = inFile
        
    fileOut = open(outFile,'wb')
    newKeys = 'date,display_date,description,link,series,html\n'
    
    fileOut.write(newKeys)
    
    print "Generating new csv as", outFile
    
    for index, row in data.iterrows():
        date = row['created_at']
        displayDate = ' '.join([entry for entry in row['created_at'].split() if not entry.startswith('+')])
        description = '<b>Text:</b> '+' '.join(row['text'].split())
        try:
            description += '<br><b>Location:</b> '+str(row['place'])
        except:
            None
        try:
            description += '<br><b>Retweets:</b> '+str(row['retweet_count'])
        except:
            None
        try:
            description += '<br><b>Favorites:</b> '+str(row['favorite_count'])
        except:
            None
        
        link = row[contentCol]; media = row[mediaCol]
        
        if not link.startswith('http') and str(link).lower() != 'false':
            link = 'https://'+link
        if not media.startswith('http') and str(media).lower() != 'false':
            media = 'https://'+media
            
        series = row[sort]
        
        if sort == 'place':
            series = str(series).split(', ')[-placeLevel]
            
        inKeep = ((series in keep) == (keepStyle == 'direct')) or keep == 'null'
        
        if embed == 'media':    
            html = "<img src='%s'>" % media
        else:
            html = "<iframe width='800' height='600' src='%s'></iframe>" % media
            
        cleaned = lambda x: str(x).replace(',','').replace('"','').replace("'",'')
        content = [date,displayDate,description,link,series]
        content = [cleaned(item) for item in content]
        content.append(html)
        lens = [len(str(item)) for item in content]
        
        if str(link).lower() != 'false' and min(lens) != 0 and inKeep:
            fileOut.write("%s,%s,%s,%s,%s,%s\n" % tuple(content))
            
    fileOut.close(); sleep(1)
    
    if directory != '' and directory[-1] != '/':
        directory += '/'
    outDir = directory+'TimeLine'+name
    
    command = "timeline-setter -c %s -o %s -O" % (outFile,outDir)
    
    print "Running timeline-setter"

    process = subprocess.Popen(command, shell=True)
    output = process.communicate()[0]
    
    fileDirect = os.getcwd()+'/'+outDir+'/timeline.html'
    
    print "Operation complete, timeline available at:",fileDirect
    
    return fileDirect
    
    
    
"""def showWordCloud(text,show=True):
    plt.figure(figsize=(8,8)).gca()
    fontPath = '/Library/Fonts/Microsoft/'
    font = 'Verdana.ttf'
    wc = WordCloud(background_color="white", max_words=2000,font_path=fontPath+font,stopwords=['ebola','link','atweeter','user'],
                   height = 800, width = 800)
    wc.generate(text)
    plt.imshow(wc)
    plt.axis("off")
    if show:
        plt.show()
    else:
        return plt"""

def showWordCloud(text,show=True):
    plt.figure(figsize=(8,8)).gca()
    stopWordsNew = ['link','atweeter','user','rt']
    try:
	    fontPath = '/Library/Fonts/Microsoft/'
	    font = 'Verdana.ttf'
	    wc = WordCloud(background_color="white", max_words=2000,font_path=fontPath+font,stopwords=stopWordsNew,
		           height = 800, width = 800)
	    wc.generate(text)
    except:
	    fontPath = '/usr/share/fonts/truetype/ubuntu-font-family'
	    font = 'Ubuntu-L.ttf'
	    wc = WordCloud(background_color="white", max_words=2000,stopwords=stopWordsNew,
		           height = 800, width = 800)
	    wc.generate(text)

    plt.imshow(wc)
    plt.axis("off")
    if show:
        plt.show()
    else:
        return plt



def getWordWeights(dataIn,daysPast,directory, timeStamp,mode = 'image'):
    if type(dataIn) is dict:
        data = deepcopy(dataIn['data'])
    else:
        data = deepcopy(dataIn)
    dates = [parser.parse(entry['created_at']) for index,entry in data.iterrows()]
    rightBound = max(dates)
    leftBound = rightBound - datetime.timedelta(days = daysPast)
    data = [entry for index,entry in data.iterrows() if leftBound < parser.parse(entry['created_at']) < rightBound]
    
    if  'nlpCat' in data[0].keys():
        CatCol = 'nlpCat'
    elif 'nltkCat' in data[0].keys():
        CatCol = 'nltkCat'
    else:
        CatCol = 'tweetType'
    
    wordList = dict()
    
    if mode == 'image':
        wordList['all'] = [prepTweet(entry['text']) for entry in data]
        
        cats = set([entry[CatCol] for entry in data])
        for cat in cats:
            wordList[cat] = [prepTweet(entry['text']) for entry in data if entry[CatCol] == cat]
        cats.add('all')
        for cat in cats:
            wordList[cat] = ' '.join([' '.join([word.split("'")[0] for word in entry if word not in blockKeys]) for entry in wordList[cat]]) 
        return wordList
        
    elif mode != 'image':    
        wordWeights = dict()
        wordCloud = []
        wordList['all'] = [prepTweet(entry['text']) for entry in data] 
    
        cats = set([entry[CatCol] for entry in data])
        for cat in cats:
            wordList[cat] = [prepTweet(entry['text']) for entry in data if entry[CatCol] == cat] 
    
        cats.add('all')
        for cat in cats:
            wordList[cat] = [[word.split("'")[0] for word in entry if word not in blockKeys] for entry in wordList[cat]]
        
        
        for cat in cats:
            wordWeights[cat] = dict()  
            for tweet in wordList[cat]:
                for word in tweet:
                    if word not in wordWeights[cat].keys():
                        wordWeights[cat][word] = 1
                    else:
                        wordWeights[cat][word] += 1
                        
        for cat in cats:
            listed = []
            for key in wordWeights[cat].keys():
                listed.append('{text: "%s", weight: %s}' % (str(key),wordWeights[cat][key]))
            wordCloud.append('{%s: [%s]}' % (cat,', '.join(listed)))
        
    jsonOut = '{wordcloud: [%s]}' % ', '.join(wordCloud)
    outName = "wordcloud.json"
    print "Writing wordcloud to '"+outName + "'"
    
    outFile = open(directory+outName, "w")
    outFile.write(jsonOut)
    outFile.close()
    return directory+outName


def lemList(listed):
    listed = list(set([lmtzr.lemmatize(word) for word in listed if len(word)>1]))


def stripUnicode(text):
    """Strips unicode special characters for text storage (smileys, etc)"""
    if text == None:
        return "NaN"
    else:
        if type(text) == unicode:
            return str(unicodedata.normalize('NFKD', text).encode('ascii', 'ignore'))
        else:
            return str(text)



def prepTweet(word):
    word =  stripUnicode(word)
    original = text = str(word)
    
    text = text.replace("&amp",'') #cleanup conversion bug
    toAdd = set()
        
    if '?' in text:
	toAdd.add('$?')
    if '!' in text:
	toAdd.add('$!')
    if '...' in text:
	toAdd.add('$...')

    punctuations = ".,\"-_%!?=+\n\t:;()*&$/"
    
    #Remove accentuated characters
    text = unicode(text)
    text = ''.join(char for char in unicodedata.normalize('NFD', text) if unicodedata.category(char) != 'Mn')
        
    #End of string operations, continuing with list ops.    
    

    while 'http' in text:
	toAdd.add('$link')
	temp = text.index('http')
	text = text[:temp] + text[text.find(' ',temp):]
    while 'RT @' in text:
	toAdd.add('$RT')
	temp = text.index('RT @')
	text = text[:temp] + text[text.find(' ',temp):]
    """while '@' in text:
	toAdd.add('@user')
	temp = text.index('@')
	if temp == len(text) - 1:
		text = text[:-1]
	else:
		text = text[:temp] + text[text.find(' ',temp):]"""
    for char in punctuations:
	text = text.replace(char,' ')
    while '  ' in text:
        text = text.replace('  ',' ')
    while text.startswith(' '):
        text = text[1:]
    while text.endswith(' '):
        text = text[:-1]
    listed = text.lower().split(' ')
        
    lemList(listed) #Lemmatize list to common stem words
    
    toDel = set()


    listed = [word for word in [word for word in listed if word not in stopWords] if word not in toDel] + list(toAdd) 
    
    return listed
    
