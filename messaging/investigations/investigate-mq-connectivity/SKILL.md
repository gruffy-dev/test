---
name: investigate-mq-connectivity
description: >-
  Investigate an explicitly reported IBM MQ connectivity failure across the
  local queue manager, listener, and channel using approved read-only evidence.
  Use when connection setup or message-channel connectivity is failing; do not
  use to change or test connectivity through active control commands.
---

# Investigate MQ connectivity

## Purpose

Identify the earliest locally evidenced break across queue-manager,
listener, and channel state without actively changing or probing the MQ
environment.

## Information required

- Target MQ queue manager.
- Exact listener or channel name when known.
- Source, destination, symptom, and time context when available.

Ask one concise clarification question when the target and all relevant object
names are missing. Do not use wildcards to compensate for missing scope.

## Investigation workflow

1. Inspect current queue-manager status.
2. Inspect an exact listener and its definition when inbound connectivity is
   relevant and the listener name is known.
3. Inspect an exact channel and its definition when message-channel or client
   connectivity is relevant and the channel name is known.
4. Relate configured addresses, ports, channel roles, retry state, and local
   status only when supported by returned evidence.
5. Identify which external evidence remains required, such as remote MQ,
   network, DNS, firewall, or client diagnostics.
6. Report the earliest evidenced break and remaining uncertainty.

## Evidence standards

- Distinguish configuration, local process state, and tested reachability.
- Do not claim end-to-end connectivity merely because local components are
  running.
- Do not infer remote state, firewall policy, certificate validity, or client
  authorization without supporting evidence.
- Treat `Something went wrong!` and MQSC error messages as unavailable or
  failed evidence.
- Separate direct observations from hypotheses.

## Safety constraints

- Use only declared read-only capabilities for exact object names.
- Do not use wildcards or broaden the investigation into an inventory.
- Do not ping, start, stop, reset, resolve, alter, define, or delete MQ objects.
- Do not construct or submit provider-specific commands.
- Avoid reproducing connection or security configuration unless material.

## Expected result

Provide the evidenced local path, first observed break, likely explanation,
external evidence gaps, uncertainty, and safest next read-only step.
