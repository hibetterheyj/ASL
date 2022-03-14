# Main Lib

```shell
# CUDA 11.0
# pytorch=1.7.1, pytorch-lightning=1.2.0
conda create -n cl python=3.8
conda activate cl

# conda install pytorch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2 cudatoolkit=11.0 -c pytorch -y
pip install torch==1.7.1+cu110 torchvision==0.8.2+cu110 torchaudio==0.7.2 -f https://download.pytorch.org/whl/torch_stable.html

# conda install pytorch-lightning=1.2.0 -c conda-forge -y
pip install pytorch-lightning==1.2.0

python -m pip install --upgrade pip
python -m pip install cython
python -m pip install detectron2==0.4 -f \
  https://dl.fbaipublicfiles.com/detectron2/wheels/cu110/torch1.7/index.html

python -m pip install jupyterlab notebook
conda install -c conda-forge jupyterlab_pygments ipywidgets

# pydensecrf
# python -m pip install pydensecrf (cannot work)
python -m pip install git+https://github.com/lucasb-eyer/pydensecrf.git
```

- detectron2 installation guide: use release from <https://github.com/facebookresearch/detectron2/releases>
