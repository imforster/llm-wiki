---
type: entity
created: 2026-05-12
updated: 2026-05-12
sources: ["[[trusted-remote-execution-rex]]"]
tags: [tool, policy-language, authorization, aws, open-source]
---

# Cedar

Open-source policy language by [[aws]] for authorization decisions. Used by [[rex]] to define what operations a script or agent is permitted to perform. Designed for fine-grained, auditable access control.

- **Website**: [cedarpolicy.com](https://cedarpolicy.com/en)
- **Model**: `permit(principal, action, resource)` — explicit allow-list
- **Properties**: fast evaluation, analyzable (can prove properties about policies), human-readable

Cedar is the policy engine behind Amazon Verified Permissions and now Rex. In the agentic context, it provides the enforcement layer that makes "least privilege" concrete — every system call must match a permit statement or it's denied.

## See Also
- [[rex]]
- [[aws]]
- [[agentic-ai-governance]]
