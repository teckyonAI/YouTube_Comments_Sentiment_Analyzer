import pandas as pd
from googleapiclient.discovery import build

def set_url(url):
  
    start = '//'
    url=(url.split(start))[1]
    return url

def video_key(url):
    start = 'watch?v='
    end = '&'
    url=(url.split(start))[1].split(end)[0]
    return url
def scrape_comments(ID):
    api_key = "AIzaSyDQbvPYV1sYRiE109Les7R1yDLIZXhLeTw" 
    youtube = build('youtube', 'v3', developerKey=api_key)
    box = [[ 'Comment', 'Likes']]
    data = youtube.commentThreads().list(part='snippet', videoId=ID, maxResults='100', textFormat="plainText").execute()

    for i in data["items"]:

        
        comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]
        
        likes = i["snippet"]['topLevelComment']["snippet"]['likeCount']
        

        box.append([ comment, likes, ])

        totalReplyCount = i["snippet"]['totalReplyCount']

        if totalReplyCount > 0:

            parent = i["snippet"]['topLevelComment']["id"]

            data2 = youtube.comments().list(part='snippet', maxResults='100', parentId=parent,
                                            textFormat="plainText").execute()

            for i in data2["items"]:
                
                comment = i["snippet"]["textDisplay"]
                
                likes = i["snippet"]['likeCount']
                

                box.append([ comment,  likes, ])

    while ("nextPageToken" in data):

        data = youtube.commentThreads().list(part='snippet', videoId=ID, pageToken=data["nextPageToken"],
                                             maxResults='100', textFormat="plainText").execute()

        for i in data["items"]:
            
            comment = i["snippet"]['topLevelComment']["snippet"]["textDisplay"]
            
            likes = i["snippet"]['topLevelComment']["snippet"]['likeCount']
            

            box.append([comment, likes])

            totalReplyCount = i["snippet"]['totalReplyCount']

            if totalReplyCount > 0:

                parent = i["snippet"]['topLevelComment']["id"]

                data2 = youtube.comments().list(part='snippet', maxResults='100', parentId=parent,
                                                textFormat="plainText").execute()

                for i in data2["items"]:
                    
                    comment = i["snippet"]["textDisplay"]
                    
                    likes = i["snippet"]['likeCount']
                    

                    box.append([comment, likes])

    df = pd.DataFrame({'Comment': [i[0] for i in box],
                       'Likes': [i[1] for i in box]})

    df.to_csv('youtube-comments.csv', index=False, header=False)


def clean_df (df):
    df["Comment"] = df["Comment"].str.replace(':',' ', regex=True).replace('(','').replace(')','').replace('{','').replace('}','').replace('!','').replace('/','').replace(',','').replace(" '' ",'')
    return df

def predict_sentiments(df,model,cv):
    
    sentiments=[]
    for i in range(0,len(df)):
        vect = cv.transform(df['Comment'].values.astype('U'))
        prediction = model.predict(vect[i])
        if prediction >= 0.6:
            label="Positive "
        elif  prediction < 0.00001:
            label="Neutral"  
        elif prediction<= 0.2:
            label="Negative"
    
        sentiments.append(label)
    df['sentiments'] = sentiments 
    return df
