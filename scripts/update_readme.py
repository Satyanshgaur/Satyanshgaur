#!/usr/bin/env python3
import os
import re
import json
import textwrap
from datetime import datetime, timezone

README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")
STATE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "state.json")
START_TAG = "<!-- satyansh-mini:start -->"
END_TAG = "<!-- satyansh-mini:end -->"

def load_state():
    if os.path.exists(STATE_PATH):
        try:
            with open(STATE_PATH, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {"generation_count": 0, "last_updated": None}

def save_state(state):
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    with open(STATE_PATH, "w") as f:
        json.dump(state, f, indent=2)

def update_readme_content(generated_text, model_name="SmolLM-135M-Instruct", lora_name="satyansh-lora-r16"):
    state = load_state()
    state["generation_count"] += 1
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    state["last_updated"] = now_utc
    save_state(state)
    
    count = state["generation_count"]
    clean_text = generated_text.strip().strip('"').strip("'")
    
    # Wrap text cleanly for the wide terminal box (width ~92 chars)
    wrapped_lines = textwrap.wrap(clean_text, width=92)
    if not wrapped_lines:
        wrapped_lines = [clean_text]
    inner_text = "\n".join([f"| {line:<98} |" for line in wrapped_lines])
    
    meta_line = f"[ Run: #{count:04d} | Model: {model_name} | LoRA: {lora_name} | Runner: GitHub Actions (CPU) ]"
    meta_formatted = f"| {meta_line:<98} |"
    
    formatted_block = f"""{START_TAG}
{inner_text}
|                                                                                                    |
{meta_formatted}
{END_TAG}"""

    if not os.path.exists(README_PATH):
        print(f"[!] {README_PATH} not found.")
        return False
        
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
        
    pattern = re.compile(rf"{re.escape(START_TAG)}[\s\S]*?{re.escape(END_TAG)}")
    if pattern.search(content):
        new_content = pattern.sub(lambda _: formatted_block, content)
    else:
        print("[!] Delimiter tags not found in README.")
        return False
        
    with open(README_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print(f"[*] README.md updated successfully (Generation #{count})")
    return True

if __name__ == "__main__":
    import sys
    text = sys.argv[1] if len(sys.argv) > 1 else "today's special from satyansh's vault: Hardware reality dictates software architecture."
    update_readme_content(text)
