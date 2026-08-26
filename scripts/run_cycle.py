#!/usr/bin/env python3
import os
import sys
import subprocess
from fetch_activity import get_dynamic_prompt
from generate import load_model_and_tokenizer, generate_text, DEFAULT_MODEL
from update_readme import update_readme_content

def main():
    device = "cuda" if os.environ.get("USE_GPU", "1") == "1" else "cpu"
    # Auto fallback to CPU if CUDA is requested but not available
    import torch
    if device == "cuda" and not torch.cuda.is_available():
        device = "cpu"
        
    adapter_path = os.path.join(os.path.dirname(__file__), "..", "adapter")
    has_adapter = os.path.exists(os.path.join(adapter_path, "adapter_model.safetensors"))
    
    print("========================================")
    print("      satyansh-mini Autonomous Run      ")
    print("========================================")
    
    prompt = get_dynamic_prompt()
    print(f"[*] Prompt: {prompt}")
    
    model, tokenizer, dev = load_model_and_tokenizer(
        DEFAULT_MODEL,
        adapter_path=adapter_path if has_adapter else None,
        device=device
    )
    
    output = generate_text(
        model,
        tokenizer,
        prompt_text=prompt,
        device=dev,
        max_new_tokens=70,
        temperature=0.3,
        top_p=0.9
    )
    
    # Strip any residual quotes or wrapping markdown
    clean_output = output.strip().strip('"').strip("'")
    print(f"\n[*] Generated Output:\n{clean_output}\n")
    
    model_tag = "SmolLM-135M-Instruct (LoRA)" if has_adapter else "SmolLM-135M-Instruct (Base)"
    update_readme_content(clean_output, model_name=model_tag)
    print("========================================")

if __name__ == "__main__":
    main()
