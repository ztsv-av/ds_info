# Intrusion Detection and Prevention

An intrusion detection system (IDS) is a special network device that can detect attacks and suspicious activity.

IDS is a network security system that detects, and in some cases responds to, a cybersecurity attack on the network. There are three ways how IDSs are classified. The first way is how it reacts to an attack (passive IDS and active IDS). Second is how it detects an attack, or its attack recognition method (signature recognision and anomaly recognition). Finally, third way is its detection scope - where it runs on a system and what types of threats it detects.

## Different Ways to Classify Detection Systems

1. Response Capability.

An intrusion detection system is classified by how it responds when a threat is detected.
- A passive IDS monitors, logs, and detects security breaches, but takes no action to stop or prevent the attack. A passive IDS:
- - Can send an alert, but it is the network administrator's job to interpret the degree of the threat and respond accordingly.
- - Might perform shunning dropping undesirable traffic without additional actions, which simply drops offending traffic without additional actions.
- - Cannot be detected on the network because it takes no detectible action.
- An active IDS can automate responses, which may include dynamic policy adjustment and reconfiguration of supporting network devices to block the offending traffic.
- Can terminate sessions by using the TCP-RST command. It can also terminate or restart other processes on the system.
- Performs behaviors that can be seen by anyone watching the network. Usually these actions are necessary to block malicious activities or discover the identity of an intruder. Updating filters and performing reverse lookups are common behaviors of an active IDS.

2. Recognition Method

The recognition method defines how the system distinguishes attacks and threats from normal activity.
- Signature recognition, also referred to as pattern matching or dictionary recognition, looks for patterns in network traffic and compares them to known attack patterns called signatures.
- - IDS signatures are written and updated by the IDS vendor in response to identified vulnerabilities.
- - Signature-based recognition cannot detect unknown attacks; only attacks with published signature files can be identified. For this reason, it is important to update signature files on a regular basis.
- Anomaly recognition, also referred to as behavior recognition and heuristic recognition, monitors traffic to define a standard activity pattern as normal.
- - Clipping levels, or thresholds, are used to identify deviations from the norm.
- - When a threshold is reached, an alert is generated or actions are taken.
- - Anomaly-based systems can recognize and respond to some unknown attacks (attacks that do not have a corresponding signature file).
- - Anomaly recognition usually causes more false positives than signature-based IDS.
- - Anomaly-based recognition systems can be fooled by incremental changes within the clipping level, which cause the changed state to become the normal level of activity, allowing a higher level of irregularity to go unnoticed.

3. Detection Scope

Systems can be classified based on where the system runs and the scope of threats it looks for.
- A host-based IDS (HIDS) is installed on a single host and monitors all traffic coming into the host. An HIDS:
- - Detects attacks that are unique to the services on the system. It can monitor application activity and modifications, as well as local system files, logon audit files, and kernel audit files.
- - Is typically unaware of other devices on the network, but it can be detected and become the target of an attack itself.
- - May rely on the auditing and logging capabilities of the operating system.
- - Can analyze encrypted traffic (because services running on the host decrypt the traffic).
Anti-virus software is the most common form of host-based IDS.
- A network-based IDS (NIDS) is a dedicated device installed on the network. It analyzes all traffic on the network. An NIDS is:
- - Typically implemented as part of a firewall device acting as a router. When an NIDS is implemented as a standalone device, all traffic must be directed to the device using one of the following strategies:
- - - Connect the IDS and other devices using a hub. The IDS will then see all traffic sent to all devices on the subnet.
- - - Connect the IDS to a switch and enable spanning or diagnostic capabilities on the switch port to forward all traffic to that switch port.
- - - Use a tap to connect the IDS directly to the network medium.
- Mostly unaware of individual hosts on the network. It cannot be detected by attacking systems.
- Suited for detecting and blocking port scanning and DoS attacks.
- Unable to analyze encrypted traffic.

## Other Monitoring Techniques

In addition to implementing an IDS or IPS, you can also catch threats to your network by performing regular monitoring with common network tools.

- Use a packet sniffer to examine network traffic. It can look for specific types of traffic that should not be on your network or for traffic types associated with known attacks.
- Use a port scanner to check for open ports on a system or a firewall. Compare the list of opened ports with the list of ports allowed by your network design and security policy.
- - Close all unused ports.
- - Investigate the cause of incorrectly opened ports. Make sure that administrators do not open ports unnecessarily. Verify that the system does not have malware installed that could have opened ports for its own purposes.
- Run security scanning software on each system to detect malware or other security vulnerabilities (such as opened ports, weak passwords, or missing operating system patches).
- Keep operating systems and applications up to date with the latest patches. - Download the most recent signature files to protect against attacks.
- Monitor system logs for unusual activity that could indicate an attempted (or successful) attack. Check firewall logs in order to identify the type of traffic that has been blocked to identify past attempted attacks. If possible, take additional measures to block unwanted traffic before it reaches your network.

Another way to protect your servers and networks is to create fake resources.
- A honeypot is a device or virtual machine that entices intruders by displaying a vulnerability, displaying a configuration flaw, or appearing to contain valuable data.
- A honeynet is a network of honeypots.
- A tarpit (or sticky honeypot) is a honeypot that answers connection requests in such a way that the attacking computer is stuck for a period of time.

Using these solutions fulfills two main goals.
- Attackers are offered targets that will occupy their time and attention, distracting them from valid resources.
- You can observe attackers and gather information about their attack methods or gather evidence for identification or prosecution purposes.
