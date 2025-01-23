# Intructlab Setup
## Instructlab Container aufsetzen

sudo docker run -it --name instructlab_vg --gpus=1 nvidia/cuda:12.6.3-cudnn-devel-rockylinux9

Script im container ausführen:

https://github.com/nextvisiongmbh/admin/blob/main/scripts/instructlab.sh

```
#/bin/bash
set -e

dnf install -y gcc gcc-c++ make git python3.11 python3.11-devel which

git clone https://github.com/instructlab/instructlab || true
cd instructlab

python3.11 -m venv --upgrade-deps .venv
source .venv/bin/activate
pip cache remove llama_cpp_python

pip install torch psutil
pip install flash-attn --no-build-isolation

CMAKE_ARGS="-DGGML_CUDA=on -DGGML_NATIVE=off" pip install -e .[cuda]
pip install vllm@git+https://github.com/opendatahub-io/vllm@v0.6.2

# Faster model download
pip install huggingface_hub[hf_transfer]
export HF_HUB_ENABLE_HF_TRANSFER=1

# If you are working on instructlab itself:
if [ -n "$DEV" ]; then
    dnf install -y \
        https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm \
        https://dl.fedoraproject.org/pub/epel/epel-next-release-latest-9.noarch.rpm

    dnf config-manager --set-enabled crb
    dnf install -y aspell-en expect
    CMAKE_ARGS="-DGGML_CUDA=on -DGGML_NATIVE=off" pip install -r requirements-dev.txt
fi
```

## Zusätzlich

```
dnf install -y wget
dnf install -y nano
```

## Config

``ilab config init``

Path to model: /root/.cache/instructlab/models/Mistral-Nemo-Instruct-2407.Q4_K_M.gguf



## Modelle herunterladen

### Für einfache Inferenz und Datengenerierung:
``ilab model download -rp MaziyarPanahi/Mistral-Nemo-Instruct-2407-GGUF --filename Mistral-Nemo-Instruct-2407.Q4_K_M.gguf --hf-token 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``
### Für Training (Safe-Tensor Modell):
``ilab model download --repository mistralai/Mistral-Nemo-Instruct-2407 --hf-token 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``
### Ilab Granite Modell als Baseline:
``ilab model download --repository instructlab/granite-7b-lab --hf-token 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``

## Taxonomie erstellen

``mkdir -p /root/.local/share/instructlab/taxonomy/compositional_skills/technology/tables/dates``

``cd /root/.local/share/instructlab/taxonomy/compositional_skills/technology/tables/dates``

``wget https://raw.githubusercontent.com/nextvisiongmbh/taxonomy_tests/refs/heads/main/skills/science/tables/qna.yaml``

### Check validity
`ilab taxonomy diff`

Gewünschter Output: ``Taxonomy in /root/.local/share/instructlab/taxonomy is valid :)``

## Daten generieren

### Model Serven
``ilab model serve --model-path /root/.cache/instructlab/models/Mistral-Nemo-Instruct-2407.Q4_K_M.gguf --backend llama-cpp --gpus 1``
### Daten generieren
``ilab data generate --endpoint-url http://localhost:8000/v1``
## Modell trainieren

Generierte Daten anzeigen:
``cd /root/.local/share/instructlab/datasets/``



``ilab model train --data-path /root/.local/share/instructlab/datasets/messages_Mixtral-8x7B-Instruct-v0_2025-01-17T15_46_59.jsonl --model-path /root/.cache/instructlab/models/mistralai/Mistral-Nemo-Instruct-2407 --device cuda --pipeline accelerated --disable-accelerate-full-state-at-epoch --is-padding-free 0 --lora-rank 128``