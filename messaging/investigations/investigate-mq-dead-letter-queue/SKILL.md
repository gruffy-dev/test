---
name: investigate-mq-dead-letter-queue
description: >-
  Investigate the configured IBM MQ dead-letter queue using approved
  queue-manager configuration and exact queue status evidence. Use for
  dead-letter backlog, capacity, or availability questions; do not use to
  browse, replay, move, delete, or inspect message contents.
---

# Investigate an MQ dead-letter queue

## Purpose

Establish which dead-letter queue is configured and assess its current
capacity and consumer state without accessing any messages.

## Information required

- Target MQ queue manager.

Ask one concise clarification question when the target cannot be inferred
safely.

## Investigation workflow

1. Inspect queue-manager configuration to identify the configured dead-letter
   queue.
2. If no dead-letter queue is configured, report that fact and stop.
3. Use the exact returned dead-letter queue name to inspect current queue
   status and relevant queue configuration.
4. Compare point-in-time depth with capacity and current input or output
   activity when returned.
5. Identify the operational evidence required to understand message causes;
   do not obtain that evidence by reading message contents.

## Evidence standards

- Treat the configured dead-letter queue name as configuration, not proof that
  the queue exists or is healthy.
- Treat queue depth as a point-in-time observation, not a trend.
- Do not infer why messages reached the dead-letter queue without separate
  evidence.
- Treat `Something went wrong!` and MQSC error messages as unavailable or
  failed evidence.
- Separate direct observations from hypotheses.

## Safety constraints

- Use only declared read-only capabilities and the exact configured queue
  name.
- Do not use wildcards or inspect unrelated queues.
- Do not browse, get, move, replay, delete, or clear messages.
- Do not alter queue-manager or queue configuration.
- Do not construct or submit provider-specific commands.

## Expected result

Provide the configured dead-letter queue, observed queue condition, capacity
risk, supported interpretation, uncertainty, and safest next read-only step.
