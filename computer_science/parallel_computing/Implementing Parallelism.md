# Techniques Used to Implement Parallelism

- Data-level parallelism: In this case, several data streams are processed simultaneously. For example, an algorithm working on the content of a given file through multiple threads simultaneously (Gebali, 2016).
- Instruction-level parallelism: This is the typical parallel processing of a given algorithm. In this case, multiple instructions are processed in parallel and simultaneously.
- Thread-level parallelism: A program can be broken down into multiple threads whereby each thread can share CPU and memory resources. In this particular case, multiple threads can be executed in parallel with one or multiple CPUs.
- Process-level parallelism: Unlike a thread, a process controls its own resources and does not share computer resources with other processes. In this type of parallelism, several processes are running simultaneously and in parallel, independently of each other.
