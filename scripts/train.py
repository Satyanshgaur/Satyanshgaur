#!/usr/bin/env python3
import os
import torch
from datasets import load_dataset
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig
from trl import SFTTrainer, SFTConfig

MODEL_ID = "HuggingFaceTB/SmolLM-135M-Instruct"
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "train.jsonl")
OUTPUT_ADAPTER_DIR = os.path.join(os.path.dirname(__file__), "..", "adapter")

def train():
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[*] Training on device: {device}")
    
    if device == "cuda":
        print(f"[*] GPU: {torch.cuda.get_device_name(0)}")
        print(f"[*] VRAM Available: {torch.cuda.get_device_properties(0).total_memory / (1024**3):.2f} GB")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        dtype=torch.float16 if device == "cuda" else torch.float32,
        device_map="auto" if device == "cuda" else None
    )

    # LoRA Configuration
    peft_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )

    print(f"[*] Loading training data from: {DATA_PATH}")
    dataset = load_dataset("json", data_files=DATA_PATH, split="train")
    print(f"[*] Total training examples: {len(dataset)}")

    # SFT Training Arguments
    training_args = SFTConfig(
        output_dir="./checkpoints",
        num_train_epochs=12,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=2,
        learning_rate=6e-4,
        lr_scheduler_type="cosine",
        warmup_steps=2,
        logging_steps=2,
        fp16=(device == "cuda"),
        bf16=False,
        save_strategy="no",
        report_to="none",
        max_length=256,
    )

    trainer = SFTTrainer(
        model=model,
        train_dataset=dataset,
        peft_config=peft_config,
        args=training_args,
        processing_class=tokenizer,
    )

    print("\n[*] Starting LoRA fine-tuning on GPU with DATA.md technical dossier...")
    trainer.train()

    print(f"\n[*] Saving updated LoRA adapter to: {OUTPUT_ADAPTER_DIR}")
    os.makedirs(OUTPUT_ADAPTER_DIR, exist_ok=True)
    trainer.model.save_pretrained(OUTPUT_ADAPTER_DIR)
    tokenizer.save_pretrained(OUTPUT_ADAPTER_DIR)
    print("[*] LoRA fine-tuning complete and adapter successfully saved!")

if __name__ == "__main__":
    train()
