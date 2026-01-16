A single OS thread switch is microseconds, but the effective performance loss from cache disruption can reach milliseconds for cache-heavy workloads.

| Overhead source              | What happens                           | Approx cost          |
| ---------------------------- | -------------------------------------- | -------------------- |
| Register save/restore        | CPU saves and restores registers       | ~0.1–1 µs            |
| Stack switch                 | Switch to another thread’s stack       | ~0.1 µs              |
| Scheduler bookkeeping        | OS updates run queues                  | ~0.1 µs              |
| TLB effects                  | Address translation cache invalidation | ~0.1–1 µs            |
| Instruction cache misses     | Reload code for new thread             | ~0.5–5 µs            |
| Data cache misses            | Reload data for new thread             | ~1–100 µs            |
| Branch predictor disruption  | Incorrect branch predictions           | ~0.1–1 µs            |
| Python GIL handling          | Lock release/acquire, wakeups          | ~0.5–5 µs            |
| Lost locality (total impact) | Cold caches over several accesses      | ~1 µs → milliseconds |

```
# thread X doing training task
def train():
    while True:
        batch = next(train_loader)
        loss = model(batch)
        loss.backward()
        optimizer.step()

# thread Y doing logging task
def log():
    while True:
        print(get_current_loss())
        time.sleep(1)
```

```
# thread X loads data batch and puts it into queue
def load_data():
    while True:
        batch = preprocess(next(dataset))
        queue.put(batch)

# thread Y doing training task
def train():
    while True:
        batch = queue.get()
        step(batch)

# thread Z doing logging task
def log():
    while True:
        print(get_current_loss())
        time.sleep(1)
```
