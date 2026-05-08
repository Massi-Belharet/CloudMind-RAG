This document defines and discusses business objectives, drivers, and
requirements, and how these factors can influence your design decisions when
constructing hybrid and multicloud architectures.

## Objectives

An organization can adopt a hybrid or multicloud architecture either as a
permanent solution to meet specific business objectives, or as a temporary state
to facilitate certain requirements, such as a migration to the cloud.

Answering the following questions about your business is a good way to define your business requirements, and to establish specific expectations about how to achieve some or all of your business objectives. These questions focus on what's needed for your business, not how to achieve it technically.

- Which business goals are driving the decision to adopt a hybrid or multicloud architecture?
- What business and technical objectives is a hybrid or multicloud architecture going to help achieve?
- What business drivers influenced these objectives?
- What are the specific business requirements?

In the context of hybrid and multicloud architectures, one business goal for an
enterprise customer might be to expand online sales operations or markets from a
single region to become one of the global leaders in their market segment. One
of the business objectives might be to start accepting purchase orders from
users across the globe (or from specific regions) within six months.

To support the previously mentioned business requirements and objectives, one
potential primary technical objective is to expand the IT infrastructure and
applications architecture of a company from an on-premises-only model to a
hybrid architecture, using the global capabilities and services of public
clouds. This objective should be specific and measurable, clearly defining the
expansion scope in terms of target regions and timelines.

> [!NOTE]
> **Note:** Sometimes business requirements are defined to satisfy certain business strategies. A business strategy can be defined as a long term plan to draw a path to achieve certain business objectives.

In general, a hybrid or multicloud architecture is rarely a goal in itself, but
rather a means of meeting technical objectives driven by certain business
requirements. Therefore, choosing the right hybrid or multicloud architecture
requires first clarifying these requirements.

It's important to differentiate between the business objectives and technical
objectives of your IT project. Your business objectives should focus on the goal
and mission of your organization. Your technical objectives should focus on
building a technological foundation that enables your organization to meet their
business requirements and objectives.

Business drivers influence the achievement of the business objective and goals.
Therefore, clearly identifying the business drivers can help shape the business
objectives or goals to be more relevant to market needs and trends.

The following flowchart illustrates business drivers, goals, objectives, and
requirements, and the technical objectives and requirements, and how all these
factors relate to each other:

![Flow chart showing things to consider when developing technical requirements, including business drivers, goals, objectives, and requirements, as well as technical objectives.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns/architectures-flowchart.svg)

## Business and technical drivers

Consider how your business drivers influence your technical objectives. Some
common, influencing, business drivers when choosing a hybrid
architecture include the following:

- Heeding laws and regulations about data sovereignty.
- Reducing capital expenditure (CAPEX) or general IT spending with the support of cloud financial management and cost optimization disciplines like [FinOps](https://cloud.google.com/learn/what-is-finops).
  - Cloud adoption can be driven by scenarios that help reduce CAPEX, like building a Disaster Recovery solution in a hybrid or multicloud architecture.
- Improving the user experience.
- Increasing flexibility and agility to respond to changing market demands.
- Improving transparency about costs and resource consumption.

Consider your list of business drivers for adopting a hybrid or multicloud
architecture together. Don't consider them in isolation. Your final decision
should depend on the balance of your business priorities.

After your organization realizes the benefits of the cloud, it might decide to
fully migrate if there are no constraints---like costs or specific compliance
requirements that require highly secure data to be hosted on-premises---that
prevent it from doing so.

Although adopting a single cloud provider can offer several benefits, such as
reduced complexity, built-in integrations among services, and cost optimization
options like
[committed use discounts](https://docs.cloud.google.com/docs/cuds),
there are still some scenarios where a multicloud architecture can be beneficial
for a business. The following are the common business drivers for adopting a
multicloud architecture, along with the associated considerations for each
driver:

- **Heeding laws and regulations about data sovereignty** : The most common scenario is when an organization is expanding its business to a new region or country and has to comply with new data-hosting regulations.
  - If the existing used cloud service provider (CSP) has no local cloud region in that country, then for compliance purposes the common solution is to use another CSP that has a local cloud region in that country.
- **Reducing costs**: Cost reduction is often the most common business driver for adopting a technology or architecture. However, it's important to consider more than just the cost of services and potential pricing discounts when deciding whether to adopt a multicloud architecture. Account for the cost of building and operating a solution across multiple clouds, and any architecture constraints that might arise from existing systems.

Sometimes, the potential challenges associated with a multicloud
strategy might outweigh the benefits. A multicloud strategy might introduce
additional costs later on.

[Common challenges](https://cloud.google.com/learn/what-is-multicloud#section-6)
associated with developing a multicloud strategy include the following:

- Increasing management complexity.
- Maintaining consistent security.
- Integrating software environments.
- Achieving consistent cross-cloud performance and reliability.
- Building a technical team with multicloud skills might be expensive and might require expanding the team, unless it's managed by a third party company.
- Managing the product pricing and management tools from each CSP.
  - Without a solution that can provide unified cost visibility and dashboards, it can be difficult to efficiently manage costs across multiple environments. In such cases, you might use the Looker cloud cost management solution where applicable. For more information, see [The strategy for effectively optimizing cloud billing cost management](https://cloud.google.com/blog/products/data-analytics/cloud-cost-management).
- **Using the unique capabilities from each CSP** : A multicloud architecture enables organizations to use additional new technologies to improve their own business capability offerings without being limited to the choices offered by a single cloud provider.
  - To avoid any unforeseen risk or complexity, assess your potential challenges through a feasibility and effectiveness assessment, including the common challenges mentioned previously.
- **Avoiding vendor lock-in** : Sometimes, enterprises want to avoid being locked into a single cloud provider. A multicloud approach lets them choose the best solution for their business needs. However, the feasibility of this decision depends on several factors, such as the following:
  - Technical dependencies
  - Interoperability considerations between applications
  - Costs of rebuilding or refactoring applications
  - Technical skill sets
  - Consistent security and manageability
- **Enhancing the reliability and availability level of business critical
  applications**: In some scenarios, a multicloud architecture can provide resilience to outages. For example, if one region of a CSP goes down, traffic can be routed to another CSP in the same region. This scenario assumes that both cloud providers support the required capabilities or services in that region.

When data residency regulations in a specific country or region mandate
the storage of sensitive data---like personally identifiable information
(PII)---within that location, a multicloud approach can provide a compliant
solution. By using two CSPs in one region to provide resilience to outages,
you can facilitate compliance with regulatory restrictions while also
addressing availability requirements.

The following are some resilience considerations to assess before
adopting a multicloud architecture:

- Data movement: How often might data move within your multicloud environment?
  - Might data movement incur significant data transfer charges?
- Security and manageability: Are there any potential security or manageability complexities?
- Capability parity: Do both CSPs in the selected region offer the required capabilities and services?
- Technical skill set: Does the technical team have the skills required to manage a multicloud architecture?

Consider all these factors when assessing the feasibility of using a
multicloud architecture to improve resilience.

When assessing the feasibility of a multicloud architecture, it's important to
consider
[the long-term benefits](https://cloud.google.com/learn/what-is-multicloud#section-8).
For example, deploying applications on multiple clouds for disaster recovery or
increased reliability might increase costs in the short term, but could prevent
outages or failures. Such failures can cause long-term financial and
reputational damage. Therefore, it's important to weigh short-term costs against
the long-term potential value of adopting multicloud. Also, the long-term
potential value can vary based on the organization size, technology scale,
criticality of the technology solution, and the industry.

Organizations that plan to successfully create a hybrid or multicloud
environment, should consider
[building a Cloud Center of Excellence (COE)](https://services.google.com/fh/files/misc/cloud_center_of_excellence.pdf).
A COE team can become the conduit for transforming the way that
internal teams within your organization serve the business during your
transition to the cloud. A COE is one of the ways that your organization can
adopy the cloud faster, drive standardization, and maintain stronger alignment
between your business strategy and your cloud investments.

If the objective of the hybrid or multicloud architecture is to create a
temporary state, common business drivers include:

- The need to reduce CAPEX or general IT spending for short-term projects.
- The ability to provision such infrastructure quickly to support a business use case. For example:
  - This architecture might be used for limited-time projects. It could be used to support a project that requires a high scale distributed infrastructure within a limited duration, while still using data that is on-premises.
- The need for multi-year digital transformation projects that require a large enterprise to establish and that use a hybrid architecture for some time to help them align their infrastructure and applications modernization with their business priorities.
- The need to create a temporary hybrid, multicloud, or mixed architecture after a corporate merger. Doing so enables the new organization to define a strategy for the final state of its new cloud architecture. It's common for two merging companies to use different cloud providers, or for one company to use an on-premises private data center and the other to use the cloud. In either case, the first step in merger and acquisition is almost always to integrate the IT systems.

## Technical drivers

The preceding section discussed business drivers. To get approved, major
architectural decisions almost always need the support of those drivers.
However, technical drivers, which can be based on either a technical gain or a
constraint, can also influence business drivers. In some scenarios, it's
necessary to translate technical drivers into business drivers and explain how
they might positively or negatively affect the business.

The following non-exhaustive list contains some common technical drivers for
adopting a hybrid or multicloud architecture:

- Building out technological capabilities, such as advanced analytics services and AI, that might be difficult to implement in existing environments.
- Improving the quality and performance of service.
- Automating and accelerating application rollouts to achieve a faster time to market and shorter cycle times.
- Using high-level APIs and services to speed up development.
- Accelerating the provisioning of compute and storage resources.
- Using serverless services to build elastic services and capabilities faster and at scale.
- Using global infrastructure capabilities to build global or multi-regional architectures to satisfy certain technical requirements.

The most common technical driver for both temporary hybrid and temporary
multicloud architectures is to facilitate a migration from on-premises to the
cloud or to an extra cloud. In general, cloud migrations almost always naturally
lead to hybrid cloud setup. Enterprises often have to systematically transition
applications and data based on their priorities. Similarly, a short-term setup
might be intended to facilitate a proof of concept using advanced technologies
available in the cloud for a certain period.

## Technical design decisions

The identified technical objective and its drivers are key to making a
business-driven architecture decision and to selecting one of the architecture
patterns discussed in this guide. For example, to support a specific business
goal, a company might set a business objective to build a research and
development practice for three to six months. The main business requirement to
support this objective might be to build the required technology environment for
research and design with the lowest possible CAPEX.

The technical objective in this case is to have a temporary hybrid cloud setup.
The driver for this technical objective is to take advantage of the on-demand
pricing model of the cloud to meet the previously mentioned business
requirement. Another driver is influenced by the specific technology
requirements that require a cloud-based solution with high compute capacity and
quick setup.

## Use Google Cloud for hybrid and multicloud architectures

Using open source solutions can make it easier to adopt a hybrid and multicloud
approach, and to minimize vendor lock-in. However, you should consider the
following potential complexities when planning an architecture:

- Interoperability
- Manageability
- Cost
- Security

Building on a cloud platform that contributes to and
[supports open source](https://cloud.google.com/learn/what-is-a-cloud-service-provider#section-7)
might help to simplify your path to adopting hybrid and multicloud
architectures.
[Open cloud](https://cloud.google.com/open-cloud)
empowers you with an approach that provides maximum choice and abstracts
complexity. In addition, Google Cloud offers the flexibility to migrate,
build, and optimize applications across hybrid and multicloud environments while
minimizing vendor lock-in, using best-in-breed solutions, and meeting regulatory
requirements.

Google is also one of the
[largest contributors](https://opensource.googleblog.com/2020/08/open-source-by-numbers-at-google.html)
to the open source ecosystem and works with the open source community to develop
well-known
[open source technologies](https://opensource.google/)
like Kubernetes. When rolled out as a managed service, Kubernetes can help
reduce complexities around hybrid and multicloud manageability and security.