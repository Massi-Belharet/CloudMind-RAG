This document provides guidance on common and
proven approaches and considerations to migrate your workload to the cloud. It
expands on guidance in
[Design a hybrid and multicloud architecture strategy](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/strategy#design_a_hybrid_and_multicloud_architecture_strategy),
which discusses several possible, and recommended, steps to design a strategy
for adopting a hybrid or multicloud architecture.

> [!NOTE]
> **Note:** The phrase *migrate your workload to the cloud* refers to hybrid and multicloud scenarios, not to a complete cloud migration.

## Cloud first

A common way to begin using the public cloud is the *cloud-first* approach.
In this approach, you deploy your new workloads to the public cloud while your
existing workloads stay where they are. In that case, consider a classic
deployment to a private computing environment only if a public cloud deployment
is impossible for technical or organizational reasons.

The cloud-first strategy has advantages and disadvantages. On the positive side,
it's forward looking. You can deploy new workloads in a modernized fashion while
avoiding (or at least minimizing) the hassles of migrating existing workloads.

While a *cloud-first* approach can provide certain advantages, it could
potentially result in missed opportunities for improving or using existing
workloads. New workloads might represent a fraction of the overall IT landscape,
and their effect on IT expenses and performance can be limited. Allocating time
and resources to migrating an existing workload could potentially lead to more
substantial benefits or cost savings compared to attempting to accommodate a new
workload in the cloud environment.

Following a strict *cloud-first* approach also risks increasing the overall
complexity of your IT environment. This approach might create redundancies,
lower performance due to potential excessive cross-environment communication, or
result in a computing environment that isn't well suited for the individual
workload. Also, compliance with industry regulations and data privacy laws can
restrict enterprises from migrating certain applications that hold sensitive
data.

Considering these risks, you might be better off using a cloud-first approach
only for selected workloads. Using a cloud-first approach lets you concentrate
on the workloads that can benefit the most from a cloud deployment or migration.
This approach also considers the modernization of existing workloads.

A common example of a cloud-first hybrid architecture is when legacy
applications and services holding critical data must be integrated with new data
or applications. To complete the integration, you can use a hybrid
architecture that modernizes legacy services by using API interfaces, which
unlocks them for consumption by new cloud services and applications.
With a cloud
[API management platform](https://docs.cloud.google.com/solutions/unlocking-legacy-applications),
like
[Apigee](https://docs.cloud.google.com/apigee),
you can implement such use cases with minimal application changes and add
security, analytics, and scalability to the legacy services.

## Migration and modernization

Hybrid multicloud and IT modernization are distinct concepts that are linked in
a virtuous circle. Using the public cloud can facilitate and simplify the
modernization of IT workloads. Modernizing your IT workloads can help you
get more from the cloud.

The primary goals of modernizing workloads are as follows:

- Achieve greater agility so that you can adapt to changing requirements.
- Reduce the costs of your infrastructure and operations.
- Increase reliability and resiliency to minimize risk.

However, it might not be feasible to modernize every application in the
migration process at the same time. As described in
[Migration to Google Cloud](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started),
you can implement one of the following
[migration types](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#types_of_migrations),
or even combine multiple types as needed:

- Rehost (lift and shift)
- Replatform (lift and optimize)
- Refactor (move and improve)
- Rearchitect (continue to modernize)
- Rebuild (remove and replace, sometimes called *rip and replace*)
- Repurchase

When making strategic decisions about your hybrid and multicloud architectures,
it's important to consider the feasibility of your strategy from a cost and time
perspective. You might want to consider a phased migration approach, starting
with lifting and shifting or replatforming and then refactoring or
rearchitecting as the next step. Typically, lifting and shifting helps to
optimize applications from an
infrastructure perspective. After applications are running in the cloud, it's
easier to use and integrate cloud services to further optimize them using
cloud-first architectures and capabilities. Also, these applications can still
communicate with other environments over a hybrid network connection.

For example, you can refactor or rearchitect a large, monolithic VM-based
application and turn it into several independent microservices, based on a
cloud-based microservice architecture. In this example, the microservices
architecture uses Google Cloud managed container services like
[Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine)
or
[Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run).
However, if the architecture or infrastructure of an application isn't supported
in the target cloud environment as it is, you might consider starting with
replatforming, refactoring, or rearchitecting your migration strategy to
overcome those constraints where feasible.

When using any of these migration approaches, consider modernizing your
applications (where applicable and feasible). Modernization can require adopting
and implementing
[Site Reliability Engineering (SRE)](https://cloud.google.com/sre)
or DevOps principles, such that you might also need to extend application
modernization to your private environment in a hybrid setup. Even though
implementing SRE principles involves engineering at its core, it's more of a
transformation process than a technical challenge. As such, it will likely
require procedural and cultural changes. To learn more about how the first step
to implementing SRE in an organization is to get leadership buy-in, see
[With SRE, failing to plan is planning to fail](https://cloud.google.com/blog/products/devops-sre/sre-success-starts-with-getting-leadership-on-board).

## Mix and match migration approaches

Each migration approach discussed here has certain strengths and weaknesses. A
key advantage of following a hybrid and multicloud strategy is that it isn't
necessary to settle on a single approach. Instead, you can decide which approach
works best for each workload or application stack, as shown in the following
diagram.

![Flowchart showing different approaches to migrating workloads from your cloud environment.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns/architectures-migration-approach.svg)

This conceptual diagram illustrates the various migration and modernization
paths or approaches that can be simultaneously applied to different workloads,
driven by the unique business, technical requirements, and objectives of each
workload or application.

In addition, it's not necessary that the same application stack components
follow the same migration approach or strategy. For example:

- The backend on-premises database of an application can be replatformed from self-hosted MySQL to a managed database using [Cloud SQL](https://docs.cloud.google.com/sql) in Google Cloud.
- The application frontend virtual machines can be refactored to run on containers using [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview), where Google manages the cluster configuration, including nodes, scaling, security, and other preconfigured settings.
- The on-premises hardware load balancing solution and web application firewall WAF capabilities can be replaced with [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing) and [Google Cloud Armor](https://docs.cloud.google.com/armor).

Choose rehost (lift and shift), if any of the following is true of the
workloads:

- They have a relatively small number of dependencies on their environment.
- They aren't considered worth refactoring, or refactoring before migration isn't feasible.
- They are based on third-party software.

Consider refactor (move and improve) for these types of workloads:

- They have dependencies that must be untangled.
- They rely on operating systems, hardware, or database systems that can't be accommodated in the cloud.
- They aren't making efficient use of compute or storage resources.
- They can't be deployed in an automated fashion without some effort.

Consider whether rebuild (remove and replace) meets your needs for these
types of workloads:

- They no longer satisfy current requirements.
- They can be incorporated with other applications that provide similar capabilities without compromising business requirements.
- They are based on third-party technology that has reached its end of life.
- They require third-party license fees that are no longer economical.

The
[Rapid Migration Program](https://docs.cloud.google.com/solutions/cloud-migration-program)
shows how Google Cloud helps customers to use best practices, lower risk,
control costs, and simplify their path to cloud success.