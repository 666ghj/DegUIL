import os
import torch
from time import strftime, gmtime, localtime

ratio = 0.5
k = 10  # hit@k
device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu') # HACK: use cuda:1->3
model = 'DegUIL'
dataset = 'FT'
options = 'structure'
epochs = 100

# ---- netEncode ----
dim_feature = 256
num_layer = 2
lr = 5e-4
weight_decay = 1e-5
batch_size = 2 ** 7

# ---- UILAggregator ----
neg_num = 5
supervised = True
msa_out_dim = 64
alpha = 10
beta = 1

# ----- other config -----
percent = 99

# ---- MLP ----
MLP_hid = 128


log = strftime("logs/{}_{}_{}_{:.1f}_%m-%d_%H-%M-%S.txt".format( # HACK: %H:%M:%S非法路径更改为%H-%M-%S
        model, ''.join([s[0] for s in options.split()]), k, ratio
    ), localtime())

best_embs_file = ''


def init_args(args):
    global device, model, epochs, log, best_embs_file, dataset, ratio
    global alpha, beta

    ratio = args.ratio
    device = args.device
    model = args.model
    dataset = args.dataset

    log_path = './logs'
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    best_embs_path = './datasets/bestEmbs'
    if not os.path.exists(best_embs_path):
        os.mkdir(best_embs_path)

    # save embeds file of best mrr
    best_embs_file = os.path.join(best_embs_path, '{}_{}_{}_best_embs.pkl'.format(model, dataset, ratio))
    # best_embs_file = os.path.join(best_embs_path, '{}_{}_deg_best_embs.pkl'.format(model, dataset))

    log = strftime("logs/{}_{}_{}_{:.1f}_%m-%d_%H-%M-%S.txt".format( # HACK: %H:%M:%S非法路径更改为%H-%M-%S
        model, ''.join([s[0] for s in options.split()]), k, ratio
    ), localtime())

