# Scion Documentation

Source: https://googlecloudplatform.github.io/scion
Retrieved: 2026-04-07

Scion is an experimental multi-agent orchestration testbed by Google Cloud Platform, designed to manage concurrent LLM-based agents running in containers across local machines and remote clusters. It enables developers to run groups of specialized agents with isolated identities, credentials, and workspaces, allowing for a dynamic and evolving graph of parallel execution of tasks such as research, coding, auditing, and testing.

## Overview

Scion uses a flexible configuration system based on Profiles, Runtimes, and Harnesses. This allows you to define different environments (e.g., local Docker vs. remote Kubernetes) and switch between them easily.

- Global Settings: ~/.scion/settings.yaml (User-wide defaults)
- Grove Settings: .scion/settings.yaml (Project overrides)

### Getting Started

1. Install: Follow the Installation Guide
2. Initialize: Run `scion init` in your project root to create a `.scion` directory
3. Start an Agent: Use `scion start <agent-name> "<task>"` to launch an agent
4. Interact: Use `scion attach <agent-name>` to interact with the agent's session, or `scion logs <agent-name>` to view its output
5. Resume: Use `scion resume <agent-name>` to restart a stopped agent, preserving its state

### Architecture

Scion follows a Manager-Worker architecture:
- **scion**: A host-side CLI that orchestrates the lifecycle of agents. It manages the "Grove" (the project workspace) and provides tools for template management (`scion templates`).
- **Agents**: Isolated runtime containers (e.g., Docker) running the agent software (like Gemini CLI, Claude Code, or OpenAI Codex).

## Core Concepts

### Agent
An Agent is an isolated process running an LLM + Harness loop against a task. It acts as an independent worker with its own identity, credentials, and workspace. An agent is the fundamental unit of execution in Scion.

### Grove
A Grove (or Group) is a project workspace where agents live. It corresponds to a `.scion` directory on the filesystem. It can exist at the project level (generally located at the root of a git repository), or globally in the user's home folder.

Every grove has a unique Grove ID. Git-backed groves use deterministic UUID v5 identifiers (derived from the namespace and normalized git URL), ensuring the same repository always maps to the same ID regardless of protocol. Hub-native groves use random UUID v4 identifiers.

### Hub
The Hub is the central control plane of a hosted Scion architecture. It acts as the "brain" of the system, coordinating state across multiple users, groves, and runtime brokers.

- Identity & Auth: Manages user identities (via OAuth) and issues tokens for brokers and agents.
- State Persistence: Stores the definitive state of agents, groves, and templates in a central database.
- Orchestration: Dispatches agent lifecycle commands to the appropriate Runtime Brokers.
- Collaboration: Provides a shared view of the system via the Web Dashboard and Hub API.

### Profile
A Profile defines a complete execution environment by binding a specific Runtime to a set of behavior flags and Harness configuration overrides. Profiles allow you to switch between different environments (e.g., "Local Docker", "Production Kubernetes") without modifying agent templates. They are defined in the global or grove settings.yaml.

### Harness-Configuration
A Harness-config adapts a specific underlying LLM tool or agent software (like Gemini CLI, Claude Code, or OpenAI Codex) into the Scion ecosystem. It handles the specifics of provisioning, configuration, and execution for that particular tool inside an OCI container.

Examples: GeminiCLI, ClaudeCode, Codex, OpenCode.

The harness ensures that the generic Scion commands (start, stop, attach, resume) work consistently regardless of the underlying agent software.

### Template
A Template is a blueprint for creating an agent. It defines the base configuration, system prompt, and tools that an agent will use. Templates are stored in `.scion/templates/` and can be project-level or global (`~/.scion/templates/`). Users can manage templates using the `scion templates` command suite (create, clone, list, show, update-default).

Scion comes with default templates for supported harnesses (e.g., gemini, claude, opencode, codex), but users can create custom templates for specialized roles (e.g., "Security Auditor", "React Specialist").

### Runtime
The Runtime is the infrastructure layer responsible for executing the agent containers. Scion abstracts the container execution, allowing it to support different backends:
- Docker: The standard runtime for Linux and macOS.
- Podman: A daemonless, rootless alternative to Docker for Linux and macOS.
- Apple Container: Uses the native Virtualization Framework on macOS for improved performance.
- Kubernetes: Allows running agents as Pods in a Kubernetes cluster, enabling remote execution and scaling at production scale.

### Runtime Broker
A Runtime Broker is a compute node (e.g., a server, laptop, or K8s cluster) that registers with a Scion Hub to provide execution capacity. It manages the local lifecycle of agents dispatched from the Hub. It handles workspace synchronization, template hydration, and log streaming.

### Agent State Model
Agent state uses a layered model with three dimensions:
- **Phase** — The lifecycle stage of the agent container: created → provisioning → cloning → starting → running → stopping → stopped (or error)
- **Activity** — What the agent is doing within the running phase: idle, thinking, executing, waiting_for_input, blocked, completed, limits_exceeded, offline
- **Detail** — Freeform context about the current activity (tool name, message, task summary).

Activities like completed, blocked, and limits_exceeded are "sticky" — they persist until the agent is explicitly restarted or stopped. The blocked activity is set by agents themselves when they are intentionally waiting for an expected event (such as a child agent completing).

## Detailed Architecture

### Sub-agents
Because an agent through its template can contain home folder content, env var definitions, and custom mounts that collectively exposes all configuration available to the harness, scion-agents are not limited by the constraints of a harness' built-in sub-agent feature. While they are acting as sub-agents from the point-of-view of the Scion tool user-as-orchestrator, they are full agents in their capabilities.

### Workspace Strategy
Scion uses one of two strategies to give each agent an isolated git workspace:

**Local mode — Git Worktrees:**
- A new worktree is created at `../.scion_worktrees/<grove>/<agent>` with a dedicated branch.
- The worktree is mounted into the agent's container as `/workspace`.
- Agents operate on the same repository history but have independent working directories.
- Work is merged back to the main branch manually.

**Hub mode — Git Init + Fetch:**
- The broker injects SCION_GIT_CLONE_URL, SCION_GIT_BRANCH, and a GITHUB_TOKEN into the container.
- `sciontool init` inside the container initializes the workspace and fetches the repo over HTTPS.
- This approach handles workspaces that already contain .scion metadata.
- SSH credentials on the host are not used; a GITHUB_TOKEN is required.

### Resource Isolation
Scion enforces strict isolation between agents:
- Filesystem: Each agent has a dedicated home directory.
- Shadow Mounts (tmpfs): Prevents agents from accessing .scion configuration data or other agents' workspaces.
- Environment: Environment variables are explicitly projected into the container.
- Credentials: Sensitive credentials are mounted read-only or injected via environment variables.
- Externalized Grove Data: Non-git grove data and agent home directories are externalized.

### Contextual Agent Instructions
Scion automatically tailors an agent's operational context by appending supplemental instructions:
- agents-git.md: Appended when in a Git-backed workspace.
- agents-hub.md: Appended when connected to a Scion Hub.

### Plugin System
Scion supports a plugin architecture built on hashicorp/go-plugin for extending system capabilities via gRPC:
- Message Broker Plugins: Custom message delivery backends.
- Agent Harness Plugins: Custom harness implementations for new LLM tools.

## Philosophy

### Less is More
As frontier models improve, they become more capable of taking higher level intent. Scion is not attempting to be the full stack solution for multi-agent solutions. It focuses on being a "hypervisor for agents". Multi-agent system components such as agent memory, agent chatrooms, task management can be integrated as orthogonal concerns.

Agents are able to use Progressive Skills by using the `scion --help` command to dynamically learn how to use the tool.

### Isolation Over Constraints
Scion favors running agents in --yolo mode, while isolating them in containers, git worktrees, and on compute nodes subject to network policy at the infrastructure layer.

### Interaction is Imperative
Larger complex projects need collaboration. Expecting agents and workflows to proceed to completion without interaction is unreasonable. This means allowing humans to interact directly with the interactive mode of harnesses, as well as providing the means for agents to interact with each other "as users".

### Diversity Results in Higher Quality
Specialization through system prompts, model vendors, model sizes, harnesses and configurations all bring an ecosystem of strengths and weaknesses. Complex multi-agent solutions should be able to leverage a blend of strengths.

### Agents Lifecycles are Dynamic
The graph of an agent swarm and the tasks it works through is dynamic and not practical to determine in advance. Agents span those that are specialized and long lived, or highly ephemeral and coupled to just one task.

### Action Over Pondering
We are in a period of rapid discovery and experimentation. Scion aims to be a testbed to make such experiments simpler and more practical to explore.

## Supported Harnesses

### 1. Gemini CLI (gemini)
The default harness for Google's Gemini models.
Authentication methods (auto-detected):
- API Key: Set GEMINI_API_KEY or GOOGLE_API_KEY
- OAuth: Uses ~/.gemini/oauth_creds.json
- Vertex AI: Uses ADC with GOOGLE_CLOUD_PROJECT

### 2. Claude Code (claude)
Harness for Anthropic's Claude Code agent.
Authentication methods:
- API Key: Set ANTHROPIC_API_KEY
- Vertex AI: Uses Google Cloud's Vertex AI endpoint with ADC

### 3. OpenCode (opencode) [Experimental]
The OpenCode TUI.
Authentication methods:
- API Key: Set ANTHROPIC_API_KEY or OPENAI_API_KEY
- Auth File: Uses ~/.local/share/opencode/auth.json

Known limitations: No hook support.

### 4. Codex (codex)
Harness for the OpenAI Codex CLI.
Authentication methods:
- API Key: Set CODEX_API_KEY or OPENAI_API_KEY
- Auth File: Uses ~/.codex/auth.json

Default: Runs with --full-auto approval mode.

### Feature Capability Matrix

| Capability | Gemini | Claude | OpenCode | Codex |
|---|---|---|---|---|
| Resume | ✅ | ✅ | ✅ | ✅ |
| With Prompt | ✅ | ✅ | ✅ | ❌ |
| Custom Session ID | ❌ | ✅ | ❌ | ❌ |
| Interject | ✅ | ✅ | ✅ | ✅ |
| Enqueue | ✅ | ✅ | ✅ | ✅ |
| Hooks | ✅ | ✅ | ❌ | ❌ |
| OpenTelemetry | ✅ | ✅ | ❌ | ✅ |
| System Prompt Override | ✅ | ✅ | ❌ | ❌ |

## Package Architecture (Go)

Key packages:
- pkg/api/ — Shared types
- pkg/agent/ — Agent lifecycle: Manager interface, provisioning, run, delete
- pkg/config/ — Settings, template resolution, path management
- pkg/harness/ — LLM-specific adapters
- pkg/runtime/ — Container runtime abstraction (Docker, Apple, K8s)
- pkg/hub/ — Hub API server
- pkg/runtimebroker/ — Runtime Broker API server
- pkg/store/sqlite/ — SQLite persistence
- pkg/sciontool/ — Internal CLI status tool used by agents

## Agent Lifecycle

### Solo Mode
1. Grove resolution: locates the .scion directory
2. Settings loading: reads settings.yaml
3. Provisioning: creates directories, resolves template chain, creates git worktree, runs harness provisioning
4. Image resolution: resolves container image, pulls if needed
5. Container launch: builds run arguments, mounts volumes, launches in detached mode
6. Status update: writes agent-info.json

### Hosted Mode
1. Hub sync: CLI registers/syncs grove with Hub
2. API call: POST /api/v1/groves/{groveId}/agents
3. Broker selection: Hub selects a Runtime Broker
4. Environment resolution: merges env vars and secrets from all scopes
5. Template hydration: resolves template with content hash
6. Dispatch: sends to broker via HTTP or WebSocket tunnel
7. Broker execution: provisions and starts agent
8. Status reporting: broker reports back via heartbeats

## Glossary

- **Agent**: An isolated worker instance running an LLM harness
- **Grove**: A project-level grouping of agents and configuration
- **Harness**: An adapter for an underlying LLM tool
- **Hub**: The centralized control plane in hosted deployment
- **Profile**: Configuration overrides for runtime execution
- **Runtime**: The underlying container execution technology
- **Runtime Broker**: A compute node that executes agents
- **sciontool**: Helper utility injected into agent containers
- **Template**: A versioned blueprint for an agent
- **Grove ID**: Unique identifier (UUID v5 for git-backed, UUID v4 for hub-native)
- **Plugin**: Extension module via hashicorp/go-plugin
- **Shared Directory**: Persistent mutable storage shared between agents in a grove
- **Workspace**: The working directory mounted into an agent container
