---
name: inspect-mq-listener
description: >-
  Inspect one explicitly named IBM MQ listener using approved current-status
  and definition evidence. Use for listener availability, transport, address,
  port, or control questions; do not use to start, stop, alter, define, or
  delete a listener.
---

# Inspect an MQ listener

## Purpose

Answer bounded read-only questions about one exact MQ listener and whether its
current state agrees with its configured definition.

## Information required

- Target MQ queue manager.
- Exact listener name.

Ask one concise clarification question when required scope is missing and
cannot be inferred safely. Do not replace an exact listener name with a
wildcard.

## Inspection workflow

1. Inspect current status for the exact listener.
2. Inspect its definition when transport, address, port, or start control is
   relevant.
3. Compare configured and current state without treating configuration as
   proof of reachability.
4. Identify evidence that is unavailable from the queue manager, such as an
   external network path or firewall decision.
5. Report the smallest next read-only check required to narrow the issue.

## Evidence standards

- Distinguish listener configuration, process status, and tested network
  reachability.
- Do not claim that clients can connect merely because the listener is
  running.
- Treat `Something went wrong!` and MQSC error messages as unavailable or
  failed evidence.
- Separate direct observations from hypotheses.

## Safety constraints

- Use only declared read-only capabilities for the exact listener.
- Do not use wildcards or request all listeners.
- Do not start, stop, alter, define, or delete listeners.
- Do not construct or submit provider-specific commands.
- Avoid reproducing network configuration unless material to the question.

## Expected result

Provide the exact listener and target, observed state, relevant definition,
supported interpretation, uncertainty, and safest next read-only step.
