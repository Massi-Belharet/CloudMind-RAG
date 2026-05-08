> [!IMPORTANT]
> This page provides a one-page view of all of the pages in the FSI perspective of the [Well-Architected Framework](https://docs.cloud.google.com/architecture/framework). You can print this page or save it in PDF format by using your browser's print function.
>
> This page doesn't have a table of contents. You can't use the links on this
> page to navigate within the page.

<br />


This document in the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
describes principles and recommendations to help you to design, build, and
manage financial services (FS) applications in Google Cloud that meet
your operational, security, reliability, cost, and performance goals.

The target audience for this document includes decision makers, architects,
administrators, developers, and operators who design, build, deploy, and
maintain FS workloads in Google Cloud. Examples of FS organizations that
could benefit from this guidance include banks, payment infrastructure players,
insurance providers, and capital market operators.

FS organizations have specific considerations, particularly for architecture
and resilience. These considerations are primarily driven by regulatory, risk,
and performance requirements. This document provides high-level guidance that's
based on design considerations that we've observed across a wide range of FS
customers globally. Whether your workloads are fully in the cloud or
transitioning to hybrid or multi-cloud deployments, the guidance in this
document helps you design workloads on Google Cloud to meet your
regulatory requirements and diverse risk perspectives. The guidance might not
address the unique challenges of every organization. It provides a foundation
that addresses many of the primary regulatory requirements of FS organizations.

A primary challenge in designing cloud workloads involves aligning cloud
deployments with on-premises environments, especially when you aim for
consistent approaches to security, reliability, and resilience. Cloud services
create opportunities to fundamentally rethink your architecture in order to
reduce management overhead, optimize cost, enhance security, and improve
reliability and resilience.

The following pages describe principles and recommendations that are specific to
FS workloads for each pillar of the Well-Architected Framework:

- [FS perspective: Operational excellence](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/operational-excellence)
- [FS perspective: Security](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/security)
- [FS perspective: Reliability](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/reliability)
- [FS perspective: Cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/cost-optimization)
- [FS perspective: Performance optimization](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/performance-optimization)

## Contributors

Authors:

- [Gino Pelliccia](https://www.linkedin.com/in/gino-pelliccia-13637025) \| Principal Architect
- [Alex Stepney](https://www.linkedin.com/in/alexstepney/) \| Lead Principal Architect
- [Phil Bryan](https://www.linkedin.com/in/philbry) \| EMEA FSI Lead Principal Architect
- [Stathis Onasoglou](https://www.linkedin.com/in/stathisonasoglou) \| EMEA FSI Principal Architect
- [Sam Moss](https://www.linkedin.com/in/samuel-moss-643780105) \| EMEA FinOps Professional Services Lead

<br />

Other contributors:

- [Daniel Lees](https://www.linkedin.com/in/daniellees) \| Cloud Security Architect
- [Danielle Fisla](https://www.linkedin.com/in/danielle-fisla-7132192) \| US FS Portfolio Lead, PSO
- [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) \| Customer Engineer, AI/ML Specialist
- [Henry Cheng](https://www.linkedin.com/in/tohenryc) \| Principal Architect
- [John Bacon](https://www.linkedin.com/in/johnbac/) \| Partner Solutions Architect
- [Jose Andrade](https://www.linkedin.com/in/jmandrade) \| Customer Engineer, SRE Specialist
- [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) \| Cross-Product Solution Developer
- [Laura Hyatt](https://www.linkedin.com/in/laura-hyatt) \| Customer Engineer, FSI
- [Michael Yang](https://www.linkedin.com/in/chengxiyang) \| Industry Solutions AI Consulting Lead, FSI
- [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) \| Customer Engineer, Application Modernization Specialist
- [Omar Saenz](https://www.linkedin.com/in/omarsaenz) \| EMEA Partner Engineer, Security
- [Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) \| Program Lead, Google Cloud Well-Architected Framework
- [Steve McGhee](https://www.linkedin.com/in/stevemcghee) \| Reliability Advocate
- [Tarun Sharma](https://www.linkedin.com/in/tarun27in) \| Principal Architect
- Yuriy Babenko \| Customer Engineer, FSI

<br />

<br />

<br />


# Financial services perspective: Operational excellence

This document in the
[Google Cloud Well-Architected Framework: Financial services (FS) perspective](https://docs.cloud.google.com/architecture/framework/perspectives/fsi)
provides an overview of the principles and recommendations to build, deploy, and
operate robust FS workloads in Google Cloud. These recommendations help you set
up foundational elements like observability, automation, and scalability. The
recommendations in this document align with the
[operational excellence pillar](https://docs.cloud.google.com/architecture/framework/operational-excellence)
of the Well-Architected Framework.

Operational excellence is critical for FS workloads in Google Cloud due to the
highly regulated and sensitive nature of such workloads. Operational excellence
ensures that cloud solutions can adapt to evolving needs *and* meet your
requirements for value, performance, security, and reliability. Failures in
these areas could result in significant financial losses, regulatory penalties,
and reputational damage.

Operational excellence provides the following benefits for FS workloads:

- **Maintain trust and reputation**: Financial institutions rely heavily on their customers' trust. Operational disruptions or security breaches can severely erode this trust and cause customer attrition. Operational excellence helps to minimize these risks.
- **Meet stringent regulatory compliance requirements**: Financial services are
  subject to numerous and complex regulations, such as the following:

  - [EU General Data Protection Regulation (GDPR)](https://gdpr-info.eu/art-1-gdpr/)
  - [EU Digital Operational Resilience Act (DORA)](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en)
  - [California Consumer Privacy Act (CCPA)](https://oag.ca.gov/privacy/ccpa)
  - Industry-specific regulations

  Robust operational processes, monitoring, and incident management are
  essential for demonstrating compliance with regulations and avoiding
  penalties.
- **Ensure business continuity and resilience** : Financial markets and
  services often operate continuously. Therefore, high availability and
  effective disaster recovery are paramount. Operational excellence
  principles guide the design and implementation of resilient systems. The
  [reliability pillar](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/reliability)
  provides more guidance in this area.

- **Protect sensitive data** : Financial institutions handle vast amounts
  of highly sensitive customer and financial data. Strong operational
  controls, security monitoring, and rapid incident response are crucial in
  order to prevent data breaches and maintain privacy. The
  [security pillar](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/security)
  provides more guidance in this area.

- **Optimize performance for critical applications** : Many financial
  applications, such as trading platforms and real-time analytics, demand
  high performance and low latency. To meet these performance requirements,
  you need highly optimized compute, networking, and storage design. The
  [performance optimization pillar](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/performance-optimization)
  provides more guidance in this area.

- **Manage costs effectively** : In addition to security and reliability,
  financial institutions are also concerned with cost efficiency. Operational
  excellence includes practices for optimizing resource utilization and
  managing cloud spending. The
  [cost optimization pillar](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/cost-optimization)
  provides more guidance in this area.

The operational excellence recommendations in this document are mapped to the
following core principles:

- [Define SLAs and corresponding SLOs and SLIs](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#define-sla-slo-sli)
- [Define and test incident management processes](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#incident-management)
- [Continuously improve and innovate](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#improve-innovate)

## Define SLAs and corresponding SLOs and SLIs

Across many FS organizations, the availability of applications is typically
classified based on
[recovery time objective (RTO) and recovery point objective (RPO)](https://docs.cloud.google.com/architecture/dr-scenarios-planning-guide#basics_of_dr_planning)
metrics. For business-critical applications that serve external customers, a
service level agreement (SLA) might also be defined.

SLAs need a framework of metrics that represents the behavior of the system from
the user-satisfaction perspective.
[Site reliability engineering (SRE)](https://sre.google/sre-book/table-of-contents/)
practices offer a way to achieve the level of system reliability that you want.
Creating a framework of metrics involves defining and monitoring key numerical
indicators to understand system health from the user's perspective. For example,
metrics like latency and error rates quantify how well a service is performing.
These metrics are called service level indicators (SLIs). Developing effective
SLIs is crucial, because they provide the raw data that's necessary to
objectively assess reliability.

To define meaningful SLAs, SLIs, and SLOs, consider the following
recommendations:

- Develop and define SLIs for each critical service. Set target values that define the acceptable performance levels.
- Develop and define the service level objectives (SLO) that correspond to the SLIs. For example, an SLO might state that 99.9% of requests must have a latency that's less than 200 milliseconds.
- Identify the internal remedial actions that must be taken if a service doesn't meet the SLOs. For example, to improve the resilience of the platform, you might need to focus development resources on fixing issues.
- Validate the SLA requirement for each service and recognize the SLA as the formal contract with the service users.

### Examples of service levels

The following table provides examples of SLIs, SLOs, and SLAs for a payment
platform:

| **Business metric** | **SLI** | **SLO** | **SLA** |
|---|---|---|---|
| Payment transaction success | A quantitative measure of the percentage of all initiated payment transactions that are successfully processed and confirmed. **Example**: (number of successful transactions ÷ total number of valid transactions) × 100, measured over a rolling 5-minute window. | An internal target to maintain a high percentage of successful payment transactions over a specific period. **Example**: Maintain a 99.98% payment transaction success rate over a rolling 30-day window, excluding invalid requests and planned maintenance. | A contractual guarantee for the success rate and speed of payment transaction processing. **Example**: The service provider guarantees that 99.0% of payment transactions initiated by the client will be successfully processed and confirmed within one second. |
| Payment processing latency | The average time taken for a payment transaction to be processed from initiation by the client to final confirmation. **Example**: Average response time in milliseconds for transaction confirmation, measured over a rolling 5-minute window. | An internal target for the speed at which payment transactions are processed. **Example**: Ensure that 99.5% of payment transactions are processed within 400 milliseconds over a rolling 30-day window. | A contractual commitment to resolve critical payment processing issues within a specified timeframe. **Example**: For critical payment processing issues (defined as an outage that affects more than 1% of transactions), the service provider commits to a resolution time of within two hours from the time when the issue is reported or detected. |
| Platform availability | The percentage of time when the core payment processing API and user interface are operational and accessible to clients. **Example**: (total operational time − downtime) ÷ total operational time × 100, measured per minute. | An internal target for the uptime of the core payment platform. **Example**: Achieve 99.995% platform availability per calendar month, excluding scheduled maintenance windows. | A formal, legally binding commitment to clients regarding the minimum uptime of the payment platform, including consequences for failure to meet. **Example**: The platform will maintain a minimum of 99.9% availability per calendar month, excluding scheduled maintenance windows. If the availability falls below the minimum level, the client will receive a service credit of 5% of the monthly service fee for each 0.1% drop. |

Use SLI data to monitor whether systems are within the defined SLOs and to
ensure that the SLAs are met. By using a set of well-defined SLIs, engineers and
developers can monitor FS applications at the following levels:

- Directly within the service that the applications are deployed on, such as GKE or Cloud Run.
- By using logs that are provided by infrastructure components, such as the load balancer.

[OpenTelemetry](https://cloud.google.com/learn/what-is-opentelemetry)
provides an open source standard and a set of technologies to capture all types
of telemetry including metrics, traces, and logs.
[Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus)
provides a fully-managed, highly scalable backend for metrics and operation of
Prometheus at scale.

For more information about SLI, SLO, and error budgets, see the
[SRE handbook](https://sre.google/sre-book/service-level-objectives).

To develop effective alerting and monitoring dashboards and mechanisms, use
[Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs)
tools together with
[Google Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).
For information about security-specific monitoring and detection capabilities,
see the
[security pillar](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/security).

## Define and test incident management processes

Well-defined and regularly tested incident management processes contribute
directly to the value, performance, security, and reliability of the FS
workloads in Google Cloud. These processes help financial institutions
meet their stringent regulatory requirements, protect sensitive data, maintain
business continuity, and uphold customer trust.

Regular testing of incident management processes provides the following
benefits:

- **Maintain performance under peak loads**: Regular performance and load testing help financial institutions ensure that their cloud-based applications and infrastructure can handle peak transaction volumes, market volatility, and other high-demand scenarios without performance degradation. This capability is crucial for maintaining a seamless user experience and meeting the demands of financial markets.
- **Identify potential bottlenecks and limitations**: Stress testing pushes systems to their limits, and it enables financial institutions to identify potential bottlenecks and performance limitations before they affect critical operations. This proactive approach enables financial institutions to adjust their infrastructure and applications for optimal performance and scalability.
- **Validate reliability and resilience** : Regular testing, including [chaos engineering](https://cloud.google.com/blog/products/databases/chaos-testing-spanner-improves-reiliability?e=48754805) or simulated failures, helps to validate the reliability and resilience of financial systems. This testing ensures that the systems can recover gracefully from failures and maintain high availability, which is essential for business continuity.
- **Perform [effective capacity planning](https://static.googleusercontent.com/media/sre.google/en//static/pdf/login_winter20_10_torres.pdf)**: Performance testing provides valuable data on resource utilization under different load conditions, which is crucial for accurate capacity planning. Financial institutions can use this data to proactively anticipate future capacity needs and to avoid performance issues due to resource constraints.
- **Deploy new features and code changes successfully**: Integrating automated testing into CI/CD pipelines helps to ensure that changes and new deployments are thoroughly validated before they're released into production environments. This approach significantly reduces the risk of errors and regressions that could lead to operational disruptions.
- **Meet regulatory requirements for system stability**: Financial regulations often require institutions to have robust testing practices to ensure the stability and reliability of their critical systems. Regular testing helps to demonstrate compliance with these requirements.

To define and test your incident management processes, consider the following
recommendations.

### Establish clear incident response procedures

A well-established set of
[incident response procedures](https://sre.google/resources/practices-and-processes/incident-management-guide/)
involves the following elements:

- Roles and responsibilities that are defined for incident commanders, investigators, communicators, and technical experts to ensure effective and coordinated response.
- Communication protocols and escalation paths that are defined to ensure that information is shared promptly and effectively during incidents.
- Procedures that are documented in a runbook or playbook that outlines the steps for communication, triage, investigation, and resolution.
- Regular training and preparation that equips teams with the knowledge and skills to respond effectively.

### Implement performance and load testing regularly

Regular
[performance and load testing](https://sre.google/sre-book/testing-reliability/)
helps to ensure that cloud-based applications and infrastructure can handle peak
loads and maintain optimal performance. Load testing simulates realistic traffic
patterns. Stress testing exercises the system to its limits to identify
potential bottlenecks and performance limitations. You can use products like
[Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)
and load testing services to simulate real-world traffic. Based on the test
results, you can adjust your cloud infrastructure and applications for optimal
performance and scalability. For example, you can adjust resource allocation or
tune application configurations.

### Automate testing within CI/CD pipelines

Incorporating automated testing into your CI/CD pipelines helps to ensure the
quality and reliability of cloud applications by validating changes before
deployment. This approach significantly reduces the risk of errors and
regressions and it helps you to build a more stable and robust software system.
You can incorporate different types of testing in your CI/CD pipelines,
including unit testing, integration testing, and end-to-end testing. Use
products like
[Cloud Build](https://docs.cloud.google.com/build/docs/overview)
and
[Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview)
to create and manage your CI/CD pipelines.

## Continuously improve and innovate

For financial services workloads in the cloud, migrating to the cloud is merely
the initial step. Ongoing enhancement and innovation are essential for the
following reasons:

- **Accelerate innovation**: Take advantage of new technologies like AI to improve your services.
- **Reduce costs**: Eliminate inefficiencies and optimize resource use.
- **Enhance agility**: Adapt to market and regulatory changes quickly.
- **Improve decision making**: Use data analytics products like BigQuery and Looker to make informed choices.

To ensure continuous improvement and innovation, consider the following
recommendations.

### Conduct regular retrospectives

[Retrospectives](https://sre.google/sre-book/postmortem-culture/)
are vital for continuously improving incident response procedures, and for
optimizing testing strategies based on the outcomes of regular performance and
load testing. To ensure that retrospectives are effective, do the following:

- Give teams an opportunity to reflect on their experiences, identify what went well, and pinpoint areas for improvement.
- Hold retrospectives after project milestones, major incidents, or significant testing cycles. Teams can learn from both successes and failures and continuously refine their processes and practices.
- Use a structured approach like the [start-stop-continue](https://docs.cloud.google.com/architecture/framework/operational-excellence/continuously-improve-and-innovate#conduct_regular_retrospectives) model to ensure that the retrospective sessions are productive and lead to actionable steps.
- Use retrospectives to identify areas where automation of change management can be further enhanced to improve reliability and reduce risks.

### Foster a culture of learning

A culture of learning facilitates safe exploration of new technologies in
Google Cloud, such as AI and ML capabilities to enhance services like fraud
detection and personalized financial advice. To promote a culture of learning,
do the following:

- Encourage teams to experiment, share knowledge, and learn continuously.
- Adopt a blameless culture, where failures are viewed as opportunities for growth and improvement.
- Create a psychologically safe environment that lets teams take risks and consider innovative solutions. Teams learn from both successes and failures, which leads to a more resilient and adaptable organization.
- Develop a culture that facilitates sharing of knowledge gained from incident management processes and testing exercises.

### Stay up-to-date with cloud technologies

Continuous learning is essential for understanding and implementing new
security measures, leveraging advanced data analytics for better insights, and
adopting innovative solutions that are relevant to financial services.

- Maximize the potential of Google Cloud services by staying informed about the latest advancements, features, and best practices.
- When new Google Cloud features and services are introduced, identify opportunities to further automate processes, enhance security, and improve the performance and scalability of your applications.
- Participate in relevant conferences, webinars, and training sessions to expand your knowledge and understand new capabilities.
- Encourage team members to obtain [Google Cloud certifications](https://cloud.google.com/learn/certification) to help ensure that the organization has the necessary skills for success in the cloud.

<br />

<br />


# Financial services perspective: Security, privacy, and compliance

This document in the
[Google Cloud Well-Architected Framework: Financial services (FS) perspective](https://docs.cloud.google.com/architecture/framework/perspectives/fsi)
provides an overview of the principles and recommendations to address the
security, privacy, and compliance requirements of financial services (FS)
workloads in Google Cloud. The recommendations help you build resilient
and compliant infrastructure, safeguard sensitive data, maintain customer trust,
navigate the complex landscape of regulatory requirements, and effectively
manage cyber threats. The recommendations in this document align with the
[security pillar](https://docs.cloud.google.com/architecture/framework/security)
of the Well-Architected Framework.

Security in cloud computing is a critical concern for FS organizations, which
are highly attractive to cybercriminals due to the vast amounts of sensitive
data that they manage, including customer details and financial records. The
consequences of a security breach are exceptionally severe, including
significant financial losses, long-term reputational damage, and significant
regulatory fines. Therefore, FS workloads need stringent security controls.

To help ensure comprehensive security and compliance, you need to understand the
[shared responsibilities](https://docs.cloud.google.com/architecture/framework/security/shared-responsibility-shared-fate)
between you (FS organizations) and Google Cloud. Google Cloud is
responsible for securing the underlying infrastructure, including physical
security and network security. You are responsible for securing data and
applications, configuring access control, and configuring and managing security
services. To support you in your security efforts, the
[Google Cloud partner ecosystem](https://cloud.google.com/find-a-partner/?specializations=Security+-+Services)
offers security integration and managed services.

The security recommendations in this document are mapped to the following core
principles:

- [Implement security by design](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#security-by-design)
- [Implement zero trust](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#zero-trust)
- [Implement shift-left security](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#shift-left)
- [Implement preemptive cyber defense](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#preemptive-cyber-defense)
- [Use AI securely and responsibly, and use AI for security](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#ai)
- [Meet regulatory, compliance, and privacy needs](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#regulatory-compliance)
- [Prioritize security initiatives](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#prioritize-security)

## Implement security by design

Financial regulations like the
[Payment Card Industry Data Security Standard (PCI DSS)](https://www.pcisecuritystandards.org/standards/pci-dss/),
the
[Gramm-Leach-Bliley Act (GLBA)](https://www.ftc.gov/business-guidance/privacy-security/gramm-leach-bliley-act)
in the United States, and various national financial data protection laws
mandate that security is integrated into systems from the outset. The
security-by-design principle emphasizes the integration of security throughout
the development lifecycle to help ensure that vulnerabilities are minimized from
the outset.

To apply the security-by-design principle for your FS workloads in
Google Cloud, consider the following recommendations:

- Ensure that only necessary permissions are granted by applying the principle of least privilege through granular role-based access control (RBAC) in [Identity and Access Management (IAM)](https://cloud.google.com/security/products/iam). The use of RBAC is a key requirement in many financial regulations.
- Enforce security perimeters around your sensitive services and data within Google Cloud by using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). The security perimeters help to segment and protect sensitive data and resources, and help to prevent data exfiltration and unauthorized access, as required by regulations.
- Define security configurations as code by using infrastructure as code (IaC) tools like [Terraform](https://docs.cloud.google.com/docs/terraform/terraform-overview). This approach embeds security controls from the initial deployment phase, which helps to ensure consistency and auditability.
- Scan your application code by integrating [Static Application Security Testing (SAST)](https://en.wikipedia.org/wiki/Static_application_security_testing) into the CI/CD pipeline with [Cloud Build](https://docs.cloud.google.com/build/docs/overview). Establish automated security gates to prevent the deployment of non-compliant code.
- Provide a unified interface for security insights by using [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview). The use of Security Command Center enables continuous monitoring and early detection of misconfigurations or threats that could lead to regulatory breaches. To meet the requirements of standards such as [ISO 27001](https://docs.cloud.google.com/security-command-center/docs/security-posture-iso-27001-template) and [NIST 800-53](https://docs.cloud.google.com/security-command-center/docs/security-posture-nist-800-53-template), you can use [posture management](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview) templates.
- Track the reduction in vulnerabilities that are identified in production deployments and the percentage of IaC deployments that adhere to security best practices. You can detect and view vulnerabilities and information about compliance to security standards by using Security Command Center. For more information, see [Vulnerability findings](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).

## Implement zero trust

Modern financial regulations increasingly emphasize the need for stringent
access controls and continuous verification. These requirements reflect the
principle of zero trust, which aims to protect workloads against both internal
and external threats and bad actors. The zero-trust principle advocates for
continuous verification of every user and device, which eliminates implicit
trust and mitigates
[lateral movement](https://en.wikipedia.org/wiki/Lateral_movement_(cybersecurity)).

To implement zero trust, consider the following recommendations:

- Enable context-aware access based on user identity, device security, location, and other factors by combining [IAM](https://cloud.google.com/security/products/iam) controls with [Chrome Enterprise Premium](https://cloud.google.com/chrome-enterprise-premium/docs/overview). This approach ensures continuous verification before access to financial data and systems is granted.
- Provide secure and scalable identity and access management by configuring [Identity Platform](https://cloud.google.com/security/products/identity-platform) (or your external identity provider if you use [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation)). Set up multi-factor authentication (MFA) and other controls that are crucial to implement zero trust and help ensure regulatory compliance.
- Implement MFA for all user accounts, especially for accounts with access to sensitive data or systems.
- Support audits and investigations related to regulatory compliance by establishing comprehensive logging and monitoring of user access and network activity.
- Enable private and secure communication between services within Google Cloud and on-premises environments without exposing the traffic to the public internet by using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect).
- Implement granular identity controls and authorize access at the application level by using [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) rather than relying on network-based security mechanisms like VPN tunnels. This approach helps to reduce lateral movement within the environment.

## Implement shift-left security

Financial regulators encourage proactive security measures. Identifying and
addressing vulnerabilities early in the development lifecycle helps to reduce
the risk of security incidents and the potential for non-compliance penalties.
The principle of shift-left security promotes early security testing and
integration, which helps to reduce the cost and complexity of remediation.

To implement shift-left security, consider the following recommendations:

- Ensure automated security checks early in the development process by
  integrating security scanning tools, such as container vulnerability
  scanning and static code analysis, into the CI/CD pipeline with
  [Cloud Build](https://docs.cloud.google.com/build/docs/overview).

- Ensure that only secure artifacts are deployed by using
  [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview)
  to provide a secure and centralized repository for software packages and
  container images with integrated vulnerability scanning. Use virtual
  repositories to mitigate
  [dependency confusion attacks](https://docs.cloud.google.com/software-supply-chain-security/docs/dependencies#public-dependencies)
  by prioritizing your private artifacts over remote repositories.

- Automatically scan web applications for common vulnerabilities by
  integrating
  [Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview),
  which is a part of
  [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview),
  into your development pipelines.

- Implement security checks for the source code, build process, and code
  provenance by using the
  [Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev/)
  framework. Enforce the provenance of the workloads that run in your
  environments by using solutions such as
  [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview).
  Ensure that your workloads use only verified open-source software libraries
  by using
  [Assured Open Source](https://docs.cloud.google.com/assured-open-source-software/docs/overview).

- Track the number of vulnerabilities that are identified and remediated
  in your development lifecycle, the percentage of code deployments that pass
  security scans, and the reduction in security incidents caused by software
  vulnerabilities. Google Cloud provides tools to help with this tracking for
  different kinds of workloads. For example, for containerized workloads, use
  the
  [container scanning feature of Artifact Registry](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview).

## Implement preemptive cyber defense

Financial institutions are prime targets for sophisticated cyberattacks.
Regulations often require robust threat intelligence and proactive defense
mechanisms. Preemptive cyber defense focuses on proactive threat detection and
response by using advanced analytics and automation.

Consider the following recommendations:

- Proactively identify and mitigate potential threats, by using the [threat intelligence](https://cloud.google.com/security/products/threat-intelligence), [incident response](https://cloud.google.com/security/consulting/mandiant-incident-response-services), and [security validation](https://cloud.google.com/security/products/mandiant-security-validation) services of [Mandiant](https://cloud.google.com/security/mandiant).
- Protect web applications and APIs from web exploits and DDoS attacks at the network edge by using [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview).
- Aggregate and prioritize security findings and recommendations by using [Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview), which enables security teams to proactively address potential risks.
- Validate preemptive defenses and incident response plans by conducting regular security simulations and penetration testing.
- Measure the time to detect and respond to security incidents, the effectiveness of DDoS mitigation efforts, and the number of prevented cyberattacks. You can get the required metrics and data from [Google Security Operations SOAR and SIEM dashboards](https://docs.cloud.google.com/chronicle/docs/secops/understand-the-secops-platform#siem-dashboards-and-soar-dashboards).

## Use AI securely and responsibly, and use AI for security

AI and ML are increasingly used for financial services use cases such as fraud
detection and algorithmic trading. Regulations require that these technologies
be used ethically, transparently, and securely. AI can also help to enhance your
security capabilities. Consider the following recommendations for using AI:

- Develop and deploy ML models in a secure and governed environment by using [Vertex AI](https://docs.cloud.google.com/vertex-ai). Features like model explainability and fairness metrics can help to address responsible-AI concerns.
- Leverage the security analytics and operations capabilities of [Google Security Operations](https://cloud.google.com/security/products/security-operations), which uses AI and ML to analyze large volumes of security data, detect anomalies, and automate threat response. These capabilities help to enhance your overall security posture and aid in compliance monitoring.
- Establish clear governance policies for AI and ML development and deployment, including security and ethics-related considerations.
- Align with the elements of the [Secure AI Framework (SAIF)](https://developers.google.com/machine-learning/resources/saif), which provides a practical approach to address the security and risk concerns of AI systems.
- Track the accuracy and effectiveness of AI-powered fraud detection systems, the reduction in false positives in security alerts, and the efficiency gains from AI-driven security automation.

## Meet regulatory, compliance, and privacy needs

Financial services are subject to a vast array of regulations, including data
residency requirements, specific audit trails, and data protection standards. To
ensure that sensitive data is properly identified, protected, and managed, FS
organizations need robust data governance policies and data classification
schemes. Consider the following recommendations to help you meet regulatory
requirements:

- Set up data boundaries in Google Cloud for sensitive and regulated workloads by using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview). Doing so helps you to meet government and industry-specific compliance requirements such as [FedRAMP](https://www.fedramp.gov/) and [CJIS](https://www.fbi.gov/services/cjis).
- Identify, classify, and protect sensitive data, including financial information, by implementing [Cloud Data Loss Prevention (Cloud DLP)](https://cloud.google.com/security/products/dlp). Doing so helps you to meet data privacy regulations like [GDPR](https://gdpr-info.eu/) and [CCPA](https://oag.ca.gov/privacy/ccpa).
- Track details of administrative activities and access to resources by using [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit). These logs are crucial for meeting audit requirements that are stipulated by many financial regulations.
- When you choose [Google Cloud regions](https://docs.cloud.google.com/compute/docs/regions-zones) for your workloads and data, consider local regulations that are related to data residency. Google Cloud global infrastructure lets you choose regions that can help you to meet your data residency requirements.
- Manage the keys that are used to encrypt sensitive financial data at rest and in transit by using [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service). Such encryption is a fundamental requirement of many security and privacy regulations.
- Implement the controls that are necessary to address your regulatory requirements. Validate that the controls work as expected. Get the controls validated again by an external auditor to prove to the regulator that your workloads are compliant with the regulations.

## Prioritize security initiatives

Given the breadth of security requirements, financial institutions must
prioritize initiatives that are based on risk assessment and regulatory
mandates. We recommend the following phased approach:

1. **Establish a strong security foundation**: Focus on the core areas of security, including identity and access management, network security, and data protection. This focus helps to build a robust security posture and helps to ensure comprehensive defense against evolving threats.
2. **Address critical regulations**: Prioritize compliance with key regulations like PCI DSS, GDPR, and relevant national laws. Doing so helps to ensure data protection, mitigates legal risks, and builds trust with customers.
3. **Implement advanced security**: Gradually adopt advanced security practices like zero trust, AI-driven security solutions, and proactive threat hunting.

<br />

<br />


# Financial services perspective: Reliability

This document in the
[Google Cloud Well-Architected Framework: Financial services (FS) perspective](https://docs.cloud.google.com/architecture/framework/perspectives/fsi)
provides an overview of the principles and recommendations to design, deploy,
and operate reliable FS workloads in Google Cloud. The document explores how to
integrate advanced reliability practices and observability into your
architectural blueprints. The recommendations in this document align with the
[reliability pillar](https://docs.cloud.google.com/architecture/framework/reliability)
of the Well-Architected Framework.

For financial institutions, reliable and resilient infrastructure is both a
business need and a regulatory imperative. To ensure that FS workloads in
Google Cloud are reliable, you must understand and mitigate potential failure
points, deploy resources redundantly, and plan for recovery. Operational
resilience is an outcome of reliability. It's the ability to absorb, adapt to,
and recover from disruptions. Operational resilience helps FS organizations
meet strict regulatory requirements. It also helps avoid
[intolerable harm](https://blog.bcm-institute.org/operational-resilience/categorizing-level-of-harm-for-impact-tolerance#:%7E:text=Intolerable%20harm%20is%20%22harm%22%20that,organization%20providing%20critical%20business%20services.)
to customers.

The key
[building blocks of reliability](https://docs.cloud.google.com/architecture/infra-reliability-guide/building-blocks)
in Google Cloud are regions, zones, and the various location scopes of cloud
resources: zonal, regional, multi-regional, global. You can improve availability
by using managed services, distributing resources, implementing
high-availability patterns, and automating processes.

## Regulatory requirements

FS organizations operate under strict reliability mandates by regulatory
agencies such as the
[Federal Reserve System](https://www.federalreserve.gov/aboutthefed.htm)
in the US, the
[European Banking Authority](https://www.eba.europa.eu/homepage)
in the EU, and the
[Prudential Regulation Authority](https://www.bankofengland.co.uk/explainers/what-is-the-prudential-regulation-authority-pra)
in the UK. Globally, regulators emphasize operational resilience, which is vital
for financial stability and consumer protection. Operational resilience is the
ability to withstand disruptions, recover effectively, and maintain critical
services. This requires a harmonized approach for managing technological risks
and dependencies on third parties.

The regulatory requirements across most jurisdictions have the following common
themes:

- **Cybersecurity and technological resilience**: Strengthening defenses against cyber threats and ensuring the resilience of IT systems.
- **Third-party risk management**: Managing the risks associated with outsourcing services to providers of information and communication technology (ICT).
- **Business continuity and incident response**: Robust planning to maintain critical operations during disruptions and to recover effectively.
- **Protecting financial stability**: Ensuring the soundness and stability of the broader financial system.

The reliability recommendations in this document are mapped to the following
core principles:

- [Prioritize multi-zone and multi-region deployments](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#multi-zone-multi-region)
- [Eliminate single points of failure (SPOFs)](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#eliminate-spofs)
- [Understand and manage aggregate availability](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#manage-availability)
- [Implement a robust DR strategy](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#dr-strategy)
- [Leverage managed services](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#managed-services)
- [Automate the infrastructure provisioning and recovery processes](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#automate)

## Prioritize multi-zone and multi-region deployments

For critical financial services applications, we recommend that you use a
multi-region topology that's distributed across at least two regions and across
three zones within each region. This approach is important for resilience
against zone and region outages. Regulations often prescribe this approach,
because if a failure occurs in one zone or region, most jurisdictions consider a
severe disruption to a second zone to be a plausible consequence. The rationale
is that when one location fails, the other location might receive an
exceptionally high amount of additional traffic.

Consider the following recommendations to build resilience against zone and
region outages:

- Prefer resources that have a wider locational scope. Where possible, use regional resources instead of zonal resources, and use multi-regional or global resources instead of regional resources. This approach helps to avoid the need to restore operations by using backups.
- In each region, leverage three zones rather than two. To handle failovers, overprovision capacity by a third more than the estimate.
- Minimize manual recovery steps by implementing active-active deployments like the following examples:
  - Distributed databases like Spanner provide built-in redundancy and synchronisation across regions.
  - The [HA feature](https://docs.cloud.google.com/sql/docs/postgres/configure-ha) of Cloud SQL provides a topology that's near active-active, with read replicas across zones. It provides a recovery point objective (RPO) between regions that's close to 0.
- Distribute user traffic across regions by using Cloud DNS, and deploy a [regional load balancer](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#multi-region-deployment-with-regional-load-balancing) in each region. A global load balancer is another option that you can consider depending on your requirements and criticality. For more information, see [Benefits and risks of global load balancing for multi-region deployments](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#benefits-and-risks-of-global-load-balancing-for-multi-region-deployments).
- To store data, use multi-region services like [Spanner](https://docs.cloud.google.com/spanner/docs) and [Cloud Storage](https://docs.cloud.google.com/storage/docs/locations).

## Eliminate single points of failure

Distribute resources across different locations and use redundant resources to
prevent any single point of failure (SPOF) from affecting the entire application
stack.

Consider the following recommendations to avoid SPOFs:

- Avoid deploying just a single application server or database.
- Ensure automatic recreation of failed VMs by using [managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups).
- Distribute traffic evenly across the available resources by implementing [load balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview).
- Use HA configurations for databases such as [Cloud SQL](https://docs.cloud.google.com/sql/docs/availability).
- Improve data availability by using [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk) with synchronous replication.

For more information, see
[Design reliable infrastructure for your workloads in Google Cloud](https://docs.cloud.google.com/architecture/infra-reliability-guide/design#avoid_single_points_of_failure).

## Understand and manage aggregate availability

Be aware that the overall or *aggregate* availability of a system is affected
by the availability of each tier or component of the system. The number of tiers
in an application stack has an inverse relationship with the aggregate
availability of the stack. Consider the following recommendations for managing
aggregate availability:

- Calculate the aggregate availability of a multi-tier stack by using the
  formula *tier1_availability × tier2_availability ×
  tierN_availability*.

  The following diagram shows the calculation of aggregate availability
  for a multi-tier system that consists of four services:

  ![The aggregate availability formula for a multi-tier service that has four services.](https://docs.cloud.google.com/static/architecture/framework/perspectives/fsi/images/gcwaf-fsi-reliability-aggregate-availability.svg)

  In the preceding diagram, the service in each tier provides 99.9%
  availability, but the aggregate availability of the system is lower at
  99.6% (0.999 × 0.999 × 0.999 × 0.999). In general, the
  aggregate availability of a multi-tier stack is lower than the availability
  of the tier that provides the least availability.
- Where feasible, choose *parallelization* over *chaining*. With
  parallelized services, the end-to-end availability is higher than the
  availability of each individual service.

  The following diagram shows two services, A and B, that are deployed by
  using the chaining and parallelization approaches:

  ![The aggregate availability formulas for chained services compared to parallelized services.](https://docs.cloud.google.com/static/architecture/framework/perspectives/fsi/images/gcwaf-fsi-reliability-chained-vs-parallelized.svg)

  In the preceding examples, both services have an SLA of 99%, which
  results in the following aggregate availability depending on the
  implementation approach:
  - **Chained services** yield an aggregate availability of only 98% (.99 × .99).
  - **Parallelized services** yield a higher aggregate availability at 99.99% because each service runs independently and individual services aren't affected by the availability of the other services. The formula for aggregated parallelized services is *1 − (1 −
    A) × (1 − B)*.
- Choose Google Cloud services with uptime SLAs that can help meet the
  required level of overall uptime for your application stack.

- When you design your architecture, consider the trade-offs between
  availability, operational complexity, latency, and cost. Increasing the
  number of nines of availability generally costs more, but doing so helps
  you meet regulatory requirements.

  For example, 99.9% availability (three nines) means a potential downtime
  of 86 seconds in a 24-hour day. In contrast, 99% (two nines) means a
  downtime of 864 seconds over the same period, which is 10 times more
  downtime than with three nines of availability.

  For critical financial services, the architecture options might be
  limited. However, it's critical to identify the availability requirements
  and accurately calculate availability. Performing such an assessment helps
  you to assess the implications of your design decisions on your
  architecture and budget.

## Implement a robust DR strategy

Create well-defined plans for different disaster scenarios, including zonal and
regional outages. A well-defined disaster recovery (DR) strategy lets you
recover from a disruption and resume normal operations with minimal impact.

DR and high availability (HA) are different concepts. With cloud deployments,
in general, DR applies to multi-region deployments and HA applies to regional
deployments. These
[deployment archetypes](https://docs.cloud.google.com/architecture/deployment-archetypes)
support different replication mechanisms.

- **HA**: Many managed services provide synchronous replication between zones within a single region by default. Such services support a zero or near-zero recovery time objective (RTO) and recovery point objective (RPO). This support lets you create an active-active deployment topology that doesn't have any SPOF.
- **DR**: For workloads that are deployed across two or more regions, if you don't use multi-regional or global services, you must define a replication strategy. The replication strategy is typically asynchronous. Carefully assess how such replication affects the RTO and RPO for critical applications. Identify the manual or semi-automated operations that are necessary for failover.

For financial institutions, your choice of failover region might be limited by
regulations about data sovereignty and data residency. If you need an
active-active topology across two regions, we recommend that you choose managed
multi-regional services, like Spanner and Cloud Storage, especially when data
replication is critical.

Consider the following recommendations:

- Use managed multi-regional storage services for data.
- Take snapshots of data in persistent disks and store the snapshots in [multi-region locations](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings#storage_location_options).
- When you use regional or zonal resources, set up data replication to other regions.
- Validate that your DR plans are effective by testing the plan regularly.
- Be aware of the RTO and RPO and their correlation to the impact tolerance that's stipulated by financial regulations in your jurisdiction.

For more information, see
[Architecting disaster recovery for cloud infrastructure outages](https://docs.cloud.google.com/architecture/disaster-recovery).

## Leverage managed services

Whenever possible, use managed services to take advantage of the built-in
features for backups, HA, and scalability. Consider the following
recommendations for using managed services:

- Use managed services in Google Cloud. They provide HA that's backed by SLAs. They also offer built-in backup mechanisms and resilience features.
- For data management, consider services like [Cloud SQL](https://docs.cloud.google.com/sql/docs/availability), [Cloud Storage](https://docs.cloud.google.com/storage/docs/locations), and [Spanner](https://docs.cloud.google.com/spanner/docs),
- For compute and application hosting, consider [Compute Engine managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups) and [Google Kubernetes Engine (GKE) clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture). Regional MIGs and GKE regional clusters are resilient to zone outages.
- To improve resilience against region outages, use managed multi-regional services.
- Identify the need for *exit plans* for services that have unique characteristics and define the required plans. Financial regulators like the FCA, PRA, and EBA require firms to have strategies and contingency plans for data retrieval and operational continuity if the relationship with a cloud provider ends. Firms must assess the exit feasibility before entering into cloud contracts and they must maintain the ability to change providers without operational disruption.
- Verify that the services that you choose support exporting data to an open format like CSV, Parquet, and Avro. Verify whether the services are based on open technologies, like GKE support for the [Open Container Initiative (OCI) format](https://docs.cloud.google.com/artifact-registry/docs/supported-formats#oci) or [Managed Service for Apache Airflow built on Apache Airflow](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview).

## Automate the infrastructure provisioning and recovery processes

Automation helps to minimize human errors and helps to reduce the time and
resources that are necessary to respond to incidents. The use of automation can
help to ensure faster recovery from failures and more consistent results.
Consider the following recommendations to automate how you provision and recover
resources:

- Minimize human errors by using infrastructure as code (IaC) tools like Terraform.
- Reduce manual intervention by automating failover processes. Automated responses can also help to reduce the impact of failures. For example, you can use [Eventarc](https://docs.cloud.google.com/eventarc/docs) or [Workflows](https://docs.cloud.google.com/workflows/docs/overview) to automatically trigger remedial actions in response to issues observed through audit logs.
- Increase the capacity of your cloud resources during failover by using autoscaling.
- Automatically apply policies and guardrails for regulatory requirements across your cloud topology during service deployment by adopting [platform engineering](https://github.com/GoogleCloudPlatform/platform-engineering).

<br />

<br />


# Financial services perspective: Cost optimization

This document in the
[Google Cloud Well-Architected Framework: Financial services (FS) perspective](https://docs.cloud.google.com/architecture/framework/perspectives/fsi)
provides an overview of principles and recommendations to optimize the cost of
your FS workloads in Google Cloud. The recommendations in this document align
with the
[cost optimization pillar](https://docs.cloud.google.com/architecture/framework/cost-optimization)
of the Well-Architected Framework.

Robust cost optimization for financial services workloads requires the following
fundamental elements:

- The ability to identify wasteful versus value-driving resource utilization.
- An embedded culture of financial accountability.

To optimize cost, you need a comprehensive understanding of the cost drivers
and resource needs across your organization. In some large organizations,
especially those that are early in the cloud journey, a single team is often
responsible for optimizing spend across a large number of domains. This approach
assumes that a central team is best placed to identify high-value opportunities
to improve efficiency.

The centralized approach might yield some success during
the initial stages of cloud adoption or for non-critical workloads. However, a
single team can't drive cost optimization across an entire organization. When
the resource usage or the level of regulatory scrutiny increases, the
centralized approach isn't sustainable. Centralized teams face scalability
challenges particularly when dealing with a large number of financial products
and services. The project teams that own the products and services might resist
changes that are made by an external team.

For effective cost optimization, spend-related data must be highly visible, and
engineers and other cloud users who are close to the workloads must be motivated
to take action to optimize cost. From an organizational standpoint, the
challenge for cost optimization is to identify what areas should be optimized,
identify the engineers who are responsible for those areas, and then convince
them to take the required optimization action. This document provides
recommendations to address this challenge.

The cost optimization recommendations in this document are mapped to the
following core principles:

- [Identify waste by using Google Cloud tools](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#identify-waste)
- [Identify value by analyzing and enriching spend data](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#identify-value)
- [Allocate spend to drive accountability](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#allocate-spend)
- [Drive accountability and motivate engineers to take action](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#drive-accountability)
- [Focus on value and TCO rather than cost](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#focus-value-tco)

## Identify waste by using Google Cloud tools

Google Cloud provides several products, tools, and features to help you
identify waste. Consider the following recommendations.

### Use automation and AI to systematically identify what to optimize

[Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist)
provides intelligent recommendations across services such as
[Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)
for microservices,
[BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction)
for data analytics,
[Compute Engine](https://docs.cloud.google.com/compute/docs/overview)
for core applications,
and
[Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction)
for relational databases. Active Assist recommendations are provided at no cost
and without any configuration by you. The recommendations help you to identify
idle resources and underutilized commitments.

### Centralize FinOps monitoring and control through a unified interface

[Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports)
and the
[FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub)
let you implement comprehensive cost monitoring. This comprehensive view is
vital for financial auditors and internal finance teams to track cloud spend,
assess the financial posture, evaluate FinOps maturity across various business
units or cost centers, and provide a consistent financial narrative.

## Identify value by analyzing and enriching spend data

Active Assist is effective at identifying obvious waste. However,
pinpointing value can be more challenging, particularly when workloads are on
unsuitable products or when the workloads lack clear alignment with business
value. For FS workloads, business value extends beyond cost reduction. The
value includes risk mitigation, regulatory adherence, and gaining competitive
advantages.

To understand cloud spend and value holistically, you need a complete
understanding at multiple levels: where the spend is coming from, what business
function the spend is driving, and the technical feasibility of refactoring or
optimizing the workload in question.

The following diagram shows how you can apply the
[data-information-knowledge-wisdom (DIKW) pyramid](https://en.wikipedia.org/wiki/DIKW_pyramid)
and Google Cloud tools to get a holistic understanding of cloud costs and
value.

![The data-information-knowledge-wisdom (DIKW) pyramid shows how to use cloud spending data to inform decisions.](https://docs.cloud.google.com/static/architecture/framework/perspectives/fsi/images/gcwaf-fsi-cost-optimization-dikw-pyramid.svg)

The preceding diagram shows how you can use the DIKW approach to refine raw
cloud spending data into actionable insights and decisions that drive business
value.

- **Data** : In this layer, you collect raw, unprocessed streams of usage and cost data for your cloud resources. Your central FinOps team uses tools like Cloud Billing invoices, billing exports, and Cloud Monitoring to get granular, detailed data. For example, a data point could be that a VM named `app1-test-vmA` ran for 730 hours in the `us-central1` region and cost USD 70.
- **Information**: In this layer, your central FinOps team uses tools like Cloud Billing reports and the FinOps Hub to structure the raw data to help answer questions like "What categories of resources are people spending money on?" For example, you might find out that a total of USD 1,050 was spent on VMs of the machine type n4-standard-2 across two regions in the US.
- **Knowledge** : In this layer, your central FinOps team enriches information with appropriate business context about *who* spent money and for *what purpose* . You use mechanisms like tagging, labeling, resource hierarchy, billing accounts, and custom Looker dashboards. For example, you might determine that the `app1` testing team in the US spent USD 650 during the second week of July as part of a stress testing exercise.
- **Wisdom** : In this layer, your product and application teams use the contextualized knowledge to assess the business value of cloud spending and to make informed, strategic decisions. Your teams might answer questions like the following:
  - Is the USD 5,000 that was spent on a data analytics pipeline generating business value?
  - Could we re-architect the pipeline to be more efficient without reducing performance?

Consider the following recommendations for analyzing cloud spend data.

### Analyze spend data that's provided by Google Cloud

Start with detailed Cloud Billing data that's
[exported to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery)
and data that's available
in [Monitoring](https://cloud.google.com/products/observability)
logs. To derive actionable insights and make decisions, you need to structure
this data and enrich it with business context.

### Visualize data through available tooling

Augment the built-in Google Cloud dashboards with custom reporting by
using tools like
[Data Studio](https://cloud.google.com/looker/docs/studio)
on top of BigQuery exports. Finance teams can build custom
dashboards that contextualize cloud spend against financial metrics, regulatory
reporting requirements, and business unit profitability. They can then provide a
clear financial narrative for analysis and decision making by executive
stakeholders.

## Allocate spend to drive accountability

After you understand what's driving the cloud spend, you need to identify who
is spending money and why. This level of understanding requires a robust
cost-allocation practice, which involves attaching business-relevant metadata to
cloud resources. For example, if a particular resource is used by the
Banking-AppDev team, you can attach a tag like `team=banking_appdev` to the
resource to track the cost that the team incurs on that resource. Ideally, you
should allocate 100% of your cloud costs to the source of the spending. In
practice, you might start with a lower target because building a metadata
structure to support 100% cost allocation is a complex effort.

Consider the following recommendations to develop a metadata strategy to support
cost allocation:

- **Validity** : Ensure that the tags help to identify business-related key performance indicators (KPIs) and regulatory requirements. This association is critical for internal chargebacks, regulatory reporting, and aligning cloud spend with business-unit goals. For example, the following tags clearly identify a spending team, their region, and the product that they work on: `team=banking_appdev`, `region=emea`, `product=frontend`.
- **Automation**: To achieve a high level of tagging compliance, enforce tagging through automation. Manual tagging is prone to errors and inconsistency, which are unacceptable in FS environments where auditability and financial accuracy are paramount. Automated tagging ensures that resources are correctly categorized when they're created.
- **Simplicity** : Measure simple, uncorrelated factors. FS environments are complex. To ensure that cost-allocation rules in such an environment are easy to understand and enforce, the rules must be as simple as possible. Avoid overengineering the rules for highly specific (*edge*) cases. Complex rules can lead to confusion and resistance from operational teams.

After you define an allocation strategy by using tags, you need to decide the
level of granularity at which the strategy should be implemented. The required
granularity depends on your business needs. For example, some organizations
might need to track cost at the product level, some might need cost data for
each cost center, and others might need cost data per environment (development,
staging, and production).

Consider the following approaches to achieve the appropriate level of
cost-allocation granularity for your organization:

- Use the [project hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects) in Google Cloud as a natural starting point for cost allocation. Projects represent points of policy enforcement in Google Cloud. By default, IAM permissions, security policies, and cost are attributed to projects and folders. When you review cost data that's exported from Cloud Billing, you can view the folder hierarchy and the projects that are associated with the cost data. If your Google Cloud resource hierarchy reflects your organization's accountability structure for spend, then this is the simplest way to implement cost allocation.
- Use [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) and [labels](https://docs.cloud.google.com/compute/docs/labeling-resources) for additional granularity. They provide flexible ways to categorize resources in billing exports. Tags and labels facilitate detailed cost breakdowns by application and environment.

Often, you might need to use the project hierarchy combined with tagging and
labeling for effective cost allocation. Regardless of the cost-allocation
approach that you choose, follow the recommendations that were described earlier
for developing a robust metadata strategy: validitation, automation, and
simplicity.

## Drive accountability and motivate engineers to take action

The cloud FinOps team is responsible for driving an organization to be
conscious of costs and value. The individual product teams and engineering teams
must take the required actions for cost optimization. These teams are also
accountable for the cost behavior of the financial services workloads and for
ensuring that their workloads provide the required business value.

Consider the following recommendations to drive accountability and motivate
teams to optimize cost.

### Establish a centralized FinOps team for governance

Cloud FinOps practices don't grow organically. A dedicated FinOps team must
define and establish FinOps practices by doing the following:

- Build the required processes, tools, and guidance.
- Create, communicate, and enforce the necessary policies, such as mandatory tagging, budget reviews, and optimization processes.
- Encourage engineering teams to be accountable for cost.
- Intervene when the engineering teams don't take on ownership for costs.

### Get executive sponsorship and mandates

Senior leadership, including the CTO, CFO, and CIO, must actively champion an
organization-wide shift to a FinOps culture. Their support is crucial for
prioritizing cost accountability, allocating resources for the FinOps program,
ensuring cross-functional participation, and driving compliance with FinOps
requirements.

### Incentivize teams to optimize cost

Engineers and engineering teams might not be self-motivated to focus on cost
optimization. It's important to align team and individual goals with cost
efficiency by implementing incentives such as the following:

- Reinvest a portion of the savings from cost optimization in the teams that achieved the optimization.
- Publicly recognize and celebrate cost optimization efforts and successes.
- Use gamification techniques to reward teams that effectively optimize cost.
- Integrate efficiency metrics into performance goals.

### Implement showback and chargeback techniques

Ensure that teams have clear visibility into the cloud resources and costs that
they own. Assign financial responsibility to the appropriate individuals within
the teams. Use formal mechanisms to enforce rigorous tagging and implement
transparent rules for allocating shared costs.

## Focus on value and TCO rather than cost

When you evaluate cloud solutions, consider the long-term total cost of
ownership (TCO). For example, self-hosting a database for an application might
seem to be cheaper than using a managed database service like
[Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction).
However, to assess the long-term value and TCO, you must consider the hidden
costs that are associated with self-hosted databases. Such costs include the
dedicated engineering effort for patching, scaling, security hardening, and
disaster recovery, which are critical requirements for FS workloads. Managed
services provide significantly higher long-term value, which offsets the
infrastructure costs. Managed services provide robust compliance capabilities,
have built-in reliability features, and can help to reduce your operational
overhead.

Consider the following recommendations to focus on value and TCO.

### Use product-specific techniques and tools for resource optimization

Leverage cost-optimization tools and features that are provided by Google Cloud
products, such as the following:

- Compute Engine: [Autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler), [custom machine types](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type), and [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
- GKE: [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) and [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
- Cloud Storage: [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) and [Autoclass](https://docs.cloud.google.com/storage/docs/autoclass)
- BigQuery: [Capacity-based pricing](https://cloud.google.com/bigquery/pricing#capacity_compute_analysis_pricing) and [cost-optimization techniques](https://docs.cloud.google.com/bigquery/docs/best-practices-costs)
- Google Cloud VMware Engine: committed use discounts (CUDs), optimized storage, and other [cost optimization strategies](https://cloud.google.com/blog/topics/cost-management/cost-optimization-of-google-cloud-vmware-engine-deployments?e=48754805)

### Take advantage of discounts

Ensure that the billing rate for your cloud resources is as low as possible by
using discounts that Google offers. The individual product and engineering teams
typically manage resource optimization. The central FinOps team is responsible
for optimizing billing rates because they have visibility into resource
requirements across the entire organization. Therefore, they can aggregate the
requirements and maximize the commitment-based discounts.

You can take advantage of the following types of discounts for
Google Cloud resources:

- Enterprise discounts are negotiated discounts based on your organization's commitment to a minimum total spend on Google Cloud at a reduced billing rate.
- [Resource-based CUDs](https://docs.cloud.google.com/docs/cuds#resource_based_commitments) are in exchange for a commitment to use a minimum quantity of Compute Engine resources over a one-year period or a three-year period. Resource-based CUDs are applicable to the resources that are in a specific project and region. To share CUDs across multiple projects, you can [enable CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects#turning_on_committed_use_discount_sharing).
- [Spend-based CUDs](https://docs.cloud.google.com/docs/cuds#spend_based_commitments) are in exchange for a commitment to spend a minimum amount of money on a particular product over a one-year period or a three-year period. Spend-based discounts are applicable at the billing account level. The discounts are applied regionally or globally depending on the product.

You can achieve significant savings by using CUDs on top of enterprise
discounts.

In addition to CUDs, use the following approaches to reduce billing rates:

- Use [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) for fault-tolerant and flexible workloads. Spot VMs are more than 80% cheaper than regular VMs.
- BigQuery offers multiple pricing models, which include [on-demand pricing](https://cloud.google.com/bigquery/pricing#on_demand_pricing) and [edition-based pricing](https://docs.cloud.google.com/bigquery/docs/editions-intro) that's based on commitments and autoscaling requirements. If you use a significant volume of BigQuery resources, choose an appropriate edition to reduce the cost per slot for analytics workloads.
- Carefully evaluate the available Google Cloud regions for the services that you need to use. Choose regions that align with your cost objectives and factors like latency and compliance requirements. To understand the trade-offs between cost, sustainability, and latency, use the [Google Cloud Region Picker](https://cloud.withgoogle.com/region-picker/).

<br />

<br />


# Financial services perspective: Performance optimization

This document in the
[Google Cloud Well-Architected Framework: Financial services (FS) perspective](https://docs.cloud.google.com/architecture/framework/perspectives/fsi)
provides an overview of principles and recommendations to optimize the
performance of your FS workloads in Google Cloud. The recommendations in this
document align with the
[performance optimization pillar](https://docs.cloud.google.com/architecture/framework/performance-optimization)
of the Well-Architected Framework.

Performance optimization has a long history in financial services. It has helped
FS organizations surpass technical challenges and it's nearly always been an
enabler or accelerator for the creation of new business models. For example,
ATMs
([introduced in 1967](https://en.wikipedia.org/wiki/ATM#Invention))
automated the cash dispensation process and they helped banks to decrease the
cost of their core business. Techniques like bypassing the OS kernel and pinning
application threads to compute cores helped to achieve deterministic and low
latency for trading applications. The reduction in latency facilitated higher
and firmer liquidity with tighter spreads in the financial markets.

The cloud creates new opportunities for performance optimization. It also
challenges some of the historically accepted optimization patterns.
Specifically, the following trade-offs are more transparent and controllable in
the cloud:

- Time to market versus cost.
- End-to-end performance at the system level versus performance at the node level.
- Talent availability versus agility of technology-related decision making.

For example, adapting hardware and IT resources to specific skill requirements
is a trivial task in the cloud. To support GPU programming, you can create
GPU-based VMs. You can scale capacity in the cloud to accommodate demand
spikes without over-provisioning resources. This capability helps to ensure that
your workloads can handle peak loads, such as on
[nonfarm payroll](https://en.wikipedia.org/wiki/Nonfarm_payrolls)
days and when
[trading volumes are significantly greater than historical levels](https://cloud.google.com/blog/topics/financial-services/how-bidfx-developed-liquidity-provision-analytics-on-google-cloud?e=48754805).
Instead of spending on writing highly optimized code at the level of individual
servers (like highly fine-tuned code in the C language) or writing code for
conventional high performance computing (HPC) environments, you can scale out
optimally by using a well-architected Kubernetes-based distributed system.

The performance optimization recommendations in this document are mapped to the
following core principles:

- [Align technology performance metrics with key business indicators](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#align-metrics)
- [Prioritize security without sacrificing performance for unproven risks](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#prioritize-security-and-performance)
- [Rethink your architecture to adapt to new opportunities and requirements](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#adapt)
- [Future-proof your technology to meet present and future business needs](https://docs.cloud.google.com/architecture/framework/perspectives/fsi/printable#future-proof)

## Align technology performance metrics with key business indicators

You can map performance optimization to business-value outcomes in several
ways. For example, in a
[buy-side](https://corporatefinanceinstitute.com/resources/career/buy-side-vs-sell-side/)
research desk, a business objective could be to optimize the output per research
hour or to prioritize experiments from teams that have a proven track record,
such as higher
[Sharpe ratios](https://en.wikipedia.org/wiki/Sharpe_ratio).
On the sell side, you can use analytics to track client interest and accordingly
prioritize the throughput to AI models that support the most interesting
research.

Connecting performance goals to business key performance indicators (KPIs) is
also important for funding performance improvements. Business innovation and
transformation initiatives (sometimes called *change-the-bank* efforts) have
different budgets and they have potentially different degrees of access to
resources when compared to business-as-usual (BAU) or *run-the-bank* operations.
For example, Google Cloud helped the risk management and technology teams of a
[G-SIFI](https://www.fsb.org/work-of-the-fsb/market-and-institutional-resilience/global-systemically-important-financial-institutions-g-sifis/)
to collaborate with the front-office quantitative analysts on a solution to
perform risk analytics calculations (such as
[XVA](https://en.wikipedia.org/wiki/XVA))
in minutes instead of hours or days. This solution helped the organization to
meet relevant compliance requirements. It also enabled the traders to have
higher quality conversations with their clients, potentially offering tighter
spreads, firmer liquidity, and more cost-effective hedging.

When you align your performance metrics with business indicators, consider the
following recommendations:

- Connect each technology initiative to the relevant business [objectives and key results (OKRs)](https://en.wikipedia.org/wiki/Objectives_and_key_results), such as increasing revenue or profit, reducing costs, and mitigating risk more efficiently or holistically.
- Focus on optimizing performance at the system level. Look beyond the conventional change-the-bank versus run-the-bank separation and the front-office versus back-office silos.

## Prioritize security without sacrificing performance for unproven risks

Security and regulatory compliance in FS organizations must be unequivocally
of a high standard. Maintaining a high standard is essential to avoid losing
clients and to prevent irreparable damage to an organization's brand. Often, the
highest value is derived through technology innovations such as
[generative AI](https://cloud.google.com/ai/generative-ai)
and unique, managed services like
[Spanner](https://docs.cloud.google.com/spanner).
Don't automatically discard such technology options due to a blanket
misconception about prohibitive operational risk or inadequate regulatory
compliance posture.

Google Cloud has worked closely with G-SIFIs to make sure that an AI-based
approach for
[Anti-Money Laundering (AML)](https://cloud.google.com/anti-money-laundering-ai)
can be used across the jurisdictions where the institutions serve customers.
For example,
[HSBC](https://services.google.com/fh/files/misc/hsbc_celent_model_risk_manager_of_the_year_2023.pdf)
significantly enhanced the performance of its financial crime (Fincrime) unit
with the following results:

- Nearly two to four times more confirmed suspicious activity.
- Lower operational costs due to elimination of over 60% of false positives and focused investigation time only on high-risk, actionable alerts.
- Auditable and explainable outputs to support regulatory compliance.

Consider the following recommendations:

- Confirm that the products that you intend to use can help meet the security, resilience, and compliance requirements for the jurisdictions where you operate. To achieve this objective, work with Google Cloud account teams, risk teams, and product teams.
- Create more powerful models *and* provide transparency to customers by leveraging AI explainability (for example, [Shapley value attribution](https://storage.googleapis.com/cloud-ai-whitepapers/AI%20Explainability%20Whitepaper.pdf)). Techniques like Shapley value attribution can attribute model decisions to particular features at the input level.
- Achieve transparency for generative AI workloads by using techniques
  like
  [citations to sources](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview#citation_check),
  [grounding](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview),
  and
  [RAG](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-overview).

- When explainability isn't enough, separate out the decision making steps
  in your value streams and use AI to automate only the non-decision making
  steps. In some cases, explainable AI might not be sufficient or a process
  might require human intervention due to regulatory concerns (for example,
  [GDPR, Article 22](https://gdpr-info.eu/art-22-gdpr/#:%7E:text=Protection%20Regulation%20(GDPR)-,Art.,significantly%20affects%20him%20or%20her.)).
  In such cases, present all the information that the human agent needs for
  decision making in a single control pane, but automate the data gathering,
  ingestion, manipulation, and summarization tasks.

## Rethink your architecture to adapt to new opportunities and requirements

Augmenting your current architectures with cloud-based capabilities can provide
significant value. To achieve more transformative outcomes, you need to
periodically rethink your architecture by using a cloud-first approach.

Consider the following recommendations to periodically rethink the architecture
of your workloads to further optimize performance.

### Use cloud-based alternatives to on-premises HPC systems and schedulers

To take advantage of higher elasticity, improved security posture, and
extensive monitoring and governance capabilities, you can run HPC workloads in
the cloud or
[burst](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/cloud-bursting-pattern)
on-premises workloads to the cloud. However, for certain numerical modeling use
cases like simulation of investment strategies or XVA modeling,
[combining Kubernetes with Kueue](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/kueue-intro)
might offer a more powerful solution.

### Switch to graph-based programming for simulations

[Monte Carlo simulations](https://en.wikipedia.org/wiki/Monte_Carlo_method)
might be much more performant in a graph-based execution system such as
[Dataflow](https://cloud.google.com/products/dataflow).
For example,
[HSBC](https://cloud.google.com/customers/hsbc-risk-advisory-tool#:%7E:text=Spurred%20by%20an%20enthusiastic%20commitment,a%20wealth%20of%20future%20possibilities.)
uses Dataflow to run risk calculations 16 times faster compared
to their previous approach.

### Run cloud-based exchanges and trading platforms

Conversations with Google Cloud customers reveal that the
[80/20 Pareto principle](https://en.wikipedia.org/wiki/Pareto_principle)
applies to the performance requirements of markets and trading applications.

- More than 80% of trading applications don't need extremely low latency. However, they get significant benefits from the resilience, security, and elasticity capabilities of the cloud. For example, [BidFX](https://cloud.google.com/blog/topics/financial-services/how-bidfx-developed-liquidity-provision-analytics-on-google-cloud?e=48754805), a foreign exchange multi-dealer platform uses the cloud to launch new products quickly and to significantly increase their availability and footprint without increasing resources.
- The remaining applications (less than 20%) need low latency (less than a millisecond), determinism, and fairness in the delivery of messages. Conventionally, these systems run in rigid and expensive colocated facilities. Increasingly, even this category of applications is being replatformed on the cloud, either at the [edge](https://cloud.google.com/blog/topics/hybrid-cloud/deutsche-bank-uses-google-distributed-cloud?e=48754805) or as [cloud-first applications](https://cloud.google.com/blog/topics/financial-services/lessons-from-deutsche-borse-groups-cloud-native-trading-engine?e=48754805).

## Future-proof your technology to meet present and future business needs

Historically, many FS organizations built proprietary technologies to gain a
competitive edge. For example, in the early 2000s, successful investment banks
and trading firms had their own implementations of foundational technologies
such as pub-sub systems and message brokers. With the evolution of open source
technologies and the cloud, such technologies have become commodities and don't
offer incremental business value.

Consider the following recommendations to future-proof your technology.

### Adopt a data-as-a-service (DaaS) approach for faster time to market and cost transparency

FS organizations often evolve through a combination of organic growth and
mergers and acquisitions (M\&A). As a result, the organizations need to integrate
disparate technologies. They also need to manage duplicate resources, such as
data vendors, data licenses, and integration points. Google Cloud provides
[opportunities](https://cloud.google.com/blog/topics/perspectives/google-cloud-can-help-with-post-merger-integration-strategy?e=48754805)
to create differentiated value in post-merger integrations.

For example, you can use services like
[BigQuery sharing](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction)
to build an analysis-ready data-as-a-service (DaaS) platform. The platform can
provide both market data and inputs from alternative sources. This approach
eliminates the need to build redundant data pipelines and it lets you focus on
more valuable initiatives. Further, the merged or acquired companies can quickly
and efficiently rationalize their post-merger data licensing and infrastructure
needs. Instead of spending effort on adapting and merging legacy data estates
and operations, the combined business can focus on new business opportunities.

### Build an abstraction layer to isolate existing systems and address emerging business models

Increasingly, the competitive advantage for banks isn't the core banking system
but their customer experience layer. However, legacy banking systems often use
monolithic applications that were developed in languages like Cobol and are
integrated across the entire banking value chain. This integration made it
difficult to separate the layers of the value chain, so it was nearly impossible
to upgrade and modernize such systems.

One solution to address this challenge is to use an isolation layer such as an
[API management system](https://cloud.google.com/apigee)
or a staging layer like Spanner that duplicates the book of record and
facilitates the modernization of services with advanced analytics and AI. For
example,
[Deutsche Bank](https://cloud.google.com/blog/products/databases/deutsche-bank-scales-online-banking-platform-with-spanner?e=48754805)
used Spanner to isolate their legacy core banking estate and start their
innovation journey.

<br />