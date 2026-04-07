# Chapter 02: Thread Synchronization and Coordination

## 1. `Thread_definition.py` — Basic Thread Creation
* **Concept:** Creating and running basic threads using the `threading` module.
* **Execution:** Used a loop to create 10 threads calling `my_func`. Started and joined each one sequentially.
* **End Use:** Running a single function multiple times concurrently (e.g., background tasks).
* **When to Use:** For simple concurrent execution without needing custom classes.
* **How to Use:** Use `threading.Thread(target=..., args=...)`, then `start()` and `join()`.
* **Advantages:** Simple, clean, and requires no class overhead.
* **Disadvantages:** Sequential `start/join` in a loop prevents real concurrency; lacks complex management.
git commit --amend -m "Add descriptive comments to Chapter 01 and 02"
---

## 2. `Thread_determine.py` — Named Threads
* **Concept:** Assigning unique names to threads for identification.
* **Execution:** Defined three functions (A, B, C) and used `threading.currentThread().getName()` to log their execution.
* **End Use:** Critical for debugging and logging in multi-threaded environments.
* **When to Use:** When you need to track specific thread behavior in complex logs.
* **How to Use:** Pass `name='...'` during thread creation; retrieve with `getName()`.
* **Advantages:** Improves debuggability; clearly identifies execution flow.
* **Disadvantages:** Only identifies threads; does not influence execution logic or priority.

---

## 3. `Thread_name_and_processes.py` — Thread Class with Process ID
* **Concept:** Subclassing `Thread` and monitoring Process IDs (PIDs).
* **Execution:** Created `MyThreadClass` to print its name and PID, demonstrating that all threads share one process.
* **End Use:** Understanding the shared memory model and the limitations of the Python GIL.
* **When to Use:** When custom thread behavior is needed through object-oriented subclassing.
* **How to Use:** Inherit from `threading.Thread` and override the `run()` method.
* **Advantages:** Clean, reusable design; easy to add custom properties to threads.
* **Disadvantages:** Shared PID confirms no true CPU parallelism in standard Python (CPython).

---

## 4. `MyThreadClass.py` — Custom Thread Class with Duration
* **Concept:** Simulating workloads using custom classes and random sleep intervals.
* **Execution:** Created 9 threads with varying sleep durations (1-10s) and measured total execution time.
* **End Use:** Simulating real-world concurrent tasks like file downloads or API requests.
* **When to Use:** When threads need individual properties (like specific timers or data sets).
* **How to Use:** Pass custom arguments to `__init__` and call `Thread.__init__(self)`.
* **Advantages:** Object-oriented; total time is determined by the slowest thread, not the sum.
* **Disadvantages:** Unpredictable output order; potential for "messy" console printing without locks.

---

## 5. `MyThreadClass_lock.py` — Thread Lock (Sequential)
* **Concept:** Mutual Exclusion (Mutex) using `threading.Lock()`.
* **Execution:** Added a lock to the 9-thread simulation; each thread acquired the lock for its entire duration.
* **End Use:** Protecting shared resources (files/databases) from simultaneous access.
* **When to Use:** When data integrity is more important than speed.
* **How to Use:** Call `lock.acquire()` before the task and `lock.release()` after.
* **Advantages:** Prevents race conditions and ensures data integrity.
* **Disadvantages:** Eliminates concurrency benefits; risk of deadlocks if a lock isn't released.

---

## 6. `MyThreadClass_lock_2.py` — Thread Lock (Optimized)
* **Concept:** Fine-grained locking to improve performance.
* **Execution:** Released the lock before `time.sleep()`, allowing other threads to enter their critical sections during the wait.
* **End Use:** Balancing data protection with execution speed.
* **When to Use:** When only a small portion of the thread's work (like a print or write) needs protection.
* **How to Use:** Keep the "locked" section as short as possible.
* **Advantages:** Much faster than full-task locking; allows threads to overlap during non-critical work.
* **Disadvantages:** Requires careful analysis of what truly needs to be "locked."

---

## 7. `Rlock.py` — Reentrant Lock
* **Concept:** Using `threading.RLock()` to allow nested lock acquisition.
* **Execution:** Implemented a `Box` class where methods calling each other both required the same lock.
* **End Use:** Solving deadlocks in recursive functions or nested method calls.
* **When to Use:** When a thread needs to re-acquire a lock it already holds.
* **How to Use:** Replace `Lock()` with `RLock()`; must be released as many times as it is acquired.
* **Advantages:** Prevents "self-deadlock" in complex class structures.
* **Disadvantages:** Slightly more overhead than a standard lock.

---

## 8. `Semaphore.py` — Semaphore for Signaling
* **Concept:** Controlling resource access via `threading.Semaphore()`.
* **Execution:** Used a semaphore (starting at 0) to force a consumer to wait for a producer's signal.
* **End Use:** Managing resource pools or simple producer-consumer signaling.
* **When to Use:** To limit the number of threads accessing a resource or for basic synchronization.
* **How to Use:** `acquire()` decrements the counter; `release()` increments it and wakes waiting threads.
* **Advantages:** Precise control over the number of allowed concurrent threads.
* **Disadvantages:** Can lead to race conditions on shared variables if not used with a lock.

---

## 9. `Event.py` — Thread Event Signaling
* **Concept:** One-to-many signaling using `threading.Event()`.
* **Execution:** A Producer sets an event after creating data; a Consumer waits for the event to trigger.
* **End Use:** Notifying threads that a specific condition (like "Data Ready") has been met.
* **When to Use:** For simple "stop/go" signals between threads.
* **How to Use:** Use `event.wait()` to block and `event.set()` to signal all waiting threads.
* **Advantages:** Simple and clean; does not require manual counter management.
* **Disadvantages:** Risk of missing signals if `clear()` is called too quickly.

---

## 10. `Condition.py` — Thread Condition Variable
* **Concept:** Complex coordination using `threading.Condition()`.
* **Execution:** Managed a buffer where the Producer waits if the list is full and the Consumer waits if it's empty.
* **End Use:** Sophisticated Producer-Consumer models with state-dependent logic.
* **When to Use:** When threads must wait for a specific state change in shared data.
* **How to Use:** Use `with condition:`, `wait()` to pause, and `notify()` to wake others.
* **Advantages:** Prevents both buffer overflow and underflow; more powerful than Events.
* **Disadvantages:** Higher complexity; prone to bugs if state logic is incorrect.

---

## 11. `Barrier.py` — Thread Barrier Synchronization
* **Concept:** Synchronizing multiple threads at a specific checkpoint.
* **Execution:** Three "runner" threads wait at a `finish_line.wait()` until all arrive before proceeding.
* **End Use:** Phased parallel algorithms where all parts must finish before the next step starts.
* **When to Use:** When you need a "meeting" point for a fixed number of threads.
* **How to Use:** Define `Barrier(n)`; all threads call `wait()`.
* **Advantages:** Guarantees all threads stay "in sync" through different execution phases.
* **Disadvantages:** If one thread fails to reach the barrier, all other threads block indefinitely.

---

## 12. `Threading_with_queue.py` — Thread-Safe Queue
* **Concept:** Using the `queue.Queue` class for safe data exchange.
* **Execution:** One producer adds items to a queue while three consumers process them concurrently.
* **End Use:** Standard practice for producer-consumer patterns in Python.
* **When to Use:** Whenever threads need to share data safely without manual locking logic.
* **How to Use:** Use `put()` to add data and `get()` to retrieve it.
* **Advantages:** Automatically handles all internal locking; highly scalable with multiple consumers.
* **Disadvantages:** Requires a "poison pill" or timeout to stop consumer threads gracefully.

