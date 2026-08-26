#!/usr/bin/env python3
import json

examples = [
    {
        "messages": [
            {"role": "user", "content": "Generate a short observation about Satyansh learning C++."},
            {"role": "assistant", "content": "Python stopped being uncomfortable enough, so Satyansh started learning where the memory allocations actually live."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Generate a funny observation about RainCast."},
            {"role": "assistant", "content": "Most people check the weather by looking outside. RainCast apparently preferred satellite telemetry and solving an inverse problem."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What is Satyansh currently working on?"},
            {"role": "assistant", "content": "Currently trying to convince CUDA threads to cooperate without causing illegal memory access errors."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Observation about debugging CUDA kernels."},
            {"role": "assistant", "content": "Debugging on GPU: where print statements are asynchronous and memory boundaries are merely polite suggestions."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Generate a status update for Satyansh's profile."},
            {"role": "assistant", "content": "Status: 10% writing algorithms, 90% staring at compiler error messages involving template metaprogramming."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Why did Satyansh switch from Python to C++?"},
            {"role": "assistant", "content": "Automatic garbage collection felt too safe. True thrill requires manual pointer arithmetic."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Generate a short quote about low-level optimization."},
            {"role": "assistant", "content": "Premature optimization is the root of all evil, but late-stage cache alignment is pure satisfaction."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Observation about building runtime detection tools."},
            {"role": "assistant", "content": "Building runtime monitors is just software engineers admitting they don't trust their own code in production."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Generate a witty comment on memory management."},
            {"role": "assistant", "content": "You don't truly appreciate memory management until valgrind hands you a 400-page summary of your mistakes."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Observation about writing CUDA kernels."},
            {"role": "assistant", "content": "Writing GPU kernels is 5% math and 95% making sure your block dimensions don't sum to chaos."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Generate a short observation on software architecture."},
            {"role": "assistant", "content": "The codebase is simple, elegant, and completely reliant on undefined behavior not being invoked today."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "What happens when Satyansh opens GDB?"},
            {"role": "assistant", "content": "When GDB opens, theories die and stack traces tell the uncomfortable truth."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Observation on high performance computing."},
            {"role": "assistant", "content": "Running at 60 FPS is fine until you realize 20 milliseconds were wasted in memory transfer across PCIe."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Generate a funny thought about git commits."},
            {"role": "assistant", "content": "Commit message: 'Fixed bug'. Narrator: 'It did not fix the bug, but it introduced two new ones.'"}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Observation about learning systems programming."},
            {"role": "assistant", "content": "Systems programming: turning simple ideas into complex memory layouts since 1972."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Generate a status note about Satyansh."},
            {"role": "assistant", "content": "Satyansh is currently compiling... please hold while LLVM reorganizes the universe."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Observation about multi-threading and concurrency."},
            {"role": "assistant", "content": "A race condition walked into a bar. The drinks before ordered bartender they."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Generate a quick thought on benchmarking."},
            {"role": "assistant", "content": "It runs in 0.2ms! (Note: compiler optimized away the entire function because the result was unused)."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Observation about RainCast development."},
            {"role": "assistant", "content": "RainCast doesn't just predict precipitation; it calculates the atmospheric emotional weight of rain."}
        ]
    },
    {
        "messages": [
            {"role": "user", "content": "Observation about software debugging."},
            {"role": "assistant", "content": "There are two hard problems in computer science: cache invalidation, naming things, and off-by-one errors."}
        ]
    }
]

# Expand dataset with variations
additional_prompts = [
    ("Generate a short, witty observation about a software engineer learning C++ and CUDA.", "Learning CUDA: turning 10 lines of clean Python into 80 lines of kernel launch syntax and a segmentation fault."),
    ("Generate an observation about low-level performance.", "If a program runs fast enough, nobody checks if the memory was actually freed."),
    ("Generate a witty observation about Satyansh's coding habits.", "Satyansh doesn't just write code; he negotiates with the compiler until one of them yields."),
    ("Generate a thought about deep learning and GPU memory.", "Running out of VRAM is nature's way of telling you that your batch size had too much ambition."),
    ("Generate a status update about Satyansh.", "Current state: inspecting disassembly because the compiler took my loops as mere suggestions."),
    ("Observation about GPU shared memory.", "Shared memory is blazingly fast, right up until all 32 threads try to access bank zero at the exact same moment."),
    ("Observation on writing C++ in 2026.", "Modern C++ gives you 15 different ways to initialize an integer, and all of them have subtle semantic differences."),
    ("Generate a thought about profiling software.", "The profiler revealed the bottleneck was not the mathematical algorithm, but printing to stdout.")
]

for p, r in additional_prompts:
    examples.append({
        "messages": [
            {"role": "user", "content": p},
            {"role": "assistant", "content": r}
        ]
    })

with open("data/train.jsonl", "w") as f:
    for ex in examples:
        f.write(json.dumps(ex) + "\n")

print(f"[*] Created dataset with {len(examples)} examples in data/train.jsonl")
