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

> ***Steps involved in preprocessing and cleanning***

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

<p align="left">
  <img width="50%" height="50%" src='https://github.com/RituparnaSharma/Projects/blob/master/Twitter%20comments%20Sentiment%20Analyisis/Imagses/pepsi%20big.png'>
  <img width="50%" height="50%" src='https://github.com/RituparnaSharma/Projects/blob/master/Twitter%20comments%20Sentiment%20Analyisis/Imagses/pepsi.png'>
  <img width="70%" height="70%" src='https://github.com/RituparnaSharma/Projects/blob/master/Twitter%20comments%20Sentiment%20Analyisis/Imagses/frequent%20words.png'>
  
</p>




