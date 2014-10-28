from CGVis import *
from dateutil import parser

vaccData = {'name':'VaccAut Tracker',
             'file':"/Users/jamesschlitt/ChatterGrabber/studies/vaccAut/search/vaccAut_CollectedTweets.csv",
             'cats':'null'}


allData = {vaccData['name']:vaccData}

for exp in allData.keys():
    allData[exp]['data'] = pd.DataFrame.from_csv(allData[exp]['file'],index_col='id')

outDir = '/Users/jamesschlitt/ChatterGrabber/studies/vaccAut/'
makeTimeLine(vaccData,name='images',sort='NLPCat',keep=[1,2,3,4,5],directory=outDir)
makeTimeLine(vaccData,name='links',sort='NLPCat',keep=[1,2,3,4,5],directory=outDir)