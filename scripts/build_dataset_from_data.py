#!/usr/bin/env python3
import json
import os

VAULT_PREFIX = "today's special from satyansh's vault: "

# Curated dataset entries directly distilled from DATA.md
entries = [
    # CommuneOS
    (
        "Generate today's special from Satyansh's vault regarding CommuneOS.",
        "today's special from satyansh's vault: Single-agent LLM systems choke on 15-second context pollution, which is why CommuneOS splits duties across 6 cooperating agents and a local regex fallback for when rate limits hit."
    ),
    (
        "What is the story behind Satyansh winning the Paytm Hackathon?",
        "today's special from satyansh's vault: CommuneOS took 1st place at the Paytm Hackathon by replacing monolithic LLM prompts with an orchestrated 6-agent pipeline and 230ms mock-override test cycles."
    ),
    (
        "Observation about CommuneOS resume parsing.",
        "today's special from satyansh's vault: Why trust an LLM API alone when you can back it up with PyMuPDF and 30+ regex pattern matchers the moment rate limits kick in?"
    ),

    # Satellite Link Optimizer
    (
        "Generate a special observation about Satellite Link Optimizer.",
        "today's special from satyansh's vault: Checking 1,300+ LEO satellites takes 75 µs per SGP4 evaluation, but the real magic is a 192x Numba JIT speedup for Maseng-Bakken stochastic rain fading."
    ),
    (
        "Tell me about Satyansh's satellite link modeling.",
        "today's special from satyansh's vault: While others guess when signals drop, Satellite Link Optimizer predicts RF degradation with XGBoost and precision ITU-R tropospheric physics at 275,000 steps per second."
    ),
    (
        "Why use Numba JIT for rain fading?",
        "today's special from satyansh's vault: Pure Python Monte Carlo simulations will test your patience; Numba JIT compiles your stochastic rain dynamics directly into machine code for a 192x speedup."
    ),

    # GraphMem (RecalNet)
    (
        "Generate an insight from Satyansh's vault about GraphMem.",
        "today's special from satyansh's vault: Vector embeddings forget relationships; GraphMem builds persistent directed multigraphs in SQLite with 12ms multi-hop traversal on a consumer 6GB RTX 3050."
    ),
    (
        "Observation about local-first AI and RecalNet.",
        "today's special from satyansh's vault: Cloud RAG sends your data across continents; RecalNet executes graph extraction and traversal 100% offline via local CUDA kernels and Ollama."
    ),

    # Orbit Ops
    (
        "Generate today's special from Satyansh's vault about Orbit Ops.",
        "today's special from satyansh's vault: Fusing NASA TEMPO satellite atmospheric scans with ground sensor telemetry to downscale 10km regional grids into street-level pollution maps with 92% precision."
    ),
    (
        "How does Orbit Ops handle massive geospatial data?",
        "today's special from satyansh's vault: Parallelized xarray and dask pipelines feed TimescaleDB and PostGIS so street-level air quality forecasts respond asynchronously in under 45ms."
    ),

    # Plant Scout
    (
        "What's in Satyansh's vault regarding Plant Scout?",
        "today's special from satyansh's vault: Real agricultural AI doesn't leak test data; Plant Scout uses leaf-ID aware partitioning and custom ResNet9 with mixed precision on an autonomous Jetson Nano robot."
    ),
    (
        "Observation about edge AI on Jetson Nano.",
        "today's special from satyansh's vault: When deploying on a field robot with limited compute, custom lightweight ResNet9 and torch.amp mixed precision keep inference real-time in the dust."
    ),

    # Task Server
    (
        "Generate a note about Satyansh's Task Server.",
        "today's special from satyansh's vault: No web frameworks, no bloated JSON parsers—just pure Java 11 TCP sockets, worker pools, and lock-guarded concurrent queues delivering sub-millisecond task dispatch."
    ),

    # Term-Folio
    (
        "Tell me about Satyansh's portfolio interface.",
        "today's special from satyansh's vault: Why choose between a CRT terminal and a modern web GUI when Term-Folio lets you switch between workspace.sh and a 3D WebGL physics knowledge graph?"
    ),

    # Sahai AI
    (
        "Observation about Sahai AI.",
        "today's special from satyansh's vault: Empathetic AI assistance grounded in clinical literature via FAISS RAG and LoRA fine-tuning, with automated crisis escalation logic."
    ),

    # CUDA & GPU Architecture
    (
        "Generate today's special from Satyansh's vault regarding CUDA kernels.",
        "today's special from satyansh's vault: Memory bandwidth is the ultimate speed limit; if your shared memory access pattern hits bank conflicts, your 32 warp threads serialize right back to single-core speeds."
    ),
    (
        "What is Satyansh's engineering philosophy on hardware?",
        "today's special from satyansh's vault: Hardware reality dictates software architecture. Cache hierarchies, memory controllers, and PCIe lane saturation don't care about software abstractions."
    ),
    (
        "Observation about GPU shared memory optimization.",
        "today's special from satyansh's vault: A single byte of memory padding in your CUDA struct can be the difference between a 32-way bank conflict and peak hardware throughput."
    ),
    (
        "Generate a vault observation on C++ and performance.",
        "today's special from satyansh's vault: Modern C++ gives you zero-cost abstractions, right until you forget that cache misses cost 200 clock cycles and pointer chasing ruins your day."
    ),
    (
        "What happens during kernel fusion?",
        "today's special from satyansh's vault: Kernel fusion is simply refusing to pay the PCIe and global memory round-trip tax twice for back-to-back matrix operations."
    ),
    (
        "Generate today's special from Satyansh's vault.",
        "today's special from satyansh's vault: Debugging distributed systems and GPU kernels: where print statements are asynchronous, race conditions are timing-dependent, and the hardware always tells the truth."
    ),
    (
        "What is today's special from Satyansh's vault?",
        "today's special from satyansh's vault: Simplicity is the ultimate sophistication. Eliminate unnecessary layers, align your data to cache lines, and let the hardware do what it was built for."
    ),
    (
        "Status update from Satyansh's technical vault.",
        "today's special from satyansh's vault: Currently profiling lock-free data structures and custom CUDA kernels to shave microseconds off inference latency."
    ),
    (
        "Generate today's special from Satyansh's vault about distributed computing.",
        "today's special from satyansh's vault: High-throughput inference isn't just about faster GPUs; it's about minimizing host-to-device transfers and keeping compute engines saturated."
    )
]

# Variations and prompts to ensure strong generalization
prompt_variations = [
    ("What's in Satyansh's vault today?", 0),
    ("Give me today's special from Satyansh's vault.", 1),
    ("Generate a thought from Satyansh's vault.", 6),
    ("Today's special from Satyansh's vault:", 15),
    ("What is today's technical insight from Satyansh?", 16),
    ("Observation from Satyansh Gaur's portfolio.", 17),
    ("Generate today's special from Satyansh's vault.", 20),
]

training_data = []
for p, r in entries:
    training_data.append({
        "messages": [
            {"role": "user", "content": p},
            {"role": "assistant", "content": r}
        ]
    })

# Add variation pairs
for p, idx in prompt_variations:
    training_data.append({
        "messages": [
            {"role": "user", "content": p},
            {"role": "assistant", "content": entries[idx][1]}
        ]
    })

# Additional targeted pairs for all specific project queries
extra_pairs = [
    ("Tell me about CommuneOS architecture.", "today's special from satyansh's vault: Decoupling a monolithic agent into 6 specialized LLM agents (Identity, Discovery, Learning, Mentor, Health, Organizer) reduced latency from 15s to 230ms in test harnesses."),
    ("Tell me about the Satellite Link Optimizer project.", "today's special from satyansh's vault: Modeling 1,300+ satellites with SGP4 orbital mechanics and Numba-accelerated Maseng-Bakken rain attenuation at 275,000 evaluations per second."),
    ("Tell me about RecalNet GraphMem.", "today's special from satyansh's vault: A local-first directed multigraph memory engine running on consumer 6GB GPUs with 12ms retrieval latency and 100% SQLite persistence."),
    ("Tell me about Orbit Ops air quality platform.", "today's special from satyansh's vault: NASA TEMPO satellite atmospheric data downscaled to street-level with xarray, dask, PostGIS, and TimescaleDB with 92% validation accuracy."),
    ("Tell me about Plant Scout field robot.", "today's special from satyansh's vault: Custom ResNet9 deployed on NVIDIA Jetson Nano field robots with leaf-ID grouped validation guaranteeing 0% data leakage."),
    ("Tell me about Task Server in Java.", "today's special from satyansh's vault: Pure multithreaded raw TCP socket server in Java with dedicated worker pools and lock-guarded concurrent queues."),
    ("What are Satyansh's core skills?", "today's special from satyansh's vault: High-performance CUDA C++, GPU memory hierarchy optimization, distributed multi-agent systems, and hardware-aware deep learning pipelines.")
]

for p, r in extra_pairs:
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
