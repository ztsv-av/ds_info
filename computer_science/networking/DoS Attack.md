# DoS Attack

Denial of Service (DoS) and Distributed Denial of Service (DDoS) attacks impact system availability by flooding the target system with traffic or requests or by exploiting a system or software flaw. The goal of a DoS attack is to make a service or device unavailable to respond to legitimate requests. Attackers may choose to overload the CPU, disk subsystem, memory, or network (most common).

## Types of DoS Attacks.

1. In a DoS attack, a single attacker directs an attack against a single target, sending packets directly to the target.

2. In a Distributed DoS (DDoS) attack, multiple PCs attack a victim simultaneously. A series of computers scan target computers to find weaknesses and then compromise the most vulnerable systems. In a DDoS attack:
- The attacker identifies one of the computers as the master (also known as zombie master or bot herder).
- The master uses zombies/bots (compromised machines) to attack.
- The master directs the zombies to attack the same target.

3. A Distributed Reflective Denial of Service (DrDoS) uses an amplification network to increase the severity of the attack. Packets are sent to the amplification network addressed as coming from the target. The amplification network responds back to the target system.

4. A friendly or unintentional DoS attack is when a website experiences such heavy traffic that users can no longer access the website. This is done when many people flood to the website and cause the server to crash.

5. A Permanent denial-of-service (PDoS) is an attack that damages a system so badly that it requires the replacement or re-installation of hardware. Unlike the distributed denial-of-service attack, a PDoS attack exploits security flaws which allow remote administration on the management interfaces of the victim's hardware, like routers, printers, or other networking hardware. The attacker uses these vulnerabilities to replace a device's firmware with a modified, corrupt, or defective firmware image.

6. Protocol and packet abuse is any method that takes advantage of the way protocols and packets work.
- Packet abuse includes modifying packets to not follow standards, using those packets to cause an abnormal reaction on a server when it receives the packets which results in the server releasing information that it should not have released.
- Protocol abuse includes using old protocols to attack a network or encapsulating a protocol within another protocol to bypass firewall restrictions.
- These manipulated protocols and packets can cause a DoS attack on a system, because the system doesn't know how to deal with them.

## DoS Attacks that use ICMP Protocol

1. Ping Flood - a ping flood is a simple DoS attack where the attacker overwhelms the victim with ICMP Echo Request (ping) packets. In a ping flood:
- The attack succeeds only if the attacker has more bandwidth than the victim.
- The attacker hopes that the victim will respond with ICMP Echo Reply packets, thus consuming outgoing bandwidth as well as incoming bandwidth.

2. Ping of Death - the ping of death (also called a long ICMP attack) is a DoS attack that uses the ping utility to send oversized ICMP packets. In the ping of death:
- The attacker sends one very large ICMP packet (larger than 65,536 bytes) directly to the victim.
- The size of the packet causes the system to freeze, crash, or reboot.

3. Smurf - a Smurf attack is a form of DrDoS attack that spoofs the source address in ICMP packets. A Smurf attack requires an attacker system, an amplification network, and a victim computer or network.
- The attacker sends ICMP packets to an amplification network or broadcast address. The packets spoof the source address to be that of the target.
- The amplification network responds by sending packets to the target (victim) site.
- The victim has thousands of replies to packets sent by the attacker.
- Many personal firewalls block all ICMP protocol messages in response to these attacks. The most effective protection measure the victim of a Smurf attack can perform during an attack is to communicate with upstream providers. A simple phone call to request filtering on your behalf can weaken the effectiveness of a Smurf attack.

## DoS Attacks That Use the TCP Protocol

1. SYN Flood - the SYN flood exploits the TCP three-way handshake as follows:
- The attacker floods a victim site with SYN packets.
- The victim responds to each SYN packet with a SYN ACK packet.
- The attacker does not respond with the last portion of the handshake (an ACK packet), leaving the victim waiting for a response.
- The attacker continues to send the victim SYN frames with a spoofed address.
- The victim continues to attempt sessions with the attacker, allocating resources to accommodate each of these inbound session requests.
So many resources are allocated that the victim cannot process a legitimate inbound request for a TCP/IP session.

A variation of the SYN flood attack is a half-open scan attack in which the attackers sends SYN packets designed for certain ports. This is a form of port scanning also known as half-open scanning. The attacker doesn't send enough packets to cause a denial of service, but is able to determine the victim's open ports.

2. LAND - a LAND attack is when an attacker floods the victim's system with packets that have forged headers. In a LAND attack:
- The packets have the same source and destination address (the victim's). The packets also have the same source and destination port.
- The victim's system has no procedure to deal with these packets.
- The victim's system holds the packets in RAM.
- As the victim's system continues to hold more and more packets in RAM, it is unable to process legitimate requests.

3. Christmas (Xmas) Tree - a Christmas (Xmas) tree attack (also known as Christmas tree scan, nastygram, kamikaze, or lamp test segment) uses an IP packet with every option turned on for the protocol being used. Christmas tree packets can be used to conduct reconnaissance by scanning for open ports and a DoS attack if sent in large numbers.
- When sent to a target host, the TCP header of a Christmas tree packet has the flags FIN, URG and PSH set. By default, closed ports on the host are required to reply with a TCP connection rest flag (RST). Open ports must ignore the packets, informing the attacker of which ports are open.
- Christmas tree packets require much more processing by network devices compared to typical packets. A DoS attack occurs if a large number of these packets are sent to the target host.
- Because Xmas tree scan packets do not have the SYN flag turned on, they can pass through firewalls and reach the target host.

## DoS Attacks that use the UDP Protocol

1. Fraggle - a Fraggle attack sends a large amount of UDP packets directed to broadcast addresses aimed at port 7 (echo) and port 19 (chargen--character generation) with spoofed source addresses. Fraggle is a variation of the Smurf attack, using UDP instead of ICMP to perpetrate an attack when firewall filters block ICMP messages.

2. NTP-Based - the NTP protocol is prone to amplification attacks, because NTP
- Will reply to a packet with a spoofed source IP address, and
- Has at least one built-in command that will send a long reply to a short request.

NTP contains a command called monlist (or sometimes MON_GETLIST) which can be sent to an NTP server for monitoring purposes. It returns the addresses of up to the last 600 machines that the NTP server has interacted with. This response is bigger than the request sent making it ideal for an amplification attack. An attacker, armed with a list of open NTP servers on the internet, can easily pull off a DDoS attack using NTP.

3. Teardrop - the Teardrop attack manipulates the UDP fragment number and location. In the Teardrop attack:
- Fragmented UDP packets with overlapping offsets are sent.
- When the victim system rebuilds the packets, an invalid UDP packet is created, causing the system to crash or reboot.

## DoS and DDoS Attack Countermeasures

Countermeasures for DoS and DDoS attacks include implementing:

- Intrusion Detection Systems (IDS) or Intrusion Protection Systems (IPS).
- Strong anti-virus and anti-spyware software on all systems with internet connectivity.
- File and folder hashes on system files and folders to identify if they have been compromised.
- Reverse DNS lookup to verify the source address.
- External firewalls with the following filters:
- - Ingress filters that specify any inbound frame must have a public IP address from outside of the organization's LAN.
- - Egress filters that specify any outbound frame must have a private IP address within the organization's LAN.
- - Address filters to prevent traffic from specific attackers (if known).
- Filters to block unwanted traffic when a DoS attack begins. This will help to minimize the effects of the DoS attack. You can also contact your ISP to implement filtering closer to the source and reduce the bandwidth used by the attack.
- System patches and updates to remove flaws that are often exploited by DoS attacks.
