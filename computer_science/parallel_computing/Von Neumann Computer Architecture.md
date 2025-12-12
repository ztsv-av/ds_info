# Von Neumann Computer Architecture

The first computers were created based on the model developed by John von Neumann. This model consisted of a central processing unit (CPU), memory, and an input–output (I/O) system. A CPU is comprised of a processing unit and a control unit. Following the von Neumann model, early computers had one CPU, which would execute one instruction at a time. This meant that instructions needed to be executed sequentially, and if any of the instructions were delayed awaiting a response from an I/O request, the entire program would also have to wait. To solve this problem, the concept of multithreading, where several threads can work together on the same program, was created. 

For example, a thread can be initiated to request some data from storage while the parent thread can continue with the other instructions until the I/O request is fulfilled.
