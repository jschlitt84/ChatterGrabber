#Command to update code and cd to proper directory
prepDemo() {
cd ~/Desktop/ChatterGrabber_Demo
source workshopScripts.sh
git pull
}

compareSize() {
wc -l ~/Desktop/Results/Exercise*/ebolaTracker_CollectedTweets.csv
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


#Runs demo 1
runDemo1() {
prepDemo 
python TwitterSpout.py 'https://docs.google.com/spreadsheets/d/1pTIezGy3WsOBZhbv8W6Vl4QO7w13mI7SFrlAZVt05T8/edit#gid=0' -e
export EXPT='1'
closeDemo
}


#Runs demo 2a
runDemo2a() {
prepDemo
python TwitterSpout.py 'https://docs.google.com/spreadsheets/d/19PbY9h30orTlPY_s_DLgeRCICRNQzopdp3aw4pTjM74/edit#gid=0' -e
export EXPT='2a'
closeDemo
}

#Runs demo 2b
runDemo2b() {
prepDemo
python TwitterSpout.py 'https://docs.google.com/spreadsheets/d/1OiIJ2PosY4i5aRGRIqxTSHgE4jS34anbIzIyr8yqx9Q/' -e
export EXPT='2b'
closeDemo
}

#Runs demo 2c
runDemo2c() {
prepDemo
python TwitterSpout.py 'https://docs.google.com/spreadsheets/d/1EOH6_w_Qd3E3inqgT2UpP0jxvcJDvnE_9hId2gn73Y4/' -e
export EXPT='2c'
closeDemo
}

#Runs demo 3a
runDemo3a() {
prepDemo
python TwitterSpout.py 'https://docs.google.com/spreadsheets/d/1CJriN5AFgKaPmizDJC1XtosCfQ0A0lKObWKaZ0td4Bw/' -e
export EXPT='3a'
closeDemo
}

#Runs demo 3a
runDemo3b() {
prepDemo
python TwitterSpout.py 'https://docs.google.com/spreadsheets/d/1oGAnVf3tRbirLGlndot7DzlfCpFDzSghA_YtyAqnRR8/' -e
export EXPT='3b'
closeDemo
}

#Move sheet for 3c
moveSheet() {
mv ~/Downloads/EbolaScores1.csv\ -\ EbolaScores1.csv.csv ~/Desktop/ChatterGrabber_Demo/nlpTrainers/EbolaScores1.csv
}

#Runs demo 3c
runDemo3c() {
prepDemo
python TwitterSpout.py 'https://docs.google.com/spreadsheets/d/143XGZvKfMEm2vpNXUA--jvY11lxNt9lp7ZiVKxfQJdQ/' -e
export EXPT='3c'
closeDemo
}

#Runs demo 4
runDemo4() {
prepDemo
python TwitterSpout.py 'https://docs.google.com/spreadsheets/d/15FKEpeAc-l9pPoBYGBhPNfm0JpqUr7WRT4HJEgg8A24/' -e
export EXPT='4'
closeDemo
}

#Runs Final
finalDemo() {
prepDemo
python TwitterSpout.py 'https://docs.google.com/spreadsheets/d/1N5j04MDFL-2tOXezQyZStnBLnaWXgJwn0LmN5dH0wrw/' -e
export EXPT='Final'
closeDemo
}

rickRoll() {
firefox 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
}

trololo() {
firefox 'https://www.youtube.com/watch?v=2Z4m4lnjxkY'
}
