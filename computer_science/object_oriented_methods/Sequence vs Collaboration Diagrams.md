# Sequence vs Collaboration Diagrams

Collaboration diagrams and sequence diagrams give the same information but display it differently. These diagrams are so similar that some modeling tools can convert from one diagram type to the other. All collaboration diagrams show objects and messages and the links between them. Objects are the things that participate in the activity, and they provide the information needed to the methods that they call. Messages represent the initiation of an operation on an object. Objects can have one or more messages associated with them. The connections between objects are referred to as links. This is how collaboration diagrams are different from sequence diagrams; they visually represent the relationships between objects, whereas in sequence diagrams the messages are represented. Collaboration diagrams are not as good as sequence diagrams when trying to show the series of events, but they do a better job representing the complexities of branching.

When looking at sequence and collaboration diagrams, it is common to look at both diagrams at a particular point and time in the system. This static lens does not lend itself well to seeing the changes that go on in a dynamic system. When modeling these systems, it is important to not lose sight of the significance of the interactions within the system. Both sequence and collaboration diagrams do an excellent job representing dynamic systems. The sequence of steps, objects in the process, and the messages that are exchanged, are best represented in a sequence diagram. The collaboration diagram includes similar information but places more emphasis on the relationship between objects. This diagram highlights the objects in a system and their relationships.

## Sequence vs Collaboration Example

The sequence diagram below models a very simple home environment control system. It consists of a means for a user to set the desired temperature and to see the current and desired temperature. Once the system is set, the MainController object calls itself indefinitely, constantly checking the current versus desired temperature and controlling the furnace and air conditioner to compensate for any differences.

![image](https://user-images.githubusercontent.com/73081144/178642237-08af31f6-8def-4ff2-b7d2-e7eac5fec89b.png)

The collaboration diagram below models the same home environment control system as the sequence diagram. It is easy to identify the differences between the two types of diagrams. It is easy to see the sequential flow of messages with the sequence diagram whereas the collaboration diagram makes it easy to see the overall structure and relationships among the objects.

![image](https://user-images.githubusercontent.com/73081144/178642286-cbb6242c-059c-4a42-befb-4ff03e5f8c7c.png)
