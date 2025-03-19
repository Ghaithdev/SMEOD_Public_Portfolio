Question 1 of 20Correct
What is the best location for firewalls that supports a three-tier architecture and defense-in-depth?
Responses
(Between sections of varying trust levels)
Between switch ports
Between database servers
Between physical floors
Explanation
Maintaining functionality and security is an ongoing balancing act. The key rule is to give an entity the least access necessary, while still allowing it to perform its job. With network architecture, the key is to provide proper segmentation so that a person can access the appropriate data while reducing the risk of potential compromise.

If you look at the requirements for systems that reside on your network, you will probably notice that they can be grouped into several categories according to the type of information they contain, including: public, semi-public, middleware, and private.

Systems in each category serve a similar purpose and have common security requirements. This allows you to group resources within a category by placing them into a common network section. You should locate firewalls:

• Between the Internet and the other networks
• Between the semi-public and private network
• Between sections of varying trust levels

Skip to navigation
Question 2 of 20Correct
What type of cloud deployment is built, operated, and managed by a single company or organization?
Responses

Hybrid cloud

Public cloud

Community cloud

Private cloud
Explanation
There are three types of cloud deployments:

• Public: when all cloud services are operated by a third party
• Private: when IT resources are built, operated, and managed by a single organization, typically in their own data centers
• Hybrid: when an organization uses a combination of public cloud services with on-premise or private services; typically done when an enterprise has legacy systems of record that cannot be moved to the cloud

Skip to navigation
Question 3 of 20Correct
Which of the following TCP packet flags indicates that a connection is being shut down in a graceful fashion?
Responses
URG

ACK

RST

FIN

Explanation
When the time comes to close a connection, each end of the connection must be closed separately. Assuming that the client PC wants to close the connection first, the process starts when the PC sends a FIN packet to the server. The FIN portion indicates to the server that the PC wants to close the connection (continuing with the sequence count it has been using with the server). The server responds by sending an ACK to the PC, acknowledging the FIN that the PC sent. Next, the server sends a FIN packet to the PC to close its side of the connection. Finally, the PC sends an ACK to the server to acknowledge the FIN.

Skip to navigation
Question 4 of 20Incorrect
The ICMP is handled at which of the following layers of the OSI model?
Responses
Layer 3

Layer 5

Layer 2

Layer 7

Explanation
IP relies on the ICMP for network status messages and error reporting. ICMP messages are common on any IP network, so ICMP is just as important as TCP and UDP from a security standpoint. IP and ICMP are handled at Layer 3 of the OSI model.

Skip to navigation
Question 5 of 20Correct
In what type of isolation violation does a malicious actor leverage a compromised VM to execute code on the host computer?
Responses
VM escape

VM resource overloading

VM hyperjacking

VM sprawl

Explanation
One example of an isolation violation is known as a VM escape. A VM escape is best described as software code run from inside a guest VM but executed on the host computer. If a hypervisor has a VM escape vulnerability, an adversary can leverage a compromised guest VM and execute any code of their choosing on the host computer. This is slightly different from hyperjacking where a rogue or malicious hypervisor is installed, potentially from an external attacker host.

Skip to navigation
Question 6 of 20Correct
What is a benefit of cloud computing compared to an on-premise data center?
Responses
On-demand resources at the speed of business

Greater control of infrastructure

Resources take up to a month to provision

Trading away variable operating costs for fixed capital costs

Explanation
If deploying infrastructure in an existing data center or region was difficult, it was even more difficult for many companies to scale when expanding globally. This might have required IT teams to develop relationships, contracts, and service-level agreements in new parts of the world. Now, with the global scale of cloud providers, resources are readily available across the globe, leading to increased productivity.

Skip to navigation
Question 7 of 20Incorrect
What type of design is presented in the final phase of planning a system implementation and includes all the components and how they interlink, as well as servers, operating systems, and version numbers?
Responses
Physical
Logical
Implementation
Conceptual

Explanation
A physical design has all major components and entities identified within specific physical servers and locations or specific software services, objects, or solutions. This design level represents how the network and all its components are expected to behave, while still being on paper. The physical design is the last one created before the network design is implemented.

Skip to navigation
Question 8 of 20Correct
Which of the following IEEE 802.11 amendments currently operates in the 5 GHz frequency range and allows for a minimum of 1 Gbps bandwidth in a multi-link scenario?
Responses
802.11ax
802.11ac
802.11bg
802.11n

Explanation
802.11ac was truly designed to allow for high-speed interaction across the WLAN, supporting large numbers of simultaneous users with as effective a coverage area as possible. 802.11ac allows for a minimum of 1 Gbps in a multilink scenario, with a minimum of 500 Mbps for a single link scenario. It operates in the 5 GHz frequency range. 802.11ax is the next (future) iteration of 802.11 amendments.

Skip to navigation
Question 9 of 20Correct
What is an often-ignored IT asset in security hardening?
Responses
Desktops
Applications
Servers
Routers

Explanation
When most organizations think of security, the focus is often on the hardening of traditional IT assets: servers, desktops, and applications. Patching, updating, securing, and proper configuration management are all very important and key to security. Notwithstanding this approach as applied to traditional IT assets, there are other IT assets that end up being unintentionally ignored from a security perspective. One of these assets is related to the network infrastructure directly—routers and switches.

Skip to navigation
Question 10 of 20Correct
While the OSI protocol stack has seven layers; the TCP/IP stack has four layers. What layer in the TCP/IP stack combines the OSI physical and data link layers into one?
Responses
Transport (TCP)
Internet (IP)
Application
Network

Explanation
In the TCP/IP model, the network layer comprises both the physical and data link layers of the OSI model; the application layer encompasses the application, presentation, and session layers of the OSI model. The OSI model is more granular, as it was designed to support protocols other than just TCP/IP.

Skip to navigation
Question 11 of 20Correct
Which of the following layers of the OSI protocol stack handles the establishment and maintenance of connections?
Responses
Presentation
Session
Network
Transport

Explanation
The session layer handles the establishment and maintenance of connections between systems. It negotiates the connection, sets it up, maintains it, and makes sure that information exchanged across the connection is in sync on both sides.

Skip to navigation
Question 12 of 20Correct
What is a rough entry-level cost estimate of the hardware and software required for performing sniffing of wireless traffic?
Responses
US $2,000,000
US $50
US $5,000
US $20,000

Explanation
Contrary to popular opinion and possibly even more concerning, the equipment required to capture and analyze WLAN communications is neither expensive nor hard to obtain. For around US $50, the appropriate hardware can be purchased online. And the software component for the analysis and attack? Free. The software is often easily integrated into and available through attack frameworks.

Skip to navigation
Question 13 of 20Correct
Which layer 4 protocol is a good multicast solution for optimized real-time communications delivered over a wireless network?
Responses
IP
TCP
UDP
ICMP

Explanation
UDP is typically used in situations where it is okay if some packets are lost or reordered. In a streaming audio application, for example, each packet contains such a minuscule amount of audio data that the client can likely afford to lose one or two packets in succession without suffering a noticeable lack of quality. In addition, because it is real-time communication, retransmitting the packets does not make sense.

Skip to navigation
Question 14 of 20Correct
What are some examples of mitigating controls against a rogue AP that is masquerading as the legitimate AP?
Responses
802.3X and manual entry of known MAC addresses
802.11X and manual entry of known MAC addresses
One-time password tokens and client isolation
Certificates for mutual authentication and 802.1X

Explanation
A Rogue Access Point (Rogue AP) that is masquerading as the legitimate AP is sometimes described as the evil twin. The best prevention is early detection of its presence combined with a timely response. Certificates for mutual authentication (client to AP and AP to client) can also be used to alert end users that they are not connecting to the legitimate AP. 802.1X can prevent the rogue AP from being granted full access to the internal network itself.

Skip to navigation
Question 15 of 20Correct
What ICMP type is associated with conditions related to the exceeding of a time limit?
Responses
Type 0
Type 8
Type 11
Type 3

Explanation
Type 11 is associated with conditions related to exceeding a time limit; Type 11, code 0, for example, occurs when the TTL of an IP packet has reached a value of 0 (the packet is expired). Type 11, code 1 occurs when the TTL of the IP packet expires during the reassembly by the recipient of the packet. The station receiving and re-assembling the packet would send an ICMP TTL exceeded (type=11) fragmentation reassembly time exceeded (code=1).

Skip to navigation
Question 16 of 20Correct
Which of the following OSI layers implements IP based functionality, such as time to live and type of service?
Responses
Layer 2
Layer 4
Layer 3
Layer 7

Explanation
IP is the basis for all communication on the Internet. It is so important that it even gets its own layer in the TCP/IP stack. IP works at Layer 3 of the OSI model. Its primary purpose is to handle the transmission of packets between network endpoints, usually single hosts identified with a unique address.

IP includes some features that provide basic measures of fault-tolerance (time to live, checksum), traffic prioritization (type of service), and support for the fragmentation of large packets into multiple smaller packets (ID field, fragment offset). IP is singularly focused on routing packets from point A to point B on the network as quickly and efficiently as possible. It does not provide any mechanisms for guaranteed delivery or delivery in sequence. Instead, it relies on upper-layer protocols and applications to provide those mechanisms appropriately for the application.

Skip to navigation
Question 17 of 20Correct
What term characterizes a virtual Kali Linux machine running on a Windows 10 computer?
Responses
Hypervisor OS
Default OS
Guest OS
Host OS

Explanation
When talking about virtual machines, it is important to be able to distinguish between the main system and the virtual software. Because a host computer needs an operating system to boot, it is referred to as the host operating system. On the host operating system, a virtual machine application such as VMware can be installed. This virtual machine software enables you to run multiple guest operating systems which are actually applications running on the host OS. However, the virtual machine software segments out memory and hardware so they look and act like independent OSes, even though there is always only one physical host and one or more guest operating systems at any given time.

Skip to navigation
Question 18 of 20Correct
What type of cloud service is characterized by the customer managing configuration options and user provisioning and the cloud service provider managing all the other underlying responsibilities?
Responses
Infrastructure as a Service
Platform as a Service
Software as a Service
Functions as a Service

Explanation
In the Software-as-a-Service (SaaS) delivery model, the Cloud Service Provider (CSP) gives access to a web application that is used by several customer organizations. Typically, the user that establishes the service with the CSP can create other user accounts that are associated with the customer organization. This administrative user may also have the ability to make other preference settings that apply to the organization globally. All other security responsibilities beyond provisioning users and selecting configuration options are the duty of the cloud service provider.

Skip to navigation
Question 19 of 20Incorrect
How many bits are set aside for the fragmentation offset?
Responses
16
13
12
14

Explanation
The concept of fragmentation covers two fields: flags and fragment offset, together totaling 16 bits. Of these, 13 are set-aside for the fragmentation offset and the other 3 bits are set for flags.

Skip to navigation
Question
Question 20 of 20Correct
Which program can be used to perform detailed analysis and automatic packet decoding of network packet data in a GUI environment?
Responses
tcpdump
Wireshark
Kismet
Snort
Explanation
Wireshark is best described not as a sniffer but as a network protocol analyzer. Wireshark can understand hundreds of different protocols and media types. While Wireshark can sniff network communication, that is not its primary purpose. Its primary purpose is to better assist an analyst by providing a more effective analysis of what is being communicated.

Question 1 of 20Incorrect
Which of the following correctly provides a basis for estimating the total cost of a data loss event?
Responses
Reputational damage, cost of updating the backup infrastructure, cost of re-creating the lost data
Reputational damage, cost of updating the backup infrastructure, cost of re-creating the lost data
Value of lost data, cost of updating the backup infrastructure, cost of re-creating the lost data
Value of lost data, cost of updating the backup infrastructure, cost of re-creating the lost data
Reputational damage, cost of updating the backup infrastructure, cost of continuing operations without the lost data
Reputational damage, cost of updating the backup infrastructure, cost of continuing operations without the lost data
Value of lost data, cost of re-creating the lost data, reputational damage
Value of lost data, cost of re-creating the lost data, reputational damage
Explanation
The total cost must include the value of lost data, cost of re-creating the lost data, and reputational damage. The cost of updating the backup infrastructure is not a factor, as it is an ongoing cost associated with normal business operations, rather than a data loss event.

Skip to navigation
Question 2 of 20Correct
In the NIST 800-63 standard, which identity assurance level (IAL) requires a physical presence for identity proofing?
Responses
IAL4
IAL4
IAL3
IAL3
IAL2
IAL2
IAL1
IAL1
Explanation
The physical check is done at level 3 – IAL3; the applicant needs to be physically present and provide substantial evidence to prove their identity.

Skip to navigation
Question 3 of 20Incorrect
What is the most common approach to defense in depth?
Responses
Vector oriented
Vector oriented
Protected enclaves
Protected enclaves
Information-centric
Information-centric
Uniform protection
Uniform protection
Explanation
Uniform protection treats all systems as equally important. It is the most common approach and the usual starting point for most organizations.

Skip to navigation
Question 4 of 20Correct
Which two of the three CIA pillars is considered relevant for a list of books available from an online bookshop?
Responses
Consistency, availability
Consistency, availability
Integrity, availability
Integrity, availability
Integrity, awareness
Integrity, awareness
Confidentiality, integrity
Confidentiality, integrity
Explanation
The two pillars relevant are integrity and availability. This is because the shop should provide an accurate list of items for sale (integrity) and a 24-hour online presence for buyers to place an order (availability). Confidentiality is not applicable, as no shop wants to keep their items for sale a secret.

Skip to navigation
Question 5 of 20Correct
What are the primary functions within the MITRE ATT&CK Framework?
Responses
Tactics, Techniques
Tactics, Techniques
Administrative, Operational, Technical
Administrative, Operational, Technical
Basic, Foundational, Organizational
Basic, Foundational, Organizational
Identify, Protect, Detect, Respond, Recover
Identify, Protect, Detect, Respond, Recover
Explanation
MITRE ATT&CK™ is a globally accessible knowledge base of adversary tactics and techniques based on real-world observations. The ATT&CK knowledge base is used as a foundation for the development of specific threat models and methodologies in the private sector, in government, and in the cybersecurity product and service community.

Tactics are high-level attack steps used by an adversary. These can be compared to the steps in the Lockheed Martin Cyber Kill Chain©. MITRE ATT&CK assumes breach and thus the first tactic is initial intrusion. Any activity performed before is covered by the PRE-ATT&CK framework.

How a certain tactic is executed is described by a variety of techniques. For every technique, MITRE ATT&CK includes a description, detection and prevention recommendations, and known threat actors who use the technique.

Skip to navigation
Question 6 of 20Incorrect
What are the primary implementation tiers within the NIST Cyber Security Framework?
Responses
Partial, Risk Informed, Repeatable, Adaptive
Partial, Risk Informed, Repeatable, Adaptive
Identify, Protect, Detect, Respond, Recover
Identify, Protect, Detect, Respond, Recover
Basic, Foundational, Organizational
Basic, Foundational, Organizational
Tactics, Techniques
Tactics, Techniques
Explanation
The NIST Cyber Security Framework Implementation tiers provide context on how your organization and process are in place to manage certain types of risks. Organizations should determine the desired tier; for example, in case an organization identifies a certain control as tier 1, they should be encouraged to move to tier 2 or greater.

• Partial: Certain controls are partially implemented, processes are not formalized, and there is limited awareness of cyber security risks. This is the lowest tier within the NIST cybersecurity framework.

• Risk Informed: Risk management practices are formalized and approved by management. It has not been published organization wide and cyber risk awareness is limited to the organization level.

• Repeatable: Risk management practices are formally approved and expressed as policy. There is an organization-wide approach to manage cybersecurity risk.

• Adaptive: Adapts cybersecurity practices based on previous and current cybersecurity activities, including lessons learned and predictive indicators.

Skip to navigation
Question 7 of 20Incorrect
Which of the following drawbacks is applicable to differential backups?
Responses
Relies on previous differential instances, thus the loss of one instance impacts all subsequent instances
Relies on previous differential instances, thus the loss of one instance impacts all subsequent instances
Does not allow multiple instances based on the same full system backup
Does not allow multiple instances based on the same full system backup
In case of an outage, requires all previous differential instances to be restored before the desired one is restored
In case of an outage, requires all previous differential instances to be restored before the desired one is restored
Backup size increases without regular new full system backups
Backup size increases without regular new full system backups
Explanation
The drawback of differential backups is that they require regular, new, full system backups to keep the backup size smaller. Differential backups allow multiple instances to be taken independently of each other on the same full system backup; the same applies to the restoration process.

Skip to navigation
Question 8 of 20Correct
Which of the following backup methods can be used to restore data to any point in time?
Responses
Differential backups
Differential backups
Incremental backups
Incremental backups
Full system imaging
Full system imaging
Continuous backups
Continuous backups
Explanation
Continuous backups store data automatically to a backup medium each time a change is made to the data. Theoretically, this allows you to restore a backup of any single point in time.

Skip to navigation
Question 9 of 20Correct
Which of the following technologies does not help in preventing data leaks, but can be used to identify the source of a leak?
Responses
Digital watermarking
Digital watermarking
Firewall
Firewall
Third-party risk management systems
Third-party risk management systems
Honeypots
Honeypots
Explanation
Digital watermarking does not help in preventing data leaks, but can be used after the fact to identify the source of a leak. Firewalls are network control devices. Honeypots are systems that lure an attacker and then track TTPs. Third-party risk management systems are used to manage risk.

Skip to navigation
Question 10 of 20Incorrect
What are the primary functions within the NIST Cyber Security Framework?
Responses
Identify, Protect, Detect, Respond, Recover
Identify, Protect, Detect, Respond, Recover
Basic, Foundational, Organizational
Basic, Foundational, Organizational
Administrative, Operational, Technical
Administrative, Operational, Technical
Tactics, Techniques, Procedures
Tactics, Techniques, Procedures
Explanation
The NIST Cyber Security Framework provides an interesting framework to look at risks and offers guidelines on how to secure your environment. The core framework has five functions, and each of these functions can have multiple categories.

• Identify: Develop an organizational understanding to manage cybersecurity risk to (a) systems, (b) people, (c) assets, (d) data, and (e) capabilities.

• Protect: Develop and implement appropriate safeguards to ensure delivery of critical services; an example is to use perimeter filtering.

• Detect: Develop and implement appropriate monitoring capabilities; this means looking at certain events and alerting policies.

• Respond: Develop and implement appropriate activities to take action regarding a detected security incident.

• Recover: Develop and implement appropriate activities to plan for resilience and restore capabilities.

Skip to navigation
Question 11 of 20Incorrect
Which of the following security features of Android allows for remotely locating and wiping Android devices?
Responses
Device control
Device control
Device manager
Device manager
Call home
Call home
Find My Droid
Find My Droid
Explanation
Device Manager allows for locating and securely wiping remote devices. Devices that contain sensitive information can get stolen or lost. Therefore, Android has the capability to locate and securely wipe devices to protect sensitive information from being exposed.

Skip to navigation
Question 12 of 20Correct
Defense in depth is an effective control against a lot of threats; however, it does fall short in some aspects. What is one aspect?
Responses
Internal threats already bypassed a few of the outer security controls.
Internal threats already bypassed a few of the outer security controls.
External threats already blocked by a few of the outer security controls.
External threats already blocked by a few of the outer security controls.
Internal threats already blocked by a few of the outer security controls.
Internal threats already blocked by a few of the outer security controls.
External threats already bypassed a few of the outer security controls.
External threats already bypassed a few of the outer security controls.
Explanation
Before defense in depth, perimeter security network setups assumed that insiders were partially or fully trusted. As a result, adversaries could easily gain access to other systems once they gained a foothold inside. The layered approach of defense in depth made it more difficult for attackers, as they had to circumvent multiple controls before they could advance into the network. Although this model complicates things for attackers, it still grants some privileges to internal users.

Skip to navigation
Question 13 of 20Incorrect
Which of the following password cracking attack methods will always have a 100% success rate when cracking a password that is a combination of upper case and lower case words, numerals, and possibly special characters?
Responses
Hybrid attack
Hybrid attack
Brute-force attack
Brute-force attack
Pre-computation attack
Pre-computation attack
Dictionary attack
Dictionary attack
Explanation
The most powerful cracking method is the brute-force method. It will always recover the password no matter how complex it is—it is just a matter of time. The other attack methods may crack the password depending on the password and the wordlist being used.

Skip to navigation
Question 14 of 20Correct
What should you recommend to IT management as a viable solution for protecting an internal network that involves breaking the network into sections to limit an attacker's ability to move throughout the network with ease?
Responses
Set firewall rules to DENY ports 80 and 445.
Set firewall rules to DENY ports 80 and 445.
Implement AES-256 encryption across all network communication.
Implement AES-256 encryption across all network communication.
Implement VLANs on sensitive enclaves.
Implement VLANs on sensitive enclaves.
Create a network with no access to the Internet.
Create a network with no access to the Internet.
Explanation
Protected enclaves involve segmenting your network. This can be done by implementing many VLANs across a single network and segmenting these VLANs by means of switches or firewalls that filter traffic between sections of the network. This is a simple yet effective technique. Reducing the exposure or visibility of a system can greatly reduce the potential impact of malicious code. For example, if you have 5,000 systems on a network and a system gets compromised, it could spread to all systems. However, if you create separate segments with 100 systems per segment, a virus would impact only a small percentage of your systems, minimizing cleanup and damage.

Skip to navigation
Question 15 of 20Correct
Which of the following is a reason that Apple iOS devices are harder to compromise?
Responses
Open standard
Open standard
Apple's closed ecosystem
Apple's closed ecosystem
More configurable OS
More configurable OS
Less locked down OS
Less locked down OS
Explanation
iOS is part of Apple's closed ecosystem, which verifies all aspects of the boot cycle and is much harder to compromise.

Skip to navigation
Question 16 of 20Incorrect
Who should assign data classification labels to data?
Responses
Data protection officer
Data protection officer
Custodian of the data
Custodian of the data
Owner of the data
Owner of the data
Chief risk officer
Chief risk officer
Explanation
The owner of the data should assign the label to the data. If needed, a DLP tool can often make suggestions to the data owner on which label to use depending on the contents of the data and whether any sensitive information has been found.

Skip to navigation
Question 17 of 20Correct
Which of the following options correctly specifies the aims of risk handling by deploying defense in depth measures?
Responses
Reduce, transfer, or accept risk
Reduce, transfer, or accept risk
Estimate, reduce, or transfer risk
Estimate, reduce, or transfer risk
Estimate, accept, or terminate risk
Estimate, accept, or terminate risk
Transfer, accept, or terminate risk
Transfer, accept, or terminate risk
Explanation
The aim is to reduce, transfer, or accept risk. Risk estimation is not the aim; rather, it is a driver for devising the measures that are deployed.

Skip to navigation
Question 18 of 20Correct
What can be used to provide common grounds for effectiveness of security measures?
Responses
The trend of the rate of implementation of the CIS Controls
The trend of the rate of implementation of the CIS Controls
The established metrics to measure effectiveness of the implemented CIS Controls
The established metrics to measure effectiveness of the implemented CIS Controls
A detailed root cause analysis for each of the month's operational incidents
A detailed root cause analysis for each of the month's operational incidents
A detailed root cause analysis for each of the month's security incidents
A detailed root cause analysis for each of the month's security incidents
Explanation
Metrics are established to measure the effectiveness of the CIS Controls so that risk can be communicated using a common language. Regular communication with defined and understood metrics allows executives to better understand where the greatest risk resides. Implementation of the CIS Controls is expected to take years, and some controls are considerably more difficult to implement; therefore, reporting on the rate of implementation is not useful.

Skip to navigation
Question 19 of 20Correct
Which of the following values is added to a password before hashing to ensure that no two stored values are the same, even if the users have chosen the same passwords?
Responses
Salt values
Salt values
dkLen values
dkLen values
Input transformation values
Input transformation values
Salsa values
Salsa values
Explanation
To strengthen an algorithm, you want to ensure that no two stored values are the same, even if users have chosen the same password. This is where a salt value comes into the picture. The salt value is a randomly generated string of characters that is added to each password before hashing it and is stored next to the hashed value.

Skip to navigation
Question
Question 20 of 20Incorrect
Which of the following access control techniques requires matching classifications and clearances?
Responses

LBAC
LBAC
RBAC
RBAC

MAC
MAC

DAC
DAC
Explanation
Mandatory Access Control (MAC) controls all access. Controls are set by the system and cannot be overwritten by the administrator. MAC requires a lot of work to maintain because all data have a classification and all users have a clearance. Users must have the appropriate clearance to access data classified a certain way. Users cannot give their clearance to another person.