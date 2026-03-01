# LangGraphIntro  
*Introduction to building AI agents and workflows using LangGraph & LangChain*

## 🚀 What Is This Project?
This branch contains a beginner-friendly, hands-on LangGraph project showing how to use LangChain + LangGraph to define and execute AI workflows represented as graphs.

LangGraph is a **low-level orchestration framework** that lets you build stateful, graph-driven agent workflows using Python. You define **nodes (logic units)** and **edges (workflow transitions)** to build custom applications on top of large language models. :contentReference[oaicite:0]{index=0}

---

## 📌 Why Use LangGraph?
LangGraph is designed for:

- Building long-running, stateful agents  
- Complex graph-defined workflows  
- Multi-step execution based on state and business logic  
- Human-in-the-loop integrations  
- Low-level control with LLMs  
- Persistent execution (memory + checkpoints) :contentReference[oaicite:1]{index=1}

Unlike higher-level agent APIs, LangGraph gives you direct control of how logic flows through nodes and transitions.

---

## 📁 Project Structure
📦LangGraphIntro
┣ 📄 main.py
┣ 📄 nodes.py
┣ 📄 react.py
┣ 📄 flow.png
┣ 📄 README.md (this file)
┣ 📄 .env
┣ 📄 .gitignore
┣ 📄 pyproject.toml
┗ 📄 uv.lock


---

## 🧠 Core Concepts Used

### 💡 Graph & State
LangGraph models workflows as a **state graph**:

- **State** – shared data that flows through nodes  
- **Nodes** – Python functions or classes representing logic/execution steps  
- **Edges** – transitions between nodes defining execution paths

Nodes take the current state, perform transformations or call LLM tools, and output a new state for the next node. :contentReference[oaicite:2]{index=2}

### 🛠 LangChain
LangChain is used here to provide LLM access and tools for Rich prompts & agent support. It integrates seamlessly with LangGraph for building agents that use tools or external APIs. :contentReference[oaicite:3]{index=3}

---

## 🧪 What the Code Does

### ✔ `main.py`
This file is the **entry point** of your LangGraph workflow. It likely:

- Loads environment variables + LLM configurations  
- Defines a `StateGraph` with nodes and edges  
- Connects your node logic from `nodes.py`  
- Compiles and executes the graph workflow

(Replace these comments with the exact description after reviewing your code.)

---

### ✔ `nodes.py`
This defines the **logical units** (functions or classes) that act as processing steps for the workflow.

Typical tasks here might include:

- Calling an LLM
- Pre-processing or post-processing text
- Decision logic to route execution
- Custom utilities used in the graph

Add more explanation after reviewing the specific node functions.

---

### ✔ `react.py`
This file may contain:

- A wrapper around LangChain/LangGraph that uses a **React agent** pattern  
- Or custom logic for function/tool calls

(React is a known agent pattern supported by LangChain where agents *reason + act* in loops.)
