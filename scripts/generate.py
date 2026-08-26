#!/usr/bin/env python3
import os
import argparse
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import PeftModel

DEFAULT_MODEL = "HuggingFaceTB/SmolLM-135M-Instruct"

def load_model_and_tokenizer(model_name=DEFAULT_MODEL, adapter_path=None, device="auto"):
    if device == "auto":
        device = "cuda" if torch.cuda.is_available() else "cpu"
    
    print(f"[*] Target device: {device}")
    print(f"[*] Loading base model: {model_name}")
    
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
        
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        dtype=torch.float16 if device == "cuda" else torch.float32,
    ).to(device)
    
    if adapter_path and os.path.exists(adapter_path):
        print(f"[*] Loading LoRA adapter from: {adapter_path}")
        model = PeftModel.from_pretrained(model, adapter_path)
    else:
        print("[*] No adapter loaded, running base model.")
        
    model.eval()
    return model, tokenizer, device

def generate_text(model, tokenizer, prompt_text=None, messages=None, device="cuda", max_new_tokens=80, temperature=0.3, top_p=0.9):
    if messages is None:
        if prompt_text is None:
            prompt_text = "Generate today's special from Satyansh's vault."
        messages = [
            {"role": "user", "content": prompt_text}
        ]
    
    input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    inputs = tokenizer(input_text, return_tensors="pt").to(device)
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_new_tokens,
            temperature=temperature,
            top_p=top_p,
            repetition_penalty=1.18,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )
    
    prompt_length = inputs["input_ids"].shape[1]
    generated_tokens = outputs[0][prompt_length:]
    response = tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()
    return response

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate thoughts with SmolLM-135M-Instruct")
    parser.add_argument("--prompt", type=str, default=None, help="Prompt text")
    parser.add_argument("--adapter", type=str, default="adapter", help="Path to LoRA adapter directory")
    parser.add_argument("--device", type=str, default="auto", choices=["auto", "cuda", "cpu"], help="Inference device")
    parser.add_argument("--max_tokens", type=int, default=80, help="Max new tokens")
    parser.add_argument("--temperature", type=float, default=0.3, help="Sampling temperature")
    
    args = parser.parse_args()
    
    adapter_dir = args.adapter if os.path.exists(args.adapter) else None
    model, tokenizer, dev = load_model_and_tokenizer(DEFAULT_MODEL, adapter_path=adapter_dir, device=args.device)
    
    print("\n--- Generating Output ---")
    output = generate_text(
        model, 
        tokenizer, 
        prompt_text=args.prompt, 
        device=dev, 
        max_new_tokens=args.max_tokens, 
        temperature=args.temperature
    )
    print(f"Generated Result:\n{output}\n")
