#!/usr/bin/env python3
import json
import random
import os
import subprocess

def get_git_activity():
    try:
        res = subprocess.run(
            ["git", "log", "-n", "3", "--pretty=format:%s"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if res.returncode == 0 and res.stdout.strip():
            commits = res.stdout.strip().split("\n")
            return [c.strip() for c in commits if c.strip()]
    except Exception:
        pass
    return []

def get_dynamic_prompt():
    commits = get_git_activity()
    
    choices = [
        "Tell a technical joke about Satyansh.",
        "What does Satyansh think about GPUs?",
        "Generate a funny observation about Satyansh and performance.",
        "What is Satyansh's idea of code optimization?",
        "Tell me a joke about Satyansh learning low-level systems.",
        "Observation about Satyansh and memory management.",
        "What happens when Satyansh reviews CUDA code?",
        "What would Satyansh say about hardware limits?",
        "Tell a joke about Satyansh and multi-threading.",
        "What is Satyansh currently thinking?",
        "What does Satyansh think of high-performance computing?",
        "Observation about Satyansh and GPU computing."
    ]
    
    if commits:
        choices.append(f"Tell a technical joke about Satyansh working on '{commits[0]}'.")
        
    return random.choice(choices)

if __name__ == "__main__":
    prompt = get_dynamic_prompt()
    print(f"Prompt: {prompt}")
