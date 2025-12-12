# Network Design

Instead of deploying a network in an unstructured manner, you should develop a network design first. Network designs require some time and effort to complete, but they prevent costly errors. The network design process varies by organization, but most network designs employ the processes listed below.

## Conduct a Needs Assessment

Conducting a needs assessment is one of the most important aspects of creating a network design. A needs assessment determines:
- Why the project is being undertaken.
- What outcomes are expected.
- When the project is expected to be complete.
  
You will need to meet with a variety of individuals within your organization and gather data about the deployment. You should record your findings in a text document that you can distribute to others for review. When the needs assessment is complete, it should contain several important pieces of information:
- What are the goals of the project? What business need will it meet?
- When is the deployment needed?
- Who are the stakeholders in this project? You should identify all individuals - who will be impacted by the project in any way by asking questions such as:
- - Who requested the deployment?
- - Who will use the network after it's installed?
- - Who has the authority to approve funds for the project?
- - Who has authority to allocate IT staff to work on the project?
- - Who must give final approval to this project before it can begin?
- - Who will maintain and support the network after it is implemented?

By gathering this data, you can define the scope of the project as a part of the needs assessment. The project scope defines exactly what to do, when to do it, and who will do it. Every project scope contains three elements that must be kept in balance:
- Schedule
- Resources
- Scale

## Design the Physical Topology	
The next step is to design the physical topology. This involves planning:
- Where network wiring needs to be physically installed to meet the requirements identified in the needs assessment.
Where switches need to be physically located.
- Which wire runs will connect to which switch ports.
- How switches will connect to each other.
- Where routers will be located and how they will interconnect to create subnets.
- Where WAN links will be implemented in the network.
- Where the broadcast and collision domain boundaries will be.
- Where security devices, such as firewalls and IPS devices, will be placed.
- How wireless controllers will connect to the wired network.
- Where access points will be physically located.

## Design the Logical Topology	
The next step is to define the logical topology. You need to plan:
- VLAN boundaries.
- IP addressing information for each subnet.
- Naming conventions that will be used for network hosts.
- Protocols that will be used for WAN links.
Routing protocols that will be used.
- How data will be routed between:
- - Networks
- - Wireless and wired networks
- - The internet and your network
- Measures that will be implemented to provide network redundancy, such as:
- - STP
- - FHRP
- Security mechanisms that will be used to:
- - Protect wired networks, such as switch security measures and firewall ACLs.
- - Protect wireless networks, such as encryption mechanisms.

## Plan Network Services	
The next phase of the design involves planning the services that will be provided by the network, such as:
- DHCP servers
- DNS servers
- Directory servers
- File and print servers
- Database servers
- Web servers

## Select Hardware and Software	
The next phase of the design requires you to decide how many physical servers will be needed and where specific services will be hosted. You must also decide where they will be physically located on the network and what operating systems will be installed on them. There are several important things that you must do:
- Arrange for access to support resources provided by hardware and software vendors.
- Plan for future growth. Buy hardware that will accommodate increased capacity and demands in the future.
- Verify that the hardware is compatible with operating systems, applications, and services you intend to use.
- Plan for data protection:
- - Implement the hardware and software required to back up network data.
- - Implement the hardware required to create redundancy, such as RAID arrays, clustering, and UPS devices.
- Check the system requirements of the network operating systems you plan to use and verify that they are compatible with:
- - Your server hardware.
- - The network protocols you plan to deploy.
- - The applications and services you want to use on your network.
- - The client devices that will connect to them over the network.
- Allocate the data center space necessary for your server hardware.

## Plan Authentication and Authorization Systems	
The last phase involves designing the systems that will control how users will authenticate to the network and become authorized to use network resources. You should identify:
- Where user accounts will be stored. Will they be:
- - Stored on a centralized directory server, such as an Active Directory domain controller?
- - Maintained separately on each individual network device?
- - Maintained on an AAA system, such as a RADIUS server?
- How you will manage authorization. You need to plan how you will use ACLs to ensure that each user has access to the information they need to do their job, but no more.
