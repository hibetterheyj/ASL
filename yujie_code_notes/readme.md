# yujie_notes

## Env

```shell
conda install pytorch==1.10.1 torchvision==0.11.2 torchaudio==0.10.1 cudatoolkit=11.3 -c pytorch -c conda-forge
python -m pip install pytorch-lightning
python -m pip install opencv-python
python -m pip install gdown
```

## Dataset

- valscans.zip: around 100 scenes downloaded with poses etc. in this zip: <https://drive.google.com/file/d/1H8_soxzY-5rs8khGv-vWmBuZFsMzpoMA/view?usp=sharing>
- scannet_scenes_0to9.zip: scenes 0-9 that we used for the paper that you read: <https://drive.google.com/file/d/1rI6t0DYQMENS3dS2PTxulvSKa39Tf1Hq/view?usp=sharing>
- datapath in jonas folder on euler

```yaml
/cluster/work/riner/users/jonfrey/models/master_thesis
/cluster/work/riner/users/jonfrey/datasets/scannet
```

```shell
python download-scannet.py --preprocessed_frames -o ./scannet
gdown 1H8_soxzY-5rs8khGv-vWmBuZFsMzpoMA
```

- link to current working folder

`ln -s ~/data/cl_seg ./dataset`

### dataset missing files

- `FileNotFoundError: [Errno 2] No such file or directory: '/home/jonfrey/Datasets/scannet/scannetv2-labels.combined.tsv'`

```shell
python download-scannet.py --label_map -o ./cd ..
```

## Code running

> TODO: update README.md of ASL

```bash
# cd ~/ASL && python supervisor.py --exp=cfg/exp/MA/scannet/25k_pretrain/pretrain.py
# default: cfg/exp/MA/scannet_self_supervision/retrain_network/4_scenes/fast/debug_mem.yml
cd ~/cl_seg
python supervisor_new.py --exp=/home/he/projects/cl_seg/cfg/exp/baseline/scannet/25k_pretrain/scannet25k_pretrain.yml
python supervisor_new.py --exp=cfg/exp/baseline/scannet/25k_pretrain/scannet25k_pretrain.yml --env ws
```

### possible issues

- `ModuleNotFoundError: No module named 'pytorch_lightning.metrics'`

> <https://stackoverflow.com/questions/66807032/how-to-install-the-module-pytorch-lightning-metrics-in-raspberry-pi3>
> <https://torchmetrics.readthedocs.io/en/stable/classification/stat_scores.html?highlight=stat_scores#functional-interface>

> The metric returns a tensor of shape (..., 5), where the last dimension corresponds to [tp, fp, tn, fn, sup] (sup stands for support and equals tp + fn).

```python
# 'pytorch_lightning.metrics' are updated to 'torchmetrics' package
# from pytorch_lightning.metrics.functional.classification import stat_scores_multiple_classes
# TPS, FPS, TNS, FNS, _ = stat_scores_multiple_classes(
#       pred[b], target[b], num_classes + 1
#     )
from torchmetrics.functional import stat_scores
TPS, FPS, TNS, FNS, _ = stat_scores(pred[b], target[b], reduce='macro', num_classes=num_classes + 1)
```

- note: choose correct `reduce` argument

### test output

```shell
❯ python supervisor_new.py --exp=cfg/exp/baseline/scannet/25k_pretrain/scannet25k_pretrain.yml
# print(f"SUPERVISOR: Execute Task {sta}-{sto}")
SUPERVISOR: Execute Task 1-5
```

### tensorboard viz

- `get_tensorboard_logger`

```shell
from utils_asl import get_neptune_logger, get_tensorboard_logger
```

- possible issue about `AttributeError: module 'distutils' has no attribute 'version'
  - <https://github.com/pytorch/pytorch/issues/69894>
  - `pip install setuptools==59.5.0

### misc.

- local_rank meaning
  - In the context of multi-node training, you have:
    local_rank, the rank of the process on the local machine.
    rank, the rank of the process in the network.
    from <https://discuss.pytorch.org/t/what-is-the-difference-between-rank-and-local-rank/61940>
  - https://stackoverflow.com/questions/58833652/what-does-local-rank-mean-in-distributed-deep-learning
