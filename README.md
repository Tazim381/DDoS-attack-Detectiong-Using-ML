# Abstract

A Distributed Denial of Service (DDoS) attack is a malicious attempt to disrupt the regular functioning of a network, service, or website by overwhelming it with a flood of internet traffic. DDoS attacks pose a substantial threat to network security. Detecting these attacks in real time is a critical challenge. Detecting Distributed Denial of Service (DDoS) attacks has several significant benefits for organizations and network security. The major goal of this research paper is to use machine-learning algorithms to detect DDoS attacks, and to determine which algorithms are the most effective in terms of confusion matrix, accuracy, and cross-validation score. For the categorization of benign and malicious attacks, many Machine Learning algorithms have been applied. The dataset sdn Dataset, which includes 1,04,345 samples and 23 characteristics, was used. On the dataset collected from the Kaggle repository, the study focuses on several models that are implemented, such as Logistic Regression, Support Vector Machine (SVM), Decision Tree (DT), Random Forest (RF), and K Nearest Neighbour (KNN). Each of these algorithms has been tested and compared in terms of accuracy and cross-validation score. All of the methods are implemented in Python and run in Google Colab, a Scientific Python Development Environment. Random Forest classifier is shown to be the most accurate for predictive analysis.
Two types of requests can be found here. Two types of requests: benign and malicious.


# Introduction


A ”Distributed Denial-of-Service (DDoS) Attack” is a severe type of cybercrime that
causes disturbances by flooding a server with so many requests that it becomes inactive,
hence blocking normal users from accessing websites and services. A DDoS attack’s
primary goal is to interfere with a website’s ability to provide both internal and external
services without interruption [1]. The unique feature of DDoS attacks is their ability to
generate massive amounts of attack traffic by using numerous compromised computer
systems as sources. This range of compromised machines includes a variety of de-
vices, such as PCs, and networked resources like Internet of Things (IoT) devices.
The birth of the Internet of Things (IoT) forecasts a connected world in which items
communicate with one another to gather and exchange information on their own, elim-
inating the need for human intervention. But as the Internet of Things becomes
more and more prevalent there is a warning associated with the rise in remote work and
the number of Internet-connected devices. Despite their wide acceptance, IoT devices
might not always conform to strict security protocols, making the networks they pene-
trate vulnerable to hacking and hostile assaults. DoS/DDoS assaults have increased in
frequency, severity, and intelligence over time. At first, the most frequent threats to net-
works were transport layer DDoS attacks like TCP-SYN and UDP, as well as network
layer threats like ICMP flooding. Advanced detection methods like Machine Learning
(ML) and Deep Learning (DL) started to identify these threats, but as a result, more
sophisticated and targeted DDoS attacks—known as application-layer attacks—began
to surface. Application-layer DoS/DDoS attacks are more advanced and focused threats
that impact the resources of the servers. As a result, traditional attack detection methods
that rely on packet-level data are useless. Using data from network traffic flows to
create a network-based Intrusion Detection System (IDS) that employs advanced net-
working technologies like Software-Defined Networking (SDN) is crucial for detecting
DoS/DDoS attacks. SDN is a modern networking architecture that separates network
devices from the control plane (CP).
The way this technology operates is different from traditional network architecture. All
network control operations, such as traffic monitoring and routing, are managed by a
centralized software-based controller, even if the forwarding engine is housed in the
switches.SDN is a new concept whose programmable and dynamic structure makes
network management easier. Network administration is handled by a central controller
in SDN, which separates the control and data planes. Attacks against the controller
are the most serious of these because the attacker who takes control of the controller
can potentially control or interfere with all network traffic. The most common kind of
controller assaults are denial-of-service (DDoS) attacks, which prevent users from ac-
cessing network services. The attackers want to overload the target system with traffic
from several machines, deplete its resources, and eventually stop it from working by us-
ing DDoS assaults. Attackers employ ”botnets” made from zombie devices that online
hackers have taken over. DDoS assaults are extremely difficult to identify and stop be-
cause they use a large number of computers. DDoS assaults are becoming more frequent
and severe, and they can be devastating to a variety of network services. For this
reason, among the most crucial issues facing network service providers and managers
is the prompt identification and prevention of DDoS assaults. By using DDoS attacks
to flood communication channels between the controller and the switch or between the
controller and the application layer with superfluous flow information, different SDN
levels can be rendered inoperable. The controller does not have an internal security
system that can differentiate between legitimate and malicious communications. As
a result, it is incredibly challenging to identify an assault. Application-layer assaults,
resource-consuming attacks, and volumetric attacks are the three types of DDoS at-
tacks. Complex attacks are a subset of application-layer attacks. They gradually use
up network resources and use less bandwidth to target particular services. As such, it
is challenging to identify. This category includes assaults on the Domain Name System
(DNS) and Hypertext Transfer Protocol (HTTP). Attacks that consume a lot of re-
sources cause servers to become unavailable by exploiting weaknesses in network layer
protocols. The target machine’s RAM, CPU, and storage are all depleted by TCP-SYN
Flood. With volumetric assaults, it seeks to use the network’s bandwidth. Vulner-
abilities in Layer 3 and Layer 4 protocols are used in common attacks such as ICMP,
UDP, and TCP-SYN flood.
