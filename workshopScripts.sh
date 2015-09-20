#Command to update code and cd to proper directory
prepDemo() {
cd ~/Desktop/ChatterGrabber_Demo
source workshopScripts.sh
git pull
}

#Command to move results to uncompressed folder on desktop
closeDemo() {
export TEMPDIR='/home/chattergrabber/Desktop/Results/Exercise_'$EXPT
#rm -rf $TEMPDIR
mkdir -p $TEMPDIR
unzip -o ~/Desktop/ChatterGrabber_Demo/studies/ebolaTracker/search/CollectedTweets.zip -d $TEMPDIR
echo "Experiment "$EXPT" has completed, results may be found in the 'Results' folder on the desktop!"
printf '\n'
nautilus $TEMPDIR
}

#Open daemonScript
adminSetup() {
gedit ~/Desktop/ChatterGrabber_Demo/daemonScripts/gdiAccounts
}


#Runs demo 1a
runDemo1A() {
prepDemo 
python TwitterSpout.py 'https://docs.google.com/spreadsheets/d/1pTIezGy3WsOBZhbv8W6Vl4QO7w13mI7SFrlAZVt05T8/edit#gid=0' -e
export EXPT='1A'
closeDemo
}


#Runs demo 2a
runDemo2A() {
prepDemo
python TwitterSpout.py 'https://docs.google.com/spreadsheets/d/19PbY9h30orTlPY_s_DLgeRCICRNQzopdp3aw4pTjM74/edit#gid=0' -e
export EXPT='2A'
closeDemo
}



