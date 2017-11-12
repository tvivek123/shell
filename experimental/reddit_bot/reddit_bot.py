#!/usr/bin/python2.7
import praw
import time
import os
import requests
import subprocess
from random import randrange

l = [ "you are a dumb", "you are a shit", "you are an asshole", "you are a fuck", "you are a bitch", "you are a piss", "you are drunk", "you are a bastard", "you are a dick", "you are a cunt", "your vagina", "FUCK you", "Fuck you", "you are a poo", "you are a douche", "you are a douchebag","stfu","Stfu","STFU","gtfo","GTFO","Gtfo" ]
#l = [ "stfu","Stfu","STFU","gtfo","GTFO","Gtfo" ]
def bot_authenticate():
	r = praw.Reddit('umadbrobot', user_agent = "umadbrobot does the thing where it soothes the nerves of angry redditors")
	print "i am happy"
	return r

def run_bot(r, comments_replied_to):
	print "Obtaining 25 comments..."
	for comment in r.subreddit('all').comments(limit=25):
#		if "stfu" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
		 d = comment.body
	         if any(word in d for word in l) and  comment.id not in comments_replied_to and comment.author != r.user.me():
			v = randrange(1,451)
###			subprocess.call(["./script.sh", str(v)])
			print "angry boy found!_______________________" + comment.id
			s = subprocess.check_output(["./script.sh", str(v)]) # + "\n\n\n\n" + "^(~~^im~~ ~~^a~~ ~~^degenerate~~ ~~^bot~~)"
			comment.reply(s)
			time.sleep(601)
#		if "fuck you!" in comment.body:
#			comment.reply("gud bois no svering. mouth shat. no tipe. dun dun dun happy face :D")
#			print "Replied to comment " + comment.id
			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")
			for com in r.user.me().comments.new(limit=25):
				if comment.score < 0:
					comment.delete()
#	for reply in r.inbox.comment_replies():
#		reply.reply("You just replied to a bot. that was stupid")
#		reply.mark_read()
#		time.sleep(600)
	print "Sleeping for 3 seconds..."
	#Sleep for 10 seconds...
	time.sleep(3)
def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to

#def main:
r = bot_authenticate()
comments_replied_to = get_saved_comments()
while True:
	run_bot(r, comments_replied_to)
