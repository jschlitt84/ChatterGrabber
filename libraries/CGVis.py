import operator
import urllib
import datetime

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from random import shuffle, sample
from datetime import timedelta
from dateutil import parser
from matplotlib.dates import DateFormatter, date2num, num2date
from copy import deepcopy
from time import sleep

from mpl_toolkits.basemap import Basemap, cm
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.animation as animation
#from IPython.display import HTML


weekList = ['zero','Mon','Tue','Wed','Thu','Fri','Sat','Sun','null']
weekNum = [-1,0,1,2,3,4,5,6,7]


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
    #print "DEBOOO1", len(data)
    data = data[data.apply(lambda x: sum([1 for place in sought if str(place).lower() in str(x[str(field)]).lower()]) > 0, axis=1)]
    if exclusions != []:
        data = data[data.apply(lambda x: sum([1 for place in exclusions if str(place).lower() in str(x[str(field)]).lower()]) == 0, axis=1)]
    dataOut['data'] = data
    #print "DEBOOO2", len(data)
    return dataOut
    
def getFieldItem(dataIn,sought,prefix,field):
    dataOut = deepcopy(dataIn)
    #sought = [str(item) for item in sought]
    dataOut['name'] = prefix + ' ' + dataOut['name']
    data = dataOut['data']
    #print "DEBOOO1", len(data)
    data = data[data[field].isin(sought)]
    #print "DEBOOO2", len(data)
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
    firstDay = data.irow(0)['day']
    firstTime = getTime(data.irow(0)['time'])
    limit = len(data)
    pos = limit-1
    if mode == "hour":
        while getTime(data.irow(pos)['time']) > firstTime or getTime(data.irow(pos-1)['time']) < firstTime and pos > 0 :
            pos -= 1
    elif mode == "day":
        while getTime(data.irow(pos)['time']) > firstTime or getTime(data.irow(pos-1)['time']) < firstTime or firstDay !=data.irow(pos-1)['day'] and pos > 0:
                pos -= 1
    if pos == -1:
        pos = limit
            
                
    dayDiff = parser.parse(data.irow(pos)['created_at']).timetuple().tm_yday - parser.parse(data.irow(0)['created_at']).timetuple().tm_yday
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
    
    
def groupHourly(dataGroup, names, title, timeShift, stacked=True,show=True):
    plt.gca()
    toPlot = []
    namesShown = []
    for pos in range(len(dataGroup)):
    #for dataIn in dataGroup:
        if len(dataGroup[pos]['data']) > 0:
            data = truncData(dataGroup[pos]['data'],"hour")
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
        plt.legend(namesShown,"best")
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
    
    
def groupDaily(dataGroup, names, title, timeShift, stacked=True, show=True):
    plt.gca()
    toPlot = []
    namesShown = []
    for pos in range(len(dataGroup)):
    #for dataIn in dataGroup:
        if len(dataGroup[pos]['data']) > 0:
            data = truncData(dataGroup[pos]['data'],"day")
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
        plt.legend(namesShown,"best")
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
    plt.legend(titles,"best")
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
                if word not in counts.keys():
                    counts[word] = 1
                else:
                    counts[word] += 1
    if type(freq) is int and freq != 1:
        counts = {key: value for key, value in counts.iteritems() if value >= freq}
    sortedCounts= sorted(counts.iteritems(), key=operator.itemgetter(-1))
    if number == 'all':
        number = len(sortedCounts)
    for count in reversed(sortedCounts[-number:]):
        print count
        
        
def checkLinks(data,n='all',shown='all',linkfreq=2, imagefreq=1):
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
    
    temp = ''
    
    if shown == 'all':
        if len(sortedCounts) != 0:
            temp = "Highest Ranked Links:\n"
            for count in reversed(sortedCounts):
                temp += '\t' + str(count) + '\n'
        if len(sortedDomainCounts) != 0:
            temp += "Highest Ranked Domains:\n"
            for count in reversed(sortedDomainCounts):
                temp += '\t' + str(count) + '\n'
        if len(sortedPhotoCounts) != 0:
            temp += "Most Shared Images:\n"
            for count in reversed(sortedPhotoCounts):
                temp += '\t' + str(count) + '\n'
    else:
        if len(sortedCounts) != 0:
            temp = "Highest Ranked Links:\n"
            for count in reversed(sortedCounts[-shown:]):
                temp += '\t' + str(count) + '\n'
        if len(sortedDomainCounts) != 0:
            temp += "Highest Ranked Domains:\n"
            for count in reversed(sortedDomainCounts[-shown:]):
                temp += '\t' + str(count) + '\n'
        if len(sortedPhotoCounts) != 0:
            temp += "Most Shared Images:\n"
            for count in reversed(sortedPhotoCounts[-shown:]):
                temp += '\t' + str(count) + '\n'
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
	

def mapSubject(dataset,subject,box='tight',level='auto',
               longest=20,call='default',highlight=False,
               heatmap=True, mark = 'r', cmap='YlOrRd',
               show = True, offset = 0):
    
    if call == 'animate':
        plt.clf()
    else:
        fig = plt.figure(figsize=(9,9))
        
    box = fixBox(dataset,box)
    lats, lons, times = getData(dataset,offset)
    
    mapped = Basemap(projection='mill', 
                     llcrnrlon=box['lon1'],
                     llcrnrlat=box['lat1'],
                     urcrnrlon=box['lon2'],
                     urcrnrlat=box['lat2'])
    
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
        plt.pcolormesh(xs, ys, density, cmap = cmap)

    mapped.drawcoastlines()
    mapped.drawstates()
    mapped.drawcountries()
    parallels = np.arange(-90.,90.,5.)
    mapped.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
    meridians = np.arange(-180.,180.,5.)
    mapped.drawmeridians(meridians,labels=[0,0,0,1],fontsize=10)
    x, y = mapped(lons, lats) # compute map proj coordinates.
    mapped.plot(x, y, 'o', markersize=4,zorder=6, markerfacecolor=mark,markeredgecolor="none", alpha=0.25)
    if highlight != False:
        mapped.plot(x, y, 'o', markersize=4,zorder=6, markerfacecolor=highlight,markeredgecolor="none", alpha=0.03)
    
    title = '%s search for "%s", %s Related Tweets Found from\n%s to %s' % (dataset['name'],
                                                                            subject,
                                                                            len(dataset['data']),
                                                                            times[0],
                                                                            times[-1])
    plt.title(title)
    
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


def animateMap(dataSet,subject,box='tight',level='auto',longest=20,
               timeStamp=False,highlight=False,heatmap=True,mark='r',
               cmap='YlOrRd',makeVideo=True,makeGif=True,show=True,
               offset=0, showCluster = True):
    
    days = getDays(dataSet)
    length = len(days)
    plots = []; daySubs = []
    
    daySubs = [getFieldSub(dataSet,[day],[],day,'date') for day in days]
    
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
            clusterBox = fixBox(clusterData,'very tight')
            clusterData = getGeoSub(daySub,clusterBox,'')
            
            extraFig = mapSubject(clusterData,subject+' Cluster Analysis',box=clusterBox,level='auto',longest=longest,
                   highlight=highlight, heatmap=heatmap, show=False,
                   mark=mark, cmap=cmap, offset=offset)
            
            
            
        
    fig = plt.figure(figsize=(10,10))
    
    
    def animate(i):
        mapSubject(daySubs[i],subject,box=box,level=level,longest=longest,
                   call='animate',highlight=highlight,heatmap=heatmap,
                   mark=mark,cmap=cmap,offset=offset)
    
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
    
    plt.close()    
    return anim,fileName,extraFig
