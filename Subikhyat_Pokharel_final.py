import praw
import re
reddit = praw.Reddit(client_id='LPxIVzbv64QlEA', client_secret="nufPnXyg2YLICWpZtyrH1fac0TE",
                     password='', user_agent='Python',
                     username='supsip')
topic="netneutrality"
subreddit=reddit.subreddit(topic)
#subreddit=reddit.subreddit('news')

#ran this code once and save the file as netneutrality.txt and used that file for dataanalysis
'''num_of_post=subreddit.hot(limit=500)
i=1
j=1
with open(topic+".txt","w",encoding="utf-8")as myOutFile:
    for submission in num_of_post:
        #print(dir(submission))
        #print(str(i)+str(" Title: ")+ submission.title)
        myOutFile.write(str(20*"-------")+'\n'+str(i)+str(" Title: ")+ submission.title)
        submission.comments.replace_more(limit=0)
        for comment in submission.comments:
            #print(dir(comment))
            #print(comment.body+'\n')
            myOutFile.write(comment.body+'\n')
            if len(comment.replies)>0:
                for reply in comment.replies:
                    myOutFile.write(reply.body+'\n')
        i+=1
'''
link=[]
links=0
link_freq={}
name_rep=0
word_freq={}
with open(topic+".txt", encoding="utf-8")as myFile:
    for lines in myFile:
        line=lines.split(' ')
        #print(line)
        for word in line:
            #print(word)
            match=re.findall(r'https://\S+\.\S+', word)
            name_match = re.findall(r'Ajit', word)
            if match:
                #print(match)
                link.append(match)  #attach all the links to a list
                links += 1
                if word in link_freq:
                    link_freq[word] += 1
                else:
                    link_freq[word] = 1
            if name_match:
                #print(name_match)
                name_rep+=1
#print(dir(link))
#print(link)
print("1) There are "+str(links)+" links in the first 500 posts of the net neutrality posts on Reddit")
sort=sorted(link_freq.items(),key=lambda t:t[1],reverse=True)
print("2) The most frequently used link in the subreddit is "+str(sort[0][0])+" which was repeated "+str(sort[0][1])+" times")
print("3) Ajit Pai's name has been used "+str(name_rep)+" times on the subreddit "+str(topic))
with open(topic+".txt", encoding="utf-8")as myFile:
    for lines in myFile:
        line=lines.split(' ')
        #print(line)
        for word in line:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        #print(word_freq)
sorting=sorted(word_freq.items(),key=lambda t:t[1],reverse=True)
print("4) The most frequently used word in the subreddit is "+list(word_freq.keys())[4])   #The first 3 keys in the dictionary were symbols, the word Title and The
