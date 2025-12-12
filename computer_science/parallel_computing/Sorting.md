# Sorting

Converting a sequential sorting algorithm into a parallel algorithm involves distributing elements in order to be sorted to the different available processes. While effective, this operation can face several issues and challenges. While sorting in a sequential program, the input and the output (sorted list) are stored in memory. However, when we introduce parallel sorting, the lists can reside in a couple of areas.

The lists may be sorted on only one of the processes or spread among the available processes. Several distribution mechanisms exist but the most common method consists of enumerating the processes and using this enumeration to specific a global ordering for the sorted sequence. For example, if Xi is listed before Xj in the enumeration, all the elements stored in Xi will be smaller that the list stored in Xj. It is important to note that some enumerations may lead to more efficient parallel formulations than others.

## How Comparisons Are Performed

In the case of a sequential sorting, the compare-exchange of two elements can be easily performed since they are sorted locally in memory. However, in the case of parallel programs, the compare-exchange is not as easy since the elements reside on the same process.

In cases where a process may hold only elements of the list to be sorted, we can have processes exchange data with other processes during the comparison. Let us consider a couple of processes (Ai, Aj) which need to compare their stored elements ai and aj. Once the comparison is complete, Ai will store the smallest element while the other process stores the largest. Once the two processes exchange their elements, they can compare the data they received with their own elements. This process is illustrated in the figure below.

![image](https://user-images.githubusercontent.com/73081144/173257277-d73e7744-3c18-4acb-87b9-eab1819ea07d.png)

## More Than Element Per Process

If we are sorting a list of several elements using a number of processes, processes will still need to be able to distribute data to each other.

Let us assume we have a number of processes (n) (P1, P2, P3, … Pn) and let the number m represent the number of elements to be sorted.

Each process is assigned to a section of m/n numbers and all the processes will cooperate to sort the list (Kumar et al, 2016). Let us now assume the blocks are A0, A1, A3, … Am which are assigned to the processes. In this case, we can state that Ai<= Aj is every element of Ai is less than or equal to every element in Aj.

In this case, processes exchange blocks with other processes. Each process sends its block to another process after which the sorted blocks are merged but each process would only retain the appropriate half of the merged block. This method is known as compare-and-split since it consists of merging the blocks, comparing them, and then splitting them again.
