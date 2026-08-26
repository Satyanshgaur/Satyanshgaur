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

def update_readme_content(generated_text, model_name="SmolLM-135M-Instruct", lora_name="satyansh-lora-r16 (PEFT)"):
    state = load_state()
    state["generation_count"] += 1
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    state["last_updated"] = now_utc
    save_state(state)
    
    count = state["generation_count"]
    clean_text = generated_text.strip().strip('"').strip("'").replace('\\n', '\n')
    
    # Strip any redundant prefix so the completion text is clean
    if clean_text.lower().startswith("today's special from satyansh's vault:"):
        clean_text = clean_text[len("today's special from satyansh's vault:"):].strip()
    elif clean_text.lower().startswith("satyansh thinks:"):
        clean_text = clean_text[len("satyansh thinks:"):].strip()
        
    paragraphs = clean_text.split("\n\n")
    wrapped_paragraphs = []
    for p in paragraphs:
        lines = textwrap.wrap(p.strip(), width=65)
        if lines:
            wrapped_paragraphs.append("\n".join(lines))
            
    formatted_completion = "\n\n".join(wrapped_paragraphs) if wrapped_paragraphs else clean_text
    
    formatted_block = f"""{START_TAG}
```lua
-- ==============================================================================
-- SATYANSH-MINI // NVIM RUNTIME BUFFER (STATUS: ONLINE)
-- ==============================================================================
local vault = require("satyansh.vault")

vault.inference = {{
  model              = "{model_name}",
  adapter            = "{lora_name}",
  parameters         = "135M + 1.2M LoRA",
  precision          = "FP16",
  runner             = "github-actions-cpu",
  run_id             = {count},
  generated_at       = "{now_utc}",
}}

-- ==============================================================================
-- LATEST COMPLETION
-- ==============================================================================

local completion = [[
{formatted_completion}
]]
```
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
    text = sys.argv[1] if len(sys.argv) > 1 else "Hardware reality dictates software architecture.\n\nCache hierarchies and PCIe lane limits dictate software design at scale."
    update_readme_content(text)
