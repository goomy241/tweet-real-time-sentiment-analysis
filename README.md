# tweet-real-time-sentiment-analysis
ref: https://www.kdnuggets.com/2021/06/create-deploy-sentiment-analysis-app-api.html </br>

A web app for tweet sentiment analysis</br>

### Download Dependency
`pip install transformers`</br>
`pip install fastapi`</br>
`pip install uvicorn`</br>

### Request Format
http://127.0.0.1:8000/sentiment_analysis/?text=

### Sample Result
- Welcome page
<img width="1434" alt="welcome message" src="https://user-images.githubusercontent.com/90799662/167986337-c47c22a5-d8bf-4556-b753-352af59b86e6.png">

- Get a tweet
<img width="1439" alt="twitter_used" src="https://user-images.githubusercontent.com/90799662/167986347-aec9aa50-4fdc-4114-b8f6-039a9950d64a.png">

- Send the request and view the result
<img width="1434" alt="real-time result" src="https://user-images.githubusercontent.com/90799662/167986353-d34a5e95-2575-4c4a-aa2a-34e7dbe7a442.png">
