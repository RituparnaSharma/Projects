
<p align="center">
  <img width="30%" height="30%" src='https://github.com/RituparnaSharma/Projects/blob/master/Text%20Summerization%20using%20Transformer/Images/circle-cropped(1).png'>
</p>
<p align='center'>
  <h2 align='center'>Text Summerization Using BERT </h2>
</p>
 
 ## About
 
This repo is used to build a model on sentiment summarization. This model uses the Hugging Face Pytorch Transformer library to run extractive summaries. It works by embedding sentences first, then classifying their initial and final indexes of the consolidated text to obtain a summarized output. The advantage of using this repo is the computation time, there is also a considerable difference between computation time and performance due to its smart batching technique.



#### (A smart batching technique is used to reduce the number of train parameters. Any text anywhere is being padded to the maximum input length of each batch, which will reduce the number of parameters.)

- Dataset : https://www.kaggle.com/c/tweet-sentiment-extraction/

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
<br>
</br>

Parameters|Value|
|--------------------|-------------------|
| Model    | ***'bert-base-uncased'*** |
| Embedding Dimension | 768 |
| Output Dimension| 2 |
| Train batch size | 32 |
| Test batch size | 8 |
| Tokenizer | BertWordPieceTokenizer |
| Optimizer | AdamW |
| Learning Rate | 3e-5 |
| loss Function | BCEWithLogitsLoss |

<br>
</br>

## Technologies used 
<br>
</br>

<p align="left">
  <img width="70%" height="100%" src='https://github.com/RituparnaSharma/Projects/blob/master/Text%20Summerization%20using%20Transformer/Images/Technologies.png'>
</p>

<br>
</br>

## credits
<br>
</br>

***_[Attention is all you Need -- ](https://arxiv.org/abs/1706.03762)_*** _Thanks to the Authors of this paper for their ammzing contribution to the field of NLP._


***_[Jay Alammar -- ](http://jalammar.github.io/illustrated-bert/)_*** _Illustrated example of Bert._


***_[Abhishek Thakur -- ](https://www.kaggle.com/abhishek)_*** _This Project would not have been possible without his vertual assitance.Most of the code that I have used in this repo is taken from his  [NoteBook](https://www.kaggle.com/abhishek/bert-base-uncased-using-pytorch)._
