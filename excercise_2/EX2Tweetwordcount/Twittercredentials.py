import tweepy

consumer_key = "WZPDtmOILusm8w3vSjdxTIHZ5";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "JnuZokGOgOXXCqVM2rByZgAzvEEmx6FSPVJrg20gqbHOBSzzSM";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "210138770-nQwWSPzQl3M4nhCLA02SnrFnDrcLlZGFz9oMaui5";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "wHmRePNtDVnrqnIDHN13Br3dJHqJxrUFUgzQ5wnCHojSn";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



