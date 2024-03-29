Designing a three-server web infrastructure to host www.foobar.com with the specified requirements involves careful consideration of security, encryption, and monitoring. Here's an outline that addresses the requirements and the related specifics, as well as potential issues with the infrastructure:

Firewalls:

Purpose: Firewalls are essential for securing the network and servers from unauthorized access and potential cyber threats. They help control incoming and outgoing network traffic based on predetermined security rules.
SSL Certificate for HTTPS:

Purpose: Serving traffic over HTTPS is crucial for ensuring secure communication between the server and the client's browser. It encrypts data, providing confidentiality, integrity, and authentication for the website.
Monitoring Clients:

Purpose: Monitoring allows for the real-time tracking of the system's performance, identifying potential issues, and ensuring the infrastructure's availability and reliability.
Data Collection: Monitoring clients, like Sumologic, collect data on various metrics such as server response times, resource usage, and error rates to provide insights into the system's health and performance.
Specifics of the Infrastructure:

Monitoring Web Server QPS:
To monitor the web server's QPS (Queries Per Second), the monitoring tool can track the incoming requests and measure the server's response time. It can also monitor the server's load, CPU usage, and network bandwidth to ensure the system is operating within the desired performance limits.
Issues with the Infrastructure:

Terminating SSL at the Load Balancer Level:

Termination of SSL at the load balancer level can expose the data to potential security risks during transmission from the load balancer to the server. This could potentially compromise the confidentiality and integrity of the data being transmitted.
Single MySQL Server for Writes:

Having only one MySQL server capable of accepting writes can create a single point of failure. If this server fails, it could result in data loss or website downtime, affecting the availability and reliability of the application.
Identical Components on Servers:

Having servers with the same components increases the risk of widespread failures. If there is an issue with a specific component, it could affect all servers simultaneously, leading to a complete system outage. Introducing component diversity can mitigate this risk, ensuring redundancy and fault tolerance in the infrastructure.
By addressing these specifics and considering the potential issues, the design of the web infrastructure can be optimized for security, performance, and reliability.
