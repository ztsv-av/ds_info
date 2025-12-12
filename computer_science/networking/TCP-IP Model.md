# TCP/IP Model

TCP/IP (Transmission Control Protocol/Internet Protocol) or Internet Protocol Suite - TCP/IP is the most commonly used protocol suite. It controls transmissions between computers on a network (including the internet).

The TCP/IP model incorporates the general concepts and structure of the OSI model.

| Layer | Description |
| ----- | ----------- |
| Application | The Application layer corresponds to the Session, Presentation, and Application layers of the OSI model. Protocols associated with the Application layer include FTP, HTTP, Telnet, SMTP, DNS, and SNMP. |
| Host-to-Host | The Host-to-Host layer is comparable to the Transport layer of the OSI model. It is responsible for error checking and reliable packet delivery. Here, the data stream is broken into segments that must be assigned sequence numbers so they can be reassembled correctly on the remote side after they are transported. Protocols associated with the Host-to-Host layer include Transport Control Protocol (TCP) and User Datagram Protocol (UDP). |
| Internet | The Internet layer is comparable to the Network layer of the OSI model. It is responsible for moving packets through a network. This involves addressing hosts and making routing decisions to identify how the packet traverses the network. Protocols associated with the Internet layer include Address Resolution Protocol (ARP), Internet Control Message Protocol (ICMP), and the Internet Group Management Protocol (IGMP). |
| Network Access | The Network Access layer corresponds to the Physical and Data Link layers of the OSI model. It is responsible for describing the physical layout of the network and formatting messages on the transmission medium. |

The TCP/IP model focuses specifically on the functions in the Internet layer and Host-to-Host layers. All other functions of the traditional OSI model are encompassed in the first and fourth layers.
