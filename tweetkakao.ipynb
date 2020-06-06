{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "트윗 수집 기간은 2020-02-20 에서 2020-05-23 까지 입니다\n",
      "총 94일 간의 데이터 수집\n"
     ]
    }
   ],
   "source": [
    "import datetime\n",
    "\n",
    "days_range = []\n",
    "\n",
    "start = datetime.datetime.strptime(\"2020-02-20\", \"%Y-%m-%d\")\n",
    "end = datetime.datetime.strptime(\"2020-05-24\", \"%Y-%m-%d\")\n",
    "date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]\n",
    "\n",
    "for date in date_generated:\n",
    "    days_range.append(date.strftime(\"%Y-%m-%d\"))\n",
    "\n",
    "print(\"트윗 수집 기간은 {} 에서 {} 까지 입니다\".format(days_range[0], days_range[-1]))\n",
    "print(\"총 {}일 간의 데이터 수집\".format(len(days_range)))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import GetOldTweets3 as got\n",
    "tweetCriteria = got.manager.TweetCriteria().setQuerySearch('카톡 선물하기').setSince(\"2020-02-20\").setUntil(\"2020-05-24\")\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "데이터 수집 시작\n",
      "데이터 수집 완료= 1.53분\n",
      "총 트윗 개수 1049\n"
     ]
    }
   ],
   "source": [
    "import time \n",
    "# 수집\n",
    "print(\"데이터 수집 시작\") \n",
    "start_time = time.time() \n",
    "\n",
    "tweet = got.manager.TweetManager.getTweets(tweetCriteria)\n",
    "\n",
    "print(\"데이터 수집 완료= {0:0.2f}분\".format((time.time() - start_time)/60)) \n",
    "print(\"총 트윗 개수 {}\".format(len(tweet)))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "application/vnd.jupyter.widget-view+json": {
       "model_id": "29daca9e4bd84e35bab7edd0a7c05864",
       "version_major": 2,
       "version_minor": 0
      },
      "text/plain": [
       "HBox(children=(IntProgress(value=0, max=1049), HTML(value='')))"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n"
     ]
    }
   ],
   "source": [
    "from tqdm.notebook import tqdm \n",
    "tweet_list = [] \n",
    "\n",
    "for i in tqdm(tweet): \n",
    "    username = i.username \n",
    "    tweet_date = i.date.strftime(\"%Y-%m-%d\") \n",
    "    tweet_time = i.date.strftime(\"%H:%M:%dS\") \n",
    "    content = i.text \n",
    "    favorites = i.favorites \n",
    "    retweets = i.retweets \n",
    "    link = i.permalink \n",
    "    \n",
    "    info_list = [username, tweet_date, tweet_time, content, favorites, retweets, link] \n",
    "    tweet_list.append(info_list)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd \n",
    "# 데이터프레임 생성 \n",
    "twitter_df = pd.DataFrame(tweet_list, columns = [\"ID\", \"날짜\", \"시간\", \"내용\", \"리트윗 수\", \"좋아요 수\", \"링크\"])\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "twitter_df.to_excel('kakotalk_gift_crawing.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
