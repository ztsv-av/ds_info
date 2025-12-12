# OSI Model

OSI (Open Systems Interconnection ) Model - OSI model is a standardized method of implementing network communications. OSI model divides network communication between two devices - sender and receiver - into layers. These layers divide communication process into general tasks. There are 7 different layers: application, presentation, session, transport, network, data link, physical. When a sender sends a message to a receiver, that message goes through the 7 layers of the OSI model, from the application to the physical. Each layer preprocesses that message according to the layers' specification and then forwards it to the next layer. Next, preprocessed information is transmitted to the receiving device. When information arrives at the receiver, the same process is used, but in reverse.

## OSI Model Benefits

The OSI model:

- Provides a common language and reference point for network professionals
- Divides networking tasks into logical layers for easier comprehension
- Allows specialization of features at different levels
- Aids in troubleshooting
- Promotes standards of interoperability between networks and devices
- Provides modularity in networking features (developers can change features without changing the entire approach)

## OSI Model Limitations

However, there are limitations of the OSI model:

- OSI layers are theoretical and do not actually perform real functions.
Industry implementations rarely have a layer-to-layer correspondence with the - OSI layers.
- Different protocols are used within the OSI model to perform the different functions required to help send or receive the overall message. This can sometimes complicate the overall process.
- A particular protocol implementation may not represent every OSI layer (or may spread across multiple layers).

## OSI Layers

![image](https://user-images.githubusercontent.com/73081144/147326836-73452ecf-7c40-4af8-a100-215f86cfbe17.png)

| Layer | Description and Keywords |
| ----- | ------------------------ |
| Application (Layer 7) | The Application layer integrates network functionality into the host operating system and enables communication between network clients and services. The Application layer does not include specific applications that provide services, but rather provides the capability for services to operate on the network. Most Application layer protocols operate at multiple layers down to the Session and even Transport layers. However, these protocols are classified as Application layer protocols because they start at the Application layer (the Application layer is the highest layer where they operate). Services typically associated with the Application layer include: HTTP, Telnet, FTP, TFTP, SNMP. |
| Presentation (Layer 6) | The Presentation layer formats, or presents, data in a compatible form for receipt by the Application layer or the destination system. Specifically, the Presentation layer ensures: Formatting and translation of data between systems; negotiation of data transfer syntax between systems by converting character sets to the correct format; encapsulation of data into message envelopes by encryption and compression; restoration of data by decryption and decompression. |
| Session (Layer 5) | The Session layer manages the sessions in which data are transferred. Session layer functions include: management of multiple sessions (each client connection is called a session). A server can concurrently maintain thousands of sessions; assignment of a session ID number to each session to keep data streams separate; the setup, maintenance, and teardown of communication sessions. |
| Transport (Layer 4) | The Transport layer provides a transition between the upper and lower layers of the OSI model, making the upper and lower layers transparent from each other. Transport layer functions include: end-to-end flow control; port and socket numbers; segmentation, sequencing, and combination; connection services, either reliable (connection-oriented) or unreliable (connectionless) delivery of data. At the Transport layer, data segments are called segments. |
| Network (Layer 3) | The Network layer describes how data is routed across networks and on to the destination. Network layer functions include: identifying hosts and networks by using logical addresses; maintaining a list of known networks and neighboring routers; determining the next network point where data should be sent. Routers use a routing protocol that takes various factors into account, such as the number of hops in the path, link speed, and link reliability, to select the optimal path for data. At the Network layer, data segments are called packets. |
| Data Link (Layer 2) - Logical Link Control (LLC) and Media Access Control (MAC) | The Data Link layer defines the rules and procedures for hosts as they access the Physical layer. These rules and procedures define: how physical network devices are identified on the network by defining a unique hardware address (physical or MAC address); how and when devices have access to the LAN and can transmit on the network medium (media access control and logical topology); how to verify that the data received from the Physical layer is error free (parity and CRC); how devices control the rate of data transmission between hosts (flow control). At the Data Link layer, data segments are called frames. Switches, bridges and NICs, and WAPs function in Layer 2. |
| Physical (Layer 1) | The Physical layer of the OSI model sets standards for sending and receiving electrical signals between devices. Protocols at the Physical layer identify: how digital data (bits) are converted to electric pulses, radio waves, or pulses of light and moved across network cables; specifications for cables and connectors; the physical topology. At the Physical layer, data segments are called bits. NICs, repeaters, hubs, WAPs, and modems function in Layer 1. |

![image](https://user-images.githubusercontent.com/73081144/147327233-ee6183dd-f296-4a1f-95cf-76d1710835e7.png)

## Common OSI model layer division 

1. One way to group the OSI model layers is to separate bottom two layers (data link and physical) from the other five. This is done because the bottom layers of the OSI model relate to the network physical hardware, whereas top five layers are the networking protocols, such as TCP/IP, and they are concerned with software and the applications on the computer. 
2. Another common way is to divide 7 layers into 3 groups: 1-2, 3-4, 5-6-7. Top 3 layers handle service protocols. Middle layers handle how messages get from one device to another through the network (not concerned with the hardware). Bottom 2 layers still relate to the network physical hardware.
