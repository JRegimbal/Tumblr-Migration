'''
INSTRUCTIONS:
    if you do not have python2.7 and pytumblr installed, do that first
    hint: use the "pip install pytumblr" command to make your life easier
    if not, install pytumblr from http://github.com/tumblr/pytumblr
    if you do it this way make sure you install all its dependencies!
USAGE:
    go to https://api.tumblr.com/console/
    enter the consumer key and consumer secret as listed below
    when prompted, authorize the app to use your account
    click "show keys" in the upper right corner and copy the following:
    copy token to oauth_token_u and token secret to oauth_token_secret_u
    make sure to copy and paste within the quotes
    after that, run and follow the prompts!
'''

import pytumblr
consumer_key = '6LUblGbJymy62VVUChoJovLMOL1Ae5VKfoFeKIKknOmuuu8Jfg'
consumer_secret = 'ul6rhKrbKt5fKfQBazk6TCeozaBtAF9Zi9yLL0BGmTCLcpP8MW'
oauth_token_u = ''
oauth_token_secret_u = ''

class Migration:
    def __init__(self):
        self.client = pytumblr.TumblrRestClient(consumer_key, consumer_secret, oauth_token_u, oauth_token_secret_u)
        return

    def setParams(self):
        self.from_blog = raw_input("Enter blog url to transfer from: ")
        self.to_blog = raw_input("Enter blog url to transfer to: ")
        return

    def transfer(self):
       posts = self.client.posts(self.from_blog)
       for post in reversed(posts['posts']):
           reblog_id = post['id']
           reblog_reblog_key = post['reblog_key']
           reblog_tags = post['tags']
           self.client.reblog(self.to_blog, id=reblog_id, reblog_key=reblog_reblog_key, tags=reblog_tags)
       print "All posts from " + self.from_blog + " have been transfered to " + self.to_blog + ".\n"    
       return
    def cleanup(self):
        response = raw_input("Do you want to delete all posts on the blog you just transfered from? [y/n] ")
        if response == 'y' or response =='Y':
            posts = self.client.posts(self.from_blog)
            for post in posts['posts']:
                self.client.delete_post(self.from_blog, id=post['id'])
            print "Your posts on the blog " + self.from_blog + " have been deleted \n"    
        elif response == 'n' or response == 'N':
            print "Okay. Your posts on the blog " + self.from_blog + " have been kept.\n"
        else:
            print "Invalid response. Please enter y(es) or n(o)\n"
            self.cleanup()
        return

migration = Migration()
migration.setParams()
migration.transfer()
migration.cleanup()
