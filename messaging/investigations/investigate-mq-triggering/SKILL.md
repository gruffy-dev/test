---
name: investigate-mq-triggering
description: >-
  Investigate IBM MQ application or channel triggering for one explicitly
  named local queue using approved queue, initiation-queue, process-definition,
  and queue-manager evidence. Do not use to generate trigger events, consume
  messages, start applications, or change triggering configuration.
---

# Investigate MQ triggering

## Purpose

Determine which queue or process-definition condition is supported when an
expected MQ trigger has not resulted in application or channel processing.

## Information required

- Target MQ queue manager.
- Exact triggering local queue name.
- Expected triggered application or channel when known.

Ask one concise clarification question when essential scope is missing and
cannot be inferred safely. Do not use wildcards to discover triggering
objects.

## Investigation workflow

1. Inspect the exact application or transmission queue's current status and
   triggering configuration.
2. Identify the configured trigger control, type, threshold, initiation queue,
   process definition, and trigger data when returned.
3. Inspect the exact initiation queue named by the queue configuration when it
   is present and relevant.
4. Inspect the exact process definition named by the queue configuration when
   one is present.
5. Inspect queue-manager status only when platform availability remains a
   plausible explanation.
6. Identify evidence unavailable through these capabilities, including trigger
   monitor, operating-system process, application, or message-specific state.

## Evidence standards

- Distinguish triggering configuration, trigger-event preconditions,
  initiation-queue state, process definition, and actual application state.
- Do not infer that a trigger event occurred merely because its configuration
  appears valid.
- Do not infer that the trigger monitor consumed or acted on a trigger message.
- Do not read application or trigger messages to fill an evidence gap.
- Treat `Something went wrong!` and MQSC error messages as unavailable or
  failed evidence.
- Separate direct observations from hypotheses.

## Safety constraints

- Use only declared read-only capabilities and exact object names obtained
  from the user, trusted Target routing, or returned configuration evidence.
- Do not put, get, browse, move, replay, delete, or clear messages.
- Do not generate a trigger event or start an application or channel.
- Do not alter queue, process, or queue-manager configuration.
- Do not construct or submit provider-specific commands.

## Expected result

Provide the evidenced trigger path, first observed configuration or state gap,
remaining external evidence, uncertainty, and safest next read-only step.
