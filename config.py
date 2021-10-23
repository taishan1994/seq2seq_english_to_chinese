class Config:
    data_dir = './data/'
    save_dir = './checkpoints/'
    load_dir = './checkpoints/translate-best.pt'

    do_train = False
    do_dev = False
    do_test = False
    do_evaluate = False
    do_predict = True
    do_load_model = True

    batch_size = 16
    learning_rate = 5e-4
    warmup_steps = 0.1
    dropout = 0.2
    num_epoch = 10
    max_vocab_size = 50000
    embed_size = 300
    enc_hidden_size = 512
    dec_hidden_size = 512
    GRAD_CLIP = 1.0

    PAD_IDX = 0
    UNK_IDX = 1

    beam_size = 5
    max_beam_search_length = 100
