; (defproject tweetwordcount "0.0.1-SNAPSHOT"
;   :source-paths ["topologies"]
;   :resource-paths ["_resources"]
;   :target-path "_build"
;   :min-lein-version "2.0.0"
;   :jvm-opts ["-client"]
;   :dependencies  [[org.apache.storm/storm-core "0.9.5"]
;                   [com.parsely/streamparse "0.0.4-SNAPSHOT"]
;                   ]
;   :jar-exclusions     [#"log4j\.properties" #"backtype" #"trident" #"META-INF" #"meta-inf" #"\.yaml"]
;   :uberjar-exclusions [#"log4j\.properties" #"backtype" #"trident" #"META-INF" #"meta-inf" #"\.yaml"]
;   )


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
         {"Parse-tweet-bolt" :shuffle}
         "bolts.wordcount.WordCounter"
         ["word" "count"]
         :p 2 
        )
    }
  ]
)
