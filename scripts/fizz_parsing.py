import json
import os

all_text = []

num_posts = 0

post_ids = []

# grab data
for filename in os.listdir('data/posts'):
    f = os.path.join('data/posts', filename)
    with open(f) as data_file:    
        data = json.load(data_file)
        if 'result' in data and 'posts' in data['result']:
            for post in data['result']['posts']:
                if('postID' in post and post['postID'] not in post_ids):
                    post_ids.append(post['postID'])
                    all_text.append(post['text'])
                    num_posts += 1

print(all_text)

print("FOUND "+str(num_posts)+" POSTS!")

# Serializing json
json_object = json.dumps({'posts':all_text}, indent=4)
 
# Writing to sample.json
with open('data/post_text.json', 'w') as outfile:
    outfile.write(json_object)
    outfile.close() 


with open('data/all_post_text.txt', 'w') as outfile:
    outfile.write('\n'.join(all_text))
    outfile.close() 