# Network Protocols

A protocol is a set of standards for communication between network hosts. Protocols often provide services, such as email or file transfer. Most protocols are not intended to be used alone and rely on interaction with other dependent or complimentary protocols. A protocol suite is a group of protocols intended to be used together.

The internet protocol suite (frequently referred to as TCP/IP) is the most widely used protocol suite today.

## Web Services Protocols

- Hypertext Transfer Protocol (HTTP) - Web browsers and web servers use HTTP to exchange files (such as web pages) through the world wide web and intranets. HTTP can be described as an information requesting and responding protocol. It is typically used to request and send web documents, but is also used as the protocol for communication between agents that employ different TCP/IP protocols.

- HTTP over SSL (HTTPS) - HTTPS is a secure form of HTTP that uses SSL to encrypt data before it is transmitted.

- Secure Sockets Layer (SSL) - SSL secures messages being transmitted on the internet. It uses RSA for authentication and encryption. Web browsers use SSL to ensure safe web transactions. URLs that begin with https:// trigger your web browser to use SSL.

- Transport Layer Security (TLS) - TLS ensures that messages being transmitted on the internet are private and tamper proof. TLS is implemented through two protocols:
1. TLS Record can provide connection security with encryption (for example, with DES).
2. TLS Handshake provides mutual authentication and choice of encryption method.

## File Transfer Protocols

- File Transfer Protocol (FTP) - FTP provides a generic method for transferring files. It can protect access to files by requiring user names and passwords, and it allows file transfer between dissimilar computer systems. FTP can transfer both binary and text files, including HTML, to another host. FTP URLs are preceded by ftp:// followed by the DNS name of the FTP server. To log in to an FTP server, use ftp://username@servername.

- Trivial File Transfer Protocol (TFTP) - TFTP is similar to FTP. It lets you transfer files between a host and an FTP server. However, it does not provide user authentication or error detection. TFTP is often used when files need to be transferred between systems quickly. Because it does not perform error detection, TFTP is faster than FTP, but is susceptible to transmission errors.
Secure File Transfer Protocol (SFTP)	

- SFTP - uses Secure Shell (SSH) to secure data transfers. SSH ensures that SFTP transmissions use encrypted commands and data, which prevents clear text data transmissions.

- Secure Copy (SCP) - SCP is used to securely transfer files between systems. Like SFTP, SCP relies on SSH to ensure that data and passwords are not transmitted over the network in clear text.

## Email Protocols

- Simple Mail Transfer Protocol (SMTP) - SMTP is used to route electronic mail through the internetwork. SMTP is used:
1. Between mail servers for sending and relaying mail.
2. By all email clients to send mail.
3. By some email client programs, such as Microsoft Outlook, to receive mail from an Exchange server.

- Post Office Protocol 3 (POP3) - POP3 is used to retrieve email from a remote server and download it to a local client over a TCP/IP connection.
An email client that uses POP3 for receiving mail uses SMTP for sending mail.

- Internet Message Access Protocol version 4 (IMAP4) - IMAP4 is an email retrieval protocol designed to enable users to access their email from various locations without the need to transfer messages or files back and forth between computers. Messages remain on the remote mail server and are not automatically downloaded to a client system.
An email client that uses IMAP4 for receiving mail uses SMTP for sending mail.

## Network Services Protocols

- Dynamic Host Configuration Protocol (DHCP) - DHCP is used to automatically assign addresses and other configuration parameters to network hosts. Using a DHCP server, hosts receive configuration information at startup, reducing the amount of manual configuration required on each host.

- Domain Name System (DNS) - DNS is a distributed system throughout the internetwork that provides address and name resolution. For example, the name www.mydomain.com would be mapped to a specific IP address.

- Network Time Protocol (NTP) - NTP is used to communicate time synchronization information between systems on a network.

- Lightweight Directory Access Protocol (LDAP) - LDAP is used to search, retrieve data from, and update a directory service. The LDAP protocol follows a client/server model. One or more LDAP servers contain the directory data. The LDAP client connects to an LDAP Server to make a directory service request. By default, LDAP traffic is transmitted unsecured.

- Secure Lightweight Directory Access Protocol (LDAPS) - LDAPS is the lightweight directory access protocol over TLS/SSL. Using LDAPS makes LDAP traffic confidential and secure. LDAPS uses TCP port 636.

## Network Management Protocols

- Simple Network Management Protocol (SNMP) - SNMP is designed for managing complex networks. SNMP lets network hosts exchange configuration and status information. This information can be gathered by management software and is used to monitor and manage the network.

- Remote Terminal Emulation (Telnet) - Telnet allows a computer to remotely access the console of a computer system somewhere else in the network. At one time, Telnet was widely used for remote management tasks, but it is rarely used today. Because Telnet does not use encryption, it is recommended that you use a secure alternative to Telnet for remote management tasks, such as SSH.

- Secure Shell (SSH) - SSH allows for secure interactive control of remote systems. SSH uses RSA public key cryptography for both connection and authentication. SSH uses the IDEA algorithm for encryption by default, but it can use Blowfish and DES. SSH is a secure and preferred alternative to Telnet.

## Transport Protocols

- Transmission Control Protocol (TCP) - TCP provides services that ensure accurate and timely delivery of network communications between two hosts. TCP provides the following services to ensure message delivery:
1. Sequencing of data packets
2. Flow control
3. Error checking
4. Acknowledgement of packets sent
5. Retransmission of lost packets

- User Datagram Protocol (UDP) - UDP is a host-to-host protocol like TCP, but it does not acknowledge each packet transmitted, nor does it allow for retransmission of lost packets. This reduces its overhead, allowing for faster communications and making UDP ideal for applications like streaming audio and video. However, this speed comes at the expense of possible errors or data loss.

## Control Protocols

- Internet Control Message Protocol (ICMP) - ICMP works closely with IP to prevent errors and control information by allowing hosts to exchange packet status information. Two common management utilities, ping and traceroute, use ICMP messages to check network connectivity. ICMP also works with IP to send notices for the following:
1. When destinations are unreachable
2. Which route and hops a packet takes through the network
3. Whether devices can communicate across the network

- Internet Group Management Protocol (IGMP) - IGMP defines host groups. All group members can receive broadcast messages (multicasts) intended for the group. Multicast groups can be composed of devices within the same network or across networks (connected with a router).
