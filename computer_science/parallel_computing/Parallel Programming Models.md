# Parallel Programming Models

The basic premise of a programming model is to map the existing algorithms to the available hardware to enhance overall performance and scalability. Furthermore, advancements in parallel memory architectures have also contributed new opportunities to achieve greater levels of performance. A parallel programming model encompasses the techniques to manage parallel operations within a program. When considering a programming model, the data model and the computational model must be taken into account. The data model deals with the data scope and how the data are exchanged amongst parallel processes. On the other hand, the computational model is more concerned with the control and execution of the different processes. Furthermore, the parallel programming model defines the methods by which parallelism is achieved.

## Data Model

The data model focuses on the scope of the data across all processes as well the process to exchange data between these processes. The two types of data models are the shared memory and private memory. In shared memory, different threads share the same memory location that is used to exchange data. However, in private memory, the memory of a thread or process is only visible to that particular thread or process. The data exchange between these threads is performed through send and receive operations.

## Computational Model

The focus of this particular model is on the control and execution mechanisms of the parallel operations. The computational model is involved in the parallel operations of threads, processes, or tasks. Several parallelism methods are currently available. These methods impact how a particular thread or process operates. A couple of computational models stand out: the loop-level data parallelism and the fork task model.

### Parallel Programming Model: Shared-memory Model

This model is popular among programmers because it is easy to use and implement because no specific consideration has to be given to the way memory locations are accessed between a serialized and a parallel program. In this particular model, independent threads or processes operate in a shared space.

In this particular model, parallel threads or processes access the same memory location. This shared memory space can be used for the parallel processes to exchange data. One issue known to this model is race condition, whereby multiple processes can compete for accessing and updating the very same memory location (Memon, 2016). This race condition can be managed by the use of locks, semaphores, or Mutex. Semaphores are variables used to control access to a critical resource shared among multiple processes. For example, a variable selected as a semaphore can be set to 1 by a specific process to notify other processes that a critical resource is being used. Other resources will not attempt to access the critical resource until the semaphore is set to 0. Mutex is another abstract data type used for resource synchronization and mutual exclusive access to a shared area. Processes communicate with each other and exchange data by reading and writing data through common storage or by sending messages.

### Parallel Programming Model: Threads Model

In the case of a threads model, one specific thread can initiate multiple different threads and generate simultaneous execution paths. Programs developed with multithreading can execute different sections of one program concurrently. Each thread controls its own resources, including the counter and memory stack. However, all threads share the same memory space through which they can exchange data and communicate. In C/C++ programming, a couple of methods are typically used to create and manage threads. The first is known as explicit threading, in which a program can create thread by issuing system calls as well as managing communications between the different threads. The second approach involves creating using the OpenMP module. This module includes functions specific to creating and managing threads. The implementation of a program based on the threads model is comprised of a library of functions that can be invoked from the parallel program and a set of compiler directives that be included within the parallel program.

### Message Passing Model

This model is used when each CPU in the system manages its own memory. In this particular case, programmers would have to determine how the parallelism is implemented and how messages are exchanged between processes. In order to implement this model, programmers will need to use existing programming libraries that are designed for this specific purpose, such as OpenMP.

The message passing model was created in the 1980s through individual implementations by programmers. However, standards were created in the 1990s, resulting in the creation of the MPI model, also known as the message passing interface.

The MPI model can be used in an environment with either a distributed memory or a shared memory.

### Data Parallel Model

In this model, processes can operate on the same data structure, but each of these processes works on a specific segment of the data. In a situation where the environment has a shared memory, the processes can access the data through the shared memory. This is also the case when a distributed memory architecture is in use. The data structure is broken up into segments that are accessed independently by each process.

Part of the challenge for programmers is to specify how the data are distributed and aligned across all existing tasks or processes.

### Hybrid Model

In the case of the hybrid model, the systems are composed of multiple nodes, where each node has its own address space and multiple processors share the same memory. These systems can also be viewed as clusters of symmetric shared-memory multiprocessors that are connected through a fast network. Hybrid models can also be a cluster of multiple-instruction, multiple-data streams. One particular implementation of a hybrid solution consists in using OpenMP for each node and the MPI between the different nodes. This particular solution can be problematic and potentially complex because programmers would be required to deal with two different programming models (OpenMP and MPI). Another option is using the MPI on the shared memory and distributed memory segments of the program instead of relying entirely on the shared programming model and all of its benefits.
