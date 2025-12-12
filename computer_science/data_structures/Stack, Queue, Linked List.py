class Node:
   def __init__(self, initial_data):
      self.data = initial_data
      self.next = None

class LinkedList:
   def __init__(self):
      self.head = None
      self.tail = None

   def append(self, new_node):
      if self.head == None:
         self.head = new_node
         self.tail = new_node
      else:
         self.tail.next = new_node
         self.tail = new_node

   def prepend(self, new_node):
      if self.head == None:
         self.head = new_node
         self.tail = new_node
      else:
         new_node.next = self.head
         self.head = new_node

   def insert_after(self, current_node, new_node):
      if self.head == None:
         self.head = new_node
         self.tail = new_node
      elif current_node is self.tail:
         self.tail.next = new_node
         self.tail = new_node
      else:
         new_node.next = current_node.next
         current_node.next = new_node
   
   def remove_after(self, current_node):
     # Special case, remove head
     if (current_node == None) and (self.head != None):
        succeeding_node = self.head.next
        self.head = succeeding_node  
        if succeeding_node == None:    # Removed last item
           self.tail = None
     elif current_node.next != None:
        succeeding_node = current_node.next.next
        current_node.next = succeeding_node
        if succeeding_node == None:    # Removed tail
           self.tail = current_node


class Stack:
   def __init__(self):
      self.list = LinkedList()
      
   def push(self, new_item):
      # Create a new node to hold the item
      new_node = Node(new_item)
      
      # Insert the node as the list head (top of stack)
      self.list.prepend(new_node)

   def pop(self):
      # Copy data from list's head node (stack's top node)
      popped_item = self.list.head.data
      
      # Remove list head
      self.list.remove_after(None)
      
      # Return the popped item
      return popped_item

class Queue:
   def __init__(self):
      self.list = LinkedList()
      
   def enqueue(self, new_item):
      # Create a new node to hold the item
      new_node = Node(new_item)
      
      # Insert as list tail (end of queue)
      self.list.append(new_node)

   def dequeue(self):
      # Copy data from list's head node (queue's front node)
      dequeued_item = self.list.head.data
      
      # Remove list head
      self.list.remove_after(None)
      
      # Return the dequeued item
      return dequeued_item


# HashTable class using chaining.
class ChainingHashTable:
   # Constructor with optional initial capacity parameter.
   # Assigns all buckets with an empty list.
   def __init__(self, initial_capacity=10):
      # initialize the hash table with empty bucket list entries.
      self.table = []
      for i in range(initial_capacity):
         self.table.append([])

   # Inserts a new item into the hash table.
   def insert(self, item):
      # get the bucket list where this item will go.
      bucket = hash(item) % len(self.table)
      bucket_list = self.table[bucket]

      # insert the item to the end of the bucket list.
      bucket_list.append(item)
      
   # Searches for an item with matching key in the hash table.
   # Returns the item if found, or None if not found.
   def search(self, key):
      # get the bucket list where this key would be.
      bucket = hash(key) % len(self.table)
      bucket_list = self.table[bucket]

      # search for the key in the bucket list
      if key in bucket_list:
         # find the item's index and return the item that is in the bucket list.
         item_index = bucket_list.index(key)
         return bucket_list[item_index]
      else:
         # the key is not found.
         return None

   # Removes an item with matching key from the hash table.
   def remove(self, key):
      # get the bucket list where this item will be removed from.
      bucket = hash(key) % len(self.table)
      bucket_list = self.table[bucket]

      # remove the item from the bucket list if it is present.
      if key in bucket_list:
         bucket_list.remove(key)

# class to represent an empty bucket
class EmptyBucket:
   pass

# HashTable class definition using linear probing
class LinearProbingHashTable:

   # Constructor with optional initial capacity. All buckets are
   # assigned with an  EmptyBucket() instance called self.EMPTY_SINCE_START.
   def __init__(self, initial_capacity=10):

      # Special constants to be used as the two types of empty buckets.
      self.EMPTY_SINCE_START = EmptyBucket()
      self.EMPTY_AFTER_REMOVAL = EmptyBucket()

      # Initialize all the table buckets to be EMPTY_SINCE_START.
      self.table = [self.EMPTY_SINCE_START] * initial_capacity

   def insert(self, item):
      bucket = hash(item) % len(self.table)
      buckets_probed = 0
      while buckets_probed < len(self.table):
         # if the bucket is empty, the item can be inserted at that index.
         if type(self.table[bucket]) is EmptyBucket:
            self.table[bucket] = item
            return True
      
         # the bucket was occupied, continue probing to next index in table.
         bucket = (bucket + 1) % len(self.table)
         buckets_probed = buckets_probed + 1

      # the entire table was full and the key could not be inserted.
      return False
   
   # Removes an item with a matching key from the hash table.
   def remove(self, key):
      bucket = hash(key) % len(self.table)
      buckets_probed = 0
      while self.table[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.table):
         if self.table[bucket] == key:
            self.table[bucket] = self.EMPTY_AFTER_REMOVAL
      
         # the bucket was occupied (now or previously), so continue probing.
         bucket = (bucket + 1) % len(self.table)
         buckets_probed = buckets_probed + 1

   # Searches for an item with a matching key in the hash table. Returns the
   # item if found, or None if not found.
   def search(self, key):
      bucket = hash(key) % len(self.table)
      buckets_probed = 0
      while self.table[bucket] is not self.EMPTY_SINCE_START and buckets_probed < len(self.table):
         if self.table[bucket] == key:
            return self.table[bucket]
      
         # the bucket was occupied (now or previously), so continue probing.
         bucket = (bucket + 1) % len(self.table)
         buckets_probed = buckets_probed + 1

      # the entire table was probed or an empty cell was found.
      return None

# class to represent an empty bucket
class EmptyBucket:
   pass

# HashTable class definition using double hashing.
class DoubleHashingHashTable:

   # Constructor with optional initial capacity. The capacity should always be
   # set to a prime number.
   def __init__(self, initial_capacity=11):

      # Special constants to be used as the two types of empty cells.
      self.EMPTY_SINCE_START = EmptyBucket()
      self.EMPTY_AFTER_REMOVAL = EmptyBucket()

      # Initialize all the table cells to be EMPTY_SINCE_START.
      self.table = [self.EMPTY_SINCE_START] * initial_capacity

   # The secondary hash function. Many different functions can
   # be used here. The function used here is a common one, with
   # different (usually prime number) constants used where the 7 is.
   def h2(self, item):
      return 7 - hash(item) % 7

   # Inserts a new item into the hash table.
   def insert(self, item):
      for i in range(len(self.table)):
         # calculate bucket index for the item for this value of i.
         # hash() is used as the h1 hashing function.
         bucket = (hash(item) + self.h2(item) * i) % len(self.table)
         if type(self.table[bucket]) is EmptyBucket:
               self.table[bucket] = item
               return True

      # the entire table was full and the key could not be inserted.
      return False
      
   # Searches for an item with a matching key in the hash table.
   # Returns the item if found, or None if not found.
   def search(self, key):
      for i in range(len(self.table)):
         # calculate bucket index for the item for this value of i.
         # hash() is used as the h1 hashing function.
         bucket = (hash(key) + self.h2(key) * i) % len(self.table)
         if self.table[bucket] == key:
               return self.table[bucket]

      # the entire table was full and the key was not found
      return None

   # Removes an item with a matching key from the hash table,
   # if found.
   def remove(self, key):
      for i in range(len(self.table)):
         # calculate bucket index for the item for this value of i.
         # hash() is used as the h1 hashing function.
         bucket = (hash(key) + self.h2(key) * i) % len(self.table)
         if self.table[bucket] == key:
               self.table[bucket] = self.EMPTY_AFTER_REMOVAL