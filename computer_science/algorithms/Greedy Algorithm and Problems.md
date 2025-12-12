# Greedy Algorithm

A greedy algorithm is an approach that tries to find simple, easy-to-implement solutions to complex problems. This solution is built up step-by-step by always choosing the next move that provides the most immediate benefit. Such algorithms are called greedy because they focus on the immediate benefits rather than considering the larger problem as a whole. Once a decision has been made, it is never reconsidered, whatever situation may arise later.

Greedy algorithms are successful when they are applied to solve a problem with the following two properties:

- Greedy-choice property: This means that the global optimum solution can be achieved by selecting the local optimum. In other words, without having to reconsider the selections that are already taken, from a local optimum (i.e., the cheapest road between two adjacent cities), one can reach a global optimum (i.e., the cheapest road between the destination and the origin).
- Optimal substructure property: The optimal solution to a problem can be derived by finding the optimal solutions to its subproblems.

## Various Problems

### Egyptian Fraction

It seems that during the time of Ancient Egyptians, it was demanded that every fraction written must have a numerator that is equal to the value 1. The goal was to represent any rational number of the form n/m as the sum of different unit fractions (a unit fraction always has a numerator that is equal to 1). These sums are referred to as Egyptian fractions.

```
```

### Job Sequencing Problem

This problem is concerned with the scheduling of a set of jobs with the following characteristics:

- Each job has a deadline.
- Each job has an associated profit that will be achieved if the project is finished before the deadline.
- Each job takes a single unit of time to complete.
- The minimum possible deadline for any job is 1.
- 
Thus, the scheduling of the jobs maximizes the total profit if only one job can be scheduled at a time.

```
```

### Huffman Coding

Huffman coding provides an efficient way to store characters by assigning shorter codes to characters that occur more frequently and longer codes to characters that appear less frequently in the English language. For example, the letters E and T occur frequently in the English language; thus, it could be assigned one bit each. On the other hand, letters such as A, O, and R also occur frequently but less frequently than E and T; thus, they can be assigned two bits each, and so forth. When used in network transmission, the overall length of the transmission is shorter when using Huffman encoded characters over fixed-length encoding. This made Huffman code a good option as a data compression algorithm. Before assigning a bit pattern to each character, you need to assign a weight for each character based on its frequency of use. The letters with a high frequency of use will be assigned high weights; for example, if you assume that the frequency of the letter T is 12%, it will be assigned a weight of 12. After establishing the weight of characters, you can build a tree based on those values.
![image](https://user-images.githubusercontent.com/73081144/136143493-a8258ffd-7ead-4e21-b2aa-c1bf4fb423ce.png)

```
```

### Prim’s Algorithm

Prim’s algorithm, a greedy algorithm, is used to find a minimum spanning tree (MST) from a connected, weighted, and undirected graph. A spanning tree of a graph is a subgraph of a connected and undirected graph that has the following characteristics:

- It is a tree (there are no loops).
- All of the vertices are connected.

You can obtain multiple different spanning trees from the same weighted, connected, and undirected graph. Among all of these spanning trees, the one with weight (the sum of all of the weights in the edges) that is less than or equal to the weight of every other spanning tree is an MST. If a weighted, connected, and undirected graph has V nodes, then its MST has (V – 1) edges.

```
```

### Dial’s Algorithm

Dial’s algorithm is simply a modification of Dijkstra’s shortest path algorithm, in which a bucket queue is used as a data structure to obtain better running time. Dijkstra’s and Dial’s algorithms are similar to Prim’s algorithm, which is used to obtain the MST from a connected graph using a greedy approach.

```
```

### Graph Coloring

Graph coloring is a mechanism that is used to label the different elements of a graph (including nodes, edges, and regions) using some well-defined constraints. Some examples of such constraints when coloring are the order in which the color is applied and the restriction when applying the colors. For example, node or vertex coloring refers to an assignment of colors to the nodes or vertices of a graph in such a way that no two adjacent nodes or vertices have the same color. This means that no two nodes connected by the same edge should have the same color.

```
```

### Memory Allocation

Memory allocation can be defined as the process that is performed by an operating system (OS) where blocks of memory (also referred to as pages) are assigned to processes or threads on request. Typically, there is an OS process called allocator, which is the one that handles the request from the processes and threads. The allocator receives memory from the OS and must manage this space to satisfy the request. There are different mechanisms used to implement this functionality, such as the first fit approach, which uses the principle of a greedy algorithm.

```
```

### The Operating System

The OS often deals with multiple processes that request central processing unit (CPU) access at the same time. To handle how processes and threads are assigned to a CPU, the OS has a process scheduler, which uses different approaches to identify what process or thread should be assigned next, which one should be stopped from using the CPU, and how to keep track of the execution point if a process is removed from the CPU before it finishes its execution. The shortest job next (SJN; also known as the shortest job first SJF) is a scheduling approach or policy in which the scheduler selects the process with the smallest execution time to be the next process to get CPU time. This is a nonpre-emptive approach, and it assumes that the execution time of every process is known before being executed, which is not always true.

```
```

### Set Cover Problem

The set cover problem is a great example in which a greedy algorithm can help you find a solution to a problem, but it may not be the optimal solution. A greedy algorithm is one that makes the best choice at each stage. The set cover problem can be defined as follows:

For a given universe U with n amount of items (|U| = n) and a group of sets S1,..., Sk, where all subsets of U (S1,..., Sk ⊆ U), you define a set cover C as a collection of some of the sets from S1,..., Sk whose union is the entire universe U. On each iteration, greedy algorithm selects the smallest set and adds it to the set cover C (on first iteration it is empty) and checks if the union of sets S in set cover C equals to the universe U

```
```

### Bin Packing Problem

The bin packing problem consists of packing a set of items of different values (e.g., volume, weight, cost, and so forth) into a finite number of bins or containers such that you minimize the total number of bins or containers used. The easy-to-implement greedy algorithm solves the bin packing problem by following a straightforward greedy approximation. You select e.g. packages in sequence starting from the first package. If the weight of the package fits in the remaining e.g. truck capacity, add it to that truck, otherwise add it to the next truck until the needed number of packages is reached.

Example:  

A shipping company needs to send six different products using boxes that only support 10 pounds in weight. The weight for each of the products is given by the following table:

| Product ID | Weight |
|------------|--------|
| 00001      | 4      |
| 00002      | 7      |
| 00003      | 1      |
| 00004      | 4      |
| 00005      | 2      |
| 00006      | 1      |

After several attempts, the best option is to use two different boxes, placing products 00001, 00004, and 00005 (a total of 10 pounds) in one box and placing products 00002, 00003, and 00006 (a total of 9 pounds) in the second box.

```
```

### K-Center Problem

The k-center problem deals with the placement of a service (e.g., automated teller machines ATMs, warehouses, supermarkets, and so on) between a number of cities such that the maximum distance from a city to the service is minimized. The constraint is that the service(s) must be located on some of the cities in the problem. Thus, if you have n cities and k services, you will have k cities with a distance of 0 to the service.

```
```
