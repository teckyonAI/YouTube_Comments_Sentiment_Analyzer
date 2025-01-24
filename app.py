import streamlit as slt
import Preprocessing
import pandas as pd
import joblib
from wordcloud import WordCloud 
import seaborn as sns
import matplotlib.pyplot as plt

slt.set_page_config(layout="wide")
slt.title("Youtube Comments Sentiment Analysis")
url = slt.text_input('Youtube video Url')
# url = Preprocessing.set_url(url)
slt.sidebar.title("ZAINX")
slt.sidebar.header("Youtube_Comments")
slt.sidebar.write('Sentiment_Analysis')

if slt.button("Analyze"):
    with slt.spinner("ZAINX.."):
        video_key = Preprocessing.video_key(url)
        #slt.write(video_key)
        Preprocessing.scrape_comments(video_key)
        df = pd.read_csv('youtube-comments.csv')
        comments = df["Comment"].str.lower()
        df['Comment'] = comments
        
        # Cleaned Data
        df = Preprocessing.clean_df(df)
        # Predict Sentiments
        model = joblib.load('model1.pkl')
        cv = joblib.load('counter1.pkl') 
        df = Preprocessing.predict_sentiments(df,model,cv)
        slt.write(":heavy_minus_sign:" * 50)
        # CountPLot
        slt.header("Sentiments_Ratio")
        fig = plt.figure(figsize=(10, 4))
        sns.countplot(df["sentiments"])
        slt.pyplot(fig)
        slt.write(":heavy_minus_sign:" * 50)
        #Wordcloud of commments
        slt.header("Word_Cloud of Comments")
        df_sentences=df['Comment'].to_list()
        df_sentences = ' '.join([str(i) for i in df_sentences])
        figg = plt.figure(figsize = (20,20))
        plt.imshow(WordCloud().generate(df_sentences))
        slt.pyplot(figg)
        slt.write(":heavy_minus_sign:" * 50)
        # Top likes Comments
        slt.header("Top_liked_Comments")
        likes_df = df[(df['Likes']>1)].reset_index()
        likes_df=likes_df.drop('index',axis =1)
        slt.dataframe(data=likes_df)
        slt.write(":heavy_minus_sign:" * 50)
        # ALL Positive Comments
        slt.header("Positive_Comments")
        positive = df[(df['sentiments']!='Neutral') & (df['sentiments']!='Negative')].reset_index()
        positive=positive.drop('index',axis =1)
        slt.dataframe(positive)
        slt.write(":heavy_minus_sign:" * 50)
        # All Neutral Comments
        slt.header("Neutral_Comments")
        neutral =df[(df['sentiments']=='Neutral')].reset_index()
        neutral=neutral.drop('index',axis =1)
        slt.dataframe(neutral)
        slt.write(":heavy_minus_sign:" * 50)
