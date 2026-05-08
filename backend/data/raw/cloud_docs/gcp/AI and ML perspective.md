> [!IMPORTANT]
> This page provides a one-page view of all of the pages in the AI and ML perspective of the [Well-Architected Framework](https://docs.cloud.google.com/architecture/framework). You can print this page or save it in PDF format by using your browser's print function.
>
> This page doesn't have a table of contents. You can't use the links on this
> page to navigate within the page.

<br />


This document in the
[Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework)
describes principles and recommendations to help you to design, build, and
manage AI and ML workloads in Google Cloud that meet your
operational, security, reliability, cost, and performance goals.

The target audience for this document includes decision makers, architects,
administrators, developers, and operators who design, build, deploy, and
maintain AI and ML workloads in Google Cloud.

The following pages describe principles and recommendations that are specific
to AI and ML, for each pillar of the Well-Architected Framework:

- [AI and ML perspective: Operational excellence](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/operational-excellence)
- [AI and ML perspective: Security](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/security)
- [AI and ML perspective: Reliability](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/reliability)
- [AI and ML perspective: Cost optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization)
- [AI and ML perspective: Performance optimization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/performance-optimization)

## Contributors

Authors:

- [Benjamin Sadik](https://www.linkedin.com/in/benjaminhaimsadik) \| AI and ML Specialist Customer Engineer
- [Charlotte Gistelinck, PhD](https://www.linkedin.com/in/charlottegistelinck) \| Partner Engineer
- [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) \| Customer Engineer, AI/ML Specialist
- [Isaac Lo](https://www.linkedin.com/in/isaac-l-25525440) \| AI Business Development Manager
- [Kamilla Kurta](https://www.linkedin.com/in/kamillakurta) \| GenAI/ML Specialist Customer Engineer
- [Mohamed Fawzi](https://www.linkedin.com/in/fawzii) \| Benelux Security and Compliance Lead
- [Rick (Rugui) Chen](https://www.linkedin.com/in/rugui-chen) \| AI Infrastructure Field Solutions Architect
- [Sannya Dang](https://www.linkedin.com/in/thugiangdang) \| AI Solution Architect

<br />

Other contributors:

- [Daniel Lees](https://www.linkedin.com/in/daniellees) \| Cloud Security Architect
- [Gary Harmson](https://www.linkedin.com/in/garyharmson) \| Principal Architect
- [Jose Andrade](https://www.linkedin.com/in/jmandrade) \| Customer Engineer, SRE Specialist
- [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) \| Cross-Product Solution Developer
- [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) \| Partner Customer Engineer
- [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) \| Customer Engineer, Application Modernization Specialist
- [Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) \| Program Lead, Google Cloud Well-Architected Framework
- [Ryan Cox](https://www.linkedin.com/in/ryanlcox) \| Principal Architect
- [Samantha He](https://www.linkedin.com/in/samantha-he-05a98173) \| Technical Writer
- [Stef Ruinard](https://www.linkedin.com/in/stefruinard) \| Generative AI Field Solutions Architect
- [Wade Holmes](https://www.linkedin.com/in/wholmes) \| Global Solutions Director
- [Zach Seils](https://www.linkedin.com/in/zachseils) \| Networking Specialist

<br />

<br />

<br />


# AI and ML perspective: Operational excellence

This document in the
[Well-Architected Framework: AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml)
provides an overview of the principles and recommendations to build and operate
robust AI and ML systems on Google Cloud. These recommendations help you set up
foundational elements like observability, automation, and scalability. The
recommendations in this document align with the
[operational excellence pillar](https://docs.cloud.google.com/architecture/framework/operational-excellence)
of the Google Cloud Well-Architected Framework.

Operational excellence within the AI and ML domain is the ability to seamlessly
deploy, manage, and govern the AI and ML systems and pipelines that help drive
your organization's strategic objectives. Operational excellence lets you
respond efficiently to changes, reduce operational complexity, and ensure that
your operations remain aligned with business goals.

The recommendations in this document are mapped to the following core
principles:

- [Build a robust foundation for model development](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#build_a_robust_foundation_for_model_development)
- [Automate the model development lifecycle](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#automate_the_model-development_lifecycle)
- [Implement observability](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#implement_observability)
- [Build a culture of operational excellence](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#build_a_culture_of_operational_excellence)
- [Design for scalability](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#design_for_scalability)

## Build a robust foundation for model development

To develop and deploy scalable, reliable AI systems that help you achieve your
business goals, a robust model-development foundation is essential. Such a
foundation enables consistent workflows, automates critical steps in order to
reduce errors, and ensures that the models can scale with demand. A strong
model-development foundation ensures that your ML systems can be updated,
improved, and retrained seamlessly. The foundation also helps you to align your
models' performance with business needs, deploy impactful AI solutions quickly,
and adapt to changing requirements.

To build a robust foundation to develop your AI models, consider the following
recommendations.

### Define the problems and the required outcomes

Before you start any AI or ML project, you must have a clear understanding of
the business problems to be solved and the required outcomes. Start with an
outline of the business objectives and break the objectives down into measurable
key performance indicators (KPIs). To organize and document your problem
definitions and hypotheses in a Jupyter notebook environment, use tools like
[Vertex AI Workbench](https://docs.cloud.google.com/vertex-ai/docs/workbench/introduction).
To implement versioning for code and documents and to document your projects,
goals, and assumptions, use tools like Git. To develop and manage prompts for
generative AI applications, you can use
[Vertex AI Studio](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart).

### Collect and preprocess the necessary data

To implement data preprocessing and transformation, you can use
[Dataflow](https://docs.cloud.google.com/dataflow/docs/overview)
(for Apache Beam),
[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc-serverless/docs/overview)
(for Apache Spark), or
[BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction)
if an SQL-based process is appropriate. To validate schemas and detect
anomalies, use
[TensorFlow Data Validation (TFDV)](https://www.tensorflow.org/tfx/data_validation/get_started)
and take advantage of
[automated data quality scans](https://docs.cloud.google.com/bigquery/docs/data-quality-scan)
in BigQuery where applicable.

For generative AI, data quality includes accuracy, relevance, diversity, and
alignment with the required output characteristics. In cases where real-world
data is insufficient or imbalanced, you can generate synthetic data to help
improve model robustness and generalization. To create synthetic datasets based
on existing patterns or to augment training data for better model performance,
use
[BigQuery DataFrames and Gemini](https://cloud.google.com/blog/products/data-analytics/generate-synthetic-data-with-bigquery-dataframes-and-llms?e=48754805).
Synthetic data is particularly valuable for generative AI because it can help
improve prompt diversity and overall model robustness. When you build datasets
for fine-tuning generative AI models, consider using the synthetic data
generation capabilities in Vertex AI.

For generative AI tasks like fine-tuning or reinforcement learning from human
feedback (RLHF), ensure that labels accurately reflect the quality, relevance,
and safety of the generated outputs.

### Select an appropriate ML approach

When you design your model and parameters, consider the model's complexity and
computational needs. Depending on the task (such as classification, regression,
or generation), consider using
[Vertex AI custom training](https://docs.cloud.google.com/vertex-ai/docs/training/overview)
for custom model building or AutoML for simpler ML tasks. For
common applications, you can also access pretrained models through
[Vertex AI Model Garden](https://cloud.google.com/model-garden).
You can experiment with a variety of state-of-the-art foundation models for
various use cases, such as generating text, images, and code.

You might want to fine-tune a pretrained foundation model to achieve optimal
performance for your specific use case. For high-performance requirements in
custom training, configure
[Cloud Tensor Processing Units (TPUs)](https://docs.cloud.google.com/tpu)
or
[GPU resources](https://docs.cloud.google.com/compute/docs/gpus)
to accelerate the training and inference of deep-learning models, like large
language models (LLMs) and diffusion models.

### Set up version control for code, models, and data

To manage and deploy code versions effectively, use tools like GitHub or
GitLab. These tools provide robust collaboration features, branching strategies,
and integration with CI/CD pipelines to ensure a streamlined development
process.

Use appropriate solutions to manage each artifact of your ML system, like the
following examples:

- For code artifacts like container images and pipeline components, [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) provides a scalable storage solution that can help improve security. Artifact Registry also includes versioning and can integrate with [Cloud Build](https://docs.cloud.google.com/build/docs/overview) and [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview).
- To manage data artifacts, like datasets used for training and evaluation, use solutions like BigQuery or [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) for storage and versioning.
- To store metadata and pointers to data locations, use your version control system or a separate data catalog.

To maintain the consistency and versioning of your feature data, use
[Vertex AI Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore).
To track and manage model artifacts, including binaries and metadata, use
[Vertex AI Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction),
which lets you store, organize, and deploy model versions seamlessly.

To ensure model reliability, implement
[Vertex AI Model Monitoring](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview).
Detect data drift, track performance, and identify anomalies in production. For
generative AI systems, monitor shifts in output quality and safety compliance.

## Automate the model-development lifecycle

Automation helps you to streamline every stage of the AI and ML lifecycle.
Automation reduces manual effort and standardizes processes, which leads to
enhanced operational efficiency and a lower risk of errors. Automated workflows
enable faster iteration, consistent deployment across environments, and more
reliable outcomes, so your systems can scale and adapt seamlessly.

To automate the development lifecycle of your AI and ML systems, consider the
following recommendations.

### Use a managed pipeline orchestration system

Use
[Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction)
to automate every step of the ML lifecycle---from data preparation to model
training, evaluation, and deployment. To accelerate deployment and promote
consistency across projects, automate recurring tasks with
[scheduled pipeline runs](https://docs.cloud.google.com/vertex-ai/docs/pipelines/schedule-pipeline-run),
monitor workflows with
[execution metrics](https://docs.cloud.google.com/vertex-ai/docs/pipelines/metrics),
and develop
[reusable pipeline templates](https://docs.cloud.google.com/vertex-ai/docs/pipelines/create-pipeline-template)
for standardized workflows. These capabilities extend to generative AI models,
which often require specialized steps like
[prompt engineering](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies),
response filtering, and
[human-in-the-loop](https://cloud.google.com/discover/human-in-the-loop)
evaluation. For generative AI, Vertex AI Pipelines can automate these
steps, including the evaluation of generated outputs against quality metrics and
safety guidelines. To improve prompt diversity and model robustness, automated
workflows can also include data augmentation techniques.

### Implement CI/CD pipelines

To automate the building, testing, and deployment of ML models, use
Cloud Build.
This service is particularly effective when you run test suites for application
code, which ensures that the infrastructure, dependencies, and model packaging
meet your deployment requirements.

ML systems often need additional steps beyond code testing. For example, you
need to stress test the models under varying loads, perform bulk evaluations to
assess model performance across diverse datasets, and validate data integrity
before retraining. To simulate realistic workloads for stress tests, you can use
tools like
[Locust](https://locust.io/),
[Grafana k6](https://grafana.com/docs/k6/latest/),
or
[Apache JMeter](https://jmeter.apache.org/).
To identify bottlenecks, monitor key metrics like latency,
error rate, and resource utilization through
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).
For generative AI, the testing must also include evaluations that are specific
to the type of generated content, such as text quality, image fidelity, or code
functionality. These evaluations can involve automated metrics like
[perplexity](https://developers.google.com/machine-learning/glossary#perplexity)
for language models or human-in-the-loop evaluation for more nuanced aspects
like creativity and safety.

To implement testing and evaluation tasks, you can integrate
Cloud Build with other Google Cloud services. For example, you can
use Vertex AI Pipelines for automated model evaluation,
[BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction)
for large-scale data analysis, and Dataflow pipeline validation for
feature validation.

You can further enhance your CI/CD pipeline by using
[Vertex AI for continuous training](https://docs.cloud.google.com/vertex-ai/docs/pipelines/continuous-training-tutorial)
to enable automated retraining of models on new data. Specifically for
generative AI, to keep the generated outputs relevant and diverse, the
retraining might involve automatically updating the models with new training
data or prompts. You can use
[Vertex AI Model Garden](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models)
to select the latest base models that are available for tuning. This practice
ensures that the models remain current and optimized for your evolving business
needs.

### Implement safe and controlled model releases

To minimize risks and ensure reliable deployments, implement a model release
approach that lets you detect issues early, validate performance, and roll back
quickly when required.

To package your ML models and applications into container images and deploy
them, use
[Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview).
You can deploy your models to
[Vertex AI endpoints](https://docs.cloud.google.com/vertex-ai/docs/general/deployment).

Implement controlled releases for your AI applications and systems by using
strategies like
[canary releases](https://en.wikipedia.org/wiki/Canary_release).
For applications that use managed models like Gemini, we recommend that
you gradually release new application versions to a subset of users before the
full deployment. This approach lets you detect potential issues early,
especially when you use generative AI models where outputs can vary.

To release
fine-tuned models, you can use Cloud Deploy to manage the deployment of
the model versions, and use the canary release strategy to minimize risk. With
managed models and fine-tuned models, the goal of controlled releases is to test
changes with a limited audience before you release the applications and models
to all users.

For robust validation, use
[Vertex AI Experiments](https://docs.cloud.google.com/vertex-ai/docs/experiments/intro-vertex-ai-experiments)
to compare new models against existing ones, and use
[Vertex AI model evaluation](https://docs.cloud.google.com/vertex-ai/docs/evaluation/introduction)
to assess model performance. Specifically for generative AI, define evaluation
metrics that align with the intended use case and the potential risks. You can
use the Gen AI evaluation service in Vertex AI to assess metrics like
toxicity, coherence, factual accuracy, and adherence to safety guidelines.

To ensure deployment reliability, you need a robust rollback plan. For
traditional ML systems, use
[Vertex AI Model Monitoring](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview)
to detect data drift and performance degradation. For generative AI models, you
can track relevant metrics and set up alerts for shifts in output quality or the
emergence of harmful content by using Vertex AI model evaluation
along with Cloud Logging and Cloud Monitoring. Configure alerts based on
generative AI-specific metrics to trigger rollback procedures when necessary. To
track model lineage and revert to the most recent stable version, use insights
from
[Vertex AI Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction).

## Implement observability

The behavior of AI and ML systems can change over time due to changes in the
data or environment and updates to the models. This dynamic nature makes
observability crucial to detect performance issues, biases, or unexpected
behavior. This is especially true for generative AI models because the outputs
can be highly variable and subjective. Observability lets you proactively
address unexpected behavior and ensure that your AI and ML systems remain
reliable, accurate, and fair.

To implement observability for your AI and ML systems, consider the following
recommendations.

### Monitor performance continuously

Use metrics and success criteria for ongoing evaluation of models after
deployment.

You can use
[Vertex AI Model Monitoring](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview)
to proactively track model performance, identify training-serving skew and
prediction drift, and receive alerts to trigger necessary model retraining or
other interventions. To effectively monitor for training-serving skew, construct
a
[golden dataset](https://developers.google.com/machine-learning/glossary#golden-dataset)
that represents the ideal data distribution, and use
[TFDV](https://www.tensorflow.org/tfx/data_validation/get_started)
to analyze your training data and establish a baseline schema.

Configure Model Monitoring to compare the distribution of
input data against the golden dataset for automatic skew detection. For
traditional ML models, focus on
[metrics](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall)
like accuracy, precision, recall, F1-score, AUC-ROC, and log loss. Define custom
thresholds for alerts in Model Monitoring. For generative
AI, use the
[Gen AI evaluation service](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview)
to continuously monitor model output in production. You can also enable
automatic evaluation metrics for response quality, safety, instruction
adherence, grounding, writing style, and verbosity. To assess the generated
outputs for quality, relevance, safety, and adherence to guidelines, you can
incorporate
[human-in-the-loop](https://cloud.google.com/discover/human-in-the-loop)
evaluation.

Create feedback loops to automatically retrain models with
Vertex AI Pipelines when Model Monitoring triggers
an alert. Use these insights to improve your models continuously.

### Evaluate models during development

Before you deploy your LLMs and other generative AI models, thoroughly evaluate
them during the development phase. Use Vertex AI model evaluation to
achieve optimal performance and to mitigate risk. Use
[Vertex AI rapid evaluation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/run-evaluation)
to let Google Cloud automatically run evaluations based on the dataset and
prompts that you provide.

You can also define and integrate custom metrics that are specific to your use
case. For feedback on generated content, integrate human-in-the-loop workflows
by using Vertex AI Model Evaluation.

Use
[adversarial testing](https://developers.google.com/machine-learning/guides/adv-testing)
to identify vulnerabilities and potential failure modes. To identify and
mitigate potential biases, use techniques like subgroup analysis and
counterfactual generation. Use the insights gathered from the evaluations that
were completed during the development phase to define your model monitoring
strategy in production. Prepare your solution for continuous monitoring as
described in the
[Monitor performance continuously](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#automated-performance-monitoring)
section of this document.

### Monitor for availability

To gain visibility into the health and performance of your deployed endpoints
and infrastructure, use
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).
For your Vertex AI endpoints, track key metrics like request
rate, error rate, latency, and resource utilization, and set up alerts for
anomalies. For more information, see
[Cloud Monitoring metrics for Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/general/monitoring-metrics).

Monitor the health of the underlying infrastructure, which can include
Compute Engine instances, Google Kubernetes Engine (GKE) clusters, and TPUs and
GPUs. Get automated optimization recommendations from
[Active Assist](https://docs.cloud.google.com/recommender/docs/whatis-activeassist).
If you use autoscaling, monitor the scaling behavior to ensure that autoscaling
responds appropriately to changes in traffic patterns.

Track the status of model deployments, including canary releases and rollbacks,
by integrating Cloud Deploy with Cloud Monitoring. In addition, monitor
for potential security threats and vulnerabilities by using
[Security Command Center](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview).

### Set up custom alerts for business-specific thresholds

For timely identification and rectification of anomalies and issues, set up
custom alerting based on thresholds that are specific to your business
objectives. Examples of Google Cloud products that you can use to
implement a custom alerting system include the following:

- [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview): Collect, store, and analyze logs from all components of your AI and ML system.
- Cloud Monitoring: Create custom dashboards to visualize key metrics and trends, and define custom metrics based on your needs. Configure alerts to get notifications about critical issues, and integrate the alerts with your incident management tools like PagerDuty or Slack.
- [Error Reporting](https://docs.cloud.google.com/error-reporting/docs/grouping-errors): Automatically capture and analyze errors and exceptions.
- [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview): Analyze the performance of distributed systems and identify bottlenecks. Tracing is particularly useful for understanding latency between different components of your AI and ML pipeline.
- [Cloud Profiler](https://docs.cloud.google.com/profiler/docs/about-profiler): Continuously analyze the performance of your code in production and identify performance bottlenecks in CPU or memory usage.

## Build a culture of operational excellence

Shift the focus from just building models to building sustainable, reliable, and
impactful AI solutions. Empower teams to continuously learn, innovate, and
improve, which leads to faster development cycles, reduced errors, and increased
efficiency. By prioritizing automation, standardization, and ethical
considerations, you can ensure that your AI and ML initiatives consistently
deliver value, mitigate risks, and promote responsible AI development.

To build a culture of operational excellence for your AI and ML systems,
consider the following recommendations.

### Champion automation and standardization

To emphasize efficiency and consistency, embed automation and standardized
practices into every stage of the AI and ML lifecycle. Automation reduces manual
errors and frees teams to focus on innovation. Standardization ensures that
processes are repeatable and scalable across teams and projects.

### Prioritize continuous learning and improvement

Foster an environment where ongoing education and experimentation are core
principles. Encourage teams to stay up-to-date with AI and ML advancements, and
provide opportunities to learn from past projects. A culture of curiosity and
adaptation drives innovation and ensures that teams are equipped to meet new
challenges.

### Cultivate accountability and ownership

Build trust and alignment with clearly defined roles, responsibilities, and
metrics for success. Empower teams to make informed decisions within these
boundaries, and establish transparent ways to measure progress. A sense of
ownership motivates teams and ensures collective responsibility for outcomes.

### Embed AI ethics and safety considerations

Prioritize considerations for ethics in every stage of development. Encourage
teams to think critically about the impact of their AI solutions, and foster
discussions on fairness, bias, and societal impact. Clear principles and
accountability mechanisms ensure that your AI systems align with organizational
values and promote trust.

## Design for scalability

To accommodate growing data volumes and user demands and to maximize the value
of AI investments, your AI and ML systems need to be scalable. The systems must
adapt and perform optimally to avoid performance bottlenecks that hinder
effectiveness. When you design for scalability, you ensure that the AI
infrastructure can handle growth and maintain responsiveness. Use scalable
infrastructure, plan for capacity, and employ strategies like horizontal scaling
and managed services.

To design your AI and ML systems for scalability, consider the following
recommendations.

### Plan for capacity and quotas

Assess future growth, and plan your infrastructure capacity and resource quotas
accordingly. Work with business stakeholders to understand the projected growth
and then define the infrastructure requirements accordingly.

Use
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)
to analyze historical resource utilization, identify trends, and project future
needs. Conduct regular load testing to simulate workloads and identify
bottlenecks.

Familiarize yourself with
[Google Cloud quotas](https://docs.cloud.google.com/docs/quotas/view-manage)
for the services that you use, such as Compute Engine, Vertex AI, and
Cloud Storage. Proactively request quota increases through
the Google Cloud console, and justify the increases with data from forecasting
and load testing.
[Monitor quota usage](https://docs.cloud.google.com/monitoring/alerts/using-quota-metrics)
and set up alerts to get notifications when the usage approaches the quota
limits.

To optimize resource usage based on demand, rightsize your resources, use
[Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms)
for fault-tolerant batch workloads, and implement autoscaling.

### Prepare for peak events

Ensure that your system can handle sudden spikes in traffic or workload during
peak events. Document your peak event strategy and conduct regular drills to
test your system's ability to handle increased load.

To aggressively scale up resources when the demand spikes, configure autoscaling
policies in
[Compute Engine](https://docs.cloud.google.com/compute/docs/autoscaler)
and
[GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler).
For predictable peak patterns, consider using
[predictive autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling).
To trigger autoscaling based on application-specific signals, use custom metrics
in Cloud Monitoring.

Distribute traffic across multiple application instances by using
[Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview).
Choose an appropriate load balancer type based on your application's needs. For
geographically distributed users, you can use global load balancing to route
traffic to the nearest available instance. For complex microservices-based
architectures, consider using
[Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview).

Cache static content at the edge of Google's network by using
[Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview).

To cache frequently accessed data, use one of the following fully managed
in-memory data store services:

- [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)
- [Memorystore for Redis](https://docs.cloud.google.com/memorystore/docs/redis/memorystore-for-redis-overview)
- [Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)

Decouple the components of your system by using
[Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview)
for real-time messaging and Cloud Tasks for asynchronous task
execution

### Scale applications for production

To ensure scalable serving in production, you can use managed services like
[Vertex AI distributed training](https://docs.cloud.google.com/vertex-ai/docs/training/distributed-training)
and
[Vertex AI Inference](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview).
Vertex AI Inference lets you configure the
[machine types](https://docs.cloud.google.com/vertex-ai/docs/predictions/configure-compute#machine-types)
for your prediction nodes when you deploy a model to an endpoint or request
batch predictions. For some configurations, you can add GPUs. Choose the
appropriate machine type and accelerators to optimize latency, throughput, and
cost.

To scale complex AI and Python applications and custom workloads across
distributed computing resources, you can use
[Ray on Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/open-source/ray-on-vertex-ai/overview).
This feature can help optimize performance and enables seamless integration with
Google Cloud services. Ray on Vertex AI simplifies distributed
computing by handling cluster management, task scheduling, and data transfer. It
integrates with other Vertex AI services like training,
prediction, and pipelines. Ray provides fault tolerance and autoscaling, and
helps you adapt the infrastructure to changing workloads. It offers a unified
framework for distributed training, hyperparameter tuning, reinforcement
learning, and model serving. Use Ray for distributed data preprocessing with
[Dataflow](https://docs.cloud.google.com/dataflow/docs/overview)
or
[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc/docs/concepts/overview),
accelerated model training, scalable hyperparameter tuning, reinforcement
learning, and parallelized batch prediction.

## Contributors

Authors:

- [Charlotte Gistelinck, PhD](https://www.linkedin.com/in/charlottegistelinck) \| Partner Engineer
- [Sannya Dang](https://www.linkedin.com/in/thugiangdang) \| AI Solution Architect
- [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) \| Customer Engineer, AI/ML Specialist

<br />

Other contributors:

- [Gary Harmson](https://www.linkedin.com/in/garyharmson) \| Principal Architect
- [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) \| Cross-Product Solution Developer
- [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) \| Partner Customer Engineer
- [Ryan Cox](https://www.linkedin.com/in/ryanlcox) \| Principal Architect
- [Stef Ruinard](https://www.linkedin.com/in/stefruinard) \| Generative AI Field Solutions Architect

<br />

<br />

<br />


# AI and ML perspective: Security

This document in the
[Well-Architected Framework: AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml)
provides an overview of principles and recommendations to ensure that your AI
and ML deployments meet the security and compliance requirements of your
organization. The recommendations in this document align with the
[security pillar](https://docs.cloud.google.com/architecture/framework/security)
of the Google Cloud Well-Architected Framework.

Secure deployment of AI and ML workloads is a critical requirement, particularly
in enterprise environments. To meet this requirement, you need to adopt a
holistic security approach that starts from the initial conceptualization of
your AI and ML solutions and extends to development, deployment, and ongoing
operations. Google Cloud offers robust tools and services that are designed to
help secure your AI and ML workloads.

The recommendations in this document are mapped to the following core
principles:

- [Define clear goals and requirements](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#define_clear_goals_and_requirements)
- [Keep data secure and prevent loss or mishandling](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#keep_data_secure_and_prevent_loss_or_mishandling)
- [Keep AI pipelines secure and robust against tampering](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#keep_ai_pipelines_secure_and_robust_against_tampering)
- [Deploy on secure systems with secure tools and artifacts](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#deploy_on_secure_systems_with_secure_tools_and_artifacts)
- [Verify and protect inputs](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#verify_and_protect_inputs)
- [Monitor, evaluate, and prepare to respond to outputs](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#monitor_evaluate_and_prepare_to_respond_to_outputs)

For more information about AI security, you can also review the following
resources:

- [Google Cloud's Secure AI Framework (SAIF)](https://safety.google/cybersecurity-advancements/saif/) provides a comprehensive guide for building secure and responsible AI systems. It outlines key principles and best practices for addressing security and compliance considerations throughout the AI lifecycle.
- To learn more about Google Cloud's approach to trust in AI, see our [compliance resource center](https://cloud.google.com/compliance).

## Define clear goals and requirements

Effective AI and ML security is a core component of your overarching business
strategy. It's easier to integrate the required security and compliance controls
early in your design and development process, instead of adding controls after
development.

From the start of your design and development process, make decisions that are
appropriate for your specific risk environment and your specific business
priorities. For example, overly restrictive security measures might protect data
but also impede innovation and slow down development cycles. However, a lack of
security can lead to data breaches, reputational damage, and financial losses,
which are detrimental to business goals.

To define clear goals and requirements, consider the following
recommendations.

### Align AI and ML security with business goals

To align your AI and ML security efforts with your business goals, use a
strategic approach that integrates security into every stage of the AI
lifecycle. To follow this approach, do the following:

1. **Define clear business objectives and security requirements**:

   - **Identify key business goals**: Define clear business objectives that your AI and ML initiatives are designed to achieve. For example, your objectives might be to improve customer experience, optimize operations, or develop new products.
   - **Translate goals into security requirements**: When you clarify your business goals, define specific security requirements to support those goals. For example, your goal might be to use AI to personalize customer recommendations. To support that goal, your security requirements might be to protect customer data privacy and prevent unauthorized access to recommendation algorithms.
2. **Balance security with business needs**:

   - **Conduct risk assessments**: Identify potential security threats and vulnerabilities in your AI systems.
   - **Prioritize security measures**: Base the priority of these security measures upon their potential impact on your business goals.
   - **Analyze the costs and benefits**: Ensure that you invest in the most effective solutions. Consider the costs and benefits of different security measures.
   - **Shift left on security**: Implement security best practices early in the design phase, and adapt your safety measures as business needs change and threats emerge.

### Identify potential attack vectors and risks

Consider potential attack vectors that could affect your AI systems, such as
data poisoning, model inversion, or adversarial attacks. Continuously monitor
and assess the evolving attack surface as your AI system develops, and keep
track of new threats and vulnerabilities. Remember that changes in your AI
systems can also introduce changes to their attack surface.

To mitigate potential legal and reputational risks, you also need to address
compliance requirements related to data privacy, algorithmic bias, and other
relevant regulations.

To anticipate potential threats and vulnerabilities early and make design
choices that mitigate risks, adopt a *secure by design* approach.

Google Cloud provides a comprehensive suite of tools and services to help
you implement a secure by design approach:

- **[Cloud posture management](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)**: Use Security Command Center to identify potential vulnerabilities and misconfigurations in your AI infrastructure.
- **[Attack exposure scores and attack paths](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn)**: Refine and use the attack exposure scores and attack paths that Security Command Center generates.
- **[Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence)**: Stay informed about new threats and attack techniques that emerge to target AI systems.
- **[Logging and Monitoring](https://docs.cloud.google.com/stackdriver/docs)**: Track the performance and security of your AI systems, and detect any anomalies or suspicious activities. Conduct regular security audits to identify and address potential vulnerabilities in your AI infrastructure and models.
- **[Vulnerability management](https://cloud.google.com/security/resources/datasheets/consulting-services-threat-and-vulnerability-management)**: Implement a vulnerability management process to track and remediate security vulnerabilities in your AI systems.

For more information, see
[Secure by Design at Google](https://research.google/pubs/secure-by-design-at-google/)
and
[Implement security by design](https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design).

## Keep data secure and prevent loss or mishandling

Data is a valuable and sensitive asset that must be kept secure. Data security
helps you to maintain user trust, support your business objectives, and meet
your compliance requirements.

To help keep your data secure, consider the following recommendations.

### Adhere to data minimization principles

To ensure data privacy, adhere to the principle of data minimization. To
minimize data, don't collect, keep, or use data that's not strictly necessary
for your business goals. Where possible, use synthetic or fully anonymized data.

Data collection can help drive business insights and analytics, but it's crucial
to exercise discretion in the data collection process. If you collect personally
identifiable information (PII) about your customer, reveal sensitive information,
or create bias or controversy, then you might build biased ML models.

You can use Google Cloud features to help you improve data minimization
and data privacy for various use cases:

- To de-identify your data and also preserve its utility, apply transformation methods like pseudonymization, de-identification, and generalization such as bucketing. To implement these methods, you can use [Sensitive Data Protection](https://docs.cloud.google.com/architecture/de-identification-re-identification-pii-using-cloud-dlp).
- To enrich data and mitigate potential bias, you can use a [Vertex AI data labeling job](https://docs.cloud.google.com/vertex-ai/docs/samples/aiplatform-create-data-labeling-job-sample). The data labeling process adds informative and meaningful tags to raw data, which transforms it into structured training data for ML models. Data labeling adds specificity to the data and reduces ambiguity.
- To help protect resources from prolonged access or manipulation, use Cloud Storage features to [control data lifecycles](https://docs.cloud.google.com/storage/docs/control-data-lifecycles).

For best practices about how to implement data encryption, see
[data encryption at rest and in transit](https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design#encrypt_data_at_rest_and_in_transit)
in the Well-Architected Framework.

### Monitor data collection, storage, and transformation

Your AI application's training data poses the largest risks for the
introduction of bias and data leakage. To stay compliant and manage data across
different teams, establish a data governance layer to monitor data flows,
transformations, and access. Maintain logs for data access and manipulation
activities. The logs help you audit data access, detect unauthorized access
attempts, and prevent unwanted access.

You can use Google Cloud features to help you implement data governance
strategies:

- To establish an organization-wide or department-wide data governance platform, use [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs). A data governance platform can help you to centrally discover, manage, monitor, and govern data and AI artifacts across your data platforms. The data governance platform also provides access to trusted users. You can perform the following tasks with Knowledge Catalog:
  - Manage data lineage. BigQuery can also provide column-level lineage.
  - Manage data quality checks and data profiles.
  - Manage data discovery, exploration, and processing across different data marts.
  - Manage feature metadata and model artifacts.
  - Create a business glossary to manage metadata and establish a standardized vocabulary.
  - [Enrich the metadata](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata) with context through aspects and aspect types.
  - Unify data governance across BigLake and open-format tables like Iceberg and Delta.
  - Build a [data mesh](https://docs.cloud.google.com/architecture/data-mesh) to decentralize data ownership among data owners from different teams or domains. This practice adheres to data security principles and it can help improve data accessibility and operational efficiency.
  - [Inspect and send sensitive data results](https://docs.cloud.google.com/sensitive-data-protection/docs/add-aspects-inspection-job) from BigQuery to Knowledge Catalog.
- To build a unified open [lakehouse](https://cloud.google.com/discover/what-is-a-data-lakehouse) that is well-governed, integrate your data lakes and warehouses with managed metastore services like [Dataproc Metastore](https://docs.cloud.google.com/dataproc-metastore/docs/overview) and [Lakehouse runtime catalog](https://docs.cloud.google.com/biglake/docs/about-blms). An open lakehouse uses open table formats that are compatible with different data processing engines.
- To schedule the monitoring of features and feature groups, use [Vertex AI Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/monitor-features#create-feature-monitor).
- To scan your Vertex AI datasets at the organization, folder, or project level, use [Sensitive data discovery for Vertex AI](https://docs.cloud.google.com/sensitive-data-protection/docs/discovery-for-vertex-ai). You can also [analyze the data profiles](https://docs.cloud.google.com/sensitive-data-protection/docs/analyze-data-profiles) that are stored in BigQuery.
- To capture real-time logs and collect metrics related to data pipelines, use [Cloud Logging](https://docs.cloud.google.com/logging/docs/view/streaming-live-tailing) and [Cloud Monitoring](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs). To collect audit trails of API calls, use [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit). Don't log PII or confidential data in experiments or in different log servers.

### Implement role-based access controls with least privilege principles

Implement role-based access controls (RBAC) to assign different levels of access
based on user roles. Users must have only the minimum permissions that are
necessary to let them perform their role activities. Assign permissions based on
the
[principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege)
so that users have only the access that they need, such as no-access, read-only,
or write.

RBAC with least privilege is important for security when your
organization uses sensitive data that resides in data lakes, in feature stores,
or in hyperparameters for model training. This practice helps you to prevent
data theft, preserve model integrity, and limit the surface area for accidents
or attacks.

To help you implement these access strategies, you can use the following
Google Cloud features:

- To implement access granularity, consider the following options:

  - Map the IAM roles of different products to a user, group, or service account to allow granular access. Map these roles based on your project needs, access patterns, or [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).
  - Set [IAM policies with conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to manage granular access to your data, model, and model configurations, such as code, resource settings, and hyperparameters.
  - Explore application-level granular access that helps you secure
    sensitive data that you audit and share outside of your team.

    - **Cloud Storage** : Set IAM policies on [buckets and managed folders](https://docs.cloud.google.com/storage/docs/access-control/iam).
    - **BigQuery** : Use [IAM roles and permissions](https://docs.cloud.google.com/bigquery/docs/access-control) for datasets and resources within datasets. Also, restrict access at the [row-level](https://docs.cloud.google.com/bigquery/docs/managing-row-level-security) and [column-level](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro) in BigQuery.
- To limit access to certain resources, you can use
  [principal access boundary (PAB) policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies-create).
  You can also use
  [Privileged Access Manager](https://docs.cloud.google.com/iam/docs/temporary-elevated-access)
  to control just-in-time, temporary privilege elevation for select
  principals. Later, you can view the audit logs for this Privileged Access Manager
  activity.

- To restrict access to resources based on the IP address and end user
  device attributes, you can
  [extend Identity-Aware Proxy (IAP) access policies](https://docs.cloud.google.com/iap/docs/cloud-iap-context-aware-access-howto).

- To create access patterns for different user groups, you can use
  [Vertex AI access control with IAM](https://docs.cloud.google.com/vertex-ai/docs/general/access-control)
  to combine the predefined or custom roles.

- To protect Vertex AI Workbench instances by using context-aware access
  controls, use
  [Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs)
  and
  [Chrome Enterprise Premium](https://docs.cloud.google.com/beyondcorp-enterprise/docs/access-levels).
  With this approach, access is evaluated each time a user authenticates to
  the instance.

### Implement security measures for data movement

Implement secure perimeters and other measures like encryption and restrictions
on data movement. These measures help you to prevent data exfiltration and data
loss, which can cause financial losses, reputational damage, legal liabilities,
and a disruption to business operations.

To help prevent data exfiltration and loss on Google Cloud, you can use a
combination of security tools and services.

To implement encryption, consider the following:

- To gain more control over encryption keys, use customer-managed encryption keys (CMEKs) in Cloud KMS. When you use CMEKs, the following CMEK-integrated services encrypt data at rest for you:
  - [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/general/cmek)
  - [Cloud Storage](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys)
  - [Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/cmek)
  - [Spanner](https://docs.cloud.google.com/spanner/docs/cmek)
  - [BigQuery](https://docs.cloud.google.com/bigquery/docs/customer-managed-encryption)
- To help protect your data in Cloud Storage, use server-side encryption to store your CMEKs. If you manage CMEKs on your own servers, server-side encryption can help protect your CMEKs and associated data, even if your CMEK storage system is compromised.
- To encrypt data in transit, use HTTPS for all of your API calls to AI and ML services. To enforce HTTPS for your applications and APIs, use [HTTPS load balancers](https://docs.cloud.google.com/load-balancing/docs/https).

For more best practices about how to encrypt data, see
[Encrypt data at rest and in transit](https://docs.cloud.google.com/architecture/framework/security/implement-security-by-design#encrypt_data_at_rest_and_in_transit)
in the security pillar of the Well-Architected Framework.

To implement perimeters, consider the following:

- To create a security boundary around your AI and ML resources and prevent data exfiltration from your Virtual Private Cloud (VPC), use [VPC Service Controls](https://docs.cloud.google.com/vertex-ai/docs/general/vpc-service-controls) to define a service perimeter. Include your AI and ML resources and sensitive data in the perimeter. To control data flow, configure ingress and egress rules for your perimeter.
- To restrict inbound and outbound traffic to your AI and ML resources, [configure firewall rules](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview). Implement policies that deny all traffic by default and explicitly allow only the traffic that meets your criteria. For a policy example, see [Example: Deny all external connections except to specific ports](https://docs.cloud.google.com/firewall/docs/network-firewall-policy-examples#deny-all-external-connections-except-to-specific-ports).

To implement restrictions on data movement, consider the following:

- To share data and to scale across privacy boundaries in a secure environment, use [BigQuery sharing](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction) and [BigQuery data clean rooms](https://docs.cloud.google.com/bigquery/docs/data-clean-rooms), which provide a robust security and privacy framework.
- To share data directly into built-in destinations from business intelligence dashboards, use [Looker Action Hub](https://docs.cloud.google.com/looker/docs/action-hub), which provides a secure cloud environment.

### Guard against data poisoning

*Data poisoning* is a type of cyberattack in which attackers inject malicious
data into training datasets to manipulate model behavior or to degrade
performance. This cyberattack can be a serious threat to ML training systems.
To protect the validity and quality of the data, maintain practices that guard
your data. This approach is crucial for consistent unbiasedness, reliability,
and integrity of your model.

To track inconsistent behavior, transformation, or unexpected access to your
data, set up comprehensive
[monitoring and alerting](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#monitor-data-collection-storage-and-transformation)
for data pipelines and ML pipelines.

Google Cloud features can help you implement more protections against data
poisoning:

- To validate data integrity, consider the following:

  - Implement robust data validation checks before you use the data for training. Verify data formats, ranges, and distributions. You can use the automatic data quality capabilities in [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview).
  - Use Sensitive Data Protection with Model Armor to take advantage of comprehensive data loss prevention capabilities. For more information, see [Model Armor key concepts](https://docs.cloud.google.com/security-command-center/docs/key-concepts-model-armor). Sensitive Data Protection with Model Armor lets you discover, classify, and protect sensitive data such as intellectual property. These capabilities can help you prevent the unauthorized exposure of sensitive data in LLM interactions.
  - To detect anomalies in your training data that might indicate data poisoning, use [anomaly detection in BigQuery](https://docs.cloud.google.com/bigquery/docs/anomaly-detection-overview) with statistical methods or ML models.
- To prepare for robust training, do the following:

  - Employ [ensemble methods](https://en.wikipedia.org/wiki/Ensemble_learning) to reduce the impact of poisoned data points. Train multiple models on different subsets of the data with [hyperparameter tuning](https://docs.cloud.google.com/vertex-ai/docs/training/hyperparameter-tuning-overview).
  - Use data augmentation techniques to balance the distribution of data across datasets. This approach can reduce the impact of data poisoning and lets you add adversarial examples.
- To incorporate human review for training data or model outputs, do the
  following:

  - Analyze model evaluation metrics to detect potential biases, anomalies, or unexpected behavior that might indicate data poisoning. For details, see [Model evaluation in Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/evaluation/introduction).
  - Take advantage of domain expertise to evaluate the model or application and identify suspicious patterns or data points that automated methods might not detect. For details, see [Gen AI evaluation service overview](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview).

For best practices about how to create data platforms that focus on
infrastructure and data security, see the
[Implement security by design](https://docs.cloud.google.com/architecture/framework/security/data-security)
principle in the Well-Architected Framework.

## Keep AI pipelines secure and robust against tampering

Your AI and ML code and the code-defined pipelines are critical assets. Code
that isn't secured can be tampered with, which can lead to data leaks,
compliance failure, and disruption of critical business activities. Keeping your
AI and ML code secure helps to ensure the integrity and value of your models and
model outputs.

To keep AI code and pipelines secure, consider the following recommendations.

### Use secure coding practices

To prevent vulnerabilities, use secure coding practices when you develop your
models. We recommend that you implement AI-specific input and output
validation, manage all of your software dependencies, and consistently embed
secure coding principles into your development. Embed security into every stage
of the AI lifecycle, from data preprocessing to your final application code.

To implement rigorous validation, consider the following:

- To prevent model manipulation or system exploits, validate and sanitize
  inputs and outputs in your code.

  - Use Model Armor or fine-tuned LLMs to automatically screen prompts and responses for common risks.
  - Implement data validation within your data ingestion and preprocessing scripts for data types, formats, and ranges. For [Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction) or BigQuery, you can use Python to implement this data validation.
  - Use coding assistant LLM agents, like [CodeMender](https://deepmind.google/blog/introducing-codemender-an-ai-agent-for-code-security/), to improve code security. Keep a human in the loop to validate its proposed changes.
- To manage and secure your AI model API endpoints, use
  [Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee),
  which includes configurable features like request validation, traffic
  control, and authentication.

- To help mitigate risk throughout the AI lifecycle, you can use
  [AI Protection](https://docs.cloud.google.com/security-command-center/docs/ai-protection-overview)
  to do the following:

  - Discover AI inventory in your environment.
  - Assess the inventory for potential vulnerabilities.
  - Secure AI assets with controls, policies, and protections.
  - Manage AI systems with detection, investigation, and response capabilities.

To help secure the code and artifact dependencies in your CI/CD pipeline,
consider the following:

- To address the risks that open-source library dependencies can introduce to your project, use [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis) with [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) to detect known vulnerabilities. Use and maintain the approved versions of libraries. Store your custom ML packages and vetted dependencies in a private Artifact Registry repository.
- To embed dependency scanning into your Cloud Build MLOps pipelines, use [Binary Authorization](https://docs.cloud.google.com/build/docs/securing-builds/secure-deployments-to-run-gke). Enforce policies that allow deployments only if your code's container images pass the security checks.
- To get security information about your software supply chain, use [dashboards](https://docs.cloud.google.com/monitoring/dashboards) in the Google Cloud console that provide details about sources, builds, artifacts, deployments, and runtimes. This information includes vulnerabilities in build artifacts, build provenance, and Software Bill of Materials (SBOM) dependency lists.
- To assess the maturity level of your software supply chain security, use the [Supply chain Levels for Software Artifacts (SLSA) framework](https://slsa.dev/spec/v0.1/levels).

To consistently embed secure coding principles into every stage of development,
consider the following:

- To prevent the exposure of sensitive data from model interactions, use Logging with Sensitive Data Protection. When you use these products together, you can control what data your AI applications and pipeline components log, and hide sensitive data.
- To implement the principle of least privilege, ensure that the service accounts that you use for your Vertex AI custom jobs, pipelines, and deployed models have only the minimum required IAM permissions. For more information, see [Implement role-based access controls with least privilege principles](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#implement_role_based_access_controls_with_least_privilege_principles).
- To help secure and protect your pipelines and build artifacts, understand the security configurations (VPC and VPC Service Controls) in the environment your code runs in.

### Protect pipelines and model artifacts from unauthorized access

Your model artifacts and pipelines are intellectual property, and their
training data also contains proprietary information. To protect model weights,
files, and deployment configurations from tampering and vulnerabilities, store
and access these artifacts with improved security. Implement different access
levels for each artifact based on user roles and needs.

To help secure your model artifacts, consider the following:

- To protect model artifacts and other sensitive files, encrypt them with Cloud KMS. This encryption helps to protect data at rest and in transit, even if the underlying storage becomes compromised.
- To help secure access to your files, store them in Cloud Storage and configure access controls.
- To track any incorrect or inadequate configurations and any drift from your defined standards, use Security Command Center to configure [security postures](https://docs.cloud.google.com/security-command-center/docs/security-posture-overview).
- To enable fine-grained access control and encryption at rest, store your model artifacts in [Vertex AI Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction). For additional security, create a digital signature for packages and containers that are produced during the approved build processes.
- To benefit from Google Cloud's enterprise-grade security, use models that are available in Model Garden. Model Garden provides Google's proprietary models and it offers [third-party models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models#model_security_scanning) from featured partners.
- To enforce central management for all user and group lifecycles and to
  enforce the principle of least privilege, use IAM.

  - Create and use dedicated, least-privilege service accounts for your MLOps pipelines. For example, a training pipeline's service account has the permissions to read data from only a specific Cloud Storage bucket and to write model artifacts to Model Registry.
  - Use IAM Conditions to enforce conditional, attribute-based access control. For example, a condition allows a service account to trigger a Vertex AI pipeline only if the request originates from a trusted Cloud Build trigger.

To help secure your deployment pipelines, consider the following:

- To manage MLOps stages on Google Cloud services and resources,
  use Vertex AI Pipelines,
  which can integrate with other services and provide low-level access
  control. When you re-execute the pipelines, ensure that you perform
  [Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview)
  and
  [responsible AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/responsible-ai)
  checks before you deploy the model artifacts. These checks can help you
  detect or prevent the following security issues:

  - Unauthorized changes, which can indicate model tampering.
  - Cross-site scripting (XSS), which can indicate compromised container images or dependencies.
  - Insecure endpoints, which can indicate misconfigured serving infrastructure.
- To help secure model interactions during inference, use private
  endpoints based on
  [Private Service Connect](https://docs.cloud.google.com/vertex-ai/docs/predictions/private-service-connect)
  with
  [prebuilt containers](https://docs.cloud.google.com/vertex-ai/docs/training/exporting-model-artifacts#pickle)
  or
  [custom containers](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-custom-container).
  Create model signatures with a predefined input and output schema.

- To automate code change tracking, use Git for source code management,
  and integrate version control with robust CI/CD pipelines.

For more information, see
[Securing the AI Pipeline](https://cloud.google.com/blog/topics/threat-intelligence/securing-ai-pipeline/).

### Enforce lineage and tracking

To help meet the regulatory compliance requirements that you might have, enforce
lineage and tracking of your AI and ML assets. Data lineage and tracking
provides extensive change records for data, models, and code. Model provenance
provides transparency and accountability throughout the AI and ML lifecycle.

To effectively enforce lineage and tracking in Google Cloud, consider the
following tools and services:

- To track the lineage of models, datasets, and artifacts that are automatically encrypted at rest, use [Vertex ML Metadata](https://docs.cloud.google.com/vertex-ai/docs/ml-metadata/introduction#ml_artifact_lineage). Log metadata about data sources, transformations, model parameters, and experiment results.
- To track the [lineage of pipeline artifacts](https://docs.cloud.google.com/vertex-ai/docs/pipelines/lineage) from Vertex AI Pipelines, and to search for model and dataset resources, you can use Knowledge Catalog. Track individual pipeline artifacts when you want to perform debugging, troubleshooting, or a root cause analysis. To track your entire MLOps pipeline, which includes the lineage of pipeline artifacts, use [Vertex ML Metadata](https://docs.cloud.google.com/vertex-ai/docs/ml-metadata/analyzing). Vertex ML Metadata also lets you analyze the resources and runs. Model Registry applies and manages the versions of each model that you store.
- To track API calls and administrative actions, enable [audit logs for Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/general/audit-logging). [Analyze audit logs](https://docs.cloud.google.com/logging/docs/analyze/query-and-view) with Observability Analytics to understand who accessed or modified data and models, and when. You can also [route logs to third-party destinations](https://docs.cloud.google.com/logging/docs/export/pubsub#integrate-thru-pubsub).

## Deploy on secure systems with secure tools and artifacts

Ensure that your code and models run in a secure environment. This environment
must have a robust access control system and provide security assurances for the
tools and artifacts that you deploy.

To deploy your code on secure systems, consider the following
recommendations.

### Train and deploy models in a secure environment

To maintain system integrity, confidentiality, and availability for your AI and
ML systems, implement stringent access controls that prevent unauthorized
resource manipulation. This defense helps you to do the following:

- Mitigate model tampering that could produce unexpected or conflicting results.
- Protect your training data from privacy violations.
- Maintain service uptime.
- Maintain regulatory compliance.
- Build user trust.

To train your ML models in an environment with improved security, use managed
services in Google Cloud like Cloud Run,
GKE, and Managed Service for Apache Spark. You can also use
[Vertex AI serverless training](https://docs.cloud.google.com/vertex-ai/docs/training/overview).

This section provides recommendations to help you further help secure your
training and deployment environment.

To help secure your environment and perimeters, consider the following:

- When you
  [implement security measures](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#implement_security_measures_for_data_movement),
  as described earlier, consider the following:

  - To isolate training environments and limit access, use [dedicated projects or VPCs](https://docs.cloud.google.com/architecture/best-practices-vpc-design) for training.
  - To protect sensitive data and code during execution, use [Shielded VMs](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) or [confidential computing](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) for training workloads.
  - To help secure your network infrastructure and to control access to your deployed models, use VPCs, firewalls, and security perimeters.
- When you use Vertex AI training, you can use the
  following methods to help secure your compute infrastructure:

  - To train custom jobs that privately communicate with other authorized Google Cloud services and that aren't exposed to public traffic, [set up a Private Service Connect interface](https://docs.cloud.google.com/vertex-ai/docs/general/vpc-psc-i-setup).
  - For increased network security and lower network latency than what you get with a public IP address, use a private IP address to connect to your training jobs. For details, see [Use a private IP for custom training](https://docs.cloud.google.com/vertex-ai/docs/training/using-private-ip).
- When you use GKE or Cloud Run to set
  up a custom environment, consider the following options:

  - To secure your GKE cluster, use the appropriate network policies, pod security policies, and access controls. Use [trusted and verified container images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster#containerd) for your training workloads. To [scan container images](https://docs.cloud.google.com/artifact-analysis/docs/scan-os-automatically) for vulnerabilities, use Artifact Analysis.
  - To protect your environment from [container escapes](https://docs.cloud.google.com/security-command-center/docs/findings/threats/agent-engine-container-escape) and other attacks, implement [runtime security measures](https://docs.cloud.google.com/functions/docs/securing/execution-environment-security) for Cloud Run functions. To further protect your environment, use [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods) and [workload isolation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation).
  - To help secure your GKE workloads, follow the best practices in the [GKE security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).
  - To help meet your security requirements in Cloud Run, see the [security design overview}](https://docs.cloud.google.com/run/docs/securing/security).
- When you use Managed Service for Apache Spark for model training, follow the
  [Managed Service for Apache Spark security best practices](https://docs.cloud.google.com/dataproc/docs/concepts/security-best-practices).

To help secure your deployment, consider the following:

- When you deploy models, use Model Registry. If you deploy models in containers, use GKE Sandbox and [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs) to enhance security and isolate workloads. [Restrict access to models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/control-model-access) from Model Garden according to user roles and responsibilities.
- To help secure your model APIs, use Apigee or [API Gateway](https://docs.cloud.google.com/api-gateway/docs). To prevent abuse, implement API keys, authentication, authorization, and rate limiting. To control access to model APIs, use API keys and authentication mechanisms.
- To help secure access to models during prediction, use [Vertex AI Inference](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview). To prevent data exfiltration, use VPC Service Controls perimeters to protect [private endpoints](https://docs.cloud.google.com/vertex-ai/docs/predictions/using-private-endpoints) and govern access to the underlying models. You use private endpoints to enable access to the models within a VPC network. [IAM isn't directly applied](https://docs.cloud.google.com/vertex-ai/docs/general/endpoint-access-control) to the private endpoint, but the target service uses IAM to manage access to the models. For online prediction, we recommend that you use Private Service Connect.
- To track API calls that are related to model deployment, enable [Cloud Audit Logs for Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/general/audit-logging). Relevant API calls include activities such as endpoint creation, model deployment, and configuration updates.
- To extend Google Cloud infrastructure to edge locations, consider [Google Distributed Cloud](https://docs.cloud.google.com/distributed-cloud/docs/overview) solutions. For a fully disconnected solution, you can use [Distributed Cloud air-gapped](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch/overview), which doesn't require connectivity to Google Cloud.
- To help standardize deployments and to help ensure compliance with regulatory and security needs, use [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

### Follow SLSA guidelines for AI artifacts

Follow the standard
[Supply-chain Levels for Software Artifacts (SLSA)](https://slsa.dev/)
guidelines for your AI-specific artifacts, like models and software packages.

SLSA is a security framework that's designed to help you improve the integrity
of software artifacts and help prevent tampering. When you adhere to the SLSA
guidelines, you can enhance the security of your AI and ML pipeline and the
artifacts that the pipeline produces. SLSA adherence can provide the following
benefits:

- **Increased trust in your AI and ML artifacts**: SLSA helps to ensure that tampering doesn't occur to your models and software packages. Users can also trace models and software packages back to their source, which increases users' confidence in the integrity and reliability of the artifacts.
- **Reduced risk of supply chain attacks**: SLSA helps to mitigate the risk of attacks that exploit vulnerabilities in the software supply chain, like attacks that inject malicious code or that compromise build processes.
- **Enhanced security posture**: SLSA helps you to strengthen the overall security posture of your AI and ML systems. This implementation can help reduce the risk of attacks and protect your valuable assets.

To implement SLSA for your AI and ML artifacts on Google Cloud, do
the following:

1. **Understand SLSA levels** : Familiarize yourself with the different [SLSA levels](https://slsa.dev/spec/v0.1/levels) and their requirements. As the levels increase, the integrity that they provide also increases.
2. **Assess your current level**: Evaluate your current practices against the SLSA framework to determine your current level and to identify areas for improvement.
3. **Set your target level**: Determine the appropriate SLSA level to target based on your risk tolerance, security requirements, and the criticality of your AI and ML systems.
4. **Implement SLSA requirements** : To meet your target SLSA level,
   [implement the necessary controls and practices](https://docs.cloud.google.com/software-supply-chain-security/docs/overview),
   which could include the following:

   - **Source control**: Use a version control system like Git to track changes to your code and configurations.
   - **Build process** : Use a service that helps to secure your builds, like [Cloud Build](https://docs.cloud.google.com/build), and ensure that your build process is scripted or automated.
   - **Provenance generation** : Generate provenance metadata that captures details about how your artifacts were built, including the build process, source code, and dependencies. For details, see [Track Vertex ML Metadata](https://docs.cloud.google.com/vertex-ai/docs/ml-metadata/tracking) and [Track executions and artifacts](https://docs.cloud.google.com/vertex-ai/docs/experiments/track-executions-artifacts).
   - **Artifact signing**: Sign your artifacts to verify their authenticity and integrity.
   - **Vulnerability management** : Scan your artifacts and dependencies for vulnerabilities on a regular basis. Use tools like [Artifact Analysis.](https://docs.cloud.google.com/artifact-registry/docs/analysis)
   - **Deployment security**: Implement deployment practices that help to secure your systems, such as the practices that are described in this document.
5. **Continuous improvement**: Monitor and improve your SLSA implementation
   to address new threats and vulnerabilities, and strive for higher SLSA
   levels.

### Use validated prebuilt container images

To prevent a single point of failure for your MLOps stages, isolate the tasks
that require different dependency management into different containers. For
example, use separate containers for feature engineering, training or
fine-tuning, and inference tasks. This approach also gives ML engineers the
flexibility to control and customize their environment.

To promote MLOps consistency across your organization, use prebuilt containers.
Maintain a
[central repository](https://cloud.google.com/blog/products/containers-kubernetes/google-clouds-container-platform-for-the-next-decade-of-ai)
of verified and trusted base platform images with the following best
practices:

- Maintain a centralized platform team in your organization that builds and manages standardized base containers.
- Extend the prebuilt container images that Vertex AI provides specifically for AI and ML. Manage the container images in a central repository within your organization.

Vertex AI provides a variety of
[prebuilt containers](https://docs.cloud.google.com/vertex-ai/docs/training/pre-built-containers)
for training and inference, and it also lets you use
[custom containers](https://docs.cloud.google.com/vertex-ai/docs/training/containers-overview).
For smaller models, you can reduce latency for inference if you
[load models in containers](https://docs.cloud.google.com/run/docs/configuring/services/gpu-best-practices#model-container).

To improve the security of your container management, consider the following
recommendations:

- Use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) to create, store, and manage repositories of container images with different formats. Artifact Registry handles access control with IAM, and it has integrated observability and [vulnerability assessment](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#ar-vuln-assessment) features. Artifact Registry lets you enable container security features, scan container images, and investigate vulnerabilities.
- Run [continuous integration](https://docs.cloud.google.com/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke) steps and [build container images](https://docs.cloud.google.com/build/docs/building/build-containers) with Cloud Build. Dependency issues can be highlighted at this stage. If you want to deploy only the images that are built by Cloud Build, you can use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/cloud-build). To help prevent supply chain attacks, deploy the images built by Cloud Build in Artifact Registry. Integrate automated testing tools such as SonarQube, PyLint, or OWASP ZAP.
- Use a container platform like GKE or Cloud Run, which are optimized for GPU or TPU for AI and ML workloads. Consider the [vulnerability scanning options](https://docs.cloud.google.com/artifact-analysis/docs/container-scanning-overview) for containers in GKE clusters.

### Consider Confidential Computing for GPUs

To protect
[*data in use*](https://en.wikipedia.org/wiki/Digital_data#Data_in_use),
you can use Confidential Computing.
Conventional security measures protect data at rest and in transit, but
Confidential Computing encrypts data during processing. When you use
Confidential Computing for GPUs, you help to protect sensitive training
data and model parameters from unauthorized access. You can also help to prevent
unauthorized access from privileged cloud users or potential attackers who might
gain access to the underlying infrastructure.

To determine whether you need Confidential Computing for GPUs, consider the
sensitivity of the data, regulatory requirements, and potential risks.

If you set up Confidential Computing, consider the following options:

- For general-purpose AI and ML workloads, use [Confidential VM instances](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with NVIDIA T4 GPUs. These VM instances offer hardware-based encryption of data in use.
- For containerized workloads, use [Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-confidential-nodes). These nodes provide a secure and isolated environment for your pods.
- To ensure that your workload is running in a genuine and secure enclave, [verify the attestation](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/attestation) reports that Confidential VM provides.
- To track performance, resource utilization, and security events, monitor your Confidential Computing resources and your Confidential GKE Nodes by using Monitoring and Logging.

## Verify and protect inputs

Treat all of the inputs to your AI systems as untrusted, regardless of whether
the inputs are from end users or other automated systems. To help keep your AI
systems secure and to ensure that they operate as intended, you must detect and
sanitize potential attack vectors early.

To verify and protect your inputs, consider the following recommendations.

### Implement practices that help secure generative AI systems

Treat prompts as a critical application component that has the same importance
to security as code does. Implement a
[defense-in-depth](https://en.wikipedia.org/wiki/Defense_in_depth_(computing))
strategy that combines proactive design, automated screening, and disciplined
lifecycle management.

To help secure your generative AI prompts, you must design them for security,
screen them before use, and manage them throughout their lifecycle.

To improve the security of your prompt design and engineering, consider the
following practices:

- **Structure prompts for clarity** : Design and test all of your prompts by using [Vertex AI Studio prompt management capabilities](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/prompt-classes). Prompts need to have a clear, unambiguous structure. Define a role, [include few-shot examples](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/few-shot-examples), and give specific, bounded instructions. These methods reduce the risk that the model might misinterpret a user's input in a way that creates a security loophole.
- **Test the inputs for robustness and grounding**: Test all of your
  systems proactively against unexpected, malformed, and malicious inputs in
  order to prevent crashes or insecure outputs. Use red team testing to
  simulate real-world attacks. As a standard step in your
  Vertex AI Pipelines, automate your robustness tests. You can use
  the following testing techniques:

  - Fuzz testing.
  - Test directly against PII, sensitive inputs, and SQL injections.
  - Scan multimodal inputs that can contain malware or violate prompt policies.
- **Implement a layered defense**: Use multiple defenses and never rely
  on a single defensive measure. For example, for an application based on
  retrieval-augmented generation (RAG), use a separate LLM to classify
  incoming user intent and check for malicious patterns. Then, that LLM can
  pass the request to the more-powerful primary LLM that generates the final
  response.

- **Sanitize and validate inputs**: Before you incorporate external input or
  user-provided input into a prompt, filter and validate all of the input in
  your application code. This validation is important to help you prevent
  indirect prompt injection.

For automated prompt and response screening, consider the following
practices:

- **Use comprehensive security services** : Implement a dedicated, model-agnostic security service like Model Armor as a mandatory protection layer for your LLMs. Model Armor inspects prompts and responses for threats like prompt injection, [jailbreak attempts](https://en.wikipedia.org/wiki/Privilege_escalation#Jailbreaking), and harmful content. To help ensure that your models don't leak sensitive training data or intellectual property in their responses, use the Sensitive Data Protection integration with Model Armor. For details, see [Model Armor filters](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview#ma-filters).
- **Monitor and log interactions** : Maintain detailed logs for all of the prompts and responses for your model endpoints. Use [Logging](https://docs.cloud.google.com/logging) to audit these interactions, identify patterns of misuse, and detect attack vectors that might emerge against your deployed models.

To help secure prompt lifecycle management, consider the following practices:

- **Implement versioning for prompts**: Treat all of your production prompts like application code. Use a version control system like Git to create a complete history of changes, enforce collaboration standards, and enable rollbacks to previous versions. This core MLOps practice can help you to maintain stable and secure AI systems.
- **Centralize prompt management**: Use a central repository to store, manage, and deploy all of your versioned prompts. This strategy enforces consistency across environments and it enables runtime updates without the need for a full application redeployment.
- **Conduct regular audits and red team testing** : Test your system's defenses continuously against known vulnerabilities, such as those listed in the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-ten/). As an AI engineer, you must be proactive and red-team test your own application to discover and remediate weaknesses before an attacker can exploit them.

### Prevent malicious queries to your AI systems

Along with authentication and authorization, which this document discussed
earlier, you can take further measures to help secure your AI systems against
malicious inputs. You need to prepare your AI systems for *post-authentication*
scenarios in which attackers bypass both the authentication and authorization
protocols, and then attempt to attack the system internally.

To implement a comprehensive strategy that can help protect your system from
post-authentication attacks, apply the following requirements:

- **Secure network and application layers**: Establish a multi-layered
  defense for all of your AI assets.

  - To create a security perimeter that prevents data exfiltration of models from Model Registry or of sensitive data from BigQuery, use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). Always use [dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode) to validate the impact of a perimeter before you enforce it.
  - To help protect web-based tools such as notebooks, use [IAP](https://docs.cloud.google.com/iap/docs/concepts-overview).
  - To help secure all of the inference endpoints, use [Apigee](https://docs.cloud.google.com/apigee) for enterprise-grade security and governance. You can also use API Gateway for straightforward authentication.
- **Watch for query pattern anomalies**: For example, an attacker that
  probes a system for vulnerabilities might send thousands of slightly
  different, sequential queries. Flag abnormal query patterns that don't
  reflect normal user behavior.

- **Monitor the volume of requests**: A sudden spike in query volume
  strongly indicates a denial-of-service (DoS) attack or a model theft
  attack, which is an attempt to reverse-engineer the model. Use rate
  limiting and throttling to control the volume of requests from a single IP
  address or user.

- **Monitor and set alerts for geographic and temporal anomalies**:
  Establish a baseline for normal access patterns. Generate alerts for sudden
  activity from unusual geographic locations or at odd hours. For example, a
  massive spike in logins from a new country at 3 AM.

## Monitor, evaluate, and prepare to respond to outputs

AI systems deliver value because they produce outputs that augment, optimize,
or automate human decision-making. To maintain the integrity and trustworthiness
of your AI systems and applications, ensure that the outputs are secure and
within the expected parameters. You also need a plan to respond to incidents.

To maintain your outputs, consider the following recommendations.

### Evaluate model performance with metrics and security measures

To ensure that your AI models meet performance benchmarks, meet security
requirements, and adhere to fairness and compliance standards, thoroughly
evaluate the models. Conduct evaluations before deployment, and then continue to
evaluate the models in production on a regular basis. To minimize risks and
build trustworthy AI systems, implement a comprehensive evaluation strategy that
combines performance metrics with specific AI security assessments.

To evaluate model robustness and security posture, consider the following
recommendations:

- Implement model signing and verification in your MLOps pipeline.

  - For containerized models, use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/cloud-build) to verify signatures.
  - For models that are deployed directly to Vertex AI endpoints, use custom checks in your deployment scripts for verification.
  - For any model, use Cloud Build for [model signing](https://security.googleblog.com/2025/04/taming-wild-west-of-ml-practical-model.html).
- Assess your model's resilience to unexpected or adversarial inputs.

  - For all of your models, test your model for common data corruptions and any potentially malicious data modifications. To orchestrate these tests, you can use Vertex AI training or Vertex AI Pipelines.
  - For security-critical models, conduct adversarial attack simulations to understand the potential vulnerabilities.
  - For models that are deployed in containers, use Artifact Analysis in Artifact Registry to scan the base images for vulnerabilities.
- Use Vertex AI Model Monitoring to detect drift and skew for
  deployed models. Then, feed these insights back into the re-evaluation or
  retraining cycles.

- Use model evaluations from Vertex AI as a pipeline
  component with Vertex AI Pipelines. You can run the model
  evaluation component by itself or with other pipeline components. Compare
  the model versions against your defined metrics and datasets. Log the
  evaluation results to Vertex ML Metadata for lineage and
  tracking.

- Use or build upon the
  [Gen AI evaluation service](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview)
  to evaluate your chosen models or to implement custom human-evaluation
  workflows.

To assess fairness, bias, explainability, and factuality, consider the
following recommendations:

- [Define fairness measures](https://docs.cloud.google.com/vertex-ai/docs/evaluation/intro-evaluation-fairness) that match your use cases, and then evaluate your models for potential biases across different data slices.
- Understand which features drive model predictions in order to ensure that the features, and the predictions that result, align with domain knowledge and ethical guidelines.
- Use [Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview) to get feature attributions for your models.
- Use the Gen AI evaluation service to compute metrics. During the source verification phase of testing, the service's grounding metric checks for factuality against the source text that's provided.
- Enable [grounding](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview) for your model's output in order to facilitate a second layer of source verification at the user level.
- Review our [AI principles](https://ai.google/principles/) and adapt them for your AI applications.

### Monitor AI and ML model outputs in production

Continuously monitor your AI and ML models and their supporting infrastructure
in production. It's important to promptly identify and diagnose degradations in
model output quality or performance, security vulnerabilities that emerge, and
deviations from compliance mandates. This monitoring helps you sustain system
safety, reliability, and trustworthiness.

To monitor AI system outputs for anomalies, threats, and quality degradation,
consider the following recommendations:

- Use Model Monitoring for your model outputs to track unexpected shifts in prediction distributions or spikes in low-confidence model predictions. Actively monitor your generative AI model outputs for generated content that's unsafe, biased, off-topic, or malicious. You can also use Model Armor to screen all of your model outputs.
- Identify specific error patterns, capture quality indicators, or detect harmful or non-compliant outputs at the application level. To find these issues, use custom monitoring in Monitoring dashboards and use log-based metrics from Logging.

To monitor outputs for security-specific signals and unauthorized changes,
consider the following recommendations:

- Identify unauthorized access attempts to AI models, datasets in Cloud Storage or BigQuery, or MLOps pipeline components. In particular, identify unexpected or unauthorized changes in IAM permissions for AI resources. To track these activities and review them for suspicious patterns, use the Admin Activity audit logs and Data Access audit logs in Cloud Audit Logs. Integrate the findings from Security Command Center, which can flag security misconfigurations and flag potential threats that are relevant to your AI assets.
- Monitor outputs for high volumes of requests or requests from suspicious sources, which might indicate attempts to reverse engineer models or exfiltrate data. You can also use Sensitive Data Protection to monitor for the exfiltration of potentially sensitive data.
- Integrate logs into your security operations. Use Google Security Operations to help you detect, orchestrate, and respond to any cyber threats from your AI systems.

To track the operational health and performance of the infrastructure that
serves your AI models, consider the following recommendations:

- Identify operational issues that can impact service delivery or model performance.
- Monitor Vertex AI endpoints for latency, error rates, and traffic patterns.
- Monitor MLOps pipelines for execution status and errors.
- Use Monitoring, which provides ready-made metrics. You can also create custom dashboards to help you identify issues like endpoint outages or pipeline failures.

### Implement alerting and incident response procedures

When you identify any potential performance, security, or compliance issues, an
effective response is critical. To ensure timely notifications to the
appropriate teams, implement robust alerting mechanisms. Establish and
operationalize comprehensive, AI-aware incident response procedures to manage,
contain, and remediate these issues efficiently.

To establish robust alerting mechanisms for AI issues that you identify,
consider the following recommendations:

- Configure actionable alerts to notify the relevant teams, based on the monitoring activities of your platform. For example, configure alerts to trigger when Model Monitoring detects significant drift, skew, or prediction anomalies. Or, configure alerts to trigger when Model Armor or custom Monitoring rules flag malicious inputs or unsafe outputs.
- Define clear notification channels, which can include Slack, email, or SMS through Pub/Sub integrations. Customize the notification channels for your alert severities and the responsible teams.

Develop and operationalize an AI-aware incident response plan. A structured
incident response plan is vital to minimize any potential impacts and ensure
recovery. Customize this plan to address AI-specific risks such as model
tampering, incorrect predictions due to drift, prompt injection, or unsafe
outputs from generative models. To create an effective plan, include the
following key phases:

- **Preparation**: Identify assets and their vulnerabilities, develop
  playbooks, and ensure that your teams have appropriate privileges. This
  phase includes the following tasks:

  - Identify critical AI assets, such as models, datasets, and specific Vertex AI resources like endpoints or Vertex AI Feature Store instances.
  - Identify the assets' potential failure modes or attack vectors.
  - Develop AI-specific playbooks for incidents that match your
    organization's threat model. For example, playbooks might include the
    following:

    - A model rollback that uses versioning in Model Registry.
    - An emergency retraining pipeline on Vertex AI training.
    - The isolation of a compromised data source in BigQuery or Cloud Storage.
  - Use IAM to ensure that response teams have the necessary
    least-privilege access to tools that are required during an incident.

- **Identification and triage**: Use configured alerts to detect and
  validate potential incidents. Establish clear criteria and thresholds for
  how your organization investigates or declares an AI-related incident. For
  detailed investigation and evidence collection, use Logging
  for application logs and service logs, and use Cloud Audit Logs for
  administrative activities and data access patterns. Security teams can use
  Google SecOps for deeper analyses of security telemetry.

- **Containment**: Isolate affected AI systems or components to prevent
  further impact or data exfiltration. This phase might include the following
  tasks:

  - Disable a problematic Vertex AI endpoint.
  - Revoke specific IAM permissions.
  - Update firewall rules or Cloud Armor policies.
  - Pause a Vertex AI pipeline that's misbehaving.
- **Eradication**: Identify and remove the root cause of the incident.
  This phase might include the following tasks:

  - Patch the vulnerable code in a custom model container.
  - Remove the identified malicious backdoors from a model.
  - Sanitize the poisoned data before you initiate a secure retraining job on Vertex AI training.
  - Update any insecure configurations.
  - Refine the input validation logic to block specific prompt-injection techniques.
- **Recovery and secure redeployment**: Restore the affected AI systems to
  a known good and secure operational state. This phase might include the
  following tasks:

  - Deploy a previously validated and trusted model version from Model Registry.
  - Ensure that you find and apply all of the security patches for vulnerabilities that might be present in your code or system.
  - Reset the IAM permissions to the principle of least privilege.
- **Post-incident activity and lessons learned**: After you resolve the
  significant AI incidents, conduct a thorough post-incident review. This
  review involves all of the relevant teams, such as the AI and ML, MLOps,
  security, and data science teams. Understand the full lifecycle of the
  incident. Use these insights to refine the AI system design, update
  security controls, improve Monitoring configurations, and
  enhance the AI incident response plan and playbooks.

Integrate the AI incident response with the broader organizational frameworks,
such as IT and security incident management, for a coordinated effort. To align
your AI-specific incident response with your organizational frameworks, consider
the following:

- **Escalation**: Define clear paths for how you escalate significant AI incidents to central SOC, IT, legal, or relevant business units.
- **Communication**: Use established organizational channels for all internal and external incident reports and updates.
- **Tooling and processes**: Use existing enterprise incident management and ticketing systems for AI incidents to ensure consistent tracking and visibility.
- **Collaboration**: Pre-define collaboration protocols between AI and ML, MLOps, data science, security, legal, and compliance teams for effective AI incident responses.

## Contributors

Authors:

- [Kamilla Kurta](https://www.linkedin.com/in/kamillakurta) \| GenAI/ML Specialist Customer Engineer
- [Vidhi Jain](https://www.linkedin.com/in/vidhi-jain-jpm) \| Cloud Engineer, Analytics and AI
- [Mohamed Fawzi](https://www.linkedin.com/in/fawzii) \| Benelux Security and Compliance Lead
- [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) \| Customer Engineer, AI/ML Specialist

<br />

Other contributors:

- [Lauren Anthony](https://www.linkedin.com/in/lauren-a-5a778a44) \| Customer Engineer, Security Specialist
- [Daniel Lees](https://www.linkedin.com/in/daniellees) \| Cloud Security Architect
- [John Bacon](https://www.linkedin.com/in/johnbac/) \| Partner Solutions Architect
- [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) \| Cross-Product Solution Developer
- [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) \| Partner Customer Engineer
- [Mónica Carranza](https://www.linkedin.com/in/monicaecp/) \| Senior Generative AI Threat Analyst
- [Tarun Sharma](https://www.linkedin.com/in/tarun27in) \| Principal Architect
- [Wade Holmes](https://www.linkedin.com/in/wholmes) \| Global Solutions Director

<br />

<br />

<br />


# AI and ML perspective: Reliability

This document in the
[Google Cloud Well-Architected Framework: AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml)
provides an overview of the principles and recommendations to design and operate
reliable AI and ML systems on Google Cloud. It explores how to integrate
advanced reliability practices and observability into your architectural
blueprints. The recommendations in this document align with the
[reliability pillar](https://docs.cloud.google.com/architecture/framework/reliability)
of the Google Cloud Well-Architected Framework.

In the fast-evolving AI and ML landscape, reliable systems are essential in
order to ensure customer satisfaction and achieve business goals. To meet the
unique demands of both predictive ML and generative AI, you need AI and ML
systems that are robust, reliable, and adaptable. To handle the complexities of
[MLOps](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)---from
development to deployment and continuous improvement---you need to use a
reliability-first approach. Google Cloud offers a purpose-built AI
infrastructure that's aligned with
[site reliability engineering (SRE)](https://sre.google/)
principles and that provides a powerful foundation for reliable AI and ML
systems.

The recommendations in this document are mapped to the following core
principles:

- [Ensure that infrastructure is scalable and highly available](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#scalable-highly-available-infrastructure)
- [Use a modular and loosely coupled architecture](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#modular-loosely-coupled-architecture)
- [Build an automated end-to-end MLOps platform](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#automated-end-to-end-mlops-platform)
- [Maintain trust and control through data and model governance](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#trust-control-through-governance)
- [Implement holistic observability and reliability practices](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#holistic-observability-reliability-practices)

## Ensure that ML infrastructure is scalable and highly available

Reliable AI and ML systems in the cloud require scalable and highly
available infrastructure. These systems have dynamic demands, diverse resource
needs, and critical dependencies on model availability. Scalable architectures
adapt to fluctuating loads and variations in data volume or inference requests.
High availability (HA) helps to ensure resilience against failures at the
component, zone, or region level.

To build scalable and highly available ML infrastructure, consider the following
recommendations.

### Implement automatic and dynamic scaling capabilities

AI and ML workloads are dynamic, with demand that fluctuates based on data
arrival rates, training frequency, and the volume of inference traffic.
Automatic and dynamic scaling adapts infrastructure resources seamlessly to
demand fluctuations. Scaling your workloads effectively helps to prevent
downtime, maintain performance, and optimize costs.

To autoscale your AI and ML workloads, use the following products and features
in Google Cloud:

- **Data processing pipelines** : Create data pipelines in [Dataflow](https://docs.cloud.google.com/dataflow/docs/overview). Configure the pipelines to use [Dataflow's horizontal autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling) feature, which dynamically adjusts the number of worker instances based on CPU utilization, pipeline parallelism, and pending data. You can configure autoscaling parameters through pipeline options when you launch jobs.
- **Training jobs** : Automate the scaling of training jobs by using [Vertex AI custom training](https://docs.cloud.google.com/vertex-ai/docs/training/configure-compute). You can define worker pool specifications such as the machine type, the type and number of accelerators, and the number of worker pools. For jobs that can tolerate interruptions and for jobs where the training code implements checkpointing, you can reduce costs by using [Spot VMs](https://docs.cloud.google.com/vertex-ai/docs/training/use-spot-vms).
- **Online inference** : For online inference, use [Vertex AI endpoints](https://docs.cloud.google.com/vertex-ai/docs/general/deployment). To enable autoscaling, configure the minimum and maximum replica count. Specify a minimum of two replicas for HA. Vertex AI automatically adjusts the number of replicas based on traffic and the configured autoscaling metrics, such as CPU utilization and replica utilization.
- **Containerized workloads in
  [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)** : Configure autoscaling at the node and Pod levels. Configure the [cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) and [node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning) to adjust the node count based on pending Pod resource requests like CPU, memory, GPU, and TPU. Use [Horizontal Pod Autoscaler (HPA)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling) for deployments to define scaling policies based on metrics like CPU and memory utilization. You can also scale based on custom AI and ML metrics, such as GPU or TPU utilization and prediction requests per second.
- **Serverless containerized services** : Deploy the services in [Cloud Run](https://docs.cloud.google.com/run/docs/configuring/services/gpu#gps-max-instances) and configure autoscaling by specifying the minimum and maximum number of container instances. Use [best practices](https://docs.cloud.google.com/run/docs/configuring/services/gpu-best-practices#autoscaling-and-gpu) to autoscale GPU-enabled instances by specifying the accelerator type. Cloud Run automatically scales instances between the configured minimum and maximum limits based on incoming requests. When there are no requests, it scales efficiently to zero instances. You can leverage the automatic, request-driven scaling of Cloud Run to deploy [Vertex AI agents](https://docs.cloud.google.com/run/docs/ai-agents) and to deploy third-party workloads like [quantized models using Ollama](https://docs.cloud.google.com/run/docs/tutorials/gpu-gemma-with-ollama), [LLM model inference using vLLM](https://docs.cloud.google.com/run/docs/tutorials/gpu-gemma2-with-vllm), and [Huggingface Text Generation Inference (TGI)](https://docs.cloud.google.com/run/docs/tutorials/gpu-llama3-with-tgi).

### Design for HA and fault tolerance

For production-grade AI and ML workloads, it's crucial that you ensure
continuous operation and resilience against failures. To implement HA and fault
tolerance, you need to build redundancy and replication into your architecture
on Google Cloud. This approach helps to ensure that a failure of an
individual component doesn't cause a failure of the complete system.

- For HA and low latency in model serving, particularly for real-time inference and generative AI models, distribute your deployments across multiple locations.
- For global availability and resilience, deploy the models to multiple [Vertex AI endpoints](https://docs.cloud.google.com/vertex-ai/docs/general/deployment) across Google Cloud regions or use the [global endpoint](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#global-endpoint).
- Use global load balancing to route traffic.
- For training on GKE or Compute Engine MIGs, implement monitoring for [Xid errors](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#xid_messages). When you identify Xid errors, take appropriate remedial action. For example, [reset GPUs](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-gpus#reset-gpus), [reset Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances/reset-instance#reset-instance), or trigger hardware replacement by using the [gcloud CLI report faulty host](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host#report-a-faulty-host) command.
- Explore fault-tolerant or elastic and resilient training solutions like [recipes to use the Google Resiliency Library](https://github.com/AI-Hypercomputer/gpu-recipes/tree/main/training/a3mega/llama3-1-70b/nemo-pretraining-gke-resiliency) or integration of the [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training) logic for TPU workloads.

Implement redundancy for critical AI and ML components in Google Cloud.
The following are examples of products and features that let you implement
resource redundancy:

- Deploy [GKE regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters) across multiple zones.
- Ensure data redundancy for datasets and checkpoints by using [Cloud Storage](https://docs.cloud.google.com/storage/docs/storage-classes#standard-availability) multi-regional or dual-region buckets.
- Use Spanner for globally consistent, highly available storage of metadata.
- Configure [Cloud SQL read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica) for operational databases.
- Ensure that [vector databases](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/rag-engine/vector-db-choices) for retrieval augmented generation (RAG) are highly available and multi-zonal or multi-regional.

### Manage resources proactively and anticipate requirements

Effective resource management is important to help you optimize costs,
performance, and reliability. AI and ML workloads are dynamic and there's high
demand for specialized hardware like GPUs and TPUs. Therefore, it's crucial that
you apply proactive resource management and ensure resource availability.

Plan for capacity based on historical monitoring data, such as GPU or TPU
utilization and throughput rates, from
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)
and logs in
[Cloud Logging](https://docs.cloud.google.com/logging/docs/overview).
Analyze this telemetry data by using
[BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction)
or
[Data Studio](https://docs.cloud.google.com/looker/docs/studio)
and forecast future demand for GPUs based on growth or new models. Analysis of
resource usage patterns and trends helps you to predict when and where you need
critical specialized accelerators.

- Validate capacity estimates through rigorous load testing. Simulate traffic on AI and ML services like serving and pipelines by using tools like [Apache JMeter](https://jmeter.apache.org/) or [LoadView](https://www.loadview-testing.com).
- Analyze system behavior under stress.
  - To anticipate and meet increased workload demands in production, proactively identify resource requirements. Monitor latency, throughput, errors, and resource utilization, especially GPU and TPU utilization. Increase resource quotas as necessary.
  - For generative AI serving, test under high concurrent loads and identify the level at which accelerator availability limits performance.
- Perform continuous monitoring for model queries and set up proactive [alerts](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/manage/monitoring#create-alerts) for agents.
  - Use the [model observability dashboard](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-observability#view) to view metrics that are collected by Cloud Monitoring, such as model queries per second (QPS), token throughput, and first token latencies.

### Optimize resource availability and obtainability

Optimize costs and ensure resource availability by strategically selecting
appropriate compute resources based on workload requirements.

- For stable 24x7 inference or for training workloads with fixed or predictable capacity requirements, use [committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview) for VMs and accelerators.
- For GKE nodes and Compute Engine VMs, use
  Spot VMs and Dynamic Workload Scheduler (DWS) capabilities:

  - For fault-tolerant tasks such as evaluation and experimentation workloads, use [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms). Spot VMs can be preempted, but they can help reduce your overall costs.
  - To manage preemption risk for high-demand accelerators, you can ensure better obtainability by using [DWS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/provisioningrequest).
    - For complex batch training that needs high-end GPUs to run up to seven days, use the DWS Flex-Start mode.
    - For longer running workloads that run up to three months, use the Calendar mode to reserve specific GPUs (H100 and H200) and TPUs (Trillium).
- To optimize AI inference on GKE, you can run a
  [vLLM](https://docs.vllm.ai/en/stable/)
  engine that dynamically uses TPUs and GPUs to address fluctuating capacity
  and performance needs. For more information, see
  [vLLM GPU/TPU Fungibility](https://gke-ai-labs.dev/docs/tutorials/gpu-tpu/fungibility-recipes/).

- For advanced scenarios with complex resource and topology needs
  that involve accelerators, use tools to abstract resource management.

  - [Cluster Director](https://docs.cloud.google.com/ai-hypercomputer/docs/cluster-director) lets you deploy and manage accelerator groups with colocation and scheduling for multi-GPU training (A3 Ultra H200 and A4 B200). Cluster Director supports GKE and Slurm clusters.
  - [Ray on Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/open-source/ray-on-vertex-ai/overview) abstracts distributed computing infrastructure. It enables applications to request resources for training and serving without the need for direct management of VMs and containers.

### Distribute incoming traffic across multiple instances

Effective load balancing is crucial for AI applications that have fluctuating
demands. Load balancing distributes traffic, optimizes resource utilization,
provides HA and low latency, and helps to ensure a seamless user experience.

- **Inference with varying resource needs** : Implement load balancing based on model metrics. [GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway) lets you deploy models behind a load balancer with model-aware routing. The gateway prioritizes instances with GPU and TPU accelerators for compute-intensive tasks like generative AI and LLM inference. Configure detailed health checks to assess model status. Use serving frameworks like vLLM or Triton for LLM metrics and integrate the metrics into [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) by using [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).
- **Inference workloads that need GPUs or TPUs** : To ensure that critical AI and ML inference workloads consistently run on machines that are suitable to the workloads' requirements, particularly when GPU and TPU availability is constrained, use [GKE custom compute classes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes). You can define specific compute *profiles* with fallback policies for autoscaling. For example, you can define a profile that specifies a higher priority for reserved GPU or TPU instances. The profile can include a fallback to use cost-efficient Spot VMs if the reserved resources are temporarily unavailable.
- **Generative AI on diverse orchestration platforms** : Use a centralized load balancer. For example, for cost and management efficiency, you can route requests that have low GPU needs to Cloud Run and route more complex, GPU-intensive tasks to GKE. For inter-service communication and policy management, implement a service mesh by using [Cloud Service Mesh](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/service-mesh). Ensure consistent logging and monitoring by using Cloud Logging and Cloud Monitoring.
- **Global load distribution** : To load balance traffic from global users who need low latency, use a [global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https). Configure geolocation routing to the closest region and implement failover. Establish regional endpoint replication in Vertex AI or GKE. Configure Cloud CDN for static assets. Monitor global traffic and latency by using Cloud Monitoring.
- **Granular traffic management** : For requests that have diverse data types or complexity and long-running requests, implement granular traffic management.
  - Configure [content-based routing](https://docs.cloud.google.com/load-balancing/docs/url-map#traffic-management-guides) to direct requests to specialized backends based on attributes like URL paths and headers. For example, direct requests to GPU-enabled backends for image or video models and to CPU-optimized backends for text-based models.
  - For long-running generative AI requests or batch workloads, use WebSockets or gRPC. Implement traffic management to handle timeouts and buffering. Configure request timeouts and retries and implement rate limiting and quotas by using API Gateway or Apigee.

## Use a modular and loosely coupled architecture

In a modular, loosely coupled AI and ML architecture, complex systems are
divided into smaller, self-contained components that interact through
well-defined interfaces. This architecture minimizes module dependencies,
simplifies development and testing, enhances reproducibility, and improves fault
tolerance by containing failures. The modular approach is crucial for managing
complexity, accelerating innovation, and ensuring long-term maintainability.

To design a modular and loosely coupled architecture for AI and ML workloads,
consider the following recommendations.

### Implement small self-contained modules or components

Separate your end-to-end AI and ML system into small, self-contained modules or
components. Each module or component is responsible for a specific
function, such as data ingestion, feature transformation, model training,
inference serving, or evaluation. A modular design provides several key benefits
for AI and ML systems: improved maintainability, increased scalability,
reusability, and greater flexibility and agility.

The following sections describe Google Cloud products, features, and tools
that you can use to design a modular architecture for your AI and ML systems.

#### Containerized microservices on GKE

For complex AI and ML systems or intricate generative AI pipelines that need
fine-grained orchestration, implement modules as microservices that are
orchestrated by using GKE. Package each distinct stage as an
individual microservice within Docker containers. These distinct stages include
data ingestion that's tailored for diverse formats, specialized data
preprocessing or feature engineering, distributed model training or fine tuning
of large foundation models, evaluation, or serving.

Deploy the containerized microservices on GKE and leverage
automated scaling based on CPU and memory utilization or custom metrics like GPU
utilization, rolling updates, and reproducible configurations in YAML manifests.
Ensure efficient communication between the microservices by using
GKE service discovery. For asynchronous patterns, use
message queues like
[Pub/Sub](https://docs.cloud.google.com/pubsub/docs/pubsub-basics).

The microservices-on-GKE approach helps you build scalable,
resilient platforms for tasks like complex RAG applications where the stages can
be designed as distinct services.

#### Serverless event-driven services

For event-driven tasks that can benefit from serverless, automatic scaling, use
[Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)
or
[Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview).
These services are ideal for asynchronous tasks like preprocessing or for
smaller inference jobs. Trigger Cloud Run functions on events, such as
a new data file that's created in Cloud Storage or model updates in
Artifact Registry. For web-hook tasks or services that need a container environment,
use Cloud Run.

Cloud Run services and Cloud Run functions can
scale up rapidly and scale down to zero, which helps to ensure cost efficiency
for fluctuating workloads. These services are suitable for modular components in
Vertex AI Agents workflows. You can orchestrate component
sequences with
[Workflows](https://docs.cloud.google.com/workflows/docs/overview)
or[Application Integration](https://docs.cloud.google.com/application-integration/docs/overview).

#### Vertex AI managed services

Vertex AI services support modularity and help you simplify the
development and deployment of your AI and ML systems. The services abstract the
infrastructure complexities so that you can focus on the application logic.

- To orchestrate workflows that are built from modular steps, use Vertex AI Pipelines.
- To run custom AI and ML code, package the code in Docker containers that can run on managed services like Vertex AI custom training and Vertex AI prediction.
- For modular feature engineering pipelines, use [Vertex AI Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview).
- For modular exploration and prototyping, use notebook environments like [Vertex AI Workbench](https://docs.cloud.google.com/vertex-ai/docs/workbench/introduction) or [Colab Enterprise](https://docs.cloud.google.com/colab/docs/introduction). Organize your code into reusable functions, classes, and scripts.

#### Agentic applications

For AI agents,
[Agent Development Kit (ADK)](https://google.github.io/adk-docs/)
provides modular capabilities like
[Tools](https://google.github.io/adk-docs/tools/)
and
[State](https://google.github.io/adk-docs/sessions/state/).
To enable interoperability between frameworks like
[LangChain](https://python.langchain.com/docs/tutorials),
[LangGraph](https://langchain-ai.github.io/langgraph),
[LlamaIndex](https://www.llamaindex.ai/),
and Vertex AI, you can combine ADK with the
[Agent2Agent (A2A) protocol](https://a2a-protocol.org/latest/)
and the
[Model Context Protocol (MCP)](https://github.com/modelcontextprotocol).
This interoperability lets you compose agentic workflows by using diverse
components.

You can deploy agents on Vertex AI Agent Engine, which is a managed
runtime that's optimized for scalable agent deployment. To run containerized
agents, you can leverage the autoscaling capabilities in
Cloud Run.

### Design well-defined interfaces

To build robust and maintainable software systems, it's crucial to ensure that
the components of a system are loosely coupled and modularized. This approach
offers significant advantages, because it minimizes the dependencies between
different parts of the system. When modules are loosely coupled, changes in one
module have minimal impact on other modules. This isolation enables independent
updates and development workflows for individual modules.

The following sections provide guidance to help ensure seamless communication
and integration between the modules of your AI and ML systems.

#### Protocol choice

- For universal access, use HTTP APIs, adhere to RESTful principles, and use JSON for language-agnostic data exchange. Design the API endpoints to represent actions on resources.
- For high-performance internal communication among microservices, use [gRPC](https://grpc.io/docs/) with[Protocol Buffers (ProtoBuf)](https://developers.google.com/protocol-buffers/docs/overview) for efficient serialization and strict typing. Define data structures like ModelInput, PredictionResult, or ADK Tool data by using `.proto` files, and then generate language bindings.
- For use cases where performance is critical, leverage gRPC streaming for large datasets or for continuous flows such as live text-to-speech or video applications. Deploy the gRPC services on GKE.

#### Standardized and comprehensive documentation

Regardless of the interface protocol that you choose, standardized
documentation is crucial. The
[OpenAPI Specification](https://swagger.io/specification/)
describes RESTful APIs. Use OpenAPI to document your AI and ML APIs: paths,
methods, parameters, request-response formats that are linked to JSON schemas,
and security. Comprehensive API documentation helps to improve discoverability
and client integration. For API authoring and visualization, use UI tools like
[Swagger Editor](https://swagger.io/tools/swagger-editor/).
To accelerate development and ensure consistency, you can generate client SDKs
and server stubs by using AI-assisted coding tools like
[Gemini Code Assist](https://codeassist.google/).
Integrate OpenAPI documentation into your CI/CD flow.

#### Interaction with Google Cloud managed services like Vertex AI

Choose between the higher abstraction of the Vertex AI SDK,
which is preferred for development productivity, and the granular control that
the REST API provides.

- The Vertex AI SDK simplifies tasks and authentication. Use the SDK when you need to interact with Vertex AI.
- The REST API is a powerful alternative especially when interoperability is required between layers of your system. It's useful for tools in languages that don't have an SDK or when you need fine-grained control.

### Use APIs to isolate modules and abstract implementation details

For security, scalability, and visibility, it's crucial that you implement
robust API management for your AI and ML services. To implement API management
for your defined interfaces, use the following products:

- **[API Gateway](https://docs.cloud.google.com/api-gateway/docs/about-api-gateway)**: For APIs that are externally exposed and managed, API Gateway provides a centralized, secure entry point. It simplifies access to serverless backend services, such as prediction, training, and data APIs. API Gateway helps to consolidate access points, enforce API contracts, and manage security capabilities like API keys and OAuth 2.0. To protect backends from overload and ensure reliability, implement rate limiting and usage quotas in API Gateway.
- **[Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs)**: To streamline API development and deployment on GKE and Cloud Run, use Cloud Endpoints, which offers a developer-friendly solution for generating API keys. It also provides integrated monitoring and tracing for API calls and it automates the generation of OpenAPI specs, which simplifies documentation and client integration. You can use Cloud Endpoints to manage access to internal or controlled AI and ML APIs, such as to trigger training and manage feature stores.
- **[Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)**: For enterprise-scale AI and ML, especially sophisticated generative AI APIs, Apigee provides advanced, comprehensive API management. Use Apigee for advanced security like threat protection and OAuth 2.0, for traffic management like caching, quotas, and mediation, and for analytics. Apigee can help you to gain deep insights into API usage patterns, performance, and engagement, which are crucial for understanding generative AI API usage.

### Plan for graceful degradation

In production AI and ML systems, component failures are unavoidable, just like
in other systems. Graceful degradation ensures that essential functions continue
to operate, potentially with reduced performance. This approach prevents
complete outages and improves overall availability. Graceful degradation is
critical for latency-sensitive inference, distributed training, and generative
AI.

The following sections describe techniques that you use to plan and implement
graceful degradation.

#### Fault isolation

- To isolate faulty components in distributed architectures, implement the [circuit breaker pattern](https://martinfowler.com/bliki/CircuitBreaker.html) by using resilience libraries, such as [Resilience4j](https://resilience4j.github.io/resilience4j/) in Java and [CircuitBreaker](https://pypi.org/project/circuitbreaker/) in Python.
- To prevent cascading failures, configure thresholds based on AI and ML workload metrics like error rates and latency and define fallbacks like simpler models and cached data.

#### Component redundancy

For critical components, implement redundancy and automatic failover. For
example, use GKE multi-zone clusters or regional clusters
and deploy Cloud Run services redundantly across different
regions. To route traffic to healthy instances when unhealthy instances are
detected, use Cloud Load Balancing.

Ensure data redundancy by using Cloud Storage multi-regional buckets.
For distributed training, implement asynchronous checkpointing to resume after
failures. For resilient and elastic training, use
[Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training).

#### Proactive monitoring

Graceful degradation helps to ensure system availability during failure, but
you must also implement proactive measures for continuous health checks and
comprehensive monitoring. Collect metrics that are specific to AI and ML, such
as latency, throughput, and GPU utilization. Also, collect model performance
degradation metrics like model and data drift by using Cloud Monitoring and
[Vertex AI Model Monitoring](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview).

Health checks can trigger the need to replace faulty nodes, deploy more
capacity, or automatically trigger continuous retraining or fine-tuning of
pipelines that use updated data. This proactive approach helps to prevent both
accuracy-based degradation and system-level graceful degradation and it helps to
enhance overall reliability.

#### SRE practices

To monitor the health of your systems, consider adopting SRE practices to
implement
[service level objectives (SLOs)](https://sre.google/sre-book/service-level-objectives/).
Alerts on error budget loss and burn rate can be early indicators of reliability
problems with the system. For more information about SRE practices, see the
[Google SRE book](https://sre.google/sre-book/table-of-contents/).

## Build an automated end-to-end MLOps platform

A robust, scalable, and reliable AI and ML system on Google Cloud
requires an automated end-to-end MLOps platform for the model development
lifecycle. The development lifecycle includes initial data handling, continuous
model training, deployment, and monitoring in production. By automating these
stages on Google Cloud, you establish repeatable processes, reduce manual
toil, minimize errors, and accelerate the pace of innovation.

An automated MLOps platform is essential for establishing production-grade
reliability for your applications. Automation helps to ensure model
quality, guarantee reproducibility, and enable continuous integration and
delivery of AI and ML artifacts.

To build an automated end-to-end MLOps platform, consider the following
recommendations.

### Automate the model development lifecycle

A core element of an automated MLOps platform is the orchestration of the
entire AI and ML workflow as a series of connected, automated steps: from data
preparation and validation to model training, evaluation, deployment, and
monitoring.

- Use [Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction) as your central orchestrator:
  - Define end-to-end workflows with modular components for data processing, training, evaluation, and deployment.
  - Automate pipeline runs by using schedules or triggers like new data or code changes.
  - Implement automated parameterization and versioning for each pipeline run and create a version history.
  - Monitor pipeline progress and resource usage by using built-in logging and tracing, and integrate with [Cloud Monitoring alerts](https://docs.cloud.google.com/monitoring/alerts).
- Define your ML pipelines programmatically by using the Kubeflow Pipelines (KFP) SDK or TensorFlow Extended SDK. For more information, see [Interfaces for Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/interfaces).
- Orchestrate operations by using Google Cloud services like [Dataflow](https://docs.cloud.google.com/dataflow/docs/overview), [Vertex AI custom training](https://docs.cloud.google.com/vertex-ai/docs/training/create-custom-job), [Vertex AI Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction), and Vertex AI endpoints.
- For generative AI workflows, orchestrate the steps for prompt management, batched inference, human-in-the-loop (HITL) evaluation, and coordinating ADK components.

### Manage infrastructure as code

Infrastructure as code (IaC) is crucial for managing AI and ML system
infrastructure and for enabling reproducible, scalable, and maintainable
deployments. The infrastructure needs of AI and ML systems are dynamic and
complex. The systems often require specialized hardware like GPUs and TPUs. IaC
helps to mitigate the risks of manual infrastructure management by ensuring
consistency, enabling rollbacks, and making deployments repeatable.

To effectively manage your infrastructure resources as code, use the following
techniques.

#### Automate resource provisioning

To effectively manage IaC on Google Cloud, define and provision your AI
and ML infrastructure resources by using
[Terraform](https://developer.hashicorp.com/terraform).
The infrastructure might include resources such as the following:

- GKE clusters that are configured with node pools. The node pools can be optimized based on workload requirements. For example, you can use A100, H100, H200, or B200 GPUs for training, and use L4 GPUs for inference.
- [Vertex AI endpoints](https://docs.cloud.google.com/vertex-ai/docs/general/deployment) that are configured for model serving, with defined machine types and scaling policies.
- [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets) for data and artifacts.

#### Use configuration templates

Organize your Terraform configurations as modular templates. To accelerate the
provisioning of AI and ML resources, you can use
[Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview).
The toolkit provides
[example blueprints](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples),
which are Google-curated Terraform templates that you can use to deploy
ready-to-use HPC, AI, and ML clusters in Slurm or GKE. You
can customize the Terraform code and manage it in your version control system.
To automate the resource provisioning and update workflow, you can integrate the
code into your CI/CD pipelines by using
[Cloud Build](https://docs.cloud.google.com/build/docs/overview).

#### Automate configuration changes

After you provision your infrastructure, manage the ongoing configuration
changes declaratively:

- In Kubernetes-centric environments, manage your Google Cloud resources as Kubernetes objects by using [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview).
- Define and manage Vertex AI resources like datasets, models, and endpoints, Cloud SQL instances, Pub/Sub topics, and Cloud Storage buckets by using YAML manifests.
- Deploy the manifests to your GKE cluster in order to integrate the application and infrastructure configuration.
- Automate configuration updates by using CI/CD pipelines and use templating to handle environment differences.
- Implement configurations for Identity and Access Management (IAM) policies and service accounts by using IaC.

#### Integrate with CI/CD

- Automate the lifecycle of the Google Cloud infrastructure resources by integrating IaC into CI/CD pipelines by using tools like [Cloud Build](https://docs.cloud.google.com/build/docs/overview) and [Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/overview).
- Define triggers for automatic updates on code commits.
- Implement automated testing and validation within the pipeline. For example, you can create a script to automatically run the Terraform `validate` and `plan` commands.
- Store the configurations as artifacts and enable versioning.
- Define separate environments, such as dev, staging, and prod, with distinct configurations in version control and automate environment promotion.

### Validate model behavior

To maintain model accuracy and relevance over time, automate the training and
evaluation process within your MLOps platform. This automation, coupled with
rigorous validation, helps to ensure that the models behave as expected with
relevant data before they're deployed to production.

- Set up continuous training pipelines, which are either triggered by new data and monitoring signals like data drift or that run on a schedule.
  - To manage automated training jobs, such as hyperparameter tuning trials and distributed training configurations for larger models, use [Vertex AI custom training](https://docs.cloud.google.com/vertex-ai/docs/training/create-custom-job).
  - For fine-tuning foundation models, automate the fine-tuning process and integrate the jobs into your pipelines.
- Implement automated model versioning and securely store trained model artifacts after each successful training run. You can store the artifacts in Cloud Storage or register them in [Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction).
- Define evaluation metrics and set clear thresholds, such as minimum accuracy, maximum error rate, and minimum F1 score.
  - Ensure that a model meets the thresholds to automatically pass the evaluation and be considered for deployment.
  - Automate evaluation by using services like [model evaluation in Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/evaluation/introduction).
  - Ensure that the evaluation includes metrics that are specific to the quality of generated output, factual accuracy, safety attributes, and adherence to specified style or format.
- To automatically log and track the parameters, code versions, dataset versions, and results of each training and evaluation run, use [Vertex AI Experiments](https://docs.cloud.google.com/vertex-ai/docs/experiments/intro-vertex-ai-experiments). This approach provides a history that's useful for comparison, debugging, and reproducibility.
- To optimize [hyperparameter tuning](https://docs.cloud.google.com/vertex-ai/docs/training/hyperparameter-tuning-overview) and automate searching for optimal model configurations based on your defined objective, use [Vertex AI Vizier](https://docs.cloud.google.com/vertex-ai/docs/vizier/overview).
- To visualize training metrics and to debug during development, use [Vertex AI TensorBoard](https://docs.cloud.google.com/vertex-ai/docs/experiments/tensorboard-introduction).

### Validate inputs and outputs of AI and ML pipelines

To ensure the reliability and integrity of your AI and ML systems, you must
validate data when it enters the systems and moves through the pipelines. You
must also verify the inputs and outputs at the component boundaries. Robust
validation of all inputs and outputs---raw data, processed data, configurations,
arguments, and files---helps to prevent unexpected behavior and maintain model
quality throughout the MLOps lifecycle. When you integrate this proactive
approach into your MLOps platform, it helps detect errors before they are
propagated throughout a system and it saves time and resources.

To effectively validate the inputs and outputs of your AI and ML pipelines, use
the following techniques.

#### Automate data validation

- Implement automated data validation in your data ingestion and preprocessing pipelines by using [TensorFlow Data Validation (TFDV)](https://www.tensorflow.org/tfx/data_validation).
  - For large-scale, SQL-based data quality checks, leverage scalable processing services like [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction).
  - For complex, programmatic validation on streaming or batch data, use [Dataflow](https://docs.cloud.google.com/dataflow/docs/overview).
- Monitor data distributions over time with TFDV capabilities.
  - Visualize trends by using tools that are integrated with [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) to detect data drift. You can automatically trigger model retraining pipelines when data patterns change significantly.
- Store validation results and metrics in BigQuery for analysis and historical tracking and archive validation artifacts in Cloud Storage.

#### Validate pipeline configurations and input data

To prevent pipeline failures or unexpected behavior caused by incorrect
settings, implement strict validation for all pipeline configurations and
command-line arguments:

- Define clear schemas for your configuration files like YAML or JSON by using schema validation libraries like [jsonschema](https://github.com/python-jsonschema/jsonschema) for Python. Validate configuration objects against these schemas before a pipeline run starts and before a component executes.
- Implement input validation for all command-line arguments and pipeline parameters by using argument-parsing libraries like [`argparse`](https://docs.python.org/3/library/argparse.html). Validation should check for correct data types, valid values, and required arguments.
- Within [Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction), define the expected types and properties of component parameters by using the built-in component input validation features.
- To ensure reproducibility of pipeline runs and to maintain an audit trail, store validated, versioned configuration files in Cloud Storage or Artifact Registry.

#### Validate input and output files

Validate input and output files such as datasets, model artifacts, and
evaluation reports for integrity and format correctness:

- Validate file formats like CSV, [Parquet](https://parquet.apache.org/docs/overview/), and image types by using libraries.
- For large files or critical artifacts, validate file sizes and checksums to detect corruption or incomplete transfers by using Cloud Storage [data validation and change detection](https://docs.cloud.google.com/storage/docs/data-validation).
- Perform file validation by using [Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview) (for example, based on file upload events) or within [Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) pipelines.
- Store validation results in [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) for easier retrieval and analysis.

### Automate deployment and implement continuous monitoring

Automated deployment and continuous monitoring of models in production helps to
ensure reliability, perform rapid updates, and detect issues promptly. This
involves managing model versions, controlled deployment, automated deployment
using CI/CD, and comprehensive monitoring as described in the following
sections.

#### Manage model versions

Manage model iterations and associated artifacts by using versioning tools:

- To track model versions and metadata and to link to underlying model artifacts, use [Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction).
- Implement a clear versioning scheme (such as, semantic versioning). For each model version, attach comprehensive metadata such as training parameters, evaluation metrics from validation pipelines, and dataset version.
- Store model artifacts such as model files, pretrained weights, and serving container images in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) and use its versioning and tagging features.
- To meet security and governance requirements, define stringent access-control policies for Model Registry and Artifact Registry.
- To programmatically register and manage versions and to integrate versions into automated CI/CD pipelines, use the Vertex AI SDK or API.

#### Perform controlled deployment

Control the deployment of model versions to endpoints by using your serving
platform's traffic management capabilities.

- Implement a [rolling deployment](https://docs.cloud.google.com/vertex-ai/docs/predictions/rolling-deployment) by using the traffic splitting feature of Vertex AI endpoints.
- If you deploy your model to GKE, use advanced traffic management techniques like [canary deployment](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary):
  1. Route a small subset of the production traffic to a new model version.
  2. Continuously monitor performance and error rates through metrics.
  3. Establish that the model is reliable.
  4. Roll out the version to all traffic.
- Perform [A/B testing](https://en.wikipedia.org/wiki/A/B_testing) of AI agents:
  1. Deploy two different model-agent versions or entirely different models to the same endpoint.
  2. Split traffic across the deployments.
  3. Analyze the results against business objectives.
- Implement automated rollback mechanisms that can quickly revert endpoint traffic to a previous stable model version if monitoring alerts are triggered or performance thresholds are missed.
- Configure traffic splitting and deployment settings programmatically by using the Vertex AI SDK or API.
- Use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) to track performance and traffic across versions.
- Automate deployment with CI/CD pipelines. You can use [Cloud Build](https://docs.cloud.google.com/build/docs/overview) to build containers, version artifacts, and trigger deployment to Vertex AI endpoints.
- Ensure that the CI/CD pipelines manage versions and pull from Artifact Registry.
- Before you shift traffic, perform automated endpoint testing for prediction correctness, latency, throughput, and API function.
- Store all configurations in version control.

#### Monitor continuously

- Use [Model Monitoring](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview) to automatically detect performance degradation, data drift (changes in input distribution compared to training), and prediction drift (changes in model outputs).
  - Configure drift detection jobs with thresholds and alerts.
  - Monitor real-time performance: prediction latency, throughput, error rates.
- Define custom metrics in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) for business KPIs.
- Integrate Model Monitoring results and custom metrics with Cloud Monitoring for alerts and dashboards.
- Configure notification channels like email, Slack, or PagerDuty and configure automated remediation.
- To debug prediction logs, use [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview).
- Integrate monitoring with incident management.

For generative AI endpoints, monitor output characteristics like toxicity and
coherence:

- Monitor feature serving for drift.
- Implement granular prediction validation: validate outputs against expected ranges and formats by using custom logic.
- Monitor prediction distributions for shifts.
- Validate output schema.
- Configure alerts for unexpected outputs and shifts.
- Track and respond to real-time validation events by using [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview).

Ensure that the output of comprehensive monitoring feeds back into continuous
training.

## Maintain trust and control through data and model governance

AI and ML reliability extends beyond technical uptime. It includes trust and
robust data and model governance. AI outputs might be inaccurate, biased, or
outdated. Such issues erode trust and can cause harm. Comprehensive
traceability, strong access control, automated validation, and transparent
practices help to ensure that AI outputs are reliable, trustworthy, and meet
ethics standards.

To maintain trust and control through data and model governance, consider the
following recommendations.

### Establish data and model catalogs for traceability

To facilitate comprehensive tracing, auditing, and understanding the lineage of
your AI and ML assets, maintain a robust, centralized record of data and model
versions throughout their lifecycle. A reliable data and model catalog serves as
the single source of truth for all of the artifacts that are used and produced
by your AI and ML pipelines--from raw data sources and processed datasets to
trained model versions and deployed endpoints.

Use the following products, tools, and techniques to create and maintain
catalogs for your data assets:

- Build an enterprise-wide catalog of your data assets by using [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview). To automatically discover and build inventories of the data assets, integrate Knowledge Catalog with your storage systems, such as [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction), [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction), and [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview).
- Ensure that your data is highly available and durable by storing it in Cloud Storage [multi-region or dual-region buckets](https://docs.cloud.google.com/storage/docs/locations#considerations). Data that you upload to these buckets is stored redundantly across at least two separate geographic locations. This redundancy provides built-in resilience against regional outages and it helps to ensure data integrity.
- Tag and annotate your datasets with relevant business metadata, ownership information, sensitivity levels, and lineage details. For example, link a processed dataset to its raw source and to the pipeline that created the dataset.
- Create a central repository for model versions by using [Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction). Register each trained model version and link it to the associated metadata. The metadata can include the following:
  - Training parameters.
  - Evaluation metrics from validation pipelines.
  - Dataset version that was used for training, with lineage traced back to the relevant Knowledge Catalog entry.
  - Code version that produced the dataset.
  - Details about the framework or foundation model that was used.
- Before you import a model into Model Registry, store model artifacts like model files and pretrained weights in a service like Cloud Storage. Store custom container images for serving or custom training jobs in a secure repository like [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview).
- To ensure that data and model assets are automatically registered and updated in the respective catalogs upon creation or modification, implement automated processes within your MLOps pipelines. This comprehensive cataloging provides end-to-end traceability from raw data to prediction, which lets you audit the inputs and processes that led to a specific model version or prediction. The auditing capability is vital for debugging unexpected behavior, ensuring compliance with data usage policies, and understanding the impact of data or model changes over time.
- For Generative AI and foundation models, your catalog must also track details about the specific foundation model used, fine-tuning parameters, and evaluation results that are specific to the quality and safety of the generated output.

### Implement robust access controls and audit trails

To maintain trust and control in your AI and ML systems, it's essential that
you protect sensitive data and models from unauthorized access and ensure
accountability for all changes.

- Implement strict access controls and maintain detailed audit trails across all components of your AI and ML systems in Google Cloud.
- Define granular permissions in IAM for users, groups, and service accounts that interact with your AI and ML resources.
- Follow the principle of least privilege rigorously.
- Grant only the minimum necessary permissions for specific tasks. For example, a training service account needs read access to training data and write access for model artifacts, but the service might not need write access to production serving endpoints.

Apply IAM policies consistently across all relevant assets and
resources in your AI and ML systems, including the following:

- Cloud Storage buckets that contain sensitive data or model artifacts.
- BigQuery datasets.
- Vertex AI resources, such as model repositories, endpoints, pipelines, and Feature Store resources.
- Compute resources, such as GKE clusters and Cloud Run services.

Use auditing and logs to capture, monitor, and analyze access activity:

- Enable [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit) for all of the Google Cloud services that are used by your AI and ML system.
- Configure audit logs to capture detailed information about API calls, data access events, and configuration changes made to your resources. Monitor the logs for suspicious activity, unauthorized access attempts, or unexpected modifications to critical data or model assets.
- For real-time analysis, alerting, and visualization, stream the audit logs to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview).
- For cost-effective long-term storage and retrospective security analysis or compliance audits, export the logs to BigQuery.
- For centralized security monitoring, integrate audit logs with your security information and event management (SIEM) systems. Regularly review access policies and audit trails to ensure they align with your governance requirements and detect potential policy violations.
- For applications that handle sensitive data, such as personally identifiable information (PII) for training or inference, use [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) checks within pipelines or on data storage.
- For generative AI and agentic solutions, use audit trails to help track who accessed specific models or tools, what data was used for fine-tuning or prompting, and what queries were sent to production endpoints. The audit trails help you to ensure accountability and they provide crucial data for you to investigate misuse of data or policy violations.

### Address bias, transparency, and explainability

To build trustworthy AI and ML systems, you need to address potential biases
that are inherent in data and models, strive for transparency in system
behavior, and provide explainability for model outputs. It's especially crucial
to build trustworthy systems in sensitive domains or when you use complex models
like those that are typically used for generative AI applications.

- Implement proactive practices to identify and mitigate bias throughout the MLOps lifecycle.
- Analyze training data for bias by using tools that detect skew in feature distributions across different demographic groups or sensitive attributes.
- Evaluate the overall model performance and the performance across predefined slices of data. Such evaluation helps you to identify disparate performance or bias that affects specific subgroups.

For model transparency and explainability, use tools that help users and
developers understand why a model made a particular prediction or produced a
specific output.

- For tabular models that are deployed on [Vertex AI endpoints](https://docs.cloud.google.com/vertex-ai/docs/general/deployment), generate feature attributions by using [Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview). Feature attributions indicate the input features that contributed most to the prediction.
- Interactively explore model behavior and potential biases on a dataset by using model-agnostic tools like the [What-If Tool](https://pair-code.github.io/what-if-tool/), which integrates with TensorBoard.
- Integrate explainability into your monitoring dashboards. In situations where understanding the model's reasoning is important for trust or decision-making, provide explainability data directly to end users through your application interfaces.
- For complex models like LLMs that are used for generative AI models, explain the *process* that an agent followed, such as by using [trace logs](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/manage/tracing). Explainability is relatively challenging for such models, but it's still vital.
- In RAG applications, provide citations for retrieved information. You can also use techniques like prompt engineering to guide the model to provide explanations or show its reasoning steps.
- Detect shifts in model behavior or outputs that might indicate emerging bias or unfairness by implementing continuous monitoring in production. Document model limitations, intended use cases, and known potential biases as part of the model's metadata in the [Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction).

## Implement holistic AI and ML observability and reliability practices

Holistic observability is essential for managing complex AI and ML systems in
production. It's also essential for measuring the reliability of complex AI and
ML systems, especially for generative AI, due to its complexity, resource
intensity, and potential for unpredictable outputs. Holistic observability
involves observing infrastructure, application code, data, and model behavior to
gain insights for proactive issue detection, diagnosis, and response. This
observability ultimately leads to high-performance, reliable systems. To achieve
holistic observability you need to do the following:

- Adopt SRE principles.
- Define clear reliability goals.
- Track metrics across system layers.
- Use insights from observability for continuous improvement and proactive management.

To implement holistic observability and reliability practices for AI and ML
workloads in Google Cloud, consider the following recommendations.

### Establish reliability goals and business metrics

Identify the key performance indicators (KPIs) that your AI and ML system
directly affects. The KPIs might include revenue that's influenced by AI
recommendations, customer churn that the AI systems predicted or mitigated, and
user engagement and conversion rates that are driven by generative AI features.

For each KPI, define the corresponding technical reliability metrics that affect
the KPI. For example, if the KPI is "customer satisfaction with a conversational
AI assistant," then the corresponding reliability metrics can include the
following:

- The success rate of user requests.
- The latency of responses: time to first token (TTFT) and token streaming for LLMs.
- The rate of irrelevant or harmful responses.
- The rate of successful task completion by the agent.

For AI and ML training, reliability metrics can include model FLOPS
utilization (MFU), iterations per second, tokens per second, and tokens per
device.

To effectively measure and improve AI and ML reliability, begin by setting clear
reliability goals that are aligned with the overarching business objectives.
Adopt the SRE approach by defining SLOs that quantify acceptable levels of
reliability and performance for your AI and ML services from the users'
perspective. Quantify these technical reliability metrics with specific SLO
targets.

The following are examples of SLO targets:

- 99.9% of API calls must return a successful response.
- 95th percentile inference latency must be below 300 ms.
- TTFT must be below 500 ms for 99% of requests.
- Rate of harmful output must be below 0.1%.

Aligning SLOs directly with business needs ensures that reliability efforts are
focused on the most critical system behavior that affects users and the
business. This approach helps to transform reliability into a measurable and
actionable engineering property.

### Monitor infrastructure and application performance

Track infrastructure metrics across all of the resources that are used by your
AI and ML systems. The metrics include processor usage (CPU, GPU, and TPU),
memory usage, network throughput and latency, and disk I/O. Track the metrics
for managed environments like Vertex AI training and serving and
for self-managed resources like GKE nodes and
Cloud Run instances.

Monitor the
[four golden signals](https://sre.google/sre-book/monitoring-distributed-systems/#xref_monitoring_golden-signals)
for your AI and ML applications:

- **Latency**: Time to respond to requests.
- **Traffic**: Volume of requests or workload.
- **Error rate**: Rate of failed requests or operations.
- **Saturation**: Utilization of critical resources like CPU, memory, and GPU or TPU accelerators, which indicates how close your system is to capacity limits.

Perform monitoring by using the following techniques:

- Collect, store, and visualize the infrastructure and application metrics by using [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). You can use pre-built dashboards for Google Cloud services and create custom dashboards that are tailored based on your workload's specific performance indicators and infrastructure health.
  - Collect and integrate metrics from specialized serving frameworks like [vLLM](https://docs.vllm.ai/en/latest/design/v1/metrics.html) or [NVIDIA Triton Inference Server](https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/user_guide/metrics.html) into Cloud Monitoring by using [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus).
  - Create dashboards and configure alerts for metrics that are related to custom training, endpoints, and performance, and for metrics that [Vertex AI exports to Cloud Monitoring](https://docs.cloud.google.com/vertex-ai/docs/general/monitoring-metrics).
- Collect detailed logs from your AI and ML applications and the underlying infrastructure by using [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview). These logs are essential for troubleshooting and performance analysis. They provide context around events and errors.
- Pinpoint latency issues and understand request flows across distributed AI and ML microservices by using [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview). This capability is crucial for debugging complex Vertex AI Agents interactions or multi-component inference pipelines.
- Identify performance bottlenecks within function blocks in application code by using [Cloud Profiler](https://docs.cloud.google.com/profiler/docs/about-profiler). Identifying performance bottlenecks can help you optimize resource usage and execution time.
- Gather specific accelerator-related metrics like detailed GPU utilization per process, memory usage per process, and temperature, by using tools like [NVIDIA Data Center GPU Manager (DCGM)](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party-nvidia).

### Implement data and model observability

Reliable generative AI systems require robust data and model observability,
which starts with end-to-end pipeline monitoring.

- Track data ingestion rates, processed volumes, and transformation latencies by using services like [Dataflow](https://docs.cloud.google.com/dataflow/docs/overview).
- Monitor job success and failure rates within your MLOps pipelines, including pipelines that are managed by [Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction).

Continuous assessment of data quality is crucial.

- Manage and govern data by using [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction):
  - Evaluate accuracy by validating against ground truth or by tracking outlier detection rates.
  - Monitor freshness based on the age of data and frequency of updates against SLAs.
  - Assess completeness by tracking null-value percentages and required field-fill rates.
  - Ensure validity and consistency through checks for schema-adherence and duplication.
- Proactively detect anomalies by using Cloud Monitoring alerting and through clear data lineage for traceability.
- For RAG systems, examine the relevance of the retrieved context and the groundedness (attribution to source) of the responses.
- Monitor the throughput of vector database queries.

Key model observability metrics include input-output token counts and
model-specific error rates, such as hallucination or query resolution failures.
To track these metrics, use
[Model Monitoring](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview).

- Continuously monitor the toxicity scores of the output and user-feedback ratings.
- Automate the assessment of model outputs against defined criteria by using the [Gen AI evaluation service](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview).
- Ensure sustained performance by systematically monitoring for data and concept drift with comprehensive error-rate metrics.

To track model metrics, you can use
[TensorBoard](https://www.tensorflow.org/tensorboard)
or
[MLflow](https://mlflow.org/).
For deep analysis and profiling to troubleshoot performance issues, you can use
[PyTorch XLA profiling](https://docs.cloud.google.com/tpu/docs/pytorch-xla-performance-profiling-tpu-vm)
or
[NVIDIA Nsight](https://developer.nvidia.com/nsight-systems).

## Contributors

Authors:

- [Rick (Rugui) Chen](https://www.linkedin.com/in/rugui-chen) \| AI Infrastructure Field Solutions Architect
- [Stef Ruinard](https://www.linkedin.com/in/stefruinard) \| Generative AI Field Solutions Architect

<br />

Other contributors:

- [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) \| Customer Engineer, AI/ML Specialist
- [Hossein Sarshar](https://www.linkedin.com/in/hsarshar) \| AI Infrastructure Field Solution Architect
- [Jose Andrade](https://www.linkedin.com/in/jmandrade) \| Customer Engineer, SRE Specialist
- [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) \| Cross-Product Solution Developer
- [Laura Hyatt](https://www.linkedin.com/in/laura-hyatt) \| Customer Engineer, FSI
- Olivier Martin \| AI Infrastructure Field Solution Architect
- [Radhika Kanakam](https://www.linkedin.com/in/radhika-kanakam-18ab876) \| Program Lead, Google Cloud Well-Architected Framework

<br />

<br />

<br />


# AI and ML perspective: Cost optimization

This document in
[Well-Architected Framework: AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml)
provides an overview of principles and recommendations to optimize the cost of
your AI systems throughout the ML lifecycle. By adopting a proactive and
informed cost management approach, your organization can realize the full
potential of AI and ML systems and also maintain financial discipline. The
recommendations in this document align with the
[cost optimization pillar](https://docs.cloud.google.com/architecture/framework/cost-optimization)
of the Google Cloud Well-Architected Framework.

AI and ML systems can help you unlock valuable insights and predictive
capabilities from data. For example, you can
[reduce friction in internal processes](https://cloud.google.com/blog/products/ai-machine-learning/regnology-automates-ticket-to-code-with-genai-on-vertex-ai),
[improve user experiences](https://cloud.google.com/blog/products/ai-machine-learning/using-generative-ai-for-event-experiences),
and
[gain deeper customer insights](https://cloud.google.com/blog/products/data-analytics/square-enix-builds-a-customer-data-platform-with-google-cloud).
The cloud offers vast amounts of resources and quick time-to-value without large
up-front investments for AI and ML workloads. To maximize business value and to
align the spending with your business goals, you need to understand the cost
drivers, proactively optimize costs, set up spending controls, and adopt
[FinOps](https://cloud.google.com/learn/what-is-finops)
practices.

The recommendations in this document are mapped to the following core
principles:

- [Define and measure costs and returns](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization#define_and_measure_costs_and_returns)
- [Optimize resource allocation](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization#optimize_resource_allocation)
- [Enforce data management and governance practices](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization#enforce_data_management_and_governance_practices)
- [Automate and streamline with MLOps](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization#automate_and_streamline_with_mlops)
- [Use managed services and pre-trained models](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization#use_managed_services_and_pre-trained_models)

## Define and measure costs and returns

To effectively manage AI and ML costs in Google Cloud, you must define and
measure the cloud resource costs and the business value of your AI and ML
initiatives. To help you track expenses granularly, Google Cloud provides
comprehensive billing and cost management tools, such as the following:

- Cloud Billing reports and tables
- Data Studio dashboards, budgets, and alerts
- Cloud Monitoring
- Cloud Logging

To make informed decisions about resource allocation and optimization, consider
the following recommendations.

### Establish business goals and KPIs

Align the technical choices in your AI and ML projects with business goals and
key performance indicators (KPIs).

#### Define strategic objectives and ROI-focused KPIs

Ensure that AI and ML projects are aligned with strategic objectives like
revenue growth, cost reduction, customer satisfaction, and efficiency. Engage
stakeholders to understand the business priorities. Define AI and ML objectives
that are specific, measurable, attainable, relevant, and time-bound (SMART). For
example, a SMART objective is: "Reduce chat handling time for customer support
by 15% in 6 months by using an AI chatbot".

To make progress towards your business goals and to measure the return on
investment (ROI), define KPIs for the following categories of metrics:

- Costs for training, inference, storage, and network resources, including specific unit costs (such as the cost per inference, data point, or task). These metrics help you gain insights into efficiency and cost optimization opportunities. You can track these costs by using [Cloud Billing reports](https://docs.cloud.google.com/billing/docs/reports) and [Cloud Monitoring dashboards](https://docs.cloud.google.com/monitoring/dashboards).
- Business value metrics like revenue growth, cost savings, customer satisfaction, efficiency, accuracy, and adoption. You can track these metrics by using [BigQuery analytics](https://docs.cloud.google.com/bigquery/docs/query-overview) and [Looker dashboards](https://docs.cloud.google.com/looker/docs/dashboards).
- Industry-specific metrics like the following:

  - Retail industry: measure revenue lift and churn
  - Healthcare industry: measure patient time and patient outcomes
  - Finance industry: measure fraud reduction
- Project-specific metrics. You can track these metrics by using
  [Vertex AI Experiments](https://docs.cloud.google.com/vertex-ai/docs/experiments/intro-vertex-ai-experiments)
  and
  [evaluation](https://docs.cloud.google.com/vertex-ai/docs/evaluation/introduction).

  - Predictive AI: measure accuracy and precision
  - Generative AI: measure adoption, satisfaction, and content quality
  - Computer vision AI: measure accuracy

#### Foster a culture of cost awareness and continuous optimization

Adopt
[FinOps](https://cloud.google.com/learn/what-is-finops)
principles to ensure that each AI and ML project has
[estimated costs](https://cloud.google.com/blog/topics/cost-management/unlock-the-true-cost-of-enterprise-ai-on-google-cloud)
and has ways to measure and track actual costs throughout its lifecycle. Ensure
that the costs and business benefits of your projects have assigned owners and
clear accountability.

For more information, see
[Foster a culture of cost awareness](https://docs.cloud.google.com/architecture/framework/cost-optimization/foster-culture-cost-awareness)
in the Cost Optimization pillar of the Google Cloud Well-Architected Framework.

#### Drive value and continuous optimization through iteration and feedback

Map your AI and ML applications directly to your business goals and measure the
ROI.

To validate your ROI hypotheses, start with pilot projects and use the following
iterative optimization cycle:

1. **Monitor continuously and analyze data**: Monitor KPIs and costs to identify deviations and opportunities for optimization.
2. **Make data-driven adjustments**: Optimize strategies, models, infrastructure, and resource allocation based on data insights.
3. **Refine iteratively**: Adapt business objectives and KPIs based on the things you learned and the evolving business needs. This iteration helps you maintain relevance and strategic alignment.
4. **Establish a feedback loop**: Review performance, costs, and value with stakeholders to inform ongoing optimization and future project planning.

### Manage billing data with Cloud Billing and labels

Effective cost optimization requires visibility into the source of each cost
element. The recommendations in this section can help you use Google Cloud
tools to get granular insights into your AI and ML costs. You can also attribute
costs to specific AI and ML projects, teams, and activities. These insights lay
the groundwork for cost optimization.

#### Organize and label Google Cloud resources

- Structure your projects and resources in a hierarchy that reflects your organizational structure and your AI and ML workflows. To track and analyze costs at different levels, organize your Google Cloud resources by using organizations, folders, and projects. For more information, see [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy).
- Apply meaningful [labels](https://docs.cloud.google.com/resource-manager/docs/labels-overview) to your resources. You can use labels that indicate the project, team, environment, model name, dataset, use case, and performance requirements. Labels provide valuable context for your billing data and enable granular cost analysis.
- Maintain consistency in your labeling conventions across all of your AI and ML projects. Consistent labeling conventions ensure that your billing data is organized and can be readily analyzed.

#### Use billing-related tools

- To facilitate detailed analysis and reporting, [export the billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). BigQuery has powerful query capabilities that let you analyze the billing data to help you understand your costs.
- To aggregate costs by labels, projects, or specific time periods, you can write custom SQL queries in BigQuery. Such queries let you attribute costs to specific AI and ML activities, such as model training, hyperparameter tuning, or inference.
- To identify cost anomalies or unexpected spending spikes, use the analytic capabilities in BigQuery. This approach can help you detect potential issues or inefficiencies in your AI and ML workloads.
- To identify and manage unexpected costs, use the [anomaly detection dashboard](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies) in Cloud Billing.
- To distribute costs across different teams or departments based on resource usage, use Google Cloud's [cost allocation](https://services.google.com/fh/files/misc/cloud_finops_shared_services_cost_allocation_whitepaper.pdf) feature. Cost allocation promotes accountability and transparency.
- To gain insights into spending patterns, explore the prebuilt [Cloud Billing reports](https://docs.cloud.google.com/billing/docs/reports). You can filter and customize these reports to focus on specific AI and ML projects or services.

### Monitor resources continuously with dashboards, alerts, and reports

To create a scalable and resilient way to track costs, you need continuous
monitoring and reporting. Dashboards, alerts, and reports constitute the
foundation for effective cost tracking. This foundation lets you maintain
constant access to cost information, identify areas of optimization, and
ensure alignment between business goals and costs.

#### Create a reporting system

Create scheduled reports and share them with appropriate stakeholders.

Use
[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs)
to collect metrics from various sources, including your applications,
infrastructure, and Google Cloud services like Compute Engine,
Google Kubernetes Engine (GKE), and Cloud Run functions. To visualize
metrics and logs in real time, you can use the prebuilt Cloud Monitoring
dashboard or create custom dashboards. Custom dashboards let you define and add
metrics to track specific aspects of your systems, like model performance, API
calls, or business-level KPIs.

Use
[Cloud Logging](https://docs.cloud.google.com/logging/docs)
for centralized collection and storage of logs from your applications, systems,
and Google Cloud services. Use the logs for the following purposes:

- Track costs and utilization of resources like CPU, memory, storage, and network.
- Identify cases of over-provisioning (where resources aren't fully utilized) and under-provisioning (where there are insufficient resources). Over-provisioning results in unnecessary costs. Under-provisioning slows training times and might cause performance issues.
- Identify idle or underutilized resources, such as VMs and GPUs, and take steps to shut down or rightsize them to optimize costs.
- Identify cost spikes to detect sudden and unexpected increases in resource usage or costs.

Use
[Looker](https://docs.cloud.google.com/looker/docs/intro)
or
[Data Studio](https://docs.cloud.google.com/looker/docs/studio)
to create interactive dashboards and reports. Connect the dashboards and reports
to various data sources, including BigQuery and
Cloud Monitoring.

#### Set alert thresholds based on key KPIs

For your KPIs, determine the thresholds that should trigger alerts. Meaningful
alert thresholds can help you avoid alert fatigue. Create
[alerting policies](https://docs.cloud.google.com/monitoring/alerts)
in Cloud Monitoring to get notifications related to your KPIs. For example,
you can get notifications when accuracy drops below a certain threshold or
latency exceeds a defined limit. Alerts based on log data can notify you about
potential cost issues in real time. Such alerts let you take corrective actions
promptly and prevent further financial loss.

## Optimize resource allocation

To achieve cost efficiency for your AI and ML workloads in Google Cloud, you
must optimize resource allocation. To help you avoid unnecessary expenses and
ensure that your workloads have the resources that they need to perform
optimally, align resource allocation with the needs of your workloads.

To optimize the allocation of cloud resources to AI and ML workloads, consider
the following recommendations.

### Use autoscaling to dynamically adjust resources

Use Google Cloud services that support autoscaling, which automatically
adjusts resource allocation to match the current demand. Autoscaling provides
the following benefits:

- **Cost and performance optimization**: You avoid paying for idle resources. At the same time, autoscaling ensures that your systems have the necessary resources to perform optimally, even at peak load.
- **Improved efficiency**: You free up your team to focus on other tasks.
- **Increased agility**: You can respond quickly to changing demands and maintain high availability for your applications.

The following table summarizes the techniques that you can use to implement
autoscaling for different stages of your AI projects.

| Stage | Autoscaling techniques |
|---|---|
| Training | - Use managed services like [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/training/overview) or [GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler), which offer built-in autoscaling capabilities for training jobs. - Configure autoscaling policies to scale the number of training instances based on metrics like CPU utilization, memory usage, and job queue length. - Use custom scaling metrics to fine-tune autoscaling behavior for your specific workloads. |
| Inference | - Deploy your models on scalable platforms like [Vertex AI Inference](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview), [GPUs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling), or [TPUs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling-tpu). - Use autoscaling features to adjust the number of replicas based on metrics like request rate, latency, and resource utilization. - Implement load balancing to distribute traffic evenly across replicas and ensure high availability. |

### Start with small models and datasets

To help reduce costs, test ML hypotheses at a small scale when possible and use
an iterative approach. This approach, with smaller models and datasets, provides
the following benefits:

- **Reduced costs from the start**: Less compute power, storage, and processing time can result in lower costs during the initial experimentation and development phases.
- **Faster iteration**: Less training time is required, which lets you iterate faster, explore alternative approaches, and identify promising directions more efficiently.
- **Reduced complexity**: Simpler debugging, analysis, and interpretation of results, which leads to faster development cycles.
- **Efficient resource utilization**: Reduced chance of over-provisioning resources. You provision only the resources that are necessary for the current workload.

Consider the following recommendations:

- **Use sample data first**: Train your models on a representative subset of your data. This approach lets you assess the model's performance and identify potential issues without processing the entire dataset.
- **Experiment by using notebooks** : Start with smaller instances and scale as needed. You can use [Vertex AI Workbench](https://docs.cloud.google.com/vertex-ai/docs/workbench/introduction), a managed Jupyter notebook environment that's well suited for experimentation with different model architectures and datasets.
- **Start with simpler or pre-trained models** : Use
  [Vertex AI Model Garden](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models)
  to discover and explore the pre-trained models. Such models require fewer
  computational resources. Gradually increase the
  complexity as needed based on performance requirements.

  - Use pre-trained models for tasks like image classification and natural language processing. To save on training costs, you can fine-tune the models on smaller datasets initially.
  - Use [BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction) for structured data. BigQuery ML lets you create and deploy models directly within BigQuery. This approach can be cost-effective for initial experimentation, because you can take advantage of the pay-per-query pricing model for BigQuery.
- **Scale for resource optimization**: Use Google Cloud's flexible
  infrastructure to scale resources as needed. Start with smaller instances
  and adjust their size or number when necessary.

### Discover resource requirements through experimentation

Resource requirements for AI and ML workloads can vary significantly. To
optimize resource allocation and costs, you must understand the specific needs
of your workloads through systematic experimentation. To identify the most
efficient configuration for your models, test different configurations and
analyze their performance. Then, based on the requirements, right-size the
resources that you used for training and serving.

We recommend the following approach for experimentation:

1. **Start with a baseline** : Begin with a baseline configuration based on your initial estimates of the workload requirements. To create a baseline, you can use the cost estimator for new workloads or use an existing billing report. For more information, see [Unlock the true cost of enterprise AI on Google Cloud](https://cloud.google.com/blog/topics/cost-management/unlock-the-true-cost-of-enterprise-ai-on-google-cloud).
2. **Understand your quotas** : Before launching extensive experiments, familiarize yourself with your Google Cloud project [quotas](https://docs.cloud.google.com/docs/quotas/overview) for the resources and APIs that you plan to use. The quotas determine the range of configurations that you can realistically test. By becoming familiar with quotas, you can work within the available resource limits during the experimentation phase.
3. **Experiment systematically** : Adjust parameters like the number of CPUs, amount of memory, number and type of GPUs and TPUs, and storage capacity. [Vertex AI training](https://docs.cloud.google.com/vertex-ai/docs/training-overview) and [Vertex AI predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview) let you experiment with different machine types and configurations.
4. **Monitor utilization, cost, and performance**: Track the resource
   utilization, cost, and key performance metrics such as training time,
   inference latency, and model accuracy, for each configuration that you
   experiment with.

   - To track resource utilization and performance metrics, you can use the Vertex AI console.
   - To collect and analyze detailed performance metrics, use Cloud Monitoring.
   - To view costs, use [Cloud Billing reports](https://docs.cloud.google.com/billing/docs/reports) and [Cloud Monitoring dashboards](https://docs.cloud.google.com/monitoring/dashboards).
   - To identify performance bottlenecks in your models and optimize resource utilization, use profiling tools like [Vertex AI TensorBoard](https://docs.cloud.google.com/vertex-ai/docs/experiments/tensorboard-introduction).
5. **Analyze costs**: Compare the cost and performance of each
   configuration to identify the most cost-effective option.

6. **Establish resource thresholds and improvement targets based on quotas**:
   Define thresholds for when scaling begins to yield
   diminishing returns in performance, such as minimal reduction in training
   time or latency for a significant cost increase. Consider project quotas
   when setting these thresholds. Determine the point where the cost and
   potential quota implications of further scaling are no longer justified by
   performance gains.

7. **Refine iteratively**: Repeat the experimentation process with
   refined configurations based on your findings. Always ensure that the
   resource usage remains within your allocated quotas and aligns with
   established cost-benefit thresholds.

### Use MLOps to reduce inefficiencies

As organizations increasingly use ML to drive innovation and efficiency,
managing the ML lifecycle effectively becomes critical. ML operations (MLOps) is
a set of practices that automate and streamline the ML lifecycle, from model
development to deployment and monitoring.

#### Align MLOps with cost drivers

To take advantage of MLOps for cost efficiency, identify the primary cost
drivers in the ML lifecycle. Then, you can adopt and implement MLOps practices
that are aligned with the cost drivers. Prioritize and adopt the MLOps features
that address the most impactful cost drivers. This approach helps ensure a
manageable and successful path to significant cost savings.

#### Implement MLOps for cost optimization

The following are common MLOps practices that help to reduce cost:

- **Version control**: Tools like Git can help you to track versions of code, data, and models. Version control ensures reproducibility, facilitates collaboration, and prevents costly rework that can be caused by versioning issues.
- **Continuous integration and continuous delivery (CI/CD)** : [Cloud Build](https://docs.cloud.google.com/build/docs/overview) and [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) let you implement CI/CD pipelines to automate building, testing, and deployment of your ML models. CI/CD pipelines ensure efficient resource utilization and minimize the costs associated with manual interventions.
- **Observability** : [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) and [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) let you track model performance in production, identify issues, and trigger alerts for proactive intervention. Observability lets you maintain model accuracy, optimize resource allocation, and prevent costly downtime or performance degradation.
- **Model retraining** : [Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction) simplifies the processes for retraining models periodically or when performance degrades. When you use Vertex AI Pipelines for retraining, it helps ensure that your models remain accurate and efficient, which can prevent unnecessary resource consumption and maintain optimal performance.
- **Automated testing and evaluation** : [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/evaluation/introduction) helps you accelerate and standardize model evaluation. Implement automated tests throughout the ML lifecycle to ensure the quality and reliability of your models. Such tests can help you catch errors early, prevent costly issues in production, and reduce the need for extensive manual testing.

For more information, see
[MLOps: Continuous delivery and automation pipelines in machine learning](https://docs.cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning).

## Enforce data management and governance practices

Effective data management and governance practices are critical to cost
optimization. Well organized data can encourage teams to reuse datasets, avoid
needless duplication, and reduce the effort to obtain high quality data. By
proactively managing data, you can reduce storage costs, enhance data quality,
and ensure that your ML models are trained on the most relevant and valuable
data.

To implement data management and governance practices, consider the following
recommendations.

### Establish and adopt a data governance framework

The growing prominence of AI and ML has made data the most valuable asset for
organizations that are undergoing digital transformation. A robust framework for
[data governance](https://cloud.google.com/learn/what-is-data-governance)
is a crucial requirement for managing AI and ML workloads cost-effectively at
scale. A data governance framework with clearly defined policies, procedures,
and roles provides a structured approach for managing data throughout its
lifecycle. Such a framework helps to improve data quality, enhance security,
improve utilization, and reduce redundancy.

#### Establish a data governance framework

There are many pre-existing frameworks for data governance, such as the
frameworks published by the
[EDM Council](https://edmcouncil.org/),
with options available for different industries and organization sizes. Choose
and adapt a framework that aligns with your specific needs and priorities.

#### Implement the data governance framework

Google Cloud provides the following services and tools to help you implement a
robust data governance framework:

- [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction)
  is an intelligent data fabric that helps you unify distributed data and
  automate data governance without the need to consolidate data sets in one
  place. This helps to reduce the cost to distribute and maintain data,
  facilitate data discovery, and promote reuse.

  - To organize data, use Knowledge Catalog abstractions and set up [logical data lakes and zones](https://docs.cloud.google.com/dataplex/docs/create-lake).
  - To administer access to data lakes and zones, use [Google Groups](https://docs.cloud.google.com/iam/docs/groups-in-cloud-console) and [Knowledge Catalog roles](https://docs.cloud.google.com/dataplex/docs/lake-security).
  - To streamline data quality processes, enable [auto data quality](https://docs.cloud.google.com/dataplex/docs/auto-data-quality-overview).
- Knowledge Catalog
  is also a fully managed and scalable metadata management service. The
  [catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview)
  provides a foundation that ensures that data assets are accessible and
  reusable.

  - Metadata from the [supported Google Cloud sources](https://docs.cloud.google.com/dataplex/docs/catalog-overview#supported-sources) is automatically ingested into the universal catalog. For data sources outside of Google Cloud, [create custom entries](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources#create-custom-entry).
  - To improve the discoverability and management of data assets, enrich technical metadata with business metadata by using [aspects](https://docs.cloud.google.com/dataplex/docs/enrich-entries-metadata#aspects).
  - Ensure that data scientists and ML practitioners have sufficient [permissions](https://docs.cloud.google.com/dataplex/docs/iam-permissions) to access Knowledge Catalog and use the [search](https://docs.cloud.google.com/dataplex/docs/search-assets) function.
- [BigQuery sharing](https://docs.cloud.google.com/bigquery/docs/analytics-hub-introduction)
  lets you efficiently and securely exchange data assets across your
  organizations to address challenges of data reliability and cost.

  - Set up [data exchanges](https://docs.cloud.google.com/bigquery/docs/analytics-hub-manage-exchanges) and ensure that curated data assets can be viewed as [listings](https://docs.cloud.google.com/bigquery/docs/analytics-hub-manage-listings).
  - Use [data clean rooms](https://docs.cloud.google.com/bigquery/docs/data-clean-rooms) to securely manage access to sensitive data and efficiently partner with external teams and organizations on AI and ML projects.
  - Ensure that data scientists and ML practitioners have sufficient [permissions](https://docs.cloud.google.com/bigquery/docs/analytics-hub-grant-roles) to view and publish datasets to BigQuery sharing.

### Make datasets and features reusable throughout the ML lifecycle

For significant efficiency and cost benefits, reuse datasets and features
across multiple ML projects. When you avoid redundant data engineering and
feature development efforts, your organization can accelerate model development,
reduce infrastructure costs, and free up valuable resources for other critical
tasks.

Google Cloud provides the following services and tools to help you reuse
datasets and features:

- Data and ML practitioners can publish [data products](https://docs.cloud.google.com/architecture/build-data-products-data-mesh) to maximize reuse across teams. The data products can then be discovered and used through Knowledge Catalog and BigQuery sharing.
- For tabular and structured datasets, you can use [Vertex AI Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview) to promote reusability and streamline feature management through BigQuery.
- You can store unstructured data in Cloud Storage and govern the data by using [BigQuery object tables and signed URLs](https://docs.cloud.google.com/bigquery/docs/object-table-introduction).
- You can manage vector embeddings by including metadata in your [Vector Search indexes](https://docs.cloud.google.com/vertex-ai/docs/vector-search/create-manage-index).

## Automate and streamline with MLOps

A primary benefit of adopting MLOps practices is a reduction in costs for
technology and personnel. Automation helps you avoid the duplication of ML
activities and reduce the workload for data scientists and ML engineers.

To automate and streamline ML development with MLOps, consider the following
recommendations.

### Automate and standardize data collection and processing

To help reduce ML development effort and time, automate and standardize your
data collection and processing technologies.

#### Automate data collection and processing

This section summarizes the products, tools, and techniques that you can use to
automate data collection and processing.

Identify and choose the relevant data sources for your AI and ML tasks:

- Database options such as [Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction), [Spanner](https://docs.cloud.google.com/spanner), [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/docs/overview), [Firestore](https://docs.cloud.google.com/firestore/docs/overview), and [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction). Your choice depends on your requirements, such as latency on write access (static or dynamic), data volume (high or low), and data format (structured, unstructured, or semi-structured). For more information, see [Google Cloud databases](https://cloud.google.com/products/databases#our-portfolio-of-databases).
- Data lakes such as Cloud Storage with [BigLake](https://docs.cloud.google.com/bigquery/docs/biglake-intro).
- [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction) for governing data across sources.
- Streaming events platforms such as [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview), [Dataflow](https://docs.cloud.google.com/dataflow/docs/overview), or [Apache Kafka](https://kafka.apache.org/).
- External APIs.

For each of your data sources, choose an ingestion tool:

- Dataflow: For batch and stream processing of data from various sources, with ML-component integration. For an event-driven architecture, you can combine Dataflow with [Eventarc](https://docs.cloud.google.com/eventarc/docs) to efficiently process data for ML. To enhance MLOps and ML job efficiency, use GPU and right-fitting capabilities.
- [Cloud Run functions](https://docs.cloud.google.com/run/docs/resource-model#functions): For event-driven data ingestion that gets triggered by changes in data sources for real-time applications.
- BigQuery: For classical tabular data ingestion with frequent access.

Choose tools for data transformation and loading:

- Use tools such as [Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) or [Dataform](https://docs.cloud.google.com/dataform/docs/overview) to automate data transformations like feature scaling, encoding categorical variables, and creating new features in batch, streaming, or real time. The tools that you select depend upon your requirements and chosen services.
- Use [Vertex AI Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview) to automate feature creation and management. You can centralize features for reuse across different models and projects.

#### Standardize data collection and processing

To discover, understand, and manage data assets, use metadata management
services like
[Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview).
It helps you standardize data definitions and ensure consistency across your
organization.

To enforce standardization and avoid the cost of maintaining multiple custom
implementations, use automated training pipelines and orchestration. For more
information, see the next section.

### Automate training pipelines and reuse existing assets

To boost efficiency and productivity in MLOps, automated training pipelines are
crucial. Google Cloud offers a robust set of tools and services to build
and deploy training pipelines, with a strong emphasis on reusing existing
assets. Automated training pipelines help to accelerate model development,
ensure consistency, and reduce redundant effort.

#### Automate training pipelines

The following table describes the Google Cloud services and features that
you can use to automate the different functions of a training pipeline.

| Function | Google Cloud services and features |
|---|---|
| Orchestration: Define complex ML workflows consisting of multiple steps and dependencies. You can define each step as a separate containerized task, which helps you manage and scale individual tasks with ease. | - To create and orchestrate pipelines, use [Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction) or Kubeflow Pipelines. These tools support simple data transformation, model training, model deployment, and pipeline versioning. They let you define dependencies between steps, manage data flow, and automate the execution of the entire workflow. - For complex operational tasks with heavy CI/CD and extract, transform, and load (ETL) requirements, use [Managed Service for Apache Airflow](https://docs.cloud.google.com/composer/docs/composer-3/composer-overview). If you prefer Airflow for data orchestration, Managed Service for Apache Airflow is a compatible managed service that's built on Airflow. - For pipelines that are managed outside of Vertex AI Pipelines, use [Workflows](https://docs.cloud.google.com/workflows/docs/choose-orchestration) for infrastructure-focused tasks like starting and stopping VMs or integrating with external systems. - To automate your CI/CD process, use [Cloud Build](https://docs.cloud.google.com/build/docs/overview) with [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview). You can set up notifications and automatic triggers for when new code is pushed or when a new model needs to be trained. - For a fully-managed, scalable solution for pipeline management, use [Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/overview). |
| Versioning: Track and control different versions of pipelines and components to ensure reproducibility and auditability. | Store [Kubeflow pipeline](https://docs.cloud.google.com/artifact-registry/docs/kfp) templates in a Kubeflow Pipelines repository in [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview). |
| Reusability: Reuse existing pipeline components and artifacts, such as prepared datasets and trained models, to accelerate development. | Store your pipeline templates in [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) and share them across your organization. |
| Monitoring: Monitor pipeline execution to identify and address any issues. | Use Cloud Logging and Cloud Monitoring. For more information, see [Monitor resources continuously with dashboards, alerts, and reports](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization#monitor_resources_continuously_with_dashboards_alerts_and_reports). |

#### Expand reusability beyond pipelines

Look for opportunities to expand reusability beyond training pipelines. The
following are examples of Google Cloud capabilities that let you reuse ML
features, datasets, models, and code.

- [Vertex AI Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview) provides a centralized repository for organizing, storing, and serving ML features. It lets you reuse features across different projects and models, which can improve consistency and reduce feature engineering effort. You can store, share, and access features for both online and offline use cases.
- [Vertex AI datasets](https://docs.cloud.google.com/vertex-ai/docs/datasets/overview) enable teams to create and manage datasets centrally, so your organization can maximize reusability and reduce data duplication. Your teams can search and discover the datasets by using [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview).
- [Vertex AI Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction) lets you store, manage, and deploy your trained models. Model Registry lets you reuse the models in subsequent pipelines or for online prediction, which helps you take advantage of previous training efforts.
- [Custom containers](https://docs.cloud.google.com/vertex-ai/docs/training/containers-overview) let you package your training code and dependencies into containers and store the containers in Artifact Registry. Custom containers let you provide consistent and reproducible training environments across different pipelines and projects.

### Use Google Cloud services for model evaluation and tuning

Google Cloud offers a powerful suite of tools and services to streamline
and automate model evaluation and tuning. These tools and services can help you
reduce your time to production and reduce the resources required for continuous
training and monitoring. By using these services, your AI and ML teams can
enhance model performance with fewer expensive iterations, achieve faster
results, and minimize wasted compute resources.

#### Use resource-efficient model evaluation and experimentation

Begin an AI project with experiments before you scale up your solution. In your
experiments, track various metadata such as dataset version, model parameters,
and model type. For further reproducibility and comparison of the results, use
metadata tracking in addition to code versioning, similar to the capabilities in
Git. To avoid missing information or deploying the wrong version in production,
use
[Vertex AI Experiments](https://docs.cloud.google.com/vertex-ai/docs/experiments/intro-vertex-ai-experiments)
before you implement full-scale deployment or training jobs.

Vertex AI Experiments lets you do the following:

- Streamline and automate metadata tracking and discovery through a user friendly UI and API for production-ready workloads.
- Analyze the model's performance metrics and compare metrics across multiple models.

After the model is trained, continuously monitor the performance and data drift
over time for incoming data. To streamline this process, use
[Vertex AI Model Monitoring](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview)
to directly access the created models in
[Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction).
Model Monitoring also automates monitoring for data and
results through online and batch predictions. You can export the results to
BigQuery for further analysis and tracking.

#### Choose optimal strategies to automate training

For hyperparameter tuning, we recommend the following approaches:

- To automate the process of finding the optimal hyperparameters for your models, use [Vertex AI hyperparameter tuning](https://docs.cloud.google.com/vertex-ai/docs/training/hyperparameter-tuning-overview). Vertex AI uses advanced algorithms to explore the hyperparameter space and identify the best configuration.
- For efficient hyperparameter tuning, consider using [Bayesian optimization](https://docs.cloud.google.com/vertex-ai/docs/training/hyperparameter-tuning-overview#understanding-trials) techniques, especially when you deal with complex models and large datasets.

For distributed training, we recommend the following approaches:

- For large datasets and complex models, use the distributed training
  infrastructure of Vertex AI. This approach lets you train
  your models on multiple machines, which helps to significantly reduce
  training time and associated costs. Use tools like the following:

  - [Vertex AI tuning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models) to perform supervised fine-tuning of Gemini, Imagen, and other models.
  - [Vertex AI training](https://docs.cloud.google.com/vertex-ai/docs/training-overview) or [Ray on Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/open-source/ray-on-vertex-ai/overview) for custom distributed training.
- Choose optimized ML frameworks, like Keras and PyTorch, that support
  distributed training and efficient resource utilization.

#### Use explainable AI

It's crucial to understand why a model makes certain decisions and to identify
potential biases or areas for improvement. Use
[Vertex Explainable AI](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview)
to gain insights into your model's predictions. Vertex Explainable AI offers a way
to automate feature-based and example-based explanations that are linked to your
Vertex AI experiments.

- Feature-based: To understand which features are most influential in your model's predictions, analyze [feature attributions](https://docs.cloud.google.com/vertex-ai/docs/tabular-data/classification-explanations). This understanding can guide feature-engineering efforts and improve model interpretability.
- [Example-based](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/configuring-explanations-example-based): To return a list of examples (typically from the training set) that are most similar to the input, Vertex AI uses nearest neighbor search. Because similar inputs generally yield similar predictions, you can use these explanations to explore and explain a model's behavior.

## Use managed services and pre-trained models

Adopt an incremental approach to model selection and model development. This
approach helps you avoid excessive costs that are associated with starting
afresh every time. To control costs, use ML frameworks, managed services, and
pre-trained models.

To get the maximum value from managed services and pre-trained models, consider
the following recommendations.

### Use notebooks for exploration and experiments

[Notebook](https://en.wikipedia.org/wiki/Notebook_interface)
environments are crucial for cost-effective ML experimentation. A notebook
provides an interactive and collaborative space for data scientists and
engineers to explore data, develop models, share knowledge, and iterate
efficiently. Collaboration and knowledge sharing through notebooks significantly
accelerates development, code reviews, and knowledge transfer. Notebooks help
streamline workflows and reduce duplicated effort.

Instead of procuring and managing expensive hardware for your development
environment, you can use the scalable and on-demand infrastructure of
Vertex AI Workbench and Colab Enterprise.

- [Vertex AI Workbench](https://docs.cloud.google.com/vertex-ai/docs/workbench/introduction)
  is a Jupyter notebook development environment for the entire data science
  workflow. You can interact with Vertex AI and other Google Cloud
  services from within an instance's Jupyter notebook.
  Vertex AI Workbench integrations and features help you do the
  following:

  - Access and explore data from a Jupyter notebook by using BigQuery and Cloud Storage integrations.
  - Automate recurring updates to a model by using scheduled executions of code that runs on Vertex AI.
  - Process data quickly by running a notebook on a Managed Service for Apache Spark cluster.
  - Run a notebook as a step in a pipeline by using Vertex AI Pipelines.
- [Colab Enterprise](https://docs.cloud.google.com/colab/docs/introduction)
  is a collaborative, managed notebook environment that has the security and
  compliance capabilities of Google Cloud.
  Colab Enterprise is ideal if your project's priorities
  include collaborative development and reducing the effort to manage
  infrastructure. Colab Enterprise integrates with
  Google Cloud services and AI-powered assistance that uses
  Gemini. Colab Enterprise lets you do the following:

  - Work in notebooks without the need to manage infrastructure.
  - Share a notebook with a single user, Google group, or Google Workspace domain. You can control notebook access through Identity and Access Management (IAM).
  - Interact with features built into Vertex AI and BigQuery.

To track changes and revert to previous versions when necessary, you can
integrate your notebooks with version control tools like Git.

### Start with existing and pre-trained models

Training complex models from scratch, especially deep-learning models, requires
significant computational resources and time. To accelerate your model selection
and development process, start with existing and pre-trained models. These
models, which are trained on vast datasets, eliminate the need to train models
from scratch and significantly reduce cost and development time.

#### Reduce training and development costs

Select an appropriate model or API for each ML task and combine them to create
an end-to-end ML development process.

[Vertex AI Model Garden](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models)
offers a vast collection of pre-trained models for tasks such as image
classification, object detection, and natural language processing. The models
are grouped into the following categories:

- [Google models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/available-models#google-models) like the Gemini family of models and Imagen for image generation.
- [Open-source models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/available-models#oss-models) like Gemma and Llama.
- [Third-party models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/available-models#partner-models) from partners like Anthropic and Mistral AI.

Google Cloud provides
[AI and ML APIs](https://cloud.google.com/ai/apis)
that let developers integrate powerful AI capabilities into applications without
the need to build models from scratch.

- [Cloud Vision API](https://docs.cloud.google.com/vision/docs/apis) lets you derive insights from images. This API is valuable for applications like image analysis, content moderation, and automated data entry.
- [Cloud Natural Language API](https://docs.cloud.google.com/natural-language/docs/apis) lets you analyze text to understand its structure and meaning. This API is useful for tasks like customer feedback analysis, content categorization, and understanding social media trends.
- [Speech-to-Text API](https://docs.cloud.google.com/speech-to-text/docs/apis) converts audio to text. This API supports a wide range of languages and dialects.
- [Video Intelligence API](https://docs.cloud.google.com/video-intelligence/docs/apis) analyzes video content to identify objects, scenes, and actions. Use this API for video content analysis, content moderation, and video search.
- [Document AI API](https://docs.cloud.google.com/document-ai/docs/reference) processes documents to extract, classify, and understand data. This API helps you automate document processing workflows.
- [Dialogflow API](https://docs.cloud.google.com/dialogflow/cx/docs/reference) enables the creation of conversational interfaces, such as chatbots and voice assistants. You can use this API to create customer service bots and virtual assistants.
- [Gemini API in Vertex AI](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference) provides access to Google's most capable and general-purpose AI model.

#### Reduce tuning costs

To help reduce the need for extensive data and compute time, fine-tune your
pre-trained models on specific datasets. We recommend the following
approaches:

- **Learning transfer**: Use the knowledge from a pre-trained model for a new task, instead of starting from scratch. This approach requires less data and compute time, which helps to reduce costs.
- **Adapter tuning ([parameter-efficient tuning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models#parameter-tuning))**: Adapt models to new tasks or domains without full fine-tuning. This approach requires significantly lower computational resources and a smaller dataset.
- **[Supervised fine tuning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-supervised-tuning)**: Adapt model behavior with a labeled dataset. This approach simplifies the management of the underlying infrastructure and the development effort that's required for a custom training job.

#### Explore and experiment by using Vertex AI Studio

[Vertex AI Studio](https://cloud.google.com/generative-ai-studio)
lets you rapidly test, prototype, and deploy generative AI applications.

- **Integration with Model Garden**: Provides quick access to the latest models and lets you efficiently deploy the models to save time and costs.
- **Unified access to specialized models**: Consolidates access to a wide range of pre-trained models and APIs, including those for chat, text, media, translation, and speech. This unified access can help you reduce the time spent searching for and integrating individual services.

### Use managed services to train or serve models

Managed services can help reduce the cost of model training and simplify the
infrastructure management, which lets you focus on model development and
optimization. This approach can result in significant cost benefits and
increased efficiency.

#### Reduce operational overhead

To reduce the complexity and cost of infrastructure management, use managed
services such as the following:

- [Vertex AI training](https://docs.cloud.google.com/vertex-ai/docs/training-overview) provides a fully managed environment for training your models at scale. You can choose from various prebuilt containers with popular ML frameworks or use your own custom containers. Google Cloud handles infrastructure provisioning, scaling, and maintenance, so you incur lower operational overhead.
- [Vertex AI predictions](https://docs.cloud.google.com/vertex-ai/docs/predictions/overview) handles infrastructure scaling, load balancing, and request routing. You get high availability and performance without manual intervention.
- [Ray on Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/open-source/ray-on-vertex-ai/overview) provides a fully managed Ray cluster. You can use the cluster to run complex custom AI workloads that perform many computations (hyperparameter tuning, model fine-tuning, distributed model training, and reinforcement learning from human feedback) without the need to manage your own infrastructure.

#### Use managed services to optimize resource utilization

For details about efficient resource utilization, see
[Optimize resource utilization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/cost-optimization#optimize_resource_allocation).

## Contributors

Authors:

- [Isaac Lo](https://www.linkedin.com/in/isaac-l-25525440) \| AI Business Development Manager
- [Anastasia Prokaeva](https://www.linkedin.com/in/anastasiia-prokaieva) \| Field Solutions Architect, Generative AI
- [Amy Southwood](https://www.linkedin.com/in/amycsouthwood) \| Technical Solutions Consultant, Data Analytics \& AI

<br />

Other contributors:

- [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) \| Customer Engineer, AI/ML Specialist
- [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) \| Cross-Product Solution Developer
- [Marwan Al Shawi](https://www.linkedin.com/in/marwanalshawi) \| Partner Customer Engineer
- [Nicolas Pintaux](https://www.linkedin.com/in/nicolaspintaux) \| Customer Engineer, Application Modernization Specialist

<br />

<br />

<br />


# AI and ML perspective: Performance optimization

This document in the
[Google Cloud Well-Architected Framework: AI and ML perspective](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml)
provides principles and recommendations to help you optimize the performance of
your AI and ML workloads on Google Cloud. The recommendations in
this document align with the
[performance optimization pillar](https://docs.cloud.google.com/architecture/framework/performance-optimization)
of the Well-Architected Framework.

AI and ML systems enable advanced automation and decision-making capabilities
for your organization. The performance of these systems can directly affect
important business drivers like revenue, costs, and customer satisfaction. To
realize the full potential of AI and ML systems, you must optimize their
performance based on your business goals and technical requirements. The
performance optimization process often involves trade-offs. For example, a
design choice that provides the required performance might lead to higher costs.
The recommendations in this document prioritize performance over other
considerations.

To optimize AI and ML performance, you need to make decisions regarding factors
like the model architecture, parameters, and training strategy. When you make
these decisions, consider the entire lifecycle of the AI and ML systems and
their deployment environment. For example, very large LLMs can be highly
performant on massive training infrastructure, but might not perform well in
capacity-constrained environments like mobile devices.

The recommendations in this document are mapped to the following core
principles:

- [Establish performance objectives and evaluation methods](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#performance-objectives-evaluation-methods)
- [Run and track frequent experiments](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#run-track-exp)
- [Build and automate training and serving infrastructure](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#build-automate-training-serving)
- [Match design choices to performance requirements](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#match-design-performance)
- [Link performance metrics to design and configuration choices](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#link-perf-design)

## Establish performance objectives and evaluation methods

Your business strategy and goals are the foundation for leveraging AI and ML
technologies. Translate your business goals into measurable key performance
indicators (KPIs). Examples of KPIs include total revenue, costs, conversion
rate, retention or churn rate, customer satisfaction, and employee satisfaction.

### Define realistic objectives

According to
[site reliability engineering (SRE) best practices](https://sre.google/sre-book/service-level-objectives/#objectives-g0s1tdcz),
the objectives of a service must reflect a performance level that satisfies the
requirements of typical customers. This means that service objectives must be
realistic in terms of scale and feature performance.

Unrealistic objectives can lead to wasted resources for minimal performance
gains. Models that provide the highest performance might not lead to
optimal business outcomes. Such models might require more time and cost to train
and run.

When you define objectives, distinguish between and prioritize quality and
performance objectives:

- *Quality* refers to inherent characteristics that determine the value of an entity. It helps you assess whether the entity meets your expectations and standards.
- *Performance* refers to how efficiently and effectively an entity functions or carries out its intended purpose.

ML engineers can improve the performance metrics of a model during the training
process. Vertex AI provides an
[evaluation service](https://docs.cloud.google.com/vertex-ai/docs/evaluation/introduction)
that ML engineers can use to implement standardized and repeatable tracking of
quality metrics. The *prediction efficiency* of a model indicates how well a
model performs in production or at inference time. To monitor performance, use
[Cloud Monitoring](https://docs.cloud.google.com/monitoring#documentation)
and
[Vertex AI Model Monitoring](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview).
To select appropriate models and decide how to train them, you must translate
business goals into technical requirements that determine quality and
performance metrics.

To understand how to set realistic objectives and identify appropriate
performance metrics, consider the following example for an AI-powered fraud
detection system:

- **Business objective**: For a fraud detection system, an unrealistic business objective is to detect 100% of fraudulent transactions accurately within one nanosecond at a peak traffic of 100 billion transactions per second. A more realistic objective is to detect fraudulent transactions with 95% accuracy in 100 milliseconds for 90% of online predictions during US working hours at a peak volume of one million transactions per second.
- **Performance metrics** : Detecting fraud is a classification problem. You can measure the quality of a fraud detection system by using metrics like [recall](https://developers.google.com/machine-learning/glossary#recall), [F1 score](https://developers.google.com/machine-learning/glossary#f1), and [accuracy](https://developers.google.com/machine-learning/glossary#accuracy). To track system performance or speed, you can measure inference latency. Detecting potentially fraudulent transactions might be more valuable than accuracy. Therefore, a realistic goal might be a high recall with a p90 latency that's less than 100 milliseconds.

### Monitor performance at all stages of the model lifecycle

During experimentation and training and after model deployment, monitor your
KPIs and observe any deviations from the business objectives. A comprehensive
monitoring strategy helps you make critical decisions about model quality and
resource utilization, such as the following:

- Decide when to stop a training job.
- Determine whether a model's performance is degrading in production.
- Improve the cost and time-to-market for new models.

#### Monitoring during experimentation and training

The objective of the experimentation stage is to find the optimal overall
approach, model architecture, and hyperparameters for a specific task.
Experimentation helps you iteratively determine the configuration that provides
optimal performance and how to train the model. Monitoring helps you efficiently
identify potential areas of improvement.

To monitor a model's quality and training efficiency, ML engineers must do the
following:

- Visualize model quality and performance metrics for each trial.
- Visualize model graphs and metrics, such as histograms of weights and biases.
- Visually represent training data.
- Profile training algorithms on different hardware.

To monitor experimentation and training, consider the following
recommendations:

| Monitoring aspect | Recommendation |
|---|---|
| Model quality | To visualize and track experiment metrics like accuracy and to visualize model architecture or training data, use [TensorBoard](https://www.tensorflow.org/tensorboard/get_started). TensorBoard is an open-source suite of tools that's compatible with ML frameworks like the following: - [XGBoost](https://github.com/dmlc/xgboost/issues/5727#issuecomment-645861763) - [JAX](https://docs.jax.dev/en/latest/profiling.html#tensorboard-profiling) - [Flax](https://github.com/google/flax/blob/main/flax/metrics/tensorboard.py) - [PyTorch](https://pytorch.org/docs/stable/tensorboard.html) - [PyTorch with accelerated linear algebra (XLA)](https://docs.cloud.google.com/tpu/docs/pytorch-xla-performance-profiling-tpu-vm#analysis_in_tensorboard) for TPU training - [TensorFlow](https://www.tensorflow.org/tensorboard/get_started) |
| Experiment tracking | [Vertex AI Experiments](https://docs.cloud.google.com/vertex-ai/docs/experiments/intro-vertex-ai-experiments) integrates with managed enterprise-grade [Vertex AI TensorBoard](https://docs.cloud.google.com/vertex-ai/docs/experiments/tensorboard-introduction) instances to support experiment tracking. This integration enables reliable storage and sharing of logs and metrics. To let multiple teams and individuals track experiments, we recommend that you use the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege). |
| Training and experimentation efficiency | Vertex AI exports metrics to [Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) and collects telemetry data and logs by using an observability agent. You can visualize the metrics in the Google Cloud console. Alternatively, create dashboards or alerts based on these metrics by using Monitoring. For more information, see [Monitoring metrics for Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/general/monitoring-metrics). |
| NVIDIA GPUs | The [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) enables GPU monitoring for Compute Engine and for [other products that Ops Agent supports](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent#supported_vms). You can also use the [NVIDIA Data Center GPU Manager (DCGM)](https://docs.cloud.google.com/monitoring/agent/ops-agent/third-party-nvidia), which is a suite of tools for managing and monitoring NVIDIA GPUs in cluster environments. Monitoring NVIDIA GPUs is particularly useful for training and serving deep learning models. |
| Deep debugging | To debug problems with the training code or the configuration of a Vertex AI Training job, you can inspect the training container by using an [interactive shell session](https://docs.cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell). |

#### Monitoring during serving: Streaming prediction

After you train a model and export it to
[Vertex AI Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction),
you can create a
[Vertex AI endpoint](https://docs.cloud.google.com/vertex-ai/docs/general/deployment). This endpoint provides an HTTP endpoint for the model.

[Model Monitoring](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview)
helps you identify large changes in the distribution of input or output
features. You can also monitor
[feature attributions](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview#feature-based)
in production when compared to a baseline distribution. The baseline
distribution can be the training set or it can be based on past distributions of
production traffic. A change in the serving distribution might imply a reduction
in predictive performance compared to training.

- **Choose a monitoring objective** : Depending on the sensitivity of a use case to changes in the data that's provided to the model, you can [monitor different types of objectives](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview#v2-objectives): input feature drift, output drift, and feature attribution. [Model Monitoring v2](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/overview#v2) lets you monitor models that you deploy on a managed serving platform like Vertex AI and also on self-hosted services like Google Kubernetes Engine (GKE). In addition, for granular performance tracking, you can monitor parameters at the model level rather than for an endpoint.
- **Monitor generative AI model serving** : To ensure stability and minimize latency, particularly for LLM endpoints, set up a robust monitoring stack. [Gemini](https://docs.cloud.google.com/gemini/docs/overview) models provide [built-in metrics](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/use-provisioned-throughput#metrics), like time to first token (TTFT), which you can access directly in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). To monitor throughput, latency, and error rates across all Google Cloud models, use the [model observability dashboard](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-observability#view).

#### Monitoring during serving: Batch prediction

To monitor batch prediction, you can run standard evaluation jobs in the
[Vertex AI evaluation service](https://docs.cloud.google.com/vertex-ai/docs/evaluation/introduction).
Model Monitoring supports monitoring of
[batch inferences](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/model-monitoring-batch-predictions).
If you use Batch to run your serving workload, you can monitor resource
consumption by using the
[metrics in Metrics Explorer](https://docs.cloud.google.com/batch/docs/monitor-job-resources-using-metrics).

### Automate evaluation for reproducibility and standardization

To transition models from prototypes to reliable production systems, you need a
standardized evaluation process. This process helps you track progress across
iterations, compare different models, detect and mitigate bias, and ensure that
you meet regulatory requirements. To ensure reproducibility and scalability, you
must automate the evaluation process.

To standardize and automate the evaluation process for ML performance, complete
the following steps:

1. Define quantitative and qualitative indicators.
2. Choose appropriate data sources and techniques.
3. Standardize the evaluation pipeline.

These steps are described in the following sections.

#### 1. Define quantitative and qualitative indicators

*Computation-based metrics* are calculated by using numeric formulas.
Remember that
[training loss](https://developers.google.com/machine-learning/glossary#training-loss)
metrics might differ from the evaluation metrics that are relevant to business
goals. For example, a model that's used for supervised fraud detection might use
[cross-entropy loss](https://developers.google.com/machine-learning/glossary#cross-entropy)
for training. However, to evaluate inference performance, a more relevant metric
might be
[recall](https://developers.google.com/machine-learning/glossary#recall),
which indicates the coverage of fraudulent transactions.
Vertex AI provides an evaluation service for metrics like recall,
precision, and area under the precision-recall curve (AuPRC). For more
information, see
[Model evaluation in Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/evaluation/introduction).

*Qualitative indicators* , such as the fluency or entertainment value of
generated content, can't be objectively computed. To evaluate these indicators,
you can use the
[LLM-as-a-judge](https://en.wikipedia.org/wiki/LLM-as-a-Judge) strategy or human labeling services like
[Labelbox](https://docs.cloud.google.com/architecture/partners/model-development-data-labeling-labelbox-google-cloud).

#### 2. Choose appropriate data sources and techniques

An evaluation is statistically significant when it runs on a certain minimum
volume of varied examples. Choose the datasets and techniques that you use for
evaluations by using approaches such as the following:

- **Golden dataset**: Use trusted, consistent, and accurate data samples that reflect the probability distribution of a model in production.
- **LLM-as-a-judge**: Evaluate the output of a generative model by using an LLM. This approach is relevant only to tasks where an LLM can evaluate a model.
- **User feedback**: To guide future improvements, capture direct user feedback as a part of production traffic.

Depending on the evaluation technique, size and type of evaluation data, and
frequency of evaluation, you can use BigQuery or Cloud Storage as data
sources, including for the Vertex AI evaluation service.

- BigQuery lets you use SQL commands to run inference tasks like natural language processing and machine translation. For more information, see [Task-specific solutions overview](https://docs.cloud.google.com/bigquery/docs/ai-application-overview).
- Cloud Storage provides a [cost-efficient storage solution](https://docs.cloud.google.com/architecture/storage-advisor#object-storage) for large datasets.

#### 3. Standardize the evaluation pipeline

To automate the evaluation process, consider the following services and
tools:

- [**Vertex AI evaluation service**](https://docs.cloud.google.com/vertex-ai/docs/evaluation/using-model-evaluation): Provides ready-to-use primitives to track model performance as a part of the ML lifecycle on Vertex AI.
- [**Gen AI evaluation service**](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/evaluation-overview): Lets you evaluate any generative model or application and benchmark the evaluation results against your own judgment and evaluation criteria. This service also helps you perform specialized tasks like prompt engineering, retrieval-augmented generation (RAG), and AI agent optimization.
- [**Vertex AI automatic side-by-side (AutoSxS) tool**](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/side-by-side-eval): Supports pairwise model-based evaluation.
- [**Kubeflow**](https://docs.cloud.google.com/vertex-ai/docs/pipelines/gcpc-list#modeleval_components): Provides special components to run model evaluations.

## Run and track frequent experiments

To effectively optimize ML performance, you need a dedicated, powerful, and
interactive platform for experimentation. The platform must have the following
capabilities:

- Facilitate iterative development, so that teams can move from idea to validated results with speed, reliability, and scale.
- Let teams efficiently discover optimal configurations that they can use to trigger training jobs.
- Provide controlled access to relevant data, features, and tools to perform and track experiments.
- Support reproducibility and data lineage tracking.

### Treat data as a service

Isolate experimental workloads from production systems and set up appropriate
security controls for your data assets by using the following techniques:

| Technique | Description | Benefits |
|---|---|---|
| Resource isolation | [Isolate the resources for different environments](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy#option1) in separate Google Cloud projects. For example, provision the resources for development, staging, and production environments in separate projects like `ml-dev`, `ml-staging`, and `ml-prod`. | Resource isolation helps to prevent experimental workloads from consuming resources that production systems need. For example, if you use a single project for experiments *and* production, an experiment might consume all of the available NVIDIA A100 GPUs for Vertex AI Training. This might cause interruptions in the retraining of a critical production model. |
| Identity and access control | Apply the principles of [zero trust and least privilege](https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust) and use workload-specific service accounts. Grant access by using predefined Identity and Access Management (IAM) roles like [Vertex AI User](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`). | This approach helps to prevent accidental or malicious actions that might corrupt experiments. |
| Network security | Isolate network traffic by using [Virtual Private Cloud (VPC) networks](https://docs.cloud.google.com/vpc/docs/vpc) and enforce security perimeters by using [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview). | This approach helps to protect sensitive data and prevents experimental traffic from affecting production services. |
| Data isolation | Store experimental data in separate Cloud Storage buckets and BigQuery datasets. | Data isolation prevents accidental modification of production data. For example, without data isolation, an experiment might inadvertently alter the feature values in a shared BigQuery table, which might lead to a significant degradation in model accuracy in the production environment. |

### Equip teams with appropriate tools

To establish a curated set of tools to accelerate the entire experimentation
lifecycle---from data exploration to model training and analysis---use the
following techniques:

- **Interactive prototyping** : For rapid data exploration, hypothesis testing, and code prototyping, use Colab Enterprise or managed JupyterLab instances on Vertex AI Workbench. For more information, see [Choose a notebook solution](https://docs.cloud.google.com/vertex-ai/docs/workbench/notebook-solution).
- **Scalable model training** : Run training jobs on a managed service that supports distributed training and scalable compute resources like GPUs and TPUs. This approach helps to reduce training time from days to hours and enables more parallel experimentation. For more information, see [Use specialized components for training](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#specialized-components-training).
- **In-database ML** : Train models directly in [BigQuery ML using SQL](https://docs.cloud.google.com/bigquery/docs/bqml-introduction). This technique helps to eliminate data movement and accelerates experimentation for analysts and SQL-centric users.
- **Tracking experiments** : Create a searchable and comparable history of experiment data by logging parameters, metrics, and artifacts for every experiment run. For more information, see [Build a data and model lineage system](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#data-model-lineage).
- **Optimizing generative AI** : To optimize the performance of generative AI applications, you must experiment with prompts, model selection, and fine-tuning. For rapid prompt engineering, use [Vertex AI Studio](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/start/quickstarts/quickstart). To experiment with foundation models (like Gemini) and find a model that's appropriate for your use case and business goals, use [Model Garden](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models).

### Standardize for reproducibility and efficiency

To ensure that experiments consume resources efficiently and produce consistent
and trustworthy results, standardize and automate experiments by using the
following approaches:

- **Ensure consistent environments by using containers** : Package your training code and dependencies as Docker containers. Manage and serve the containers by using [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker). This approach lets you reproduce issues on different machines by repeating experiments in identical environments. Vertex AI provides [prebuilt containers](https://docs.cloud.google.com/vertex-ai/docs/training/pre-built-containers) for serverless training.
- **Automate ML workflows as pipelines** : Orchestrate the end-to-end ML workflow as a codified pipeline by using [Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction). This approach helps to enforce consistency, ensure reproducibility, and automatically track all of the artifacts and metadata in [Vertex ML Metadata](https://docs.cloud.google.com/vertex-ai/docs/ml-metadata/introduction).
- **Automate provisioning with infrastructure-as-code (IaC)** : Define and deploy standardized experimentation environments by using IaC tools like [Terraform](https://docs.cloud.google.com/docs/terraform/terraform-overview). To ensure that every project adheres to a standardized set of configurations for security, networking, and governance, use [Terraform modules](https://developer.hashicorp.com/terraform/language/modules).

## Build and automate training and serving infrastructure

To train and serve AI models, set up a robust platform that supports efficient
and reliable development, deployment, and serving. This platform lets your teams
efficiently improve the quality and performance of training and serving in the
long run.

### Use specialized components for training

A reliable training platform helps to accelerate performance and provides a
standardized approach to automate repeatable tasks in the ML lifecycle--from data
preparation to model validation.

- **Data collection and preparation**: For effective model training, you
  need to collect and prepare the data that's necessary for training,
  testing, and validation. The data might come from different sources and be
  of different data types. You also need to reuse relevant data across
  training runs and share features across teams. To improve the repeatability
  of the data collection and preparation phase, consider the following
  recommendations:

  - Improve data discoverability with [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/catalog-overview).
  - Centralize feature engineering in [Vertex AI Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore).
  - Preprocess data by using [Dataflow](https://docs.cloud.google.com/dataflow/docs).
- **Training execution**: When you train a model, you use data to create a
  model object. To do this, you need to set up the necessary infrastructure
  and dependencies of the training code. You also need to decide how to
  persist the training models, track training progress, evaluate the model,
  and present the results. To improve training repeatability, consider the
  following recommendations:

  - Follow the guidelines in [Automate evaluation for reproducibility and standardization](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#automate-evaluation).
  - To submit training jobs on one or more worker nodes without managing the underlying infrastructure provisioning or dependencies, use the [`CustomJob`](https://docs.cloud.google.com/vertex-ai/docs/training/create-custom-job#before) resource in Vertex AI Training. You can also use the `CustomJob` resource for [hyperparameter tuning](https://docs.cloud.google.com/vertex-ai/docs/training/using-hyperparameter-tuning) jobs.
  - [Optimize scheduling goodput](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#optimize-scheduling-goodput) by leveraging [Dynamic Workload Scheduler](https://docs.cloud.google.com/vertex-ai/docs/training/schedule-jobs-dws#enable-dws) or [reservations](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) for Vertex AI Training.
  - Register your models to [Vertex AI Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction).
- **Training orchestration** : Deploy training workloads as stages of a
  pipeline by using
  [Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction). This service provides managed
  [Kubeflow](https://www.kubeflow.org/)
  and
  [TFX](https://www.tensorflow.org/tfx)
  services. Define each step of the pipeline as a
  [component](https://www.kubeflow.org/docs/components/)
  that runs in a container. Each component works like a function, with input
  parameters and output artifacts that become inputs to the subsequent
  components in the pipeline. To optimize the efficiency of your pipeline,
  consider the recommendations in the following table:

  | Goal | Recommendations |
  |---|---|
  | Implement core automation. | - Use [Kubeflow Pipelines components](https://docs.cloud.google.com/vertex-ai/docs/pipelines/gcpc-list). - Use [Control Flows](https://www.kubeflow.org/docs/components/pipelines/user-guides/core-functions/control-flow/) for advanced pipeline designs, such as conditional gates. - Integrate the [pipeline compilation](https://docs.cloud.google.com/vertex-ai/docs/pipelines/build-pipeline#compile_your_pipeline_into_a_yaml_file) as a part of your CI/CD flow. - Execute the pipeline with [Cloud Scheduler](https://docs.cloud.google.com/vertex-ai/docs/pipelines/schedule-pipeline-run). |
  | Increase speed and cost efficiency. | - To increase the speed of iterations and reduce cost, use the [execution cache](https://docs.cloud.google.com/vertex-ai/docs/pipelines/configure-caching) of Vertex AI Pipelines. - [Specify the machine configuration](https://docs.cloud.google.com/vertex-ai/docs/pipelines/machine-types) for each component based on the resource requirements of each step. |
  | Increase robustness. | - To increase robustness against temporary issues without requiring manual intervention, configure [retries](https://docs.cloud.google.com/vertex-ai/docs/pipelines/configure-retries). - To [*fail fast*](https://en.wikipedia.org/wiki/Fail-fast_system) and iterate efficiently, configure a [failure policy](https://docs.cloud.google.com/vertex-ai/docs/pipelines/configure-failure-policy). - To handle failures, [configure email notifications](https://docs.cloud.google.com/vertex-ai/docs/pipelines/email-notifications). |
  | Implement governance and tracking. | - To experiment with different model configurations or training configurations, [add pipeline runs to experiments](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction#experiments). - Monitor [logs](https://docs.cloud.google.com/vertex-ai/docs/pipelines/logging) and [metrics](https://docs.cloud.google.com/vertex-ai/docs/pipelines/metrics) for Vertex AI Pipelines. - Follow the recommendations in [Monitor performance at all stages of the model lifecycle](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#monitor-model-perf). |

### Use specialized infrastructure for prediction

To reduce the toil of managing infrastructure and model deployments, automate
the repeatable task flows. A service-oriented approach lets you focus on speed
and faster
[time to value (TTV)](https://en.wikipedia.org/wiki/Time_to_value). Consider the
following recommendations:

| Recommendation | Techniques |
|---|---|
| Implement automatic deployment. | - After a model is trained, use automation to deploy the model. Vertex AI Pipelines provides [specialized components](https://docs.cloud.google.com/vertex-ai/docs/pipelines/gcpc-list#endpoint_components) for deploying models to Vertex AI endpoints. You can manage automatic deployment by using [Kubeflow Control Flows](https://www.kubeflow.org/docs/components/pipelines/user-guides/core-functions/control-flow/). - To decide whether to deploy a model based on an evaluation against a validation set, take advantage of the [evaluation components](https://docs.cloud.google.com/vertex-ai/docs/pipelines/model-evaluation-component) of the pipeline. You can automate deployment for batch inference by using specialized [batch prediction components](https://docs.cloud.google.com/vertex-ai/docs/pipelines/batchprediction-component) in Vertex AI. |
| Take advantage of managed scaling features. | - [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-predictions) provides batch and online inference capabilities that let you configure the [scaling behavior](https://docs.cloud.google.com/vertex-ai/docs/general/deployment#scaling). - Cloud Run supports [autoscaling GPUs](https://docs.cloud.google.com/run/docs/configuring/services/gpu-best-practices#autoscaling-and-gpu). |
| Optimize latency and throughput on Vertex AI endpoints. | - Choose an appropriate [machine type](https://docs.cloud.google.com/vertex-ai/docs/predictions/configure-compute). - Choose an appropriate [endpoint type](https://docs.cloud.google.com/vertex-ai/docs/predictions/choose-endpoint-type) for your models. [Dedicated private endpoints](https://docs.cloud.google.com/vertex-ai/docs/predictions/private-service-connect) might help to reduce latency. - If you use Vertex AI Feature Store, choose an appropriate online serving type. Optimized online serving with Private Service Connect might provide low latency. For more information, see [Online service types](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/online-serving-types). |
| Optimize resource utilization. | - To optimize resource utilization, you can [share resources across model deployments](https://docs.cloud.google.com/vertex-ai/docs/predictions/model-co-hosting). Instead of using a separate VM for each model (default behavior), you can deploy several models on a single VM. - To assure or optimize resource availability, use [reservations](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations), [Dynamic Workload Scheduler](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-flex-start-vms), or [Spot VMs](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-spot-vms). |
| Optimize model deployment. | - To avoid breaking changes, you can perform gradual migration and implement A/B testing by automatically [deploying several models to the same endpoint](https://docs.cloud.google.com/vertex-ai/docs/general/deployment#models-endpoint). Vertex AI decouples the endpoint layer from the models, which lets you split traffic between model versions. - To replace a deployed model, use a [rolling deployment strategy](https://docs.cloud.google.com/vertex-ai/docs/predictions/rolling-deployment). |
| Monitor performance. | - To improve serving performance in production, observe [logs](https://docs.cloud.google.com/vertex-ai/docs/predictions/online-prediction-logging) and [inference metrics](https://docs.cloud.google.com/vertex-ai/docs/predictions/view-endpoint-metrics) for Vertex AI endpoints. To understand the behavior of models in production, you need tools to monitor quality and performance. [Model Monitoring v2](https://docs.cloud.google.com/vertex-ai/docs/model-monitoring/set-up-model-monitoring) lets you monitor several versions of a model and iterate rapidly. |

## Match design choices to performance requirements

When you make design choices to improve performance, assess whether the choices
support your business requirements or are wasteful and counterproductive. To
choose appropriate infrastructure, models, and configurations, identify
performance bottlenecks and assess how they're linked to performance metrics.
For example, even on very powerful GPU accelerators, training tasks can
experience performance bottlenecks. These bottlenecks can be caused by data I/O
issues in the storage layer or by performance limitations of the model.

### Focus on holistic performance of the ML flow

As training requirements grow in terms of model size and cluster size, the
failure rate and infrastructure costs might increase. Therefore, the cost of
failure might increase quadratically. You can't rely solely on conventional
resource-efficiency metrics like
[model FLOPs utilization (MFU)](https://arxiv.org/pdf/2204.02311#page=66.09).
To understand why MFU might not be a sufficient indicator of overall training
performance, examine the lifecycle of a typical training job. The lifecycle
consists of the following cyclical flow:

1. **Cluster creation**: Worker nodes are provisioned.
2. **Initialization**: Training is initialized on the worker nodes.
3. **Training execution**: Resources are used for forward or backward propagation.
4. **Interruption**: The training process is interrupted during model checkpointing or due to worker-node preemptions.

After each interruption, the preceding flow is repeated.

The training execution step constitutes a fraction of the lifecycle of an ML
job. Therefore, the utilization of worker nodes for the training execution step
doesn't indicate the overall efficiency of the job. For example, even if the
training execution step runs at 100% efficiency, the overall efficiency might
be low if interruptions occur frequently or if it takes a long time to resume
training after interruptions.

#### Adopt and track goodput metrics

To ensure holistic performance measurement and optimization, shift your focus
from conventional resource-efficiency metrics like MFU to
[*goodput*](https://cloud.google.com/blog/products/ai-machine-learning/goodput-metric-as-measure-of-ml-productivity).
Goodput considers the availability and utilization of your clusters and compute
resources and it helps to measure resource efficiency across multiple layers.

The focus of goodput metrics is the *overall progress* of a job rather than
whether the job *appears to be busy*. Goodput metrics help you optimize
training jobs for tangible overall gains in productivity and performance.

Goodput gives you a granular understanding of potential losses in efficiency
through the following metrics:

- *Scheduling goodput* is the fraction of time when all of the resources that are required for training or serving are available for use.
- *Runtime goodput* represents the proportion of useful training steps that are completed during a given period.
- *Program goodput* is the peak hardware performance or MFU that a training job can extract from the accelerator. It depends on efficient utilization of the underlying compute resources during training.

#### Optimize scheduling goodput

To optimize scheduling goodput for a workload, you must identify the specific
infrastructure requirements of the workload. For example, batch inference,
streaming inference, and training have different requirements:

- Batch inference workloads might accommodate some interruptions and delays in resource availability.
- Streaming inference workloads require stateless infrastructure.
- Training workloads require longer term infrastructure commitments.

##### Choose appropriate obtainability modes

In cloud computing, *obtainability* is the ability to provision resources when
they're required. Google Cloud provides the following obtainability modes:

- **On-demand VMs**: You provision Compute Engine VMs when they're needed and run your workloads on the VMs. The provisioning request is subject to the availability of resources, such as GPUs. If a sufficient quantity of a requested resource type isn't available, the request fails.
- [**Spot VMs**](https://docs.cloud.google.com/compute/docs/instances/spot): You create VMs by using unused compute capacity. Spot VMs are billed at a discounted price when compared to on-demand VMs, but Google Cloud might [*preempt*](https://docs.cloud.google.com/compute/docs/instances/spot#preemption) Spot VMs at any time. We recommend that you use Spot VMs for stateless workloads that can fail gracefully when the host VMs are preempted.
- [**Reservations**](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type): You reserve capacity as a pool of VMs. Reservations are ideal for workloads that need capacity assurance. Use reservations to maximize scheduling goodput by ensuring that resources are available when required.
- [**Dynamic Workload Scheduler**](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler):
  This provisioning mechanism queues requests for GPU-powered VMs in a
  dedicated pool. Dynamic Workload Scheduler helps you avoid the constraints of the
  other obtainability modes:

  - Stock-out situations in the on-demand mode.
  - Statelessness constraint and preemption risk of Spot VMs.
  - Cost and availability implications of reservations.

The following table summarizes the obtainability modes for Google Cloud
services and provides links to relevant documentation:

| Product | On-demand VMs | Spot VMs | Reservations | Dynamic Workload Scheduler |
|---|---|---|---|---|
| Compute Engine | [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) | [About Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) | [About reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) | [Create a MIG with GPU VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-gpu-vms) |
| GKE | [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools) | [About Spot VMs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#overview) | [Consuming reserved zonal resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations) | [GPU, TPU, and H4D consumption with flex-start provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) |
| Cloud Batch | [Create and run a job](https://docs.cloud.google.com/batch/docs/create-run-example-job) | [Batch job with Spot VMs](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#provisioningmodel) | [Ensure resource availability using VM reservations](https://docs.cloud.google.com/batch/docs/create-run-job-reservation) | [Use GPUs and flex-start VMs](https://docs.cloud.google.com/batch/docs/create-run-job-gpus#use-gpu-vms-dws) |
| Vertex AI Training | [Create a serverless training job](https://docs.cloud.google.com/vertex-ai/docs/training/create-custom-job) | [Use Spot VMs for training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-spot-vms) | [Use reservations for training jobs](https://docs.cloud.google.com/vertex-ai/docs/training/use-reservations) | [Schedule training jobs based on resource availability](https://docs.cloud.google.com/vertex-ai/docs/training/schedule-jobs-dws) |
| Vertex AI | Get [batch inferences](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-batch-predictions) and [online inferences](https://docs.cloud.google.com/vertex-ai/docs/predictions/get-online-predictions) from custom-trained models. | [Use Spot VMs for inference](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-spot-vms) | [Use reservations for online inference](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-reservations) | [Use flex-start VMs for inference](https://docs.cloud.google.com/vertex-ai/docs/predictions/use-flex-start-vms) |

##### Plan for maintenance events

You can improve scheduling goodput by anticipating and planning for
infrastructure maintenance and upgrades.

- GKE lets you control when automatic cluster maintenance can
  be performed on your clusters. For more information, see
  [Maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).

- Compute Engine provides the following capabilities:

  - To keep an instance running during a host event, such as planned maintenance for the underlying hardware, Compute Engine performs a *live migration* of the instance to another host in the same zone. For more information, see [Live migration process during maintenance events](https://docs.cloud.google.com/compute/docs/instances/live-migration-process).
  - To control how an instance responds when the underlying host requires maintenance or has an error, you can [set a host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options) for the instance.
- For information about planning for host events that are related to large
  training clusters in AI Hypercomputer, see
  [Manage host events across compute instances](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/host-events).

#### Optimize runtime goodput

The model training process is frequently interrupted by events like model
checkpointing and resource preemption. To optimize runtime goodput, you must
ensure that the system resumes training and inference efficiently after the
required infrastructure is ready and after any interruption.

During model training, AI researchers use checkpointing to track progress and
minimize the learning lost due to resource preemptions. Larger model sizes make
checkpointing interruptions longer, which further affects overall efficiency.
After interruptions, the training application must be restarted on every node in
the cluster. These restarts can take some time because the necessary artifacts
must be reloaded.

To optimize runtime goodput, use the following techniques:

| Technique | Description |
|---|---|
| Implement automatic checkpointing. | Frequent checkpointing lets you track the progress of training at a granular level. However, the training process is interrupted for each checkpoint, which reduces runtime goodput. To minimize interruptions, you can set up automatic checkpointing, where the host's [SIGTERM](https://en.wikipedia.org/wiki/Signal_(IPC)#SIGTERM) signal triggers the creation of a checkpoint. This approach limits checkpointing interruptions to when the host needs maintenance. Remember that some hardware failures might not trigger SIGTERM signals; therefore, you must find a suitable balance between automatic checkpointing and SIGTERM events. You can set up automatic checkpointing by using the following techniques: - Preserve training progress on TPUs by using [autocheckpoint](https://docs.cloud.google.com/tpu/docs/autocheckpoint). - Use the built-in automatic checkpointing in the [MaxText](https://github.com/AI-Hypercomputer/maxtext) framework. - Configure host maintenance notifications for [GPUs](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance) and [TPUs](https://docs.cloud.google.com/tpu/docs/view-maintenance-notifications). - Use [Orbax](https://github.com/google/orbax/blob/main/README.md) for ML using JAX. - Implement [multi-tier checkpointing in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/training/multi-tier-checkpointing). |
| Use appropriate container-loading strategies. | In a GKE cluster, before nodes can resume training jobs, it might take some time to complete loading the required artifacts like data or model checkpoints. To reduce the time that's required to reload data and resume training, use the following techniques: - Preload data or container images by using [secondary boot disks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/data-container-image-preloading). - Pull container images by using [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming). - Use [larger persistent disks](https://docs.cloud.google.com/compute/docs/disks/performance#performance_limits) or provision ephemeral storage by using [Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#local-ssd-perf-nvme). - Build and decompress images by using [Zstandard](https://github.com/facebook/zstd/blob/dev/README.md). - Preload container images by using [DaemonSets](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/automatically-bootstrapping-gke-nodes-with-daemonsets). For more information about how to reduce the data reload time, see [Tips and tricks to reduce cold-start latency on GKE](https://cloud.google.com/blog/products/containers-kubernetes/tips-and-tricks-to-reduce-cold-start-latency-on-gke). |
| Use the compilation cache. | If training requires a compilation-based stack, check whether you can use a compilation cache. When you use a compilation cache, the computation graph isn't recompiled after each training interruption. The resulting reductions in time and cost are particularly beneficial when you use TPUs. [JAX](https://docs.jax.dev/en/latest/persistent_compilation_cache.html#google-cloud) lets you store the compilation cache in a Cloud Storage bucket and then use the cached data in the case of interruptions. |

#### Optimize program goodput

Program goodput represents peak resource utilization during training, which is
the conventional way to measure training and serving efficiency. To improve
program goodput, you need an optimized distribution strategy, efficient
compute-communication overlap, optimized memory access, and efficient
pipelines.

To optimize program goodput, use the following strategies:

| Strategy | Description |
|---|---|
| Use framework-level customization options. | Frameworks or compilers like [Accelerated Linear Algebra (XLA)](https://openxla.org/xla) provide many key components of program goodput. To further optimize performance, you can customize fundamental components of the computation graph. For example, [Pallas](https://docs.jax.dev/en/latest/pallas/tpu/) supports custom kernels for TPUs and GPUs. |
| Offload memory to the host DRAM. | For large-scale training, which requires significantly high memory from accelerators, you can offload some memory usage to the host DRAM. For example, XLA lets you [offload model activations](https://github.com/pytorch/xla/tree/master/examples/host_offloading) from the forward pass to the host memory instead of using the accelerator's memory. With this strategy, you can improve training performance by increasing the model capacity or the batch size. |
| Leverage [quantization](https://en.wikipedia.org/wiki/Large_language_model#Quantization) during training. | You can improve training efficiency and program goodput by leveraging model quantization during training. This strategy reduces the precision of the gradients or weights during certain steps of the training; therefore, program goodput improves. However, this strategy might require additional engineering effort during model development. For more information, see the following resources: - [Quantization-aware training on TensorFlow](https://www.tensorflow.org/model_optimization/guide/quantization/training_comprehensive_guide) - [Quantization-aware training on PyTorch](https://pytorch.org/blog/quantization-aware-training/) - [Qwix: a quantization library for JAX](https://github.com/google/qwix/blob/main/README.md) |
| Implement parallelism. | To increase the utilization of the available compute resources, you can use parallelism strategies at the model level during training and when loading data. For information about model parallelism, see the following: - [Pipeline parallelism on PyTorch](https://docs.pytorch.org/docs/stable/distributed.pipelining.html) - [Pipeline parallelism on GPUs with JAX](https://docs.jax.dev/en/latest/gpu_performance_tips.html#pipeline-parallelism-on-gpu) - [Pipeline parallelism in DeepSpeed](https://www.deepspeed.ai/tutorials/pipeline/) To achieve data parallelism, you can use tools like the following: - [FSDP](https://docs.pytorch.org/tutorials/intermediate/FSDP_tutorial.html) on PyTorch - Distributed training on [TensorFlow](https://www.tensorflow.org/guide/distributed_training) or [Keras](https://keras.io/guides/distribution/) - [Distributed data loading](https://docs.jax.dev/en/latest/distributed_data_loading.html) with JAX |

### Focus on workload-specific requirements

To ensure that your performance optimization efforts are effective and holistic,
you must match optimization decisions to the specific requirements of your
training and inference workloads. Choose appropriate AI models and use relevant
prompt optimization strategies. Select appropriate frameworks and tools based on
the requirements of your workloads.

#### Identify workload-specific requirements

Evaluate the requirements and constraints of your workloads across the following
areas:

| Area | Description |
|---|---|
| Task and quality requirements | Define the core task of the workload and the performance baseline. Answer questions like the following: - Does the task involve regression, classification, or generation? - What is the minimum acceptable quality: for example, accuracy, precision, or recall? |
| Serving context | Analyze the operational environment where you plan to deploy the model. The serving context often has a significant impact on design decisions. Consider the following factors: - **Latency**: Does the system need real-time, synchronous predictions, or is an asynchronous, batch process acceptable? - **Connectivity**: Do you need to run the model offline or on an edge device? - **Volume**: What are the expected average and peak levels for prediction load? The load levels influence your decisions regarding scaling strategies and infrastructure. |
| Team skills and economics | Assess the business value of buying the solution against the cost and complexity of building and maintaining it. Determine whether your team has the specialized skills that are required for custom model development or whether a managed service might provide faster time to value. |

#### Choose an appropriate model

If an API or an open model can deliver the required performance and quality, use
that API or model.

- For modality-specific tasks like optical character recognition (OCR),
  labeling, and content moderation, choose ML APIs like the following:

  - [Cloud Natural Language API](https://docs.cloud.google.com/natural-language/docs/reference/rest)
  - [Cloud Vision API](https://docs.cloud.google.com/vision/docs/detect-labels-image-api)
  - [Video Intelligence API](https://docs.cloud.google.com/video-intelligence/docs/features)
  - [Speech-to-Text API](https://docs.cloud.google.com/speech-to-text/docs/overview)
  - [Text-to-Speech API](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts)
  - [Cloud Translation API](https://docs.cloud.google.com/translate/docs/overview)
- For generative AI applications, consider Google models like
  [Gemini](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#gemini-models),
  [Imagen](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#imagen-models),
  and
  [Veo](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models#veo-models).

  Explore
  [Model Garden](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-garden/explore-models)
  and choose from a curated collection of foundation and task-specific Google
  models. Model Garden also provides open models like
  Gemma and third-party models, which you can run in
  Vertex AI or deploy on runtimes like GKE.
- If a task can be completed by using either an ML API or a generative AI
  model, consider the complexity of the task. For complex tasks, large models
  like Gemini might provide higher performance than smaller
  models.

#### Improve quality through better prompting

To improve the quality of your prompts at scale, use the
[Vertex AI prompt optimizer](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-optimizer).
You don't need to manually rewrite system instructions and prompts. The prompt
optimizer supports the following approaches:

- **Zero-shot optimization**: A low-latency approach that improves a single prompt or system instruction in real time.
- **Data-driven optimization**: An advanced approach that improves prompts by evaluating a model's responses to sample prompts against specific evaluation metrics.

For more prompt-optimization guidelines, see
[Overview of prompting strategies](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies).

#### Improve performance for ML and generative AI endpoints

To improve the latency or throughput (tokens per second) for ML and generative
AI endpoints, consider the following recommendations:

- Cache results by using [Memorystore](https://docs.cloud.google.com/memorystore/docs).
- For generative AI APIs, use the following techniques:
  - [Context caching](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/context-cache/context-cache-overview): Achieve lower latency for requests that contain repeated content.
  - [Provisioned Throughput](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput): Improve the throughput for Gemini endpoints by reserving throughput capacity.
- For self-hosted models, consider the following optimized inference frameworks:

  | Framework | Notebooks and guides |
  |---|---|
  | Optimized [vLLM](https://github.com/vllm-project/vllm/blob/main/README.md) containers in Model Garden | [Deploy open models with pre-built containers](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/open-models/use-prebuilt-containers) |
  | GPU-based inference on GKE | - [Serve an LLM with Ray](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/serve-llm-l4-ray) - [Serve Gemma open models with Hugging Face TGI](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-tgi) - [Serve Gemma open models with vLLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-vllm) - [Serve Gemma open models with TensorRT-LLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-gemma-gpu-tensortllm) - [Serve scalable LLMs with TorchServe](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/scalable-ml-models-torchserve) |
  | TPU-based inference | - [Serve open models using TPUs on GKE with Optimum TPU](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/optimum-tpu) - [Serve open models using vLLM TPU on Cloud TPU](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/open-models/vllm/use-vllm-tpu) |

#### Use low-code solutions and tuning

If pre-trained models don't meet your requirements, you can improve their
performance for specific domains by using the solutions:

- [AutoML](https://docs.cloud.google.com/vertex-ai/docs/beginner/beginners-guide) is a low-code solution to improve inference results with minimal technical effort for a wide range of tasks. AutoML lets you create models that are optimized on several dimensions: architecture, performance, and training stage (through checkpointing).
- [Tuning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models) helps you achieve higher quality, more stable generation and lower latency with shorter prompts and without a lot of data. We recommend that you start tuning by using the [default values for hyperparameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-use-supervised-tuning#tuning_hyperparameters). For more information, see [Supervised Fine Tuning for Gemini: A best practices guide](https://cloud.google.com/blog/products/ai-machine-learning/master-gemini-sft).

#### Optimize self-managed training

In some cases, you might decide to retrain a model or fully manage a fine-tuning
job. This approach requires advanced skills and additional time depending on the
model, framework, and resources that you use.

Take advantage of performance-optimized framework options, such as the
following:

- Use deep learning
  [images](https://docs.cloud.google.com/deep-learning-vm/docs/introduction)
  or
  [containers](https://docs.cloud.google.com/deep-learning-containers/docs/getting-started-local),
  which include the latest software dependencies and
  Google Cloud-specific libraries.

- Run model training with Ray on Google Cloud:

  - [Ray on Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/open-source/ray-on-vertex-ai/overview) lets you bring Ray's distributed training framework to Compute Engine or GKE and it simplifies the overhead of managing the framework.
  - You can self-manage Ray on GKE with KubeRay by deploying the [Ray operator](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/ray-on-gke/how-to/enable-ray-on-gke) on an existing cluster.
- Deploy training workloads on a compute cluster that you provision by
  using the open-source
  [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview).
  To efficiently provision performance-optimized clusters, use YAML-based
  [blueprints](https://docs.cloud.google.com/cluster-toolkit/docs/setup/cluster-blueprint-catalog). Manage the clusters
  by using schedulers like
  [Slurm](https://slurm.schedmd.com/overview.html)
  and GKE.

- Train standard model architectures by using
  [GPU-optimized recipes](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/README.md).

Build training architectures and strategies that optimize performance by using
the following techniques:

- Implement [distributed training](https://docs.cloud.google.com/vertex-ai/docs/training/distributed-training) on Vertex AI or on the frameworks described earlier. Distributed training enables model parallelism and data parallelism, which can help to increase the training dataset size and model size, and help to reduce training time.
- For efficient model training and to explore different performance configurations, run checkpointing at appropriate intervals. For more information, see [Optimize runtime goodput](https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable#optimize-runtime-goodput).

#### Optimize self-managed serving

For self-managed serving, you need efficient inference operations and a high
throughput (number of inferences per unit of time).

To optimize your model for inference, consider the following approaches:

- [Quantization](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/llm-optimization#quantization):
  Reduce the model size by representing its parameters in a lower precision
  format. This approach helps to reduce memory consumption and latency.
  However, quantization *after* training might change model quality. For
  example, quantization after training might cause a reduction in accuracy.

  - Post-training quantization (PTQ) is a repeatable task. Major ML frameworks like [PyTorch](https://pytorch.org/docs/stable/quantization.html) and [TensorFlow](https://www.tensorflow.org/model_optimization/guide/quantization/post_training) support PTQ.
  - You can orchestrate PTQ by using a pipeline on [Vertex AI Pipelines](https://docs.cloud.google.com/vertex-ai/docs/pipelines/introduction).
  - To stabilize model performance and benefit from reductions in model size, you can use [Qwix](https://github.com/google/qwix/blob/main/README.md).
- [Tensor parallelism](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/llm-optimization#tensor-parallelism):
  Improve inference throughput by distributing computational load across
  multiple GPUs.

- [Memory optimization](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/llm-optimization#model-memory):
  Increase throughput and optimize attention caching, batch sizes, and input
  sizes.

Use inference-optimized frameworks, such as the following:

- For generative models, use an open framework like [MaxText](https://github.com/AI-Hypercomputer/maxtext/blob/main/README.md), [MaxDiffusion](https://github.com/AI-Hypercomputer/maxdiffusion/blob/main/README.md#overview), or [vLLM](https://github.com/vllm-project/vllm/blob/main/README.md).
- Run [prebuilt container images](https://docs.cloud.google.com/vertex-ai/docs/predictions/pre-built-containers) on Vertex AI for predictions and explanations. If you choose TensorFlow, then use the [optimized TensorFlow runtime](https://docs.cloud.google.com/vertex-ai/docs/predictions/optimized-tensorflow-runtime). This runtime enables more efficient and lower cost inference than prebuilt containers that use open-source TensorFlow.
- Run [multi-host inferencing with large models on GKE](https://cloud.google.com/blog/products/ai-machine-learning/deploy-and-serve-open-models-over-google-kubernetes-engine) by using the [LeaderWorkerSet (LWS) API](https://github.com/kubernetes-sigs/lws/blob/main/README.md).
- Leverage the [NVIDIA Triton inference server](https://docs.cloud.google.com/vertex-ai/docs/predictions/using-nvidia-triton) for Vertex AI.
- Simplify the deployment of inference workloads on GKE by using LLM-optimized configurations. For more information, see [Analyze model serving performance and costs with GKE Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart).

### Optimize resource consumption based on performance goals

Resource optimization helps to accelerate training, iterate efficiently, improve
model quality, and increase the serving capacity.

#### Choose appropriate processor types

Your choice of compute platform can have a significant impact on the training
efficiency of a model.

- Deep learning models perform well on GPUs and TPUs because such models require large amounts of memory and parallel matrix computation. For more information about workloads that are well suited to CPUs, GPUs, and TPUs, see [When to use TPUs](https://docs.cloud.google.com/tpu/docs/intro-to-tpu#when_to_use_tpus).
- [Compute-optimized VMs](https://docs.cloud.google.com/compute/docs/compute-optimized-machines) are ideal for HPC workloads.

#### Optimize training and serving on GPUs

To optimize the performance of training and inference workloads that are
deployed on GPUs, consider the following recommendations:

| Recommendation | Description |
|---|---|
| **Select appropriate memory specifications.** | When you choose [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus), select memory specifications based on the following factors: - **Model capacity**: The total memory size (memory footprint) of the model's trainable parameters and gradients. - **Workload type**: Training requires more memory than serving. - **Training batch size**: For larger batches, more activations are stored and the memory requirement is higher. - **Data type**: Workloads that process high-quality images or that use high-precision arithmetics need machine types with larger memory specifications. |
| **Assess core and memory bandwidth requirements.** | In addition to memory size, consider other requirements like the number of Tensor cores and memory bandwidth. These factors influence the speed of data access and computations on the chip. |
| **Choose appropriate GPU machine types.** | Training and serving might need different GPU machine types. - Training jobs need one or more GPUs, or even multiple nodes, with significantly large memory and bandwidth. - Inference workloads require relatively less memory and fewer high-performance GPUs. We recommend that you use large machine types for training and smaller, cost-effective machine types for inference. To detect resource utilization issues, use monitoring tools like the NVIDIA DCGM agent and adjust resources appropriately. |
| **Leverage GPU sharing on GKE.** | Dedicating a full GPU to a single container might be an inefficient approach in some cases. To help you overcome this inefficiency, GKE supports the following [GPU-sharing strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/timesharing-gpus): - [Multi-instance GPU](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi): Allocate a single GPU to multiple containers on a node. - [GPU time-sharing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/timesharing-gpus): Allocate GPU time across multiple containers. Each container gets a time slice. - [NVIDIA multi-process service (MPS)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nvidia-mps-gpus): Run multi-process workloads concurrently on a single GPU by using a binary-compatible [CUDA](https://developer.nvidia.com/cuda) implementation. To maximize resource utilization, we recommend that you use an appropriate combination of these strategies. For example, when you virtualize a large H100 GPU by using the GPU time-sharing *and* multi-instance GPU strategies, the serving platform can scale up and down based on traffic. GPU resources are repurposed in real time based on the load on the model containers. |
| **Optimize routing and load balancing.** | When you deploy multiple models on a cluster, you can use [GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway) for optimized routing and load balancing. Inference Gateway extends the routing mechanisms of the [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io) by using the following capabilities: - [Request body routing logic](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-gke-inference-gateway#create-httproute) and endpoint selection. These features enable optimization strategies like using the same base model for [multiple LoRA adapters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-gke-inference-gateway#specify-model-objectives). - Generative AI-specific [security extensions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-gke-inference-gateway-configurations#ai-safety-checks) like Model Armor. |
| **Share resources for Vertex AI endpoints.** | You can configure multiple Vertex AI endpoints to use a common pool of resources. For more information about this feature and its limitations, see [Share resources across deployments](https://docs.cloud.google.com/vertex-ai/docs/predictions/model-co-hosting). |

#### Optimize training and serving on TPUs

TPUs are Google chips that help solve
[massive scale](https://cloud.google.com/transform/ai-specialized-chips-tpu-history-gen-ai)
challenges for ML algorithms. These chips provide optimal performance for AI
training and inference workloads. When compared to GPUs, TPUs provide higher
efficiency for deep learning training and serving. For information about the use
cases that are suitable for TPUs, see
[When to use TPUs](https://docs.cloud.google.com/tpu/docs/intro-to-tpu#when_to_use_tpus).
TPUs are compatible with ML frameworks like
[TensorFlow](https://docs.cloud.google.com/tpu/docs/tensorflow-pods),
[PyTorch](https://docs.cloud.google.com/tpu/docs/run-calculation-pytorch),
and
[JAX](https://docs.cloud.google.com/tpu/docs/run-calculation-jax).

To optimize TPU performance, use the following techniques, which are described
in the
[Cloud TPU performance guide](https://docs.cloud.google.com/tpu/docs/performance-guide):

- Maximize the batch size for each TPU memory unit.
- Ensure that TPUs aren't idle. For example, implement parallel data reads.
- Optimize the XLA compiler. Adjust tensor dimensions as required and avoid padding. XLA automatically optimizes for graph execution performance by using tools like fusion and broadcasting.

#### Optimize training on TPUs and serving on GPUs

TPUs support efficient training. GPUs provide versatility and wider availability
for inference workloads. To combine the strengths of TPUs and GPUs, you can
train models on TPUs and serve them on GPUs. This approach can help to reduce
overall costs and accelerate development, particularly for large models. For
information about the locations where TPU and GPU machine types are available,
see
[TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones)
and
[GPU locations](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

#### Optimize the storage layer

The storage layer of your training and serving infrastructure is critical to
performance. Training jobs and inferencing workloads involve the following
storage-related activities:

- Loading and processing data.
- Checkpointing the model during training.
- Reloading binaries to resume training after node preemptions.
- Loading the model efficiently to handle inferencing at scale.

The following factors determine your requirements for storage capacity,
bandwidth, and latency:

- Model size
- Volume of the training dataset
- Checkpointing frequency
- Scaling patterns

If your training data is in Cloud Storage, you can reduce the data loading
latency by using
[file caching in Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching). Cloud Storage FUSE lets you mount a
Cloud Storage
bucket on compute nodes that have Local SSD disks. For information about
improving the performance of Cloud Storage FUSE, see
[Performance tuning best practices](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).

A
[PyTorch connector](https://docs.cloud.google.com/storage/docs/pytorch-connector)
to Cloud Storage provides high performance for data reads and writes. This
connector is particularly beneficial for training with large datasets and for
checkpointing large models.

Compute Engine supports various
[Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types)
types. With
[Google Cloud Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hyperdisks),
you can provision the required throughput and IOPS based on training needs. To
optimize disk performance, start by resizing the disks and then consider
changing the machine type. For more information, see
[Optimize Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance).
To load test the read-write performance and latency at the storage layer, you
can use tools like
[Flexible I/O tester (FIO)](https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-linux).

For more information about choosing and optimizing storage services for your AI
and ML workloads, see the following documentation:

- [AI Hypercomputer storage services](https://docs.cloud.google.com/ai-hypercomputer/docs/storage#storage_recommendations)
- [Design storage for AI and ML workloads in Google Cloud](https://docs.cloud.google.com/architecture/ai-ml/storage-for-ai-ml)

#### Optimize the network layer

To optimize the performance of AI and ML workloads, configure your
VPC networks to provide adequate bandwidth and maximum throughput
with minimum latency. Consider the following recommendations:

| Recommendation | Suggested techniques for implementation |
|---|---|
| Optimize VPC networks. | - Configure a large [maximum transmission unit (MTU)](https://docs.cloud.google.com/vpc/docs/mtu) size. - Use [Premium Tier networking](https://docs.cloud.google.com/network-tiers/docs/overview#premium_tier). - For improved connectivity on VMs with NVIDIA ConnectX machine types (A3 Ultra and later), configure the VPC network with the [Remote Direct Memory Access (RDMA) network profile](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles). |
| Place VMs closer to each other. | - Define [compact placement policies in Compute Engine](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies). - Use [Topology Aware Scheduling in GKE](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas). |
| Configure VMs to support higher network speeds. | - Use [Google Virtual NICs (gVNICs)](https://docs.cloud.google.com/compute/docs/networking/using-gvnic). - Configure [per VM Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration). For information about testing Tier_1 networking performance, see [Benchmark higher network bandwidth for VM instances](https://docs.cloud.google.com/compute/docs/networking/benchmarking-higher-bandwidth-vms). - For multi-GPU training, optimize GPU-to-GPU network performance by using NVIDIA-specific [connectivity configurations](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth). - Install [NVIDIA GPUDirect](https://developer.nvidia.com/gpudirect) and configure the [NVIDIA collective communication library (NCCL)](https://developer.nvidia.com/nccl). For more information, see [Install the GPUDirect binary and configure NCCL](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx#install-gpudirect-tcpx-nccl). To test the performance of NCCL operations, you can use standard [NCCL tests](https://github.com/NVIDIA/nccl-tests). |

## Link performance metrics to design and configuration choices

To innovate, troubleshoot, and investigate performance issues, you must
establish a clear link between design choices and performance outcomes. You need
a reliable record of the lineage of ML assets, deployments, model outputs, and
the corresponding configurations and inputs that produced the outputs.

### Build a data and model lineage system

To reliably improve performance, you need the ability to trace every model
version back to the exact data, code, and configurations that were used to
produce the model. As you scale a model, such tracing becomes difficult. You
need a lineage system that automates the tracing process and creates a record
that's clear and can be queried for every experiment. This system lets your
teams efficiently identify and reproduce the choices that lead to the optimally
performing models.

To view and analyze the lineage of pipeline artifacts for workloads in
Vertex AI, you can use
[Vertex ML Metadata](https://docs.cloud.google.com/vertex-ai/docs/ml-metadata/introduction)
or
[Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction).
Both options let you register events or artifacts to meet governance
requirements and to query the metadata and retrieve information when needed.
This section provides an overview of the two options. For detailed information
about the differences between Vertex ML Metadata and
Knowledge Catalog, see
[Track the lineage of pipeline artifacts](https://docs.cloud.google.com/vertex-ai/docs/pipelines/lineage).

#### Default implementation: Vertex AI ML Metadata

Your first pipeline run or *experiment* in Vertex AI
creates a default Vertex ML Metadata service. The parameters and
artifact metadata that the pipeline consumes and generates are automatically
registered to a Vertex ML Metadata store. The
[data model](https://docs.cloud.google.com/vertex-ai/docs/ml-metadata/data-model)
that's used to organize and connect the stored metadata contains the following
elements:

- **Context**: A group of artifacts and executions that represents an experimentation run.
- **Execution**: A step in a workflow, like data validation or model training.
- **Artifact**: An input or output entity, object, or piece of data that a workflow produces and consumes.
- **Event**: A relationship between an artifact and an execution.

By default, Vertex ML Metadata captures and
[tracks](https://docs.cloud.google.com/vertex-ai/docs/ml-metadata/tracking)
all input and output artifacts of a pipeline run. It integrates these artifacts
with
[Vertex AI Experiments](https://docs.cloud.google.com/vertex-ai/docs/experiments/intro-vertex-ai-experiments),
[Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction),
and
[Vertex AI managed datasets](https://docs.cloud.google.com/vertex-ai/docs/datasets/overview).

[Autologging](https://docs.cloud.google.com/vertex-ai/docs/experiments/run-training-job-experiments)
is a built-in feature in Vertex AI Training to automatically log
data to Vertex AI Experiments. To efficiently track experiments for
optimizing performance, use the built-in integrations between
Vertex AI Experiments and the associated
Vertex ML Metadata service.

Vertex ML Metadata provides a filtering syntax and operators to run
queries about artifacts, executions, and contexts. When required, your teams can
efficiently retrieve information about a model's registry link and its dataset
or evaluation for a specific experiment run. This metadata can help to
accelerate the discovery of choices that optimize performance. For example, you
can
[compare pipeline runs](https://docs.cloud.google.com/vertex-ai/docs/experiments/user-journey/uj-compare-pipeline-runs),
[compare models](https://docs.cloud.google.com/vertex-ai/docs/experiments/user-journey/uj-compare-models),
and
[compare experiment runs](https://docs.cloud.google.com/vertex-ai/docs/experiments/compare-analyze-runs).
For more information, including example queries, see
[Analyze Vertex ML Metadata](https://docs.cloud.google.com/vertex-ai/docs/ml-metadata/analyzing#inputs-and-outputs).

#### Alternative implementation: Knowledge Catalog

Knowledge Catalog discovers metadata from
[Google Cloud resources](https://docs.cloud.google.com/dataplex/docs/catalog-overview#supported-sources),
including Vertex AI artifacts. You can also integrate a
[custom data source](https://docs.cloud.google.com/dataplex/docs/ingest-custom-sources).

Knowledge Catalog can read metadata across multiple
regions and organization-wide stores, whereas Vertex ML Metadata
is a project-specific resource. When compared to Vertex ML Metadata,
Knowledge Catalog involves more setup effort. However,
Knowledge Catalog might be appropriate when you need
integration with your wider data portfolio in Google Cloud and with
organization-wide stores.

Knowledge Catalog discovers and harvests metadata for
projects where the Data Lineage API is enabled. The metadata in the catalog
is organized by using a
[data model](https://docs.cloud.google.com/dataplex/docs/catalog-overview#supported-sources)
that consists of projects, entry groups, entries, and aspects.
Knowledge Catalog provides a
[specific syntax](https://docs.cloud.google.com/dataplex/docs/search-syntax)
that you can use to discover artifacts. If required, you can
[map Vertex ML Metadata artifacts](https://docs.cloud.google.com/vertex-ai/docs/pipelines/lineage#map_artifacts_to_fqn)
to Knowledge Catalog.

### Use explainability tools

The behavior of an AI model is based on data that was used to train the model.
This behavior is encoded as
[parameters](https://developers.google.com/machine-learning/glossary#parameter)
in mathematical functions. Understanding exactly *why* a model performs in a
certain way can be difficult. However, this knowledge is critical for
performance optimization.

For example, consider an image classification model where the training data
contains images of only red cars. The model might learn to identify the "car"
label based on the color of the object rather than the object's spatial and
shape attributes. When the model is tested with images that show cars of
different colors, the performance of the model might degrade. The following
sections describe tools that you can use to identify and diagnose such problems.

#### Detect data biases

In the
[exploratory data analysis (EDA)](https://cloud.google.com/blog/products/ai-machine-learning/building-ml-models-with-eda-feature-selection)
phase of an ML project, you identify issues with the data, such as
[class-imbalanced datasets](https://developers.google.com/machine-learning/glossary/fundamentals#class_imbalanced_data_set)
and
[biases](https://developers.google.com/machine-learning/glossary/fundamentals#bias-ethicsfairness).

In production systems, you often retrain models and run experiments with
different datasets. To standardize data and compare across experiments, we
recommend a systematic approach to EDA that includes the following
characteristics:

- **Automation**: As a training set grows in size, the EDA process must run automatically in the background.
- **Wide coverage**: When you add new features, the EDA must reveal insights about the new features.

Many EDA tasks are specific to the data type and the business context. To
automate the EDA process, use BigQuery or a managed data
processing service like Dataflow. For more information, see
[Classification on imbalanced data](https://www.tensorflow.org/tutorials/structured_data/imbalanced_data)
and
[Data bias metrics for Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/evaluation/data-bias-metrics).

#### Understand model characteristics and behavior

In addition to understanding the distribution of data in the training and
validation sets and their biases, you need to understand a model's
characteristics and behavior at prediction time. To understand model behavior,
use the following tools:

| Tool | Description | Purposes |
|---|---|---|
| **Example-based explanations** | You can use [example-based explanations](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview#example-based) in Vertex Explainable AI to understand a prediction by finding the most similar examples from the training data. This approach is based on the principle that similar inputs yield similar outputs. | - Identify and fix gaps in the training data by finding similar examples for an incorrect prediction. - Classify inputs that the model was not originally trained to recognize, by using [neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) from a reference set. - Identify anomalies by finding inputs that are significantly different from all of the known training examples. - Make data collection more efficient by identifying ambiguous cases, like when neighbors have mixed labels. Prioritize such cases for human review. |
| **Feature-based explanations** | For predictions that are based on tabular data or images, feature-based explanations show how much each [feature](https://developers.google.com/machine-learning/glossary/fundamentals#feature) affects a prediction when it's compared to a baseline. Vertex AI provides different [feature attribution methods](https://docs.cloud.google.com/vertex-ai/docs/explainable-ai/overview#feature-attribution-methods) depending on the model type and task. The methods typically rely on sampling and sensitivity analysis to measure how much the output changes in response to changes in an input feature. | - Identify biases that a validation step might miss. - Optimize performance by identifying the features that are most important for a prediction. To increase a model's quality and performance, ML engineers can intentionally add, remove, or engineer features. |
| **[What-If Tool](https://pair-code.github.io/what-if-tool)** | The What-If Tool was developed by Google's [People + AI Research (PAIR) initiative](https://pair.withgoogle.com/) to help you understand and visualize the behavior of image and tabular models. For examples of using the tool, see [What-If Tool Web Demos](https://pair-code.github.io/what-if-tool/explore/). | - Debug and find the root cause of incorrect predictions. - Investigate how a model performs across different subsets of data by identifying biases through a fairness analysis. - Understand a model's behavior, particularly the relationship between a model's predictions and input features. - Compare predictions by using a visual comparison tool that requires either two models or a ground truth baseline. |

## Contributors

Authors:

- [Benjamin Sadik](https://www.linkedin.com/in/benjaminhaimsadik) \| AI and ML Specialist Customer Engineer
- [Filipe Gracio, PhD](https://www.linkedin.com/in/filipegracio) \| Customer Engineer, AI/ML Specialist

<br />

Other contributors:

- [Daniel Lees](https://www.linkedin.com/in/daniellees) \| Cloud Security Architect
- [Kumar Dhanagopal](https://www.linkedin.com/in/kumardhanagopal) \| Cross-Product Solution Developer

<br />

<br />