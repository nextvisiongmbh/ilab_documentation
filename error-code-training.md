```model_name_or_path: /root/.cache/instructlab/models/mistralai/Mistral-Nemo-Instruct-2407
data_path: /root/.local/share/instructlab/internal/data.jsonl
output_dir: /root/.local/share/instructlab/checkpoints
num_epochs: 8
current_epoch: 0
last_step: 0
effective_batch_size: 96
learning_rate: 2.0e-05
lr_scheduler: cosine
num_warmup_steps: 25
save_samples: 1000
save_samples_ds: null
save_last: false
checkpoint_at_epoch: true
accelerate_full_state_at_epoch: false
log_level: INFO
seed: 42
mock_data: false
mock_len: 2600
distributed_training_framework: deepspeed
fsdp_sharding_strategy: SHARD_GRAD_OP
use_dolomite: false
lora_r: 128
lora_alpha: 32
lora_dropout: 0.1
lora_quant_bits: null
lora_target_modules:
- q_proj
- k_proj
- v_proj
- o_proj
max_batch_len: 60000
cpu_offload_optimizer: true
cpu_offload_params_fsdp: false
cpu_offload_optimizer_pin_memory: true
cpu_offload_optimizer_ratio: 1.0
NEFTune_alpha: null
chat_tmpl_path: /instructlab/.venv/lib64/python3.11/site-packages/instructlab/training/chat_templates/ibm_generic_tmpl.py
disable_flash_attn: false

{
    "script_params": {
        "model_name_or_path": "/root/.cache/instructlab/models/mistralai/Mistral-Nemo-Instruct-2407",
        "data_path": "/root/.local/share/instructlab/internal/data.jsonl",
        "output_dir": "/root/.local/share/instructlab/checkpoints",
        "num_epochs": 8,
        "current_epoch": 0,
        "last_step": 0,
        "effective_batch_size": 96,
        "learning_rate": 2e-05,
        "lr_scheduler": "cosine",
        "num_warmup_steps": 25,
        "save_samples": 1000,
        "save_samples_ds": null,
        "save_last": false,
        "checkpoint_at_epoch": true,
        "accelerate_full_state_at_epoch": false,
        "log_level": "INFO",
        "seed": 42,
        "mock_data": false,
        "mock_len": 2600,
        "distributed_training_framework": "deepspeed",
        "fsdp_sharding_strategy": "SHARD_GRAD_OP",
        "use_dolomite": false,
        "lora_r": 128,
        "lora_alpha": 32,
        "lora_dropout": 0.1,
        "lora_quant_bits": null,
        "lora_target_modules": [
            "q_proj",
            "k_proj",
            "v_proj",
            "o_proj"
        ],
        "max_batch_len": 60000,
        "cpu_offload_optimizer": true,
        "cpu_offload_params_fsdp": false,
        "cpu_offload_optimizer_pin_memory": true,
        "cpu_offload_optimizer_ratio": 1.0,
        "NEFTune_alpha": null,
        "chat_tmpl_path": "/instructlab/.venv/lib64/python3.11/site-packages/instructlab/training/chat_templates/ibm_generic_tmpl.py",
        "disable_flash_attn": false
    },
    "timestamp": "2025-01-20T07:54:41.684525"
}
Traceback (most recent call last):
  File "/instructlab/.venv/lib64/python3.11/site-packages/instructlab/training/main_ds.py", line 967, in <module>
    main(args)
  File "/instructlab/.venv/lib64/python3.11/site-packages/instructlab/training/main_ds.py", line 546, in main
    torch.cuda.set_device(int(os.environ["LOCAL_RANK"]))
  File "/instructlab/.venv/lib64/python3.11/site-packages/torch/cuda/__init__.py", line 420, in set_device
    torch._C._cuda_setDevice(device)
RuntimeError: CUDA error: invalid device ordinal
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

W0120 07:54:42.803000 139975510218560 torch/distributed/elastic/multiprocessing/api.py:858] Sending process 15625 closing signal SIGTERM
E0120 07:54:43.017000 139975510218560 torch/distributed/elastic/multiprocessing/api.py:833] failed (exitcode: 1) local_rank: 1 (pid: 15626) of binary: /instructlab/.venv/bin/python3.11
Traceback (most recent call last):
  File "/instructlab/.venv/bin/torchrun", line 8, in <module>
    sys.exit(main())
             ^^^^^^
  File "/instructlab/.venv/lib64/python3.11/site-packages/torch/distributed/elastic/multiprocessing/errors/__init__.py", line 348, in wrapper
    return f(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^
  File "/instructlab/.venv/lib64/python3.11/site-packages/torch/distributed/run.py", line 901, in main
    run(args)
  File "/instructlab/.venv/lib64/python3.11/site-packages/torch/distributed/run.py", line 892, in run
    elastic_launch(
  File "/instructlab/.venv/lib64/python3.11/site-packages/torch/distributed/launcher/api.py", line 133, in __call__
    return launch_agent(self._config, self._entrypoint, list(args))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/instructlab/.venv/lib64/python3.11/site-packages/torch/distributed/launcher/api.py", line 264, in launch_agent
    raise ChildFailedError(
torch.distributed.elastic.multiprocessing.errors.ChildFailedError:
============================================================
/instructlab/.venv/lib64/python3.11/site-packages/instructlab/training/main_ds.py FAILED
------------------------------------------------------------
Failures:
  <NO_OTHER_FAILURES>
------------------------------------------------------------
Root Cause (first observed failure):
[0]:
  time      : 2025-01-20_07:54:42
  host      : c0b201f42398
  rank      : 1 (local_rank: 1)
  exitcode  : 1 (pid: 15626)
  error_file: <N/A>
  traceback : To enable traceback see: https://pytorch.org/docs/stable/elastic/errors.html
============================================================
Training subprocess has not exited yet. Sending SIGTERM.
Waiting for process to exit, 60s...
--- Logging error ---
Traceback (most recent call last):
  File "/instructlab/src/instructlab/model/accelerated_train.py", line 233, in accelerated_train
    run_training(train_args=train_args, torch_args=torch_args)
  File "/instructlab/.venv/lib64/python3.11/site-packages/instructlab/training/__init__.py", line 36, in run_training
    return run_training(torch_args=torch_args, train_args=train_args)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/instructlab/.venv/lib64/python3.11/site-packages/instructlab/training/main_ds.py", line 831, in run_training
    raise RuntimeError(
RuntimeError: Suffered a failure during distributed training. Please see the training logs for more context.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib64/python3.11/logging/__init__.py", line 1110, in emit
    msg = self.format(record)
          ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/logging/__init__.py", line 953, in format
    return fmt.format(record)
           ^^^^^^^^^^^^^^^^^^
  File "/instructlab/src/instructlab/log.py", line 19, in format
    return super().format(record)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/logging/__init__.py", line 687, in format
    record.message = record.getMessage()
                     ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib64/python3.11/logging/__init__.py", line 377, in getMessage
    msg = msg % self.args
          ~~~~^~~~~~~~~~~
TypeError: not all arguments converted during string formatting
Call stack:
  File "/instructlab/.venv/bin/ilab", line 8, in <module>
    sys.exit(ilab())
  File "/instructlab/.venv/lib64/python3.11/site-packages/click/core.py", line 1161, in __call__
    return self.main(*args, **kwargs)
  File "/instructlab/.venv/lib64/python3.11/site-packages/click/core.py", line 1082, in main
    rv = self.invoke(ctx)
  File "/instructlab/.venv/lib64/python3.11/site-packages/click/core.py", line 1697, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/instructlab/.venv/lib64/python3.11/site-packages/click/core.py", line 1697, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/instructlab/.venv/lib64/python3.11/site-packages/click/core.py", line 1443, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/instructlab/.venv/lib64/python3.11/site-packages/click/core.py", line 788, in invoke
    return __callback(*args, **kwargs)
  File "/instructlab/.venv/lib64/python3.11/site-packages/click/decorators.py", line 33, in new_func
    return f(get_current_context(), *args, **kwargs)
  File "/instructlab/src/instructlab/clickext.py", line 354, in wrapper
    return f(*args, **kwargs)
  File "/instructlab/src/instructlab/cli/model/train.py", line 469, in train
    accelerated_train.accelerated_train(
  File "/instructlab/src/instructlab/model/accelerated_train.py", line 236, in accelerated_train
    logger.error("Failed during training loop: ", e)
Message: 'Failed during training loop: '
Arguments: (RuntimeError('Suffered a failure during distributed training. Please see the training logs for more context.'),)
Accelerated Training failed with 1
```

Fehler war aufgetreten, da mehr GPUs eingetragen waren, als verfügbar. 

Korrekte Einstellung:

`nproc_per_node: 1`
