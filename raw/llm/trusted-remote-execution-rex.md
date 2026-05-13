---
title: "Introducing Trusted Remote Execution: Policy-Enforced Scripts for AI Agents and Humans"
source: "https://aws.amazon.com/blogs/opensource/introducing-trusted-remote-execution-policy-enforced-scripts-for-ai-agents-and-humans/"
author:
  - "[[Nick MacDonald and Joshua Brindle]]"
published: 2026-05-04
created: 2026-05-04
description: "Today, we’re announcing Trusted Remote Execution (Rex, for short) — an open source scripting runtime where every system operation is authorized by policy. Scripts are written in Rhai, a lightweight language with no built-in system access. The only way to reach the host is through operations Rex explicitly provides, which are authorized against a Cedar […]"
tags:
  - "clippings"
---
Today, we’re announcing [Trusted Remote Execution](https://github.com/trusted-remote-execution) (Rex, for short) — an open source scripting runtime where every system operation is authorized by policy.

Scripts are written in [Rhai](https://rhai.rs/), a lightweight language with no built-in system access. The only way to reach the host is through operations Rex explicitly provides, which are authorized against a [Cedar](https://cedarpolicy.com/en) policy upon invocation.

## Our Journey

Running operations on production systems is a fact of life when managing software — reading logs, checking disk usage, restarting a service. The problem is that most script execution environments give a script whatever permissions the execution context has. A script intended to read a log file can just as easily delete one.

This gets worse with AI agents. When an agent generates and executes a script autonomously, there’s no human in the loop reviewing each system call. The usual safety nets — code review, approval workflows, allowlisted commands — don’t apply when the code is written at runtime.

We wanted a different model: one where an authorization policy — defined by the service owner, separate from the script — controls what the code is allowed to do at runtime. That’s what Trusted Remote Execution does.

## How It Works

Trusted Remote Execution pairs every script with a Cedar policy. The script says what to do — the policy says what’s allowed. Every operation is checked against the policy before it runs.

When a script runs, the Rhai engine has no direct access to the host. The only way to reach the system is through Rex’s purpose-built SDK of operations — `read, write, open`, and so on — each of which evaluates the Cedar policy before performing the underlying system call. If the policy doesn’t permit the action, the script receives an error and the operation never executes.

![](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2026/05/01/Screenshot-2026-04-30-at-10.52.07%E2%80%AFPM-1024x606.png)

## Agentic Operations: A Case Study

Most agentic sandboxes constrain the agent. Rex constrains what the agent can do to the host — giving the host owner full control over which operations are permitted, regardless of what the agent requests.

If an agent generates a script that exceeds the policy — from hallucination, prompt injection, or an overly eager interpretation of the task — it receives a clear `ACCESS_DENIED_EXCEPTION` rather than causing unintended side effects. The agent can observe this, reason about it, and adjust.

![](https://d2908q01vomqb2.cloudfront.net/ca3512f4dfa95a03169c5a670a4c91a19b3077b4/2026/05/01/Screenshot-2026-04-30-at-11.31.16%E2%80%AFPM-1024x264.png)

This makes it practical to give agents real operational access — reading logs, inspecting configurations, restarting services — while keeping a hard boundary around what they can touch. The policy creates a contract between the service owner and the agent, and Rex enforces it.

Want to learn how to enable agents to safely interface with your systems? See how to pair [Rex with IAM and SSM](https://trusted-remote-execution.github.io/ssm.html).

## Getting Started

*Rex runs on Linux and macOS. You’ll need Rust installed — if you don’t have it yet, see [rustup.rs.](https://rustup.rs/)*

Install `rex-runner` via Cargo:

`cargo install rex-runner`

**Create a policy:**

```python
cat > policy.cedar << 'EOF'
permit(
    principal,
    action in [
        file_system::Action::"open",
        file_system::Action::"read",

        // Uncomment to allow the write command:
        //file_system::Action::"create",
        //file_system::Action::"write",
    ],
    resource
);
EOF
```

**Create a script** that writes a file, then reads it back and returns it as the script output:

```python
cat > script.rhai << 'EOF'
write("/tmp/hello.txt", "Hello from Rex!");
cat("/tmp/hello.txt")
EOF
```

**Run it:**

```
rex-runner \
  --script-file script.rhai \
  --policy-file policy.cedar \
  --output-format human
```

The write fails because `write` and `create` are not in the policy:

```python
error: Permission denied:
  file_system::Action::"create" on /tmp/hello.txt
```

Uncomment `create` and `write` in `policy.cedar` and run again — the script completes and prints `Hello from Rex!`. The script didn’t change; only the policy did.

For the full setup guide and more examples, visit the [Getting Started guide](https://trusted-remote-execution.github.io/gettingstarted.html) or try the [interactive playground](https://trusted-remote-execution.github.io/playground.html).

## Get Involved

Trusted Remote Execution is open source under the Apache 2.0 License. We’re excited to build in the open — contributions are welcome, whether that’s adding new SDK extensions, improving documentation, or sharing how you’re using it.