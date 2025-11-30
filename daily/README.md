# Daily Projects — 90-Day Learning Sprint

This directory contains my 90-day journey building deep intuition in:
	•	Systems & Linux
	•	Data Infrastructure 
	•	AI Infrastructure (CUDA, LoRA/QLoRA, vLLM, SGLang)
	•	GPU topology & scheduling (NVLink, PCIe)
	•	Training & inference stacks
	•	RL & Async RL (for my ICML submission, AsyncWeave)
	•	Observability, Dashboards, K8s, Docker
	•	End-to-end deployment engineering

Every day I share micro-projects with code, learnings, and artifacts.
This directory acts as a public record showing consistent, high-intensity execution.

⸻

Table of Contents (Daily Projects)

Completed
	•	Day 01 – PID Controller￼
	•	Day 02 – NN From Scratch￼
	•	Day 03 – Linux Basics￼

Upcoming

(These folders will appear as projects are completed.)
	•	day04-shell-scripting
	•	day05-docker-basics
	•	… through day90-final-polish

⸻

Completed Daily Projects

Day 01 — PID Controller

📂 daily/day01-pid-controller/
A Python PID controller implementation with:
	•	P, I, D gain control
	•	overshoot, rise time, stability tuning
	•	matplotlib visualization

⸻

Day 02 — Neural Network From Scratch

📂 daily/day02-nn-from-scratch/
A full NumPy-only neural network, including:
	•	forward pass
	•	backpropagation
	•	training loop
	•	loss curve
	•	XOR classification example

⸻

Day 03 — Linux Basics

📂 daily/day03-linux-basics/
Hands-on Unix/Linux fundamentals:
	•	navigation (cd, ls)
	•	file ops (cp, mv, rm)
	•	permissions (chmod, chown)
	•	processes (ps, top, kill)
	•	pipes & redirects

⸻

90-Day Full Roadmap

Phase 1 — Systems & Infra (Days 1–21)

Linux, processes, Docker, schedulers, K8s, observability.
	1.	Linux basics
	2.	File system navigation
	3.	Shell scripting
	4.	Processes
	5.	Docker fundamentals
	6.	Docker networking
	7.	Docker Compose
	8.	Logs & monitoring
	9.	ETL fundamentals
	10.	Scheduler (RR)
	11.	Priority scheduler
	12.	Networking simulator
	13.	Prometheus basics
	14.	Grafana dashboards
	15.	FastAPI + Prometheus
	16.	ETL → database
	17.	Kubernetes cluster
	18.	K8s deployments
	19.	Rolling updates
	20.	K8s monitoring
	21.	Failure simulation

⸻

Phase 2 — Data Infrastructure (Days 22–42)

Data architecture and systems.
	22.	Columnar vs row storage
	23.	Schema design
	24.	Query planner
	25.	Vectorized execution
	26.	Indexing
	27.	Distributed FS
	28.	Replication
	29.	Raft leader election
	30.	Metadata catalog
	31.	Data lineage graph
	32.	Lineage propagation
	33.	RBAC engine
	34.	Column-level security
	35.	Streaming ingest
	36.	Backpressure simulation
	37.	Batch vs streaming
	38.	Data quality
	39.	Partitioning strategies
	40.	Time-series storage
	41.	Analytics dashboard
	42.	Cost modeling

⸻

Phase 3 — AI Infra & Deployment (Days 43–63)

CUDA → cuDNN → CUTLASS → JAX → vLLM → SGLang → quantization → scheduling.
	43.	GPU architecture
	44.	First CUDA kernel
	45.	cuDNN + CUTLASS basics
	46.	JAX + TPU mental model
	47.	NVLink vs PCIe topology
	48.	DDP/FSDP basics
	49.	LoRA finetuning
	50.	QLoRA + Unsloth
	51.	Training vs inference bottlenecks
	52.	Training observability
	53.	Basic inference server
	54.	Batching & queueing
	55.	vLLM vs SGLang
	56.	KV cache deep dive
	57.	Quantization benchmarks
	58.	LoRA/QLoRA deployment
	59.	Observability
	60.	Multi-tenant scheduling
	61.	Topology-aware placement
	62.	Training/inference interference
	63.	Integration into AsyncWeave

⸻

Phase 4 — RL & Async RL (Days 64–84)
	64.	Q-learning
	65.	Policy gradients
	66.	Actor–critic
	67.	Replay buffer
	68.	Replay visualization
	69.	Async actor–learner v1
	70.	Async actor–learner v2
	71.	Staleness metrics
	72.	Heterogeneous GPU modeling
	73.	FIFO vs RR
	74.	Load-aware scheduler
	75.	Staleness-aware scheduler
	76.	RL runner
	77.	Cluster load model
	78.	Scheduling visualization
	79.	Ray RL setup
	80.	Ray experiments
	81.	Fault injection
	82.	Checkpointing
	83.	RL experiment framework
	84.	Draft ICML notes

⸻

Phase 5 — Integration & Portfolio (Days 85–90)
	85.	Repo refactor
	86.	Master README
	87.	Dashboard consolidation
	88.	CI + tests
	89.	Portfolio screenshots
	90.	Final polish

⸻

Status

Days completed: 03 / 90

⸻

Related folders
	•	../capstones/
	•	../icml/
