
<p align="center">
  <img width="30%" height="30%" src='https://github.com/RituparnaSharma/Projects/blob/master/Text%20Summerization%20using%20Transformer/Images/circle-cropped(1).png'>
</p>
<p align='center'>
  <h2 align='center'>Text Summerization Using BERT </h2>
</p>
 
 ## About
 
This repo is the used to make a model on sentiment summerizer. This tool utilizes the HuggingFace Pytorch transformers library to run extractive summarizations. This works by first embedding the sentences, then classify its starting and ending index of summerized text to get the summerize output.The advantage of using this repo is computation time,due to its smart batching technique its create a great differnce in between compuration time and performnce also.

#### (smart batching technique is used to reduce the number of trainable parameters.Where each text is being paded to the maximuminput length of each batch,which reduce the number of parameter will be used)

-Datset : https://www.kaggle.com/c/tweet-sentiment-extraction/

## Requirements
- Python 3.6.5+
- Pytorch 0.4.1+
- transformers(Huuging-face)
- Pandas
- skleran
- tqdm
- Numpy

## Data Directory

``` bash
`-- data                                 # under workspace 
    |-- checkpoint
    |   |-- config.json                  # BERT config file
    |   |-- model.bin                    # BERT model file
    |   |-- kaggle.json                  # kaggle API 
    |   |-- vocab.txt                    # vocabulary file
    |-- text_filtering_using_bert.ipynb  # train and valid data file
```
## config


