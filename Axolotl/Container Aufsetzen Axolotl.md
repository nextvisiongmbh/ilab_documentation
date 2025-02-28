
## Init Container
``
sudo docker run -it --name axolotl_vg --gpus=1 nvidia/cuda:12.8.0-cudnn-devel-ubuntu24.04
``

## Install basic packages

```
apt-get update
apt-get install -y wget
apt-get install -y git
apt-get install -y curl
apt-get install -y nano
```
git lfs:
```
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash
apt-get install git-lfs
```

## Install Anaconda 
<a>https://docs.anaconda.com/anaconda/install/</a>

```
wget https://repo.anaconda.com/archive/Anaconda3-2024.10-1-Linux-x86_64.sh
bash ~/Anaconda3-2024.10-1-Linux-x86_64.sh
```
... accept config \
Update console: 

```
source ~/.bashrc
```

## Install axolotl
<a>https://axolotl-ai-cloud.github.io/axolotl/docs/installation.html</a>

```
conda create -n axolotl python=3.11
conda activate axolotl
pip install torch
pip install --no-build-isolation axolotl[flash-attn,deepspeed]
```

## Prepare Model

```
git clone https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407
git clone https://Vallout:<hf-token>@huggingface.co/mistralai/Mistral-Nemo-Instruct-2407
cd Mistral-Nemo-Instruct-2407/
```

## Retrieve Training Data

```
git clone https://github.com/nextvisiongmbh/ilab_documentation.git
cd ilab_documentation/
cd Datengenerierung
```

## Configure Axolotl

```
nano axolotl-config.yaml
```
File Content:
```
base_model: ./Mistral-Nemo-Instruct-2407
datasets:
  - path: /root/ilab_documentation/Datengenerierung/instruction_dataset.json
    type: alpaca
    dataset_type: instruct
lora_target_modules:
  - q_proj
  - v_proj
  - k_proj
special_tokens:
  pad_token: </s>
output_dir: ./fine-tuned-mistral
tokenizer_type: AutoTokenizer
adapter: lora
lora_r: 128
lora_alpha: 64
epochs: 3
micro_batch_size: 2
batch_size: 4
learning_rate: 2e-5
lr_scheduler_type: cosine
weight_decay: 0.01
save_steps: 500
logging_steps: 10
eval_steps: 100
warmup_steps: 100
load_in_8bit: true
```

## Training

```
axolotl train axolotl-config.yaml
```

## Inference (Testing)

Test fine-tuned model:
```
axolotl inference axolotl-config.yaml --lora-model-dir="./fine-tuned-mistral"
```
Test basic model: 
```
axolotl inference axolotl-config.yaml --base_model="./Mistral-Nemo-Instruct-2407/"
```