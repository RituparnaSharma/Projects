import tokenizers

MAX_LEN=128
TRAIN_BATCH_SIZE=32
TEST_BATCH_SIZE=4
VALID_BATCH_SIZE=8
EPOCHS=10
BASE_MODEL_PATH='bert-base-uncased'
VOCAB_PATH='/content/vocab.txt'
MODEL_PATH='model.bin'
TOKENIZER=tokenizers.BertWordPieceTokenizer(
    VOCAB_PATH,
    lowercase=True)
