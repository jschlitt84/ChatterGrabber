from TweetMatch import *
directory = '/Users/jamesschlitt/ChatterGrabber/nlpTrainers/'

files = ["GunTrackerNLTK.csv","EmergNLTKScoring.csv","lymeScores.csv","vaccAutNLPScores.csv"]
degrees = [[1],[2],[3],[4],[1,2],[1,3],[1,4],[2,3],[2,4],[3,4],[2,3,4],[1,3,4],[1,2,3],[1,2,3,4]]

for degree in degrees:
    for inFile in files:
        accuracy = evalAccuracy(directory+inFile,"naive bayes",degree)
        print "Trainer: %s\t Degrees: %s\t Accuracy: %s\t" % (inFile,degree,accuracy)