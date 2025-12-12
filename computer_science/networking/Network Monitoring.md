# Network Monitoring

Monitoring's goal is to track network conditions, identify situations that might signal potential problems, pinpoint the sources of problems, and locate areas of your network that might need to be upgraded or modified. As you monitor your network, look for your top talkers and listeners. Top talkers are the computers that send the most data, either from your network or into your network. Top listeners are the hosts that receive most of the data, streaming or downloading large amounts of data from the internet. These computers can create heavy traffic and lower performance.

## Monitoring Tools

1. Logs - a log is a record of events that have occurred on a system. Logging capabilities are built into operating systems, services, and applications. Log entries are generated in response to changes in configuration, system state, or network conditions.
- By default, some logging is enabled and performed automatically. To gather additional information, you can usually enable more extensive logging.
- Many systems have different logs for different purposes, such as a system log for operating system entries, a security log for security related entries, and an application log (also called a performance log) for events related to specific services and processes, such as connections from a web server.
- Logging requires system resources (processor, memory, and disk). You should only enable additional logging based on information you want to gather, and you should disable logging after you obtain the information you need.
- Logs must be analyzed to be useful; only by looking at the logs will you be able to discover problems. Depending on the log type, additional tools might be available to analyze logs for patterns.
- syslog is a standard for managing and sending log messages from one computer system to another. syslog can analyze messages and notify administrators about problems and performance.

2. Load Tester - a load tester is a tool that simulates a load on a server or service. For example, the load tester might simulate a large number of client connections to a website, test file downloads for an FTP site, or simulate large volumes of email. Use a load tester to make sure that a system has sufficient capacity for expected loads. A load tester can even estimate failure points where the load is more than the system can handle.

3. Throughput Tester - a throughput tester is a device that measures the amount of data that can be transferred through a network or processed by a device (such as the amount of data that can be retrieved from a disk in a specific period of time). On a network, a throughput tester sends a specific amount of data through the network and measures the time it takes to transfer that data, creating a measurement of the actual bandwidth. Use a throughput tester to validate the bandwidth on your network and identify when the bandwidth is significantly below what it should be.

A throughput tester can help you identify when a network is slow, but will not give you sufficient information to identify why it is slow.

4. Packet Sniffer - a packet sniffer is software that captures (records) frames that are transmitted on the network. Use a packet sniffer to:
- Identify the types of traffic on a network.
- View the exchange of packets between communicating devices. For example, you can capture frames related to DNS and view the exact exchange of packets for a specific name resolution request.
- Analyze packets sent to and from a specific device.
- View packet contents.

A packet sniffer is typically run on one device with the intent of capturing frames for all other devices on a subnet. Using a packet sniffer in this way requires the following configuration changes:
- By default, a NIC will only accept frames addressed to itself. To enable the packet sniffer to capture frames sent to other devices, configure the NIC in promiscuous mode. In promiscuous mode, the NIC will process every frame it sees.
- A switch will forward packets only to the switch port that holds a destination device. When your packet sniffer is connected to a switch port, it will not see traffic sent to other switch ports. To configure the switch to send all frames to the packet-sniffing device, configure port mirroring on the switch; all frames sent to all other switch ports will be forwarded on the mirrored port.

If the packet sniffer is connected to a hub, it will already see all frames sent to any device on the hub.

5. Protocol Analyzer - a protocol analyzer is a type of packet sniffer that captures transmitted frames. A protocol analyzer is a passive device that copies frames and allows you to view frame contents but does not allow you to capture, modify, and retransmit frames (activities that are used to perform an attack). Use a protocol analyzer to:
- Check for specific protocols on the network, such as SMTP, DNS, POP3, and ICMP.
- - Find devices that might be using restricted protocols (such as ICMP) or legacy protocols (for example, IPX/SPX or NetBIOS).
- - Analyze traffic that might be sent by attackers.
- Identify frames that might cause errors.
- - Determine which flags are set in a TCP handshake.
- - Detect many malformed or fragmented packets.
- Examine the data contained within a packet.
- - Identify users that are connecting to unauthorized websites.
- - Discover cleartext passwords allowed by protocols or services.
- - Identify unencrypted traffic that includes sensitive data.
- Troubleshoot communication problems or investigate the source of heavy network traffic.

A protocol analyzer shows the traffic that exists on the network and the source and destination of that traffic. It does not tell you if the destination ports on a device are open unless you see traffic originating from that port. For example, seeing traffic addressed to port 80 of a device does not automatically mean the firewall on that device is open or that the device is responding to traffic directed to that port.

When using a protocol analyzer, you can filter the frames so that you see only the frames with information of interest.
- Filters can be configured to show only frames or packets to or from specific addresses, or frames that include specific protocol types.
- A capture filter captures only the frames identified by the filter. Frames not matching the filter criteria will not be captured.
- A display filter shows only the frames that match the filter criteria. Frames not matching the filter criteria are still captured, but are not shown.
- The results of a capture can be saved in order to analyze frames at a later time or on a different device.
