<p align="center">
  <img width="30%" height="30%" src='https://github.com/RituparnaSharma/Projects/blob/master/Twitter%20comments%20Sentiment%20Analyisis/Imagses/imageonline-co-roundcorner.png'>
</p>
<p align='center'>
  <h2 align='center'>An Approach to twitter sentiment Analysis</h2>
</p>
<br>
</br>

## DEMO
<p align="left">
  <img width="70%" height="70%" src='https://github.com/RituparnaSharma/Projects/blob/master/Twitter%20comments%20Sentiment%20Analyisis/Imagses/tweet_ui.png'>
</p>

## OBJECTIVES

_This is a simple sentiment analysis prediction model.In this repository there are two model.each model is building on different dataset.
First dataset is scrabed from ### scholl out of 1.5 million sample i used only 1700 samples due to low computational memory.

> ***First Model configuration***

- data type='text'
- no of tweet:
- labels:
_Second model was the part of a hackathon.where we have given a dataset regarding an event callled SXSW held at austin.In first model I have got almost 72 percent accuarcy where as in the second model I have got 68 percent accuracy .
> ***Second Model configuration***

- data type='text'
- no of tweet:
- labels:

## About SXSW DATASET:
<br>
</br>

> ***Steps involved in preprocessing and cleanning***

<br>
</br>

Before Preprocessing |After Preprocessing|
|--------------------|-------------------|
| User Mentions       | User Mentions With @ are removed |
| HTML character such as '&lt','&gt' | converted to their appropriate signs '<','>' |
| Emojis :) (: | converted to word such as Happy,Sad etc |
| urls and links | Removed (only 3% at most tweet has URL's) |
| Abbreviations 'b4','gr8' | Converted to full forms |
| Non-ASCII characters | Removed |
| Long word such as 'Woooooo','Funnyyy' | Corrected to their proper Forms 'Wow','Funny' |
| Stop words and Punctuation | Removed |
<br>
</br>

> ***Overall sentiment of the event***
<br>
</br>
<p align="left">
  <img width="50%" height="50%" src='https://github.com/RituparnaSharma/Projects/blob/master/Twitter%20comments%20Sentiment%20Analyisis/Imagses/pi%20diagram-crop.png'>
</p>

> ***Frequently used words***
<p align="left">
  <img width="70%" height="50%" src='https://github.com/RituparnaSharma/Projects/blob/master/Twitter%20comments%20Sentiment%20Analyisis/Imagses/frequent%20words-crop.png'>
</p>
<br>
</br>

> ***Sponsers of the event***

<br>
</br>
<p align="left">
  <img width="50%" height="70%" src='https://github.com/RituparnaSharma/Projects/blob/master/Twitter%20comments%20Sentiment%20Analyisis/Imagses/imageonline-co-merged-image(1).png'>
  <br>
  </br>
  <img width="50%" height="70%" src='https://github.com/RituparnaSharma/Projects/blob/master/Twitter%20comments%20Sentiment%20Analyisis/Imagses/imageonline-co-merged-image(2).png'>
<br>
</br>

> ***Models Training and Testing***

<br>
</br>

|model |technique |Train F1 score |Test F1 Score |
|--------------------|-------------------|--------------------|-------------------|
| ***Logistic Regression***      | ***Count vectorizer*** | ***0.65*** | ***0.68***|
| Logistic Regression       | Count vectorizer + steeming | 0.64 | 0.66 |
| Logistic Regression       | Count vectorizer + Lemitization | 0.64 | 0.64 |
| Logistic Regression       | Tf-Idf | 0.65 | 0.65 |
| Logistic Regression       | Tf-Idf + Lemitization | 0.62 | 0.65 |
| ***SVC***    | ***Tf-Idf + Lemitization*** | ***0.65*** | ***0.68*** |
| Gaussian Naive Bayes       | Count vectorizer | 0.49 | 0.47 |
| Random Forrest     | Count vectorizer | 0.65 | 0.63 |
| XGBoost       | With Hyperparameter tuning and random oversampling | 0.84 | 0.66 |

<br>
</br>

> ***Final Insights***

<br>
</br>

- The event overall had a positive and neutral impact.
- There was a slight negative impact due to earthquake happened in Japan.
- Market small promising brands more.

## Technologies used

<br>
</br>

<p align="left">
  <img width="50%" height="70%" src='https://github.com/RituparnaSharma/Projects/blob/master/Twitter%20comments%20Sentiment%20Analyisis/Imagses/imageonline-co-merged-image(4).png'>
</p>
  
 <br>
</br>

