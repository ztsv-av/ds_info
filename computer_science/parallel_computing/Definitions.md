# Superscalar Execution

Superscalar execution involves allocating more than one ALU per chip and having both ALUs working in parallel to process code faster. A superscalar processor allows for multiple unrelated instructions to begin on the same time cycle on separate hardware units or pipelines. In some situations, superscalar processors can average less than one clock cycle, which translates to billions of instructions executed per second. This rate is significantly more impressive than singular scalar execution.

# True Data Dependency

In short, true data dependency exists when the output from one instruction is required as input for a different instruction. This is the most common type of data dependency that can be seen from pipelining. Pipelining involves a series of data processing elements where the output of one element is used as the input for a separate element. In general, in computer science, data dependency is a situation in which a program statement refers to the data of a preceding statement.

# Pipelining

A pipeline is a set of data processing elements that are connected in series, where the output of one element is the input for the next element. These elements are typically executed in parallel. Hence, pipelining is the process of running one of these series. In the context of implicit parallelism, pipelining occurs when a programming language enables the compiler to detect the embedded aspect that causes a series of processing elements to execute in parallel.

# Horizontal Waste

There are two primary types of waste relating to implicit parallelism: horizontal and vertical. Horizontal waste exists when certain slots within a cycle issue are unused. Superscalar processors look at multiple instructions from the same process and include both horizontal and vertical waste. It is optimal to minimize both types of waste given any process. In this context, cycle is short for clock cycle, and it refers to the time it takes for a processor to execute either a singular instruction or a set of instructions.

# Vertical Waste

Vertical waste is similar to horizontal waste, but it exists when an entire cycle is unused. In contrast, horizontal waste exists when some slot of the cycle is unused. Therefore, it may be clearly extrapolated that vertical waste is more severe than horizontal waste and that eliminating this type of waste is a higher priority than eliminating the latter, although both are important to eliminate if the goal is maximizing efficiency and speed.

# Communication

Communication in computation is defined as the exchange of data between the processor and the central processing unit. The movement of data is critical in ensuring that the performance of the computer is enhanced. There are costs that are associated with the transmission of data from one phase to another. The charges could emanate from the connecting cables and other units that are necessary to have a functional network

# Data Locality

Data locality refers to how close the data are to the code to be processed. This means that all relevant data must be locally available to the processing during the processing of a request. When dealing with data locality two concepts should be considered: near memory and far memory. In terms of performance, far memory is more expensive when compared to near memory due to the time required to seek data. 

# Contention

The data access and interprocess interaction can also lead to a level of contention that increases the total overhead. Contention occurs when multiple processes attempt to access the same process concurrently. One effective method for reducing resource contention is to restructure the parallel program to access the data in a pattern that is free of any contentions. To do so, programmers can use a distributed mapping scheme.

# One-to-All Broadcast and All-to-One Reduction

Under certain circumstances, a single process within a parallel program may send identical data to other processes, which is known as one-to-all broadcast. The source process would initially have the data to be broadcasted. However, once the process is complete, multiple copies of the initial data are generated and assigned to each process.

In an all-to-one reduction operation, the participating processes start with a buffer. The data from all processes are then combined and accumulated at a single destination process.
