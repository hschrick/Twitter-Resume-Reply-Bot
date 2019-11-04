import twitter_credentials
import tweepy
import PIL
from PIL import Image, ImageFilter
from urllib import urlretrieve
import time



class interpretor:

    def __init__(self):
        self.userList = []
        self.userKey = "hi welcome to my resume"
        f = open("tweets.text",'r')

        for line in f:
            self.userKey = line.strip()
            self.userList.append(self.userKey)


        f.close()
        #self.userList.append(self.userKey)
        print(self.userKey)



    def interpret(self):
        #           **********SIGN IN TO TWITTER USING KEYS FROM ANOTHER FILE **********
        auth = tweepy.OAuthHandler(twitter_credentials.CONSUMER_KEY, twitter_credentials.CONSUMER_SECRET)
        auth.set_access_token(twitter_credentials.ACCESS_TOKEN, twitter_credentials.ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)


        user = ''


        #           **********QUERY FOR CRAWLING SPECIFIED TAGS **********
        for tweet in tweepy.Cursor(api.search, q="YOUR BOTS QUERY HERE", count=1, lang="en", include_entities=True).items():
            if 'media' in tweet.entities:
                for image in tweet.entities['media']:

                    print("userkey: " + str(self.userList[-1]))
                    print("tweetid: " + str(tweet.id))

                        #if(str(self.userList[-1]) != str(tweet.id)):

                    #with open('tweets.text') as myfile:
                    if str(tweet.id) not in open("tweets.text").read():

                        #if(str(tweet.id) != line):
                        print("userkeyyyy : " + str(tweet.id))
                        print("tweetidddd : " + str(tweet.id))

                        self.userKey = tweet.id

                        # *****Write in users image to make editable *****
                        url = image['media_url']
                        self.filter_images(url)


                        self.userList.append(self.userKey)
                        # *****Send reply with edited image *****
                        api.update_with_media('edit.png', status='@' + tweet.user.screen_name + " here you go " + tweet.user.name + "\n\n\n check out my resume here: https://github.com/hschrick/resume/blob/master/Resume.pdf", in_reply_to_status_id=tweet.id)
                        f = open("tweets.text",'a')

                        f.write("\n"+str(self.userKey))

                        f.close()


                    break

            break



    def filter_images(self, url):
        urlretrieve(url, 'pic.jpg')

        # *****Filter images *****
        user = Image.open('pic.jpg')
        stamp = Image.open("STAMP IMAGE FILE")
        user.paste(chimp, (0,0))
        user.save('edit.png')






def main():

    inter = interpretor()
    while True:
        inter.interpret()
        print("[**********SLEEPING FOR 1 MINUTE**********]\n")
        time.sleep(30)
        print("[**********SLEEPING FOR 30 SECONDS**********]\n")
        time.sleep(20)
        print("[**********SLEEPING FOR 10 SECONDS**********]\n")
        time.sleep(10)
        print("[**********INTERPRETING DATA . . .**********]\n")


if __name__== "__main__":
  main()
