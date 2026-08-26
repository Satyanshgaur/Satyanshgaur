```text
+------------------------------------------------------------------------------+
|                                SATYANSH-MINI                                 |
|                         personal language model v0.2                         |
|                                                                              |
|               [ 135M PARAMETERS ]   |   [ STATUS: ONLINE ]                   |
|                                                                              |
|  +-- TODAY'S SPECIAL FROM SATYANSH'S VAULT -------------------------------+  |
<!-- satyansh-mini:start -->
|  today's special from satyansh's vault:                                      |
|  "Hardware reality dictates software architecture. Cache hierarchies and     |
|   PCIe lane limits dictate software design at scale."                        |
|                                                                              |
|  [ Run: #0001 | Runner: GitHub Actions (CPU) | Cost: $0.00 ]                 |
<!-- satyansh-mini:end -->
|  +------------------------------------------------------------------------+  |
|                                                                              |
|  BASE: SmolLM-135M-Instruct     |  ADAPTER: satyansh-lora-r16 (PEFT)         |
|  TRAINED: RTX 3050 6GB Laptop   |  INFERENCE: GitHub Actions (Cron Schedule) |
+------------------------------------------------------------------------------+
```

A few things the model knows about me, and you'll probably wanna know as well:

---

# Satyansh Gaur

**AI Infrastructure Engineer // Systems Programmer // Performance Architect**  
*Architecting high-performance kernels, distributed systems, and hardware-aware intelligence for next-generation compute workloads.*

[Portfolio: satyansh.indevs.in](https://satyansh.indevs.in) | [GitHub: Satyanshgaur](https://github.com/Satyanshgaur) | [LinkedIn: satyansh-gaur](https://www.linkedin.com/in/satyansh-gaur-2b1b05370) | [Kaggle: satyanshgaur1](https://www.kaggle.com/satyanshgaur1) | [X: @GaurSatyansh](https://x.com/GaurSatyansh)

---

### Core Research & Active Focus

- **GPU Architecture & Custom CUDA Kernels**: Shared memory banking, bank conflict mitigation, lock-free structures.
- **LLM Inference Engines**: Kernel fusion, GraphRAG memory engines, and multi-agent coordination frameworks.
- **Hardware-Aware Software Optimization**: Designing algorithms aligned with cache hierarchy, PCIe lane limits, memory bandwidth, and compute capabilities across NVIDIA GPUs (RTX 3050 to H100) and embedded edge compute (NVIDIA Jetson Nano).

---

### Core Projects & Technical Dossier

#### 1. CommuneOS — AI-Powered Community Operations Agent
- **Award**: 1st Place Winner at Paytm Hackathon
- **Repository**: [github.com/Satyanshgaur/communeos](https://github.com/Satyanshgaur/communeos)
- **Tech Stack**: Next.js 15 (App Router), React 19, TypeScript, Tailwind CSS, FastAPI, ChromaDB, agentfield SDK, PyMuPDF
- Coordinates 6 specialized cooperating LLM agents (Identity, Discovery, Learning, Mentor, Health, Organizer) with a centralized Memory Agent coordinator.
- Resume ingestion pipeline using PyMuPDF and ChromaDB vector store, backed by an offline regex fallback with 30+ developer keyword matchers during API rate limits.
- Integration test suite achieves sub-230ms cycles via a mock-override testing harness.

#### 2. Satellite Link Optimizer — Multi-Satellite Constellation Simulator
- **Repository**: [github.com/Satyanshgaur/Satellite-link-optimiser](https://github.com/Satyanshgaur/Satellite-link-optimiser)
- **Tech Stack**: Python 3.12, SGP4, Numba JIT, NumPy, Streamlit, XGBoost
- SGP4 orbital propagation modeling dynamic LEO/MEO constellations across 1,300+ satellites at 75 microseconds per evaluation.
- Maseng-Bakken stochastic rain fade modeling accelerated 192x via Numba JIT for large-scale Monte Carlo simulations.
- System throughput of 275,000 steps/sec with XGBoost predicting RF link degradation prior to physical outage occurrence.

#### 3. GraphMem (RecalNet) — Local-First Graph Memory Framework
- **Repository**: [github.com/Satyanshgaur/RecalNet](https://github.com/Satyanshgaur/RecalNet)
- **Tech Stack**: React, TypeScript, SQLite, Ollama, Custom CUDA Kernels
- Persistent, directed multigraph of knowledge with 100% SQLite durability running on consumer 6GB VRAM (NVIDIA RTX 3050).
- Sub-12ms multi-hop graph retrieval latency with 100% offline local extraction and fuzzy entity resolution.

#### 4. Orbit Ops — Hyperlocal Air Quality Forecasting Platform
- **Repository**: [github.com/Satyanshgaur/orbit-ops](https://github.com/Satyanshgaur/orbit-ops)
- **Tech Stack**: FastAPI, Docker, TimescaleDB, PostGIS, xarray, dask, Next.js, Mapbox
- Downscales 10km NASA TEMPO satellite atmospheric observations to street-level resolution with 92% validation accuracy against ground truth sensors.
- Asynchronous data processing pipeline responding in ~45ms.

#### 5. Plant Scout — Autonomous Field Scout & Plant Classifier
- **Repository**: [github.com/Satyanshgaur/plant_disease_classification](https://github.com/Satyanshgaur/plant_disease_classification)
- **Tech Stack**: PyTorch, ResNet9, Jetson Nano, OpenCV, One Cycle Policy, torch.amp
- Grouped dataset splits by physical leaf identity ensuring 100% data leakage-free validation.
- Custom lightweight ResNet9 neural network running real-time edge inference on autonomous wheeled field robots powered by NVIDIA Jetson Nano.

#### 6. Task Server — Multithreaded TCP Task Processor
- **Repository**: [github.com/Satyanshgaur/task-server-in-java](https://github.com/Satyanshgaur/task-server-in-java)
- **Tech Stack**: Java 11+, Raw TCP Sockets, Java Concurrency API, Thread Pools
- Pure TCP/IP communication with dedicated worker pool architectures and lock-guarded concurrent queues delivering sub-millisecond task dispatch.

#### 7. Term-Folio — High-Fidelity AI Workstation Interface
- **Repository**: [github.com/Satyanshgaur/term-folio](https://github.com/Satyanshgaur/term-folio)
- **Live Demo**: [satyansh.indevs.in](https://satyansh.indevs.in)
- **Tech Stack**: React 19, TypeScript, Three.js, WebGL, Tailwind CSS, Vercel Serverless Functions
- Dual interaction paradigm featuring CRT terminal (workspace.sh) and a 3D WebGL physics-based knowledge graph.

---

### Technical Skills & Systems Matrix

```text
+----------------------+----------------------+-------------------------------+
| 01. SYSTEMS & HPC    | 02. AI INFRA & ML    | 03. FULL STACK & PLATFORM     |
+----------------------+----------------------+-------------------------------+
| * Modern C++ (17/20) | * vLLM & Triton      | * React 19 & Next.js 15 (App) |
| * Rust (Wasm)        | * TensorRT & CUDA    | * TypeScript / ESNext         |
| * Linux Kernel Dev   | * PyTorch & torch.amp| * FastAPI & Django            |
| * Java 11+ (Sockets) | * Numba JIT & NumPy  | * PostgreSQL & TimescaleDB    |
| * GPU Memory Banking | * ChromaDB & FAISS   | * SQLite & PostGIS            |
| * Lock-Free Patterns | * GraphRAG / Graphs  | * Redis & Docker Containers   |
| * Multi-threading    | * agentfield (Multi) | * Tailwind CSS & Three.js     |
+----------------------+----------------------+-------------------------------+
```

---

### Research Publications & Technical Writing

- **Behind CommuneOS: Building a Cooperative Multi-Agent Network** (July 2026) — Architectural partitioning of 6 specialized agents, mock test harnesses, and rate-limit fallback engineering.
- **Writing Custom HPC Kernels** (February 2026) — Cache hierarchies, PCIe lane saturation, eliminating GPU shared memory bank conflicts, and lock-free concurrency.
- **CUDA Memory Hierarchy Optimization** (January 2026) — Shared memory bank structures across warp executions, memory padding, and stride alignment.

---

### Contact & Links

- Portfolio: https://satyansh.indevs.in
- GitHub: https://github.com/Satyanshgaur
- LinkedIn: https://www.linkedin.com/in/satyansh-gaur-2b1b05370
- Kaggle: https://www.kaggle.com/satyanshgaur1
- X: https://x.com/GaurSatyansh
- Email: satyanshgaur0@gmail.com / satyansh@gaur.dev
