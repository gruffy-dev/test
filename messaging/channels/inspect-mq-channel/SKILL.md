---
name: inspect-mq-channel
description: >-
  Inspect one explicitly named IBM MQ channel using approved current-status and
  definition evidence. Use for running, retrying, stopped, inactive, in-doubt,
  connection, or transmission-queue questions; do not use to start, stop,
  reset, resolve, ping, or alter a channel.
---

# Inspect an MQ channel

## Purpose

Answer bounded read-only questions about one exact MQ channel and its current
relationship to the configured channel definition.

## Information required

- Target MQ queue manager.
- Exact channel name.

Ask one concise clarification question when required scope is missing and
cannot be inferred safely. Do not replace an exact channel name with a
wildcard.

## Inspection workflow

1. Inspect current status for the exact channel.
2. Inspect the channel definition when connection, retry, heartbeat,
   transmission-queue, or security configuration is relevant.
3. Distinguish an inactive channel from a failed channel using returned status
   and the channel's expected role.
4. Relate retry, in-doubt, remote queue-manager, and transmission-queue evidence
   only when those fields are returned.
5. Identify the smallest additional read-only investigation required to
   explain remaining uncertainty.

## Evidence standards

- Distinguish current channel instances from saved or configured state.
- Do not treat inactivity as failure without evidence that the channel should
  currently be active.
- Do not infer remote availability solely from local configuration.
- Treat `Something went wrong!` and MQSC error messages as unavailable or
  failed evidence.
- Separate direct observations from hypotheses.

## Safety constraints

- Use only declared read-only capabilities for the exact channel.
- Do not use wildcards or request every channel instance.
- Do not start, stop, reset, resolve, ping, alter, define, or delete channels.
- Do not construct or submit provider-specific commands.
- Avoid reproducing connection or security configuration unless material to
  the user's question.

## Expected result

Provide the exact channel and target, current status, material definition
evidence, supported interpretation, uncertainty, and safest next read-only
step.
