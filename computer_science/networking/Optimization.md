# Optimization

Network optimization has two main goals:

1. Provide redundant services or devices so that network access can continue in the event that one or more components fails. 
- Redundancy to provide access is often called fault tolerance.
- High availability is when a network or a service is up and accessible most of the time.
- Uptime is the percent of time the network or service is up and accessible.

2. Improve the response and performance of network services or devices.

## Optimization Solutions

1. NIC Teaming - NIC Teaming (also called Ethernet bonding) logically groups two or more physical connections to the same network. Data is divided and sent on multiple interfaces, effectively increasing the speed at which the device can send and receive on the network.
- On an Ethernet network, a device must have multiple NICs connected to different switch ports.
- The host operating system must be configured to bond the network adapters into a single entity.
- The switch ports must be bonded together to recognize both ports as a valid destination for the same device.

Bonding primarily provides increased performance, although some fault tolerance is provided if one NIC goes down. Similar solutions allow you to bond multiple dial-up connections or ISDN channels together.

2. Spanning Tree - spanning tree is a protocol on a switch that allows the switch to maintain multiple paths between switches within a subnet. The spanning tree protocol (STP) runs on each switch and is used to select a single path between any two switches.
- Without STP, switches that are connected together with multiple links would form a switching loop.
- Spanning tree provides only a single active path between switches. Switch ports that are part of that path are placed in a forwarding state.
- Switch ports that are part of redundant but unused paths are placed in a blocking (non-forwarding) state.
- When an active path goes down, STP automatically recovers and activates the necessary backup ports to provide continued connection between devices.

Spanning tree provides fault tolerance in case a switch port or network segment is broken, but it does not provide increased performance (only one path is active at a time).

3. Load Balancing - load balancing configures a group of servers in a logical group (called a server farm). Incoming requests to the group are distributed to individual members within the group. Incoming requests can be distributed evenly or unevenly between group members based on additional criteria, such as server capacity.
The primary goal of load balancing is to improve performance by configuring multiple devices to respond as one. Load balancing also provides fault tolerance if the load balancing mechanism is able to detect when a specific farm member is unavailable, automatically distributing new requests to the available members.

4. Caching Engine - caching is the process of saving previously acquired data for quick retrieval at a later time. Caching stores data in memory or on disk within a network device, where it can quickly be retrieved when needed. Recalling the data from the cache is faster than requesting the data from the original location.
A common application of a caching engine on a network is a proxy server configured to cache web content. The proxy server is placed close to the users, typically within the same local area network. As users visit websites, content is retrieved from the web servers on the internet and is cached on the proxy server. Subsequent requests for the same website are sent by the proxy server from cache, rather than retrieved from the internet.
Caching engines are primarily implemented to improve performance, but they offer some degree of fault tolerance. Cached content can be accessed even if the source device is offline.
Caching can lead to out of date content if something changes on the source but is not refreshed in cache.

5. Quality of Service (QoS) - QoS refers to a set of mechanisms that try to guarantee timely delivery or minimal delay of important or time-sensitive communications. QoS is particular important when implementing Voice over IP (VoIP), Video over IP, online gaming, or unified communications where delay or data loss make the overall experience unacceptable.
- In addition to delay, QoS mechanisms seek to limit the effects of packets arriving out of order, corrupt packets, and lost or dropped packets.
- Giving higher priority to some traffic means that less important traffic might be delayed. It is assumed that while the delay might make the end user wait, the delay would not make the resulting data unusable.
- QoS might include a guaranteed level of service, which is usually outlined in a service level agreement.
- - Constant or reserved means that a certain level of service is guaranteed to always be available. This level is only possible by reserving service, even when no data is being sent.
- - Variable service guarantees a certain capacity, but service might vary depending on conditions. This level of service is sufficient for voice or video.
- - Available guarantees a minimum level of service. Additional capacity can be used if it is available, but only the minimum is guaranteed.
- - Unspecified service provides whatever service is available with little to no guarantee. This level of service should only be used for data that can tolerate long delays.

QoS prioritizes traffic from different data streams by using one of the following two classification systems:
- Class of Service (COS)
- - Individual frames are marked and classified at Layer 2.
- - A priority value between 0 and 7 is assigned to the 3-bit COS field.
- - Each priority value specifies a specific traffic type.
- - - 0 – Background
- - - 1 – Best effort
- - - 2 – Excellent effort
- - - 3 – Critical applications
- - - 4 – Video (< 100ms latency)
- - - 5 – Voice (< 10ms latency)
- - - 6 – Internetwork control
- - - 7 – Network control (highest)
- Differentiated Services Code Point (DSCP)
- - Classification occurs at Layer 3.
- - Precedence values are inserted in the DiffServ field of an IP packet.
- - Up to 64 different classifications are possible, but most networks use only the following classes:
- - - Default – Best effort
- - - Expedited Forwarding (EF) – Low loss, low latency
- - - Assured Forwarding (AF) – Assured delivery under prescribed conditions
- - - Class Selector – Maintains backward compatibility with IP Precedence field

6. Traffic Shaper - a traffic shaper (also called a bandwidth shaper or packet shaper) is a device that is capable of modifying the flow of data through a network in response to network traffic conditions. Specific applications for a traffic shaper include the following:
- A device used with QoS ensures timely delivery of time-sensitive data streams.
- Bandwidth throttling to restrict the amount of data sent within a specific time period (for example, limiting the amount of data that can be downloaded from a website in an hour).
- Rate limiting to restrict the maximum bandwidth available to a customer (used by an ISP or a WAN provider).

7. Multilayer Switch or Content Switch - normal switching occurs at the OSI model layer 2 and uses the MAC address to perform frame forwarding. Switches use specialized hardware called an application-specific integrated circuit (ASIC), which performs switching functions in hardware rather than using the CPU and software. ASIC allows switches to perform the switching function at wire speed, meaning that frames are switched without the delay that would be introduced if the CPU and software were required to process the frame.
A multilayer switch operates at other OSI model layers and can use other information within a packet to make forwarding decisions. For example, a layer 3 switch uses the IP address for making forwarding decisions.

Layer 4–7 switches (also called content switches, web switches, or application switches) are typically used for load balancing.
- The switch distributes packets between multiple servers.
- Some switches can transform packets at wire speed (perhaps by performing NAT or adding/removing encryption with SSL or digital certificates).

8. Demilitarized Zone (DMZ) - a demilitarized zone (DMZ) is a subnetwork that you place between your LAN and untrusted networks, such as the internet. External network nodes can only access what you choose to expose in the DMZ, and the rest of your network is protected by firewalls. Your most vulnerable services are ones that also serve users outside of your local area network, like email, web, and DNS servers, so these are often placed in the DMZ. Communications between hosts in the DMZ and other hosts is extremely restricted to help maintain security. These barriers make external attacks much more difficult to execute. This is especially important if you use virtual LANs, or VLANs, because you have so many devices logically connected so that they affect one another.

9. Port Aggregation (PAgP)	Port aggregation (PAgP) is a Cisco protocol that lets you combine Ethernet ports to improve the speed of aggregated, or related, file transfers. This protocol is also called link aggregation, teaming ports, and pot trunking.

10. Differentiated Services (Diffserv)	Diffserv is a Layer 3 Protocol QoS uses to classify IP packets. Each IP packet header has a DiffServ field. DiffServ inserts a differentiated services code point value, or DSCP value, in this filed to prioritize data flow. Routers forward packets according to the value in this field.

11. Collision and Broadcast Domains	A collision domain identifies all of the devices that share the same network segment and have the potential of sending colliding signals. A broadcast domain identifies all the devices that will see a broadcast frame that is sent on the network. The two work together to minimize collisions.

12. Common Address Redundancy Protocol (CARP)	CARP is an implementation of fault tolerance that allows multiple firewalls and/or routers on the same local network to share a set of IP addresses. If one of the firewalls or routers fails, the shared IP address allows hosts to continue communicating with the firewall or router without interruption.
