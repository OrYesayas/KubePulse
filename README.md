# KubePulse ☸️

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Ready-326CE5)
![CLI](https://img.shields.io/badge/Interface-CLI-black)
![License](https://img.shields.io/badge/License-MIT-green)

KubePulse is a lightweight Kubernetes diagnostic and security auditing CLI designed for DevOps engineers, SRE teams, and platform operators.

The tool enables fast health analysis of Kubernetes clusters in both connected and disconnected environments by detecting failing workloads, cluster misconfigurations, unhealthy nodes, and missing security/resource configurations.

Built with performance, readability, and operational simplicity in mind, KubePulse provides actionable diagnostics directly from the terminal using a rich and structured interface.

---

# 🚀 Features

## 🔍 Live Cluster Analysis
Connect directly to a live Kubernetes cluster using your local `kubectl` configuration and perform real-time health diagnostics.

Checks include:
- Pod failures (`CrashLoopBackOff`, `Pending`, `ImagePullBackOff`)
- High container restart counts
- Unhealthy node conditions
- Missing CPU/Memory limits
- Namespace-wide issue detection

---

## 📦 Offline / Disconnected Mode
Analyze Kubernetes environments without requiring cluster connectivity.

KubePulse supports scanning exported JSON cluster dumps, making it ideal for:
- Air-gapped environments
- Incident investigations
- Security auditing
- Local testing and demonstrations

---

## ⚙️ Automated Diagnostic Engine
The core analysis engine evaluates cluster resources against custom-built operational and security validation rules.

The analyzer automatically identifies:
- Critical workload failures
- Resource misconfigurations
- Infrastructure instability
- Security best-practice violations

---

## 🎨 Rich Terminal Interface
KubePulse uses colorized and structured terminal reporting powered by Rich.

Reports are displayed using:
- Severity levels
- Structured diagnostic tables
- Clear namespace separation
- Human-readable incident summaries

---

# 📸 Demo

## Offline Cluster Scan

```bash
python src/cli.py scan --offline-file mock_cluster.json
```

### Example Output

```text
⚠️ Running in OFFLINE/DISCONNECTED mode using: mock_cluster.json
🔍 Analyzing cluster state against configuration rules...

                                     KubePulse Security & Health Diagnostic Report
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Severity ┃ Namespace     ┃ Resource                                    ┃ Message                                     ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ CRITICAL │ production    │ Pod/payment-api-7f89                        │ Pod is in 'Pending' state.                  │
│ WARNING  │ production    │ Pod/payment-api-7f89 (Container: api)       │ High restart count detected: 12 restarts.   │
│ CRITICAL │ production    │ Pod/payment-api-7f89                        │ Container waiting: CrashLoopBackOff.        │
│ WARNING  │ frontend      │ Pod/frontend-service-2a1b                   │ Missing Memory Limits configuration.        │
│ CRITICAL │ Cluster-Level │ Node/node-worker-2                          │ Node condition 'Ready' is False.            │
└──────────┴───────────────┴─────────────────────────────────────────────┴─────────────────────────────────────────────┘

📢 Total incidents found: 5
```

---

# 🛠️ Installation

## 1. Clone the Repository

```bash
git clone https://github.com/OrYesayas/KubePulse.git
cd KubePulse
```

## 2. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# 💻 Usage

## Live Cluster Scan

Run a full real-time cluster scan:

```bash
python src/cli.py scan
```

Scan a specific namespace:

```bash
python src/cli.py scan --namespace production
```

---

## Offline / Disconnected Scan

Run diagnostics using a local cluster dump:

```bash
python src/cli.py scan --offline-file mock_cluster.json
```

---

# 🧰 Tech Stack

- Python
- Kubernetes Python Client
- Click (CLI Framework)
- Rich (Terminal UI)
- JSON-based Offline Analysis

---

# 🏗️ Architecture

KubePulse follows a modular architecture to simplify maintenance, scalability, and future feature expansion.

```text
src/
├── cli.py
├── collector.py
├── analyzer.py
├── reporter.py
└── rules/
```

## Components

### `cli.py`
Handles command parsing, CLI arguments, and execution flow using Click.

### `collector.py`
Communicates with the Kubernetes API or loads offline JSON datasets.

### `analyzer.py`
Core diagnostic engine responsible for validating resources against operational and security rules.

### `reporter.py`
Formats incidents into structured and readable terminal reports using Rich.

---

# 🎯 Motivation

Modern Kubernetes environments can become difficult to troubleshoot quickly during incidents.

KubePulse was created to provide DevOps engineers and SRE teams with a fast, lightweight, and readable diagnostic utility capable of identifying critical infrastructure problems within seconds.

The project also focuses on disconnected and air-gapped environments where traditional monitoring solutions may not be available.

---

# 🔮 Future Improvements

Planned future features include:

- YAML and HTML report export
- Prometheus integration
- Custom rule engine support
- Slack / Discord alerting
- Multi-cluster scanning
- RBAC security analysis
- Helm release inspection
- CI/CD integration support

---

# 📄 License

This project is licensed under the MIT License.

---

# 🤝 Contributing

Contributions, ideas, and improvements are welcome.

Feel free to open issues or submit pull requests.

---

# ⭐ Support

If you found this project useful, consider starring the repository to support future development.

