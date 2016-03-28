(ns tweetwordcount
  (:use [streamparse.specs])
  (:gen-class))

(defn tweetwordcount [options]
  [
    ;; Spout configuration
    {"Tweet-spout" (python-spout-spec
        options
        "spouts.tweets.Tweets"
        ["tweet"]
        )
    }
    ;;Bolt Configuration
    {"Parse-tweet-bolt" (python-bolt-spec
         options
         {"Tweet-spout" :shuffle}
         "bolts.parse.ParseTweet"
         ["valid_words"]
         :p 2 
        )

      "Count-tweet-bolt" (python-bolt-spec
         options
         {"Parse-tweet-bolt" ["valid_words"]}
         "bolts.wordcount.WordCounter"
         ["word" "count"]
         :p 2 
        )
    }
  ]
)
