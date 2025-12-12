# Troubleshooting

Good troubleshooting is a process that combines knowledge, experience, and intuition. 

## Troubleshooting Approach

Regardless of your current troubleshooting abilities, you will benefit from following a systematic approach to problem solving. The following process is effective in a variety of situations:

1. Gather information in order to identify the problem.
- Ask the user to describe the symptoms of the problem.
- Check for error messages.
- If possible, reproduce the problem.
  
At this point, it's important to resist the urge to fix the problem.

2. Identify the affected area and determine the size of the problem. Fixes for one client workstation are likely very different from fixes for an entire network segment.

3. Determine if anything has changed in the environment. Most often, problems are caused by new hardware, software, or configuration changes. If necessary, ask questions to discover what changes might have caused the problem.

4. Establish a theory of potential causes. As you do this, consider multiple approaches:
- Analyze the problem by using the OSI model and how data flows through it from both top to bottom and bottom to top.
- Use the divide and conquer technique to isolate the problem to a specific domain. For example, if other workstations can ping a router, then the problem might be limited to a single workstation.
  
5. Review the list of potential causes and select the most probable cause. Look for common errors and try quick solutions.

6. Escalate the problem if it is beyond your ability to fix or the scope of your management. For example, the problem might be a configuration error on a router that you are not authorized to access. When forwarding the problem on to someone else, be sure to describe the nature of the problem, the actions you have already taken, and the symptoms that lead you to believe the problem is outside your area of responsibility.

7. Create an action plan and account for possible side effects. Your plan might include purchases of hardware or equipment that need approval, or it might involve taking some services offline for a period of time. Identifying the effects ahead of time helps eliminate or reduce any potential negative consequences.

8. After side effects are weighed and all concerns are addressed, fix the problem. If necessary, implement additional steps to correct the problem if your first solution does not work. After you think you have resolved the problem, test the result.

9. Identify the results and effects of the solution. Make sure that the solution has fully fixed the problem and has not caused any additional problems.

10. Document the solution and process. In the future, you can check your documentation to see what has changed and remember solutions to common problems.

Remember, troubleshooting is a process of both deduction and induction. With enough experience, you will be able to identify when deviating from this process can save both time and effort.1

## Troubleshooting Commands

| Task | Tool (OS) | Description |
| ---- | --------- | ----------- |
| View the ARP table | arp (Windows) | Shows MAC-address-to-IP-address mappings, including the local MAC and IP addresses. |
| View IP Configuration Information | ipconfig (Windows 2000 and later) / ifconfig (Linux) | Displays IP configuration information for network adapters: IP address and mask; Default gateway; DNS servers; WINS servers; DHCP server used for configuration; MAC address. |
| View IP and Routing Statistics | netstat (Windows) | Shows IP-related statistics: Current connections; Incoming and outgoing connections; Active sessions, ports, and sockets; The local routing table. |
| View NetBIOS Over TCP/IP Information | nbtstat (Windows) | Displays the NetBIOS name tables for both the local computer and remote computers, as well as the NetBIOS name cache. |
| Test Host-to-Host Connectivity | ping (Windows and Linux IPv4) / ping -6 (Windows IPv6) / ping6 (Linux IPv6) | Sends an ICMP echo request/reply packet to a remote host. A response from the remote host indicates that both hosts are correctly configured and a connection exists between them. Using the -t switch with ping can be useful in determining whether the network is congested, which could cause sporadic failures in the ping stream. Many firewalls block ICMP messages. For ping to be successful, the firewall must allow ICMP messages. Most devices and firewalls allow you to select the specific ICMP messages that are allowed. |
| Identify the Path Between Two Hosts | tracert (Windows IPv4) / tracert -6 (Windows IPv6) / traceroute (Linux IPv4) / traceroute6 (Linux IPv6) / traceroute -6 (Linux IPv6) / mtr (Linux) | Like ping, traceroute uses ICMP packets to test connectivity between devices, but it also shows the path between the two devices. Responses from each hop on the route are measured three times to provide an accurate representation of how long the packet takes to reach and then return back from the destination device. The mtr command on Linux is a combination of the ping and traceroute commands. |
| Identify Latency in a Path | pathping (Windows) | Combines traceroute with ping to identify any latency that may exist in the path between the sender and receiver. Pathping performs a traceroute to the destination host, then uses the output to ping each router in the path 100 times. |
| Test Host-to-Host Connectivity Using ARP | arping (Linux) | Sends an ARP request to the specified IP address. The arping command works much like ping in that the host with the specified IP address will respond. Be aware of the following: arping works only on the local subnet (not through routers); arping often works even if the destination host is blocking ICMP messages. |
| Test Name Resolution | nslookup (Windows and Linux) / dig (Linux) / host (Linux) | Resolves (looks up) the IP address of a host name and displays information about the lookup, such as the DNS server used for the lookup request. dig is the preferred tool for testing name resolution on Linux hosts. |
| View and Modify the Routing Table | route | Displays the contents of the routing table. Can also be used to add or remove static routes. |

Occasionally, you may need to perform a ping or traceroute from outside your network. You can do this with a Looking Glass site. A Looking Glass site is a portal used to access a specialized server called a Looking Glass (LG) server. An LG server allows you to run ping and traceroute commands remotely. LG servers are typically provided by ISPs for the purpose of viewing routing information.
