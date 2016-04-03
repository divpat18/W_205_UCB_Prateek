This application was created and run on the AMI that Dan created for Ex2. In addition to that we must switch to Python 2.7 to be able to use tweepy.

The command for switching to python 2.7 is: "source /opt/py27environment/bin/activate"

The ami is missing the postgres installation. It was installed using the postgres installation steps from Ex2.

The application depends on psycopg2 to communicate with the postgres database and tweepy to communicate with Twitter.

To run the application:

Navigate to the tweetcont directory and run "sparse run -n tweetwordcount"

This runs the topolgy described in the Architecture documentation. 

To run the finalresults.py script use the following command: "python finalresults.py <word>"
If no word is specified it prints all the words in the tweetwordcount table.

To run the histogram.py use the following command: "python histogram.py <lowerCountLimit,upperCountLimit>"

Note: The histogram plot contains some expletives. That data from the live stream and we have no control over it. 

