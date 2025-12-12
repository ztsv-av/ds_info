# Flynn's Classical Taxonomy

In 1966, Michael J. Flynn proposed a classification designed to help categorize parallel computers. This classification is very useful and was heavily used to design new processors and determine the needed functionality. Parallel computers are organized in four categories, as follows:

- Single-instruction stream, single-data stream (SISD): This case is typical of a single processor. As the name indicates, the serialized computer, the CPU processes one instruction at a time. Most early computers followed the SISD architecture.
- Single-instruction stream, multiple-data stream (SIMD): In this, the same instructions are executed in several threads. This technique is usually used on algorithms that can be broken up into parallel threads. Most graphics processing units fall under this classification because processing images can be handled in parallel.
- Multiple-instruction stream, single-data stream (MISD): In this, multiple instructions are grouped and processed as one. This is typically used when multiple instructions cannot operate independently and they all must agree on the end result (Gebali, 2011).
- Multiple-instruction stream, multiple-data stream (MIMD): This is the architecture used in supercomputers, distributed systems, or multicore systems. In this, several instructions are executed in parallel by multiple processors.

The MIMD architecture is the most popular architecture and was the basis for several recent processing systems, such as the following:

- Shared-memory multiprocessors
- Distributed-memory multiprocessors
- SIMD processors
- Systolic processors
- Cluster computing
- Grid computing
- Multicore processors
- Streaming multiprocessor (SM)
