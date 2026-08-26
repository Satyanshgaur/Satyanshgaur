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
    knowledge_path = os.path.join(os.path.dirname(__file__), "..", "data", "knowledge.json")
    topics = []
    projects = []
    if os.path.exists(knowledge_path):
        with open(knowledge_path, "r") as f:
            data = json.load(f)
            topics = data.get("topics", [])
            projects = data.get("projects", [])
    
    commits = get_git_activity()
    
    choices = []
    if commits:
        choices.append(f"Generate today's special from Satyansh's vault regarding recent work on '{commits[0]}'.")
    if projects:
        proj = random.choice(projects)
        choices.append(f"Generate today's special from Satyansh's vault regarding {proj}.")
    if topics:
        top = random.choice(topics)
        choices.append(f"Generate today's special from Satyansh's vault about {top}.")
        
    choices.extend([
        "Generate today's special from Satyansh's vault.",
        "What is today's special from Satyansh's technical vault?",
        "Give me today's special from Satyansh's vault."
    ])
    
    return random.choice(choices)

if __name__ == "__main__":
    prompt = get_dynamic_prompt()
    print(f"Prompt: {prompt}")
