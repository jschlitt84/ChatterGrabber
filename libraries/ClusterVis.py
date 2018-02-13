import pandas as pd
import geopandas as gp
import numpy as np
import seaborn as sb

from collections import Counter
from shapely.geometry import Point, MultiPoint
from dateutil import parser
from mpl_toolkits.basemap import Basemap
from datetime import datetime

import hdbscan
import matplotlib.pyplot as plt
import time
import shapely

sb.set_context('poster')

def loadDataSet(ref,box,filters='null'):
    (lon1,lat1,lon2,lat2) = (box[0],box[1],box[2],box[3])
    tweetData = pd.read_csv(ref)
    if filters != 'null':
        for key,item in filters.iteritems():
            tweetData = tweetData[tweetData[key]==item]
    secsPerDay = 60*60*24
    tweetData['UTCTime'] = [float(parser.parse(i).strftime("%s"))/secsPerDay for i in tweetData['created_at']]
    tweetData.index = tweetData['text']
    #tweetData = tweetData.set_index(['id'])
    tweetData = tweetData[tweetData['NLPCat']==3]
    
    (lon1,lat1,lon2,lat2) = (box[0],box[1],box[2],box[3])
    tweetData = tweetData[(tweetData['lat'] > lat1) & 
                       (tweetData['lat'] < lat2) &
                       (tweetData['lon'] > lon1) &
                       (tweetData['lon'] < lon2)]
    tweetData = tweetData[np.isfinite(tweetData['lat'])]
    tweetData = tweetData[np.isfinite(tweetData['lon'])]
    tweetLocs = tweetData[['lat','lon','UTCTime']].dropna(how='any')

    return tweetData, tweetLocs
    
    
def getClusters(data, kwds,cfg='null'):
    labels = hdbscan.HDBSCAN(**kwds).fit_predict(data)
    return labels
    

def prepClusters(data,labels):
    workData = data
    workData['label'] = labels
    counted = dict(Counter(list(labels)))
    points = []
    hulls = []
    centX = []
    centY = []
    indexOut = []
    counts = []
    
    for (i,j) in sorted(counted.items(), key=lambda x: x[1], reverse=True):
        if i != -1:
            cluster = workData[workData['label'] == i]
            clusterCoords = zip(cluster['lon'],cluster['lat'])
            clusterPoints = MultiPoint([Point(k[0],k[1]) for k in clusterCoords])
            points.append(clusterPoints)
            hulls.append(clusterPoints.convex_hull)
            centroid = hulls[-1].centroid
            centX.append(centroid.x)
            centY.append(centroid.y)
            indexOut.append(i)
            counts.append(j)

    gdf = gp.GeoDataFrame()
    gdf['points'] = points
    gdf['hulls'] = hulls
    gdf['centX'] = centX
    gdf['centY'] = centY
    gdf['keys']= indexOut
    gdf['count'] = counts
    gdf.geometry=gdf['hulls']
    return gdf


def getTextSubsets(tweets,data,dispKey):
    textSubSets = {i:pd.join([data[data['label'] == j],tweets[['text']]],axis=1,join='inner') for i,j in dispKey.iteritems()}
    textSubSets['all'] = tweets
    return textSubSets

def getTextSubsets(tweets,data,dispKey):
    #textSubSets = {i:pd.concat([data[data['label'] == j],tweets[['text']]],axis=1,join='inner') for i,j in dispKey.iteritems()}
    #return textSubSets
    dictOut = {'all':tweets}
    for i,j in dispKey.iteritems():
        primary = data[data['label'] == j]
        secondary = tweets[['text']]
        primary = primary.join(secondary['text'])
        dictOut[i] = primary
        
    return dictOut

    textSubSets = dict()
    for i,j in dispKey.iteritems():
        dfSub = data[data['label'] == j]
        textSubSets[i] = dfSub
    return textSubSets


def getClusterFreq(cluster,keywords):
    tweets = list(cluster['text'])
    strCounts = lambda j: len([i for i in tweets if j.lower() in i.lower()])
    keywordFreqs = {i:strCounts(i) for i in keywords}
    return keywordFreqs
    plt.show()
    
    
def plotClusters(shapes,pts,box,show=8,title='',size=10):
    fig,ax = plt.subplots(figsize=(size,size))
    top9 = shapes.head(n=show).iloc[::-1]

    mapped = Basemap(projection='mill', 
                     llcrnrlon=box[0],
                     llcrnrlat=box[1],
                     urcrnrlon=box[2],
                     urcrnrlat=box[3],
                     ax=ax)

    mapped.bluemarble(zorder=0,alpha=0.3)
    
    smallest = min(box[3]-box[1],box[2]-box[0])
    mapped.drawcoastlines(zorder=3,linewidth = 0.7)
    if smallest < 5:
        mapped.drawcountries(zorder=3,linewidth = 0.6)
        mapped.drawstates(zorder=3, linewidth = 0.5)
        mapped.drawcounties(zorder=3,linewidth = 0.2)
    else:
        mapped.drawcountries(zorder=3,linewidth = 1.5)
        mapped.drawstates(zorder=3, linewidth = 0.2)
    
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

    geoPrep = [shapely.ops.transform(mapped, poly) for poly in top9.geometry.tolist()]
    top9.geometry = geoPrep
    
    top9.plot(column='count',
              ax=ax,
              cmap='YlOrRd',
              legend=True,
              scheme='QUANTILES',
              k=show,
              alpha=0.5,
              zorder=5)
    
    if show < 10:
        textArgs = {'facecolor':'white', 'alpha':0.5, 'pad':4, 'edgecolor':'b'}
        leg = ax.get_legend()
        xs, ys = mapped(list(top9['centX']),list(top9['centY']))

        for i in reversed(range(show)):
            leg.get_texts()[top9.index[i]].set_text("%s: %s" % (i,top9['count'][i]))
            plt.text(xs[i],ys[i],top9.index[i],bbox=textArgs,zorder=6)
        leg.set_bbox_to_anchor((1, 1))
    
    xs, ys = mapped(list(pts['lon']),list(pts['lat']))
    mapped.plot(xs, ys, 'o', markersize=4,zorder=6, markerfacecolor='b',markeredgecolor="none", alpha=0.30)
    plt.title(title + "Cluster Spatial Distribution")

    return list(top9.index), ax


def plotChunkTimes(textChunks,nBins='null',title='',size=10):
    fig,ax = plt.subplots(figsize=(size,0.4*size))
    secsPerDay = 60*60*24
    times = {key:[int(i*secsPerDay) for i in textChunks[key]['UTCTime']] for key in sorted(textChunks.keys())}
    
    tMax = max(times['all']); tMin = min(times['all'])
    if nBins == 'null':
        nBins = (tMax-tMin)/secsPerDay+1
    while nBins >= 100:
        nBins = nBins/2
    nBins = int(nBins)
    
    bins = np.linspace(tMin,tMax,nBins)
    
    labels = ['all: %s' % len(textChunks['all'])]
    lists = []
    for key in reversed(times.keys()):
        if key != 'all':
            labels.append('%s: %s' % (key,len(times[key])))
            lists.append(times[key])
    
    
    plt.hist(times['all'],bins,histtype = 'step',color='b',ls='--',zorder=3)
    matchedColors = plt.cm.YlOrRd(plt.Normalize()(range(len(lists))))
    plt.hist(lists, bins,color=matchedColors, stacked=True,zorder=2,alpha=0.5,edgecolor='black')
    plt.xlim((tMin,tMax))
    xTicks = plt.xticks()[0]
    plt.xticks(xTicks, [datetime.fromtimestamp(i).strftime('%m/%d/%y') for i in xTicks], rotation=45)
    
    plt.legend(labels)
    plt.title(title + "Cluster Temporal Distribution")
    plt.xlabel('Day')
    plt.ylabel('Tweets Per Day')
    
    
def plotKeywords(textChunks,keywords,n,title = '',size = 10):        
    fig,ax = plt.subplots(figsize=(size,0.4*size))
    clusterFreqs = {i:getClusterFreq(j,keywords) for i,j in textChunks.iteritems()}
    summedFreqs = {i:sum([clusterFreqs[j][i] for j in clusterFreqs.keys()]) for i in clusterFreqs[0].keys()}
    selectedKeywords = sorted(summedFreqs.items(), key=lambda x: x[1], reverse=True)[:n]

    primaryKws = [i[0] for i in selectedKeywords]
    
    plotData = pd.DataFrame(index=primaryKws)
    
    for key in sorted(textChunks.keys()):
        length = float(len(textChunks[key]))
        freqs = [(clusterFreqs[key][keyword]/length)*100 for keyword in primaryKws]
        plotData[key] = freqs
    
    plotData.T.plot.bar(ax=ax,alpha=0.5,edgecolor='black')
    plt.title(title + "Keyword Frequency By Cluster")
    ax.set_xlabel('Cluster')
    ax.set_ylabel('Frequency (%)')
    
def runClusters(ref,
                box,
                keywords,
                cfg=dict(),
                kwds={'metric':'manhattan'},
                show=9,
                n=5,
                filters='null',
                title = 'null',
                size=10):
    
    if title == 'null':
        title = ''
    elif title[-1] != ' ':
        title = title + ' '
        
    if type(ref) is str:
        tweets,data = loadDataSet(ref,box,filters)
    
    
    if 'min_cluster_size' not in kwds.keys():
        kwds['min_cluster_size'] = max(int(len(data)*0.03),5)
        kwds['min_samples'] = max(kwds['min_cluster_size']/5,2)

    labels = getClusters(data, kwds)
    shapes = prepClusters(data,labels)
    data['label'] = labels
    
    show = min(show,len(shapes))+1
    show -= 1
    
    dispKey = {shapes.index[i]:shapes['keys'][i] for i in range(show)}
    textChunks = getTextSubsets(tweets,data,dispKey)
    
    indices, ax = plotClusters(shapes,data,box,show=show,title=title,size=size)
    plotChunkTimes(textChunks,title=title,size=size)
    plotKeywords(textChunks,keywords,n,title=title,size=size)

    plt.show()
    print "DEBOO"
    quit()
    return textChunks
    return shapes
    
#texts = runClusters(lymeTweetFile,vaBox,lymeKeywords,show=5,filters={'NLPCat':3},title='Lyme Disease')