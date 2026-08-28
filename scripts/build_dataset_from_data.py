#!/usr/bin/env python3
import json
import os

jokes_and_observations = [
    (
        "Tell a technical joke about Satyansh.",
        "Satyansh would look at an H100 GPU cluster and think: 'Huh, still slow. Let me rewrite the kernel in PTX.'"
    ),
    (
        "What does Satyansh think about GPUs?",
        "Satyansh looks at modern GPUs and wonders why anyone allows 4 clock cycles of branch divergence to survive in production."
    ),
    (
        "Generate a funny observation about Satyansh and performance.",
        "Satyansh will optimize a CUDA kernel down to 3 clock cycles, then spend 2 hours staring at the disassembly wondering where the other 2 cycles went."
    ),
    (
        "What is Satyansh's idea of code optimization?",
        "Satyansh doesn't profile code to find bottlenecks; he profiles code to judge how the compiler dared to disgrace his cache hierarchy."
    ),
    (
        "Tell me a joke about Satyansh learning low-level systems.",
        "Python garbage collection felt entirely too peaceful, so Satyansh switched to C++ just to negotiate with uninitialized pointers."
    ),
    (
        "Observation about Satyansh and memory management.",
        "Satyansh believes there are only two states of matter: data aligned to 64-byte cache lines, and personal insults."
    ),
    (
        "What happens when Satyansh reviews CUDA code?",
        "Satyansh's idea of a relaxing weekend is hunting for 2-cycle latency leaks until shared memory bank conflicts reach zero."
    ),
    (
        "Observation about Satyansh's projects.",
        "Ask Satyansh for a simple weather check and he will return with an SGP4 satellite constellation simulator accelerated 192x via Numba JIT."
    ),
    (
        "What would Satyansh say about hardware limits?",
        "Satyansh would look at 80GB of HBM3 memory bandwidth and ask why PCIe transfer is taking an entire insulting microsecond."
    ),
    (
        "Tell a joke about Satyansh and multi-threading.",
        "Satyansh's code doesn't experience race conditions; threads simply synchronize out of mutual respect for his memory barriers."
    ),
    (
        "What is Satyansh currently thinking?",
        "Satyansh is currently staring at a flamegraph wondering why libc malloc felt the need to take an extra 15 nanoseconds."
    ),
    (
        "Funny thought about Satyansh and distributed systems.",
        "Single-agent LLMs were taking 15 seconds, so Satyansh engineered a 6-agent swarm and a 230ms mock harness just to prove a point."
    ),
    (
        "What does Satyansh think about software abstractions?",
        "Hardware reality dictates software architecture. Hardware doesn't care about your design patterns, and neither does Satyansh."
    ),
    (
        "Observation about Satyansh and GPU computing.",
        "Most people see a graphics card for gaming; Satyansh sees 10,000 threads waiting to be told not to hit the same memory bank."
    ),
    (
        "Tell a joke about Satyansh and debugging.",
        "When Satyansh opens GDB, compiler optimization theories die and the stack trace finally tells the truth."
    ),
    (
        "What is Satyansh's motto?",
        "Simplicity is the ultimate sophistication. Eliminate unnecessary layers, align your data, and let the hardware do what it was built for."
    ),
    (
        "Observation about Satyansh building CommuneOS.",
        "CommuneOS won 1st place at the Paytm Hackathon because while others were debugging prompts, Satyansh was compiling regex fallbacks."
    ),
    (
        "What does Satyansh think of high-performance computing?",
        "Running in 2 milliseconds is fine, right up until Satyansh calculates that PCIe bus transfers wasted 80% of the time."
    )
]

# Variations and prompts to ensure strong generalization
prompts = [
    "Tell a joke about Satyansh.",
    "What is Satyansh thinking?",
    "Generate a technical thought about Satyansh.",
    "Observation about Satyansh.",
    "What does Satyansh think about GPUs?",
    "Generate a technical joke about Satyansh.",
    "What's in Satyansh's mind today?",
    "Status update on Satyansh.",
    "Tell a joke about Satyansh's coding habits."
]

training_data = []

# Add base pairs
for p, r in jokes_and_observations:
    training_data.append({
        "messages": [
            {"role": "user", "content": p},
            {"role": "assistant", "content": r}
        ]
    })

# Add cross-variation pairs
for i, prompt in enumerate(prompts):
    target = jokes_and_observations[i % len(jokes_and_observations)][1]
    training_data.append({
        "messages": [
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": target}
        ]
    })

# Add specific queries
extra_targeted = [
    ("What would Satyansh think about this GPU?", "Satyansh would look at GPUs and think: 'Huh, still slow.'"),
    ("Why is Satyansh optimizing this code?", "Because if there are 2 nanoseconds of PCIe latency left on the table, Satyansh cannot sleep."),
    ("Tell me about Satyansh's view on CUDA.", "A single byte of memory padding in your CUDA struct is the difference between a 32-way bank conflict and peak hardware throughput.")
]

for p, r in extra_targeted:
    training_data.append({
        "messages": [
            {"role": "user", "content": p},
            {"role": "assistant", "content": r}
        ]
    })

os.makedirs("data", exist_ok=True)
with open("data/train.jsonl", "w") as f:
    for item in training_data:
        f.write(json.dumps(item) + "\n")

print(f"[*] Generated {len(training_data)} training examples in data/train.jsonl")
