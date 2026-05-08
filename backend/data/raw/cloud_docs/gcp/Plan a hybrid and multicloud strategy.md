This document focuses on how to apply predefined business
considerations when planning a hybrid and multicloud strategy. It expands on
guidance in
[Drivers, considerations, strategy, and approaches](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/drivers).
That article defines and analyzes the business considerations
enterprises should account for when planning such a strategy.

## Clarify and agree on the vision and objectives

Ultimately, the main purpose of a hybrid or multicloud strategy is to achieve
the identified business requirements and the associated technical objectives for
each business use case aligned with specific business objectives. To achieve
this goal, create a well-structured plan that includes the following
considerations:

- Which workloads should be run in each computing environment.
- Which [application architecture patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns) to apply across multiple workloads.
- Which technology and [networking architecture pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns) to use.

Know that defining a plan that considers all workloads and requirements is
difficult at best, especially in a complex IT environment. In addition, planning
takes time and might lead to competing stakeholder visions.

To avoid such situations, initially formulate a vision statement that addresses
the following questions (at minimum):

- What's the targeted business use case to meet specific business objectives?
- Why is the current approach and computing environment insufficient to meet the business objectives?
- What are the primary technological aspects to optimize for by using the public cloud?
- Why and how is the new approach going to optimize and meet your business objectives?
- How long do you plan to use your hybrid or multicloud setup?

Agreeing on the key business and technical objectives and drivers, then
obtaining relevant stakeholder sign-off can provide a foundation for the next
steps in the planning process. To effectively align your proposed solution with
the overarching architectural vision of your organization, align with your team
and the stakeholders responsible for leading and sponsoring this initiative.

## Identify and clarify other considerations

While planning a hybrid or multicloud architecture, it's important to identify
and agree about the architectural and operational constraints of your project.

On the operations side, the following non-exhaustive list provides some
requirements that might create some constraints to consider when planning your
architecture:

- Managing and configuring multiple clouds separately versus building a holistic model to manage and secure the different cloud environments.
- Ensuring consistent authentication, authorization, auditing, and policies across environments.
- Using consistent tooling and processes across environments to provide a holistic view into security, costs, and opportunities for optimization.
- Using consistent compliance and security standards to apply unified governance.

On the architecture-planning side, the biggest constraints often stem from
existing systems and can include the following:

- Dependencies between applications
- Performance and latency requirements for communication between systems
- Reliance on hardware or operating systems that might not be available in the public cloud
- Licensing restrictions
- Dependence on the availability of required capabilities in the selected regions of a multicloud architecture

For more information about the other considerations related to workload
portability, data movement, and security aspects, see
[Other considerations](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/other-considerations).

## Design a hybrid and multicloud architecture strategy

After you have clarified the specifics of the business and technical objectives
with the associated business requirements (and ideally clarified and agreed on a
vision statement), you can build your strategy to create a hybrid or multicloud
architecture.

The following flowchart summarizes the logical steps to build such a strategy.

![When strategizing, consider your business objectives, get buy in, build a high-level plan and then use that to inform your strategy.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns/architectures-logicflow.svg)

To help you determine your hybrid or multicloud architecture technical
objectives and needs, the steps in the preceding flowchart start with the
business requirements and objectives. How you implement your strategy can vary
depending on the objectives, drivers, and the technological migration path of
each business use case.

It's important to remember that a migration is a journey. The following diagram
illustrates the phases of this journey as described in
[Migrate to Google Cloud](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started).

![Migration path with four phases.](https://docs.cloud.google.com/static/architecture/images/migration-to-gcp-getting-started-migration-path.svg)

This section provides guidance about the "Assess," "Plan," "Deploy," and
"Optimize" phases in the preceding diagram. It presents this information in the
context of a hybrid or multicloud migration. You should align any migration with
the guidance and best practices discussed in the
[migration path section](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#the_migration_path)
of the Migrate to Google Cloud guide. These phases might apply to
each workload individually, not to all workloads at once. At any point in time,
several workloads might be in different phases:

### Assess phase

In the *Assess* phase, you conduct an initial workload assessment. During
this phase, consider the goals outlined in your vision and strategy planning
documents. Decide on a
[migration plan](https://docs.cloud.google.com/migration-center/docs/migration-planning-overview)
by first identifying a candidate list of workloads that could benefit from being
deployed or migrated to the public cloud.

To start, choose a workload that isn't business-critical or too difficult to
migrate (with minimal or no dependencies on any workload in other environments),
yet typical enough to serve as a blueprint for upcoming deployments or
migrations.

Ideally, the workload or application you select should be part of a targeted
business use case or function that has a measurable effect on the business after
it's complete.

To evaluate and mitigate any potential migration risks, conduct a
[migration risks assessment](https://docs.cloud.google.com/migration-center/docs/migration-risks).
it's important to assess your candidate workload to determine its suitability
for migration to a multicloud environment. This assessment involves evaluating
various aspects of the applications and infrastructure including the
following:

- Application compatibility requirements with your selected cloud providers
- Pricing models
- Security features offered by your selected cloud providers
- Application interoperability requirements

Running an assessment also helps you identify data privacy requirements,
compliance requirements, consistency requirements, and solutions across multiple cloud environments. The risks you identify can affect the workloads you choose
to migrate or operate.

There are several types of tools, like
[Google Cloud Migration Center](https://docs.cloud.google.com/migration-center/docs/migration-center-overview),
to help you assess existing workloads. For more information, see
[Migration to Google Cloud: Choose an assessment tool](https://docs.cloud.google.com/architecture/migration-to-google-cloud-choose-assessment-tool).

From a workload modernization perspective, the
[fit assessment tool](https://docs.cloud.google.com/migrate/containers/docs/mfit-about)
helps to assess a VM workload to determine if the workload is fit for
modernization to a container or for migration to Compute Engine.

### Plan phase

In the *Plan* phase, start with the identified applications and required cloud
workloads and perform the following tasks:

1. Develop a prioritized migration strategy that defines [application migration waves](https://docs.cloud.google.com/migration-center/docs/plan-migration-waves#group_applications_in_waves) and paths.
2. Identify the applicable [high-level hybrid or multicloud application architecture pattern](https://docs.cloud.google.com/architecture/hybrid-and-multi-cloud-architecture-patterns).
3. Select a networking architecture pattern that supports the selected application architecture pattern.

Ideally, you should incorporate the cloud networking pattern with the
[landing zone design](https://docs.cloud.google.com/architecture/landing-zones).
The landing zone design serves as a key foundational element of overall
hybrid and multicloud architectures. The design requires seamless
integration with these patterns. Don't design the landing zone in
isolation. Consider these networking patterns as a subset of the landing
zone design.

A landing zone might consist of different applications, each with a
different networking architecture pattern. Also, in this phase, it's
important to decide on the design of the
[Google Cloud organization, projects, and resource hierarchy](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy)
to prepare your cloud environment landing zone for the hybrid or multicloud
integration and deployment.

As part of this phase you should consider the following:

- Define the migration and modernization approach. There's more information about migration approaches later in this guide. It's also covered in more detail in the [migration types](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#types_of_migrations) section of [Migrate to Google Cloud](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started).
- Use your assessment and discovery phase findings. Align them with the candidate workload you plan to migrate. Then develop an application [migration waves plan](https://docs.cloud.google.com/migration-center/docs/plan-migration-waves). The plan should incorporate the estimated resource sizing requirements that you determined during the assessment phase.
- Define the communication model required between the distributed applications and among application components for the intended hybrid or multicloud architecture.
- Decide on a suitable [deployment archetype](https://docs.cloud.google.com/architecture/deployment-archetypes) to deploy your workload, such as zonal, regional, multi-regional, or global, for the chosen architecture pattern. The archetype you select forms the basis for constructing the application-specific deployment architectures tailored to your business and technical needs.
- Decide on measurable success criteria for the migration, with clear milestones for each migration phase or wave. Selecting criteria is essential, even if the technical objective is to have the hybrid architecture as a short term setup.
- Define application SLAs and KPIs when your applications operate in a hybrid setup, especially for those applications that might have distributed components across multiple environments.

For more information, see
[About migration planning](https://docs.cloud.google.com/migration-center/docs/migration-planning-overview)
to help plan a successful migration and to minimize the associated risks.

### Deploy phase

In the *Deploy* phase, you are ready to start executing your migration
strategy. Given the potential number of requirements, it's best to take an
iterative approach.

Prioritize your workloads based on the migration and application waves that you
developed during the planning phase. With hybrid and multicloud architectures,
start your deployment by establishing the necessary connectivity
between Google Cloud and the other computing environments. To facilitate
the required communication model for your hybrid or multicloud architecture,
base the deployment on your selected design and network connectivity type, along
with the applicable networking pattern. We recommend that you take this approach
for your overall landing zone design decision.

In addition, you must test and validate the application or service based on the
defined application success criteria. Ideally, these criteria should include
both functional and load testing (non-functional) requirements before moving to
production.

### Optimize phase

In the *Optimize* phase, test your deployment: After you complete testing, and
the application or service meets the functional and performance capacity
expectations, you can move it to production. Cloud monitoring and visibility
tools, such as
[Cloud Monitoring](https://docs.cloud.google.com/monitoring),
can provide insights into the performance, availability, and health of your
applications and infrastructure and help you optimize where needed.

For more information, see
[Migrate to Google Cloud: Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment).
To learn more about how to design such tools for hybrid or multicloud
architecture, see
[Hybrid and multicloud monitoring and logging patterns](https://docs.cloud.google.com/architecture/hybrid-and-multi-cloud-monitoring-and-logging-patterns).

## Assess candidate workloads

The choice of computing environments for different workloads significantly
affects the success of a hybrid and multicloud strategy. Workload placement
decisions should align with specific business objectives. Therefore, these
decisions should be guided by targeted business use cases that enable measurable
business effects. However, starting with the most business-critical
workload/application isn't always necessary nor recommended. For more
information, see
[Choosing the apps to migrate first](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads#choosing_the_apps_to_migrate_first)
in the Migrate to Google Cloud guide.

As discussed in the
[Business and technical drivers](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/drivers)
section, there are different types of drivers and considerations for hybrid and
multicloud architectures.

The following summarized list of factors can help you evaluate your migration
use case in the context of a hybrid or multicloud architecture with
opportunities to have a measurable business effect:

- Potential for market differentiation or innovation that is enabled by using cloud services to enable certain business functions or capabilities, such as artificial intelligence capabilities that use existing on-premises data to train machine learning models.
- Potential savings in total cost of ownership for an application.
- Potential improvements in availability, resiliency, security, or performance---for example adding a disaster recovery (DR) site in the cloud.
- Potential speedup of the development and release processes---for example, building your development and testing environments in the cloud.

The following factors can help you evaluate
[migration risks](https://docs.cloud.google.com/migration-center/docs/migration-risks):

- The potential effect of outages that are caused by a migration.
- The experience your team has with public cloud deployments, or with deployments for a new or second cloud provider.
- The need to comply with any existing legal or regulatory restrictions.

The following factors can help you evaluate the technical difficulties of a
migration:

- The size, complexity, and age of the application.
- The number of dependencies with other applications and services across different computing environments.
- Any restrictions imposed by third-party licenses.
- Any dependencies on specific versions of operating systems, databases, or other environment configurations.

After you have assessed your initial workloads, you can start prioritizing them
and defining your
[migration waves](https://docs.cloud.google.com/migration-center/docs/plan-migration-waves#group_applications_in_waves)
and
[approaches](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/adopt).
Then, you can identify applicable architecture patterns and supporting
[networking patterns](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns).
This step might require multiple iterations, because your assessment could
change over time. It's therefore worth re-evaluating workloads after you make
your first cloud deployments.