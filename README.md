# Multiple Producer / Multiple Consumer Job Queue

A simple distributed job queue built on Redis, supporting multiple concurrent producers and consumers with safe job processing and retry handling.

---

## Overview

This project implements a lightweight background job queue using Redis as the coordination layer.

It supports:

- Multiple producers enqueueing jobs concurrently  
- Multiple consumers processing jobs concurrently  
- Blocking job consumption (no polling)  
- Retry logic  
- Optional dead-letter queue  

---

## Architecture

- **Producers** push jobs into a Redis list  
- **Consumers** block on the list and process jobs  
- Redis guarantees atomic push/pop operations  

Basic flow:

1. Producer → `LPUSH queue`
2. Consumer → `BRPOP queue`
3. Process job
4. Retry or move to DLQ on failure

---

## Redis Data Structures

| Key | Type | Purpose |
|-----|------|---------|
| `queue` | List | Pending jobs |
| `queue:processing` | List | In-flight jobs |
| `queue:dlq` | List | Failed jobs |

For safer processing, use:

BRPOPLPUSH queue queue:processing

This prevents job loss if a consumer crashes mid-processing.

---

## Getting Started

### 1. Run Local Redis Open Source Instance

After installing Redis, run executable from command line:

`redis-server`

Redis will be running in the foreground.

---

### 2. Start Job Queue Server

Run the job queue server:

`python3 -m server.server`

---

### 3. Start a Consumer

Run a single consumer:

`python3 -m client.consumer`

Run multiple consumers to test concurrency:

`python3 -m client.consumer & python3 -m client.consumer &`

---

### 4. Enqueue a Job

Run a producer:

`python3 -m client.producer`

---

## Failure Handling

- **Consumer crash:**  
  Use a processing queue to avoid losing jobs.

- **Job failure:**  
  Retry up to a max limit, then move to `queue:dlq`.

- **Redis restart:**  
  Enable AOF persistence for durability.

---

## Scaling

Scale horizontally by:

- Running more producers  
- Running more consumers  

Redis handles synchronization.

---

## Why Redis?

Redis provides:

- Atomic list operations  
- Blocking pop  
- High performance  
- Simple deployment  

It’s a good balance between simplicity and reliability compared to full message brokers.

---

## Future Improvements

- Delayed jobs  
- Job priorities  
- Visibility timeouts  
- Metrics and monitoring  

---

## Summary

A minimal, practical implementation of a multiple producer / multiple consumer job queue using Redis.

Designed for clarity, correctness, and learning distributed systems fundamentals.
