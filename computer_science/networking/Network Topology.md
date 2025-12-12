# Network Topology

Topology is the term used to describe how devices are connected and how messages flow from device to device. There are two types of network topologies:
 - the physical topology describes the way the network is wired.
 - the logical topology describes the way messages are sent.

## Bus Topology

A bus topology consists of a trunk cable with nodes either inserted directly into the trunk or tapped into the trunk using offshoot cables called drop cables. When using a bus topology:
 - signals travel from one node to all other nodes.
 - a device called a terminator is placed at both ends of the trunk cable.
 - terminators absorb signals and prevent them from reflecting repeatedly back and forth on the cable.
 - it can be difficult to isolate cabling problems.

A broken cable anywhere on the bus breaks the termination and prevents communications between any devices on the network.

## Ring Topology

A ring topology connects neighboring nodes until they form a ring. Signals travel in one direction around the ring; each device on the network acts as a repeater to send the signal to the next device. With a ring:
- installation requires careful planning to create a continuous ring.
- isolating problems can require going to several physical locations along the ring.
- a malfunctioning node or cable break can prevent signals from reaching nodes further along on the ring.

## Star Topology

A star topology uses a hub or switch to connect all network connections to a single physical location. Today it is the most popular type of topology for a LAN. With a star:
 - all network connections are located in a single place, which makes it easy to troubleshoot and reconfigure.
 - nodes can be added to or removed from the network easily.
 - cabling problems usually affect only one node.

## Mesh Topology

A mesh topology exists when there are multiple paths between any two nodes on a network. Mesh topologies are created using point-to-point connections. This increases the network's fault tolerance because alternate paths can be used when one path fails. Two variations of mesh topologies exist:
- partial mesh — some redundant paths exist.
- full mesh — every node has a point-to-point connection with every other node.

Full mesh topologies are usually impractical in a standard LAN because the number of connections increases dramatically with every new node added to the network. A separate network interface and cable for each host on the network is required. However, a full mesh topology is commonly used to interconnect routers, providing alternate paths should one path go down or become overloaded. Mesh networks are also commonly used to create redundant paths between access points in a wireless network, providing alternate paths back to the wireless controller should one access point go down or become overloaded. With this topology, every access point can communicate directly with any other access point on the wireless network.


## Identifying physical topology by logical topology

You should be able to identify the physical topology by looking at the way in which devices are connected. However, it is not as easy to identify the logical topology. As the following table shows, there is often more than one way for messages to travel in a given physical topology.

| Logical Topology | Physical Topology | Description |
---|---|---|
| Bus | Bus/Star | Messages are sent to all devices connected to the bus.|
| Ring | Ring/Star | Messages are sent from device to device in a predetermined order until they reach the destination device. |
| Star | Star | Messages are sent directly to (and only to) the destination device. |
| Mesh | Mesh | Messages are sent from one device to the next until they reach the destination device. |
