---
title: "Knowledge graph validation by integrating LLMs and human-in-the-loop"
source: "https://www.sciencedirect.com/science/article/pii/S030645732500086X?__cf_chl_tk=Yh5sRbFpPOmIm_9unhfoiA3T4jYBYBUBwJAKFSQmDQA-1786478783-1.0.1.1-Vzgn6x5K8fbrCsHzvDOMp8CKS88faikI0Rq5TIqf80E"
author:
  - "[[knowledge graphs]]"
  - "[[Danilo Dessì]]"
  - "[[Francesco Osborne]]"
published:
created: 2026-08-11
description: "Ensuring the quality of knowledge graphs (KGs) is crucial for the success of the intelligent applications they support. Recent advances in large langu…"
tags:
  - "clippings"
---
## Part of special issue

[Large Language Models and Data Quality for Knowledge Graphs](https://www.sciencedirect.com/science/journal/03064573/vsi/10C05PM18JB)

Edited by Dr. Stefano Marchesin (University of Padua Department of Information Engineering, Padova,, Italy), Prof. Dr.-Ing. Gianmaria Silvello (University of Padua Department of Information Engineering, Padova,, Italy), Dr. Omar Alonso (No Organisation - Home based - 0645861,,, )

[View special issue](https://www.sciencedirect.com/science/journal/03064573/vsi/10C05PM18JB)

## Published by: Elsevier

### Published by

[![Elsevier](https://www.sciencedirect.com/us-east-1/prod/110e3dbe180bac7db7ef7ee5e3c49d1209df49d5/image/elsevier-non-solus.svg)](https://www.sciencedirect.com/journal/information-processing-and-management "Go to Information Processing & Management on ScienceDirect")

,,,

[View **PDF**](https://www.sciencedirect.com/science/article/pii/S030645732500086X/pdfft?md5=cd76927795a8e59e14d542747874f7a1&pid=1-s2.0-S030645732500086X-main.pdf)

[10.1016/j.ipm.2025.104145](https://doi.org/10.1016/j.ipm.2025.104145)

## Highlights

## Keywords

Knowledge graph validation

;

Large language models

;

Hybrid human-AI workflows

- [Previous article in this issue](https://www.sciencedirect.com/science/article/pii/S0306457325001049)
- [Next article in this issue](https://www.sciencedirect.com/science/article/pii/S0306457325001207)

## 1\. Introduction

[Knowledge graphs](https://www.sciencedirect.com/topics/social-sciences/knowledge-graph) (KGs) are conceptual models that structure domain knowledge, integrated from various sources, and stored in a machine-readable and understandable format (, ). KGs are employed in a variety of intelligent applications () supporting tasks such as question answering (), [recommender systems](https://www.sciencedirect.com/topics/computer-science/recommender-systems) (), and exploratory search (). KG-based solutions have been adopted across various domain such as medicine (), production & manufacturing (, ), tourism (), and education (). In the [scientometrics](https://www.sciencedirect.com/topics/social-sciences/scientometrics) domain, [scientific KGs](https://www.sciencedirect.com/topics/computer-science/scientific-knowledge) have recently gained significant interest as a solution for knowledge-based content exploration of scientific works (,,,, ). Some of the proposed scientific knowledge graphs have been manually curated, ensuring the high quality of these resources, such as the [Open Research](https://www.sciencedirect.com/topics/computer-science/open-research) Knowledge Graph (). Others prioritize a high coverage of the scientific domain and have been generated through automated approaches, e.g., COVID-19 Knowledge Graph () and the Computer Science Knowledge Graph ().

While automated KG generation allows the integration of content from a vast amount of sources and provides extensive coverage of a given domain, the produced resources can [face](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/face) quality issues such as the inclusion of erroneous, inconsistent or misleading facts (, ). To ensure the success of systems relying on the constructed KGs, knowledge graph validation is an essential step to be integrated within KG generation pipelines.

Against this backdrop, various approaches for KG quality evaluation have been proposed. In, the authors provide an overview of state-of-the-art validation techniques, categorized as automated methods relying on statistics (e.g., [outlier detection](https://www.sciencedirect.com/topics/computer-science/outlier-detection) and KG embedding) or rules (e.g., ontology-based rules), and methods relying on a human-in-the-loop (HiL), such as crowdsourcing. While some KG generation pipelines contain an integrated automated validation stage, HiL-based KG validation techniques do not scale well (, ) and are thus often excluded or envisioned as a future extension.

Recently, [large language models](https://www.sciencedirect.com/topics/social-sciences/large-language-model) (LLMs) have demonstrated human-like performance in a variety of natural language [processing tasks](https://www.sciencedirect.com/topics/computer-science/processing-task), significantly reducing the need of human intervention (, ). As a result, several works in the [knowledge engineering](https://www.sciencedirect.com/topics/computer-science/knowledge-engineering) domain, e.g.,,,,, have been inspired, reporting promising LLM performance in the evaluation of [semantic resources](https://www.sciencedirect.com/topics/computer-science/semantic-resource) (i.e., ontologies, KGs). However, the conducted experiments are limited in terms of the simplicity of the application domain, small size of the evaluated resource and lack of comprehensive experimental investigations. Moreover, many open questions remain: (i) how should the proposed LLM-based approaches be evaluated? (ii) how should LLM-based approaches be integrated into the generation of real KGs? (iii) could these solutions fully replace or only support human validators?

This paper primarily addresses question (iii) above, exploring how to best combine LLMs and [HiL](https://www.sciencedirect.com/topics/computer-science/human-in-the-loop) for KG validation. Specifically, we investigate the following two research questions.

*RQ1: What are different ways to combine LLMs and HiL contributors for the validation of large knowledge graphs?* We investigate novel KG validation workflows, incorporating both HiL and LLM validations, to improve the performance of KG generation pipelines. We base our work on previous research on collaborative human-LLM workflows from a spectrum of automation levels, proposed for relevance judgments tasks in, which we adopt for KG validation. As a result, we propose *nine distinct validation workflows* - three workflows that rely exclusively on human judgment, three [hybrid solutions](https://www.sciencedirect.com/topics/computer-science/hybrid-solution) involving a combination of human expertise and LLMs, and three fully automated LLM-based validation pipelines. Each workflow is tailored towards a specific evaluation goal and availability of HiL and LLM resources to provide adaptability across different use cases.

*RQ2: What are the strengths and limitations of human-LLM collaborative knowledge graph validation workflows?* To the best of our knowledge, no prior empirical investigation has been performed of the trade-offs involved in hybrid human-machine workflows for KG validation. Thus, we conduct *two experimental investigations on a large scale resource*, representing a non-trivial domain, to collect empirical evidence and facilitate a direct comparison of the achieved performance with each workflow.

To explore RQ1 and RQ2, we consider the validation of the Computer Science Knowledge Graph (CS-KG) as our use case. CS-KG is a scientific knowledge graph, automatically generated from 6.7M publications, supporting researchers and funding agencies by enabling the exploration of research dynamics (). We selected this KG for its relevance to various applications, its broad coverage of scientific concepts and domains, and its focus on a field well-known to the authors. Furthermore, CS-KG was constructed using an open methodology that already integrates a few validation techniques, which we can leverage in our analysis. Specifically, CS-KG was generated using the SCICERO pipeline (), which extracts scientific statements from literature and represents them as triples of the form $<$ *subject, predicate, object* $>$, for instance, $<$ *cloud service, acquires,* *[information integration](https://www.sciencedirect.com/topics/computer-science/information-integration "Learn more about information integration from ScienceDirect's AI-generated Topic Pages")* $>$ or $<$ *[text classification](https://www.sciencedirect.com/topics/computer-science/text-classification "Learn more about text classification from ScienceDirect's AI-generated Topic Pages")**, includes, text processing* $>$. SCICERO includes an automated validation stage, which we extend by integrating it with HiL techniques, LLM-sourced validations or a combination thereof. Subsequently we evaluate the achieved performance of these SCICERO extensions on a set of $3 . 6 K$ triples.

Our results indicate that: (1) an LLM-based validation can increase precision from 75% up to 87% without requiring any [manual validation](https://www.sciencedirect.com/topics/computer-science/manual-validation) efforts; (2) both fully manual and fully automated validation approaches present trade-offs between precision and recall; and (3) a hybrid approach, leveraging a HiL only upon a disagreement among automated methods, leads to smaller precision improvement up to 80% and overall highest F1 score reaching 82% (＋5% compared to SCICERO) with minimal manual efforts.

The remainder of this paper is structured as follows. Section reviews related research in the area. Section introduces CS-KG and its extraction pipeline SCICERO. In Section, we propose extensions of SCICERO, covering a spectrum of automation levels from purely HiL-based validation to purely LLM-based validation. Section details the design of two experiments carried out to evaluate these extended workflows. The experiment results are discussed in Section, followed by a conclusion and future work directions in Section.

## 2\. Related work

While human-LLM frameworks have not yet been proposed for the validation of [knowledge graphs](https://www.sciencedirect.com/topics/social-sciences/knowledge-graph), some semi-automatic approaches towards a scalable validation of [semantic resources](https://www.sciencedirect.com/topics/computer-science/semantic-resource) (i.e., ontologies, knowledge graphs) have been designed. Section reviews several such works, providing an overview of state-of-the-art human-in-the-loop approaches. In Section, we explore automatic triple validation methods, with a particular focus on recent LLM-based techniques designed to enhance the quality of semantic resources. Finally, Section lays the groundwork for the human-LLM workflows proposed in this paper by providing an overview of studies that examine the levels of collaboration in human-machine workflows across various domains.

### 2.1. Semantic resources evaluation workflows

A fully manual [KG creation](https://www.sciencedirect.com/topics/computer-science/graph-creation) process, which involves trained domain experts and knowledge engineers, can produce higher quality resources than a [fully automated approach](https://www.sciencedirect.com/topics/computer-science/fully-automated-approach). However, scalability becomes a significant challenge, especially for large-scale KGs. As an alternative, a human-centric KG validation, typically implying the annotation of triples as true or false by human contributors, can be included in an automated creation workflow to ensure the removal of incorrectly represented statements. Several research directions have emerged, trying to approach this issue from different angles.

#### Semi-automatic KG generation.

Human-in-the-loop approaches have been incorporated as a final step in KG extraction workflows containing some level of automation. For instance, in, HiL validation is carried out as part of the triple extraction step from medical literature to eliminate noisy triples. A similar workflow is also described in, where human judgment is added as the last stage of the KG extraction workflow. While these works avoid the manual efforts of creating the KG, they introduce a bottleneck at the validation stage.

#### Triple selection for HiL annotation.

Several approaches have been implemented to reduce the amount of triples requiring [manual validation](https://www.sciencedirect.com/topics/computer-science/manual-validation). In, HiL annotation is conducted to verify the results of an entity-linking prediction task, with triples being validated only if the prediction confidence score falls below a certain threshold. A similar approach combined with further contradiction reasoning is employed in to select which triples to manually annotate.

#### Triple prioritization for HiL annotation.

The minimization of triples to be checked by a HiL is also discussed in, where triples are prioritized based on the amount of additional triples, whose correctness can be inferred from the annotation. This line of work is continued in and by optimizing the cost and duration of the manual annotations and [computational efforts](https://www.sciencedirect.com/topics/computer-science/computational-effort).

#### HiL assistance.

A semi-automatic workflow focusing on assisting human validators is presented in. In this approach, human contributors are assisted by an automatic tool using reasoning to provide suggestions based on previously validated constraints and identified inconsistencies.

In the mentioned examples, the KG validation task is performed by the human annotators while automated approaches either generate the triples to be checked (, ), aim to reduce the amount of triples to be verified (,,,, ), or assist the human annotator with automated suggestions (). In parallel, various automated KG validation techniques have been investigated, which we summarize next.

### 2.2. Automated validation of semantic resources

Automatic KG extraction approaches typically [face](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/face) a [trade off](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/tradeoff) between the scope and quality of the resulting resource (). As a result, several research directions have emerged focusing on automated validation of semantic resources, specifically addressing tasks such as completion and error-detection ().

Related work has approached these tasks following various methods such as utilizing [KG embeddings](https://www.sciencedirect.com/topics/computer-science/knowledge-graph-embedding) (,, ), graph features () or transformers (,, ), developed to classify newly generated triples as valid or invalid. For KG completion, for instance, in, a classifier is trained on existing KG triples and subsequently applied to assess the validity of newly generated triples. Similarly, in, a classifier is trained on a reliable subset of the KG and then used to determine whether uncertain triples are erroneous.

Recently, however, LLMs have demonstrated impressive human-level performance on tasks, typically completed by human contributors across various domains (, ) without additional training required. Therefore, next, we discuss relevant LLM-based approaches in the Semantic Web domain, with focus on the validation of semantic resources.

#### Validating semantic resources with LLMs.

Over the last years LLMs have attracted much research interest from the Semantic Web community. LLMs have been widely explored for some [knowledge engineering](https://www.sciencedirect.com/topics/computer-science/knowledge-engineering) tasks such as the creation or completion of semantic resources, e.g.,,,,. However, the evaluation of semantic resources with LLMs has only recently received interest.

In, the authors include a triple validation step, using LLMs, in their KG generation workflow. Yet, they do not provide quantitative details on the performance of this validation approach or compare it to other methods.

In, the focus is on designing a prompt-chain for generating ontologies, including a validation stage where errors are identified through external services (such as OOPS and an ontology reasoner) and corrected by LLMs. The paper introduces several successfully corrected examples from the generation of the Wine Ontology. However, the authors do not specify whether the validation performance was tested in a concrete experimental setup.

The identification of ontology modeling defects through LLMs has been investigated in. While the study reports validation accuracy of 96%, the carried out experiment relied on a small dataset from the Pizza Ontology.

In, the authors propose the development of knowledge engineering task-specific assessment tests and evaluate various LLMs based on their ability to validate ontology axioms. The benchmark aims to assess [LLM](https://www.sciencedirect.com/topics/social-sciences/large-language-model) capabilities, drawing inspiration from qualification tests typically used for crowdworkers.

In, the authors investigate incorrect & missing class membership relations in ontologies using LLMs. They experiment with relations extracted from public knowledge graphs in the general domain and across various LLMs. However, the dataset size and examined relation types are limited.

Recently, in, the LLM-based validation of newly generated KG triples with focus on inconsistency detection has been explored. The authors investigate four fundamental aspects: aligning classes and properties, standardizing URIs, ensuring [semantic consistency](https://www.sciencedirect.com/topics/computer-science/semantic-consistency), and verifying [syntactic](https://www.sciencedirect.com/topics/computer-science/syntactics) accuracy.

While the reviewed literature indicates the potential of LLMs for validating semantic resources, proposed approaches are still in preliminary stages, tested on a small dataset or lack experimental evaluation. Additionally, there is a lack of studies exploring how the designed solutions should be best integrated into existing KG generation pipelines, i.e., whether they could fully replace previous automated/manual approaches or they should serve as a complementary tool.

### 2.3. Human–machine collaboration workflows

In the knowledge graph validation field, a study classifies validation approaches into methods based on human-annotation, statistics/learning, rules, and hybrid approaches that combine two or more of these methods (). The authors argue that hybrid approaches have the potential to overcome the limitations of each separate method. While human-machine collaboration lacks thorough investigations in the Semantic Web community, possible interactions between human contributors and automated approaches have received research interests in various communities.

Collaborative workflows, illustrating the roles and responsibilities in hybrid human-AI teams have been explored for moral [decision making](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/decision-making) in the medical domain (). The work highlights levels of involvement of each agent (human or AI) and the expected advantages and disadvantages in terms of workload, accountability, and ethical concerns.

A recent positioning paper identifies different levels of collaborations between human annotators and LLMs for relevance judgment tasks (). The authors discuss the implications of using [LLM](https://www.sciencedirect.com/topics/computer-science/large-language-model) annotations compared to a traditional HiL approach, considering factors such as budget and quality. They discuss [potential benefits](https://www.sciencedirect.com/topics/computer-science/potential-benefit) and scenario implementations across a spectrum from fully manual to fully automated approaches (), organized in the following categories:

- •
	*Human judgment* implies that (1) the annotations are completed manually by human participants, who perform the tasks without any support or (2) human annotators are supported by tools (e.g., document clustering) but ultimately remain the sole judges of the triple correctness.
- •
	*[AI](https://www.sciencedirect.com/topics/computer-science/artificial-intelligence "Learn more about AI from ScienceDirect's AI-generated Topic Pages")* *assistance* can be implemented in various ways with different levels of responsibility. For instance, LLMs can be employed to generate summaries or other contextual information to help the human judges in their annotations. Moreover, a task partitioning can be established where each agent focuses on tasks suited for their capabilities.
- •
	*Human verification* describes a human-in-the-loop workflow, where human participants judge the results of an automated approach and correct them if needed. A novel implementation, motivated by the “preference-testing” concept, suggests that two LLMs can provide judgments and a human participant can choose the more relevant example.
- •
	*Fully automated* workflows treat LLM judgments as reliable sources, which can completely replace human judges.

In this study, we consider interaction workflows identified in the literature, and provide experimental results for various collaboration workflows applied to a concrete use case: the validation of automatically extracted triples, part of the Computer Science Knowledge Graph, which we describe in the next section.

## 3\. Use case: Validating the computer science knowledge graph

The Computer Science Knowledge Graph (CS-KG) describes a vast collection of claims extracted from 6.7 million scientific articles in the field of Computer Science. In CS-KG, scientific claims are represented as triples in the form $<$ *subject, predicate, object* $>$, describing the relation (predicate) between two entities (subject and object). The knowledge graph contains about 10M entities, classified within the five categories *Method, Task, Material, Metric,* and *OtherEntity*, and connected through 179 object properties (, ).

For instance, the triple $<$ [support vector machine](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/support-vector-machine)*,outperforms,decision tree* $>$ *,* refers to the claim that the entity *[support vector machine](https://www.sciencedirect.com/topics/computer-science/support-vector-machine "Learn more about support vector machine from ScienceDirect's AI-generated Topic Pages")* of type *Method* outperforms the entity *[decision tree](https://www.sciencedirect.com/topics/computer-science/decision-trees "Learn more about decision tree from ScienceDirect's AI-generated Topic Pages")* of type *Method*. Since often no objective truth can be determined, as in the given example, CS-KG claims should be considered only within the context of the articles, they are linked to.

CS-KG supports a variety of tasks such as advanced literature search and trend forecasting by integrating content from various sources. Thus, the coverage of the knowledge graph is of high importance. However, it is equally important to identify and discard erroneous facts before they are incorporated into the final version of the knowledge graph.

In this section, we first explain the rationale for selecting CS-KG as our use case. Next, we present SCICERO, the generation pipeline employed to construct CS-KG. Finally, we describe the evaluation process used to assess the quality of the resulting resource.

### Use case motivation.

We selected CS-KG as our use case for two main reasons:

- •
	*Significance and Adoption.* CS-KG has attracted significant research interest and has been integrated into various applications, demonstrating its relevance and value as a resource. For instance, it has been incorporated into a research [support system](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/support-system) proposed in, which enables scientists to explore scientific literature, state-of-the-art methodologies for specific tasks, and available scientific artifacts. In, the authors introduce a resume-to-job matching method that identifies the most suitable open positions based on an applicant’s skills. They further propose an extension of their framework which leverages CS-KG to recommend relevant patents or articles, helping job candidates enhance their expertise in preparation for applications. CS-KG has also been employed in experimental investigations to facilitate the retrieval of papers within specific subfields of Computer Science (). Further research leveraging CS-KG and its predecessor, AI-KG (), includes entity extraction from scientific publications (), scholarly article classification (), and knowledge graph completion ().
- •
	*Ease of use for HiL evaluation.* The SCICERO pipeline was evaluated on a CS-KG subset containing $3 . 6 K$ triples. This dataset includes not only the final ground truth label of each evaluated triple but also individual annotations from three experts. Consequently, the SCICERO gold standard enables the simulation of HiL experiments without requiring additional manual effort. Furthermore, the domain of CS-KG aligns with the expertise of the authors of this paper, facilitating access to a pool of knowledgeable experts who can support HiL approaches. These factors were instrumental in conducting the experiments presented in this study.

### Generation of CS-KG.

displays the architecture of the SCICERO pipeline (), which extracts triples from scientific literature to generate CS-KG. The pipeline takes as input a set of scientific texts related to the field of Computer Science, along with an ontology that defines the domain’s semantics. SCICERO then generates knowledge graph triples through three main stages: extraction, entity and relationship handling, and validation.

In the *extraction* stage the framework applies the CSO classifier (), which identifies [research topics](https://www.sciencedirect.com/topics/computer-science/research-topic) described in a scientific publication, according to the Computer Science Ontology, and revised [NLP](https://www.sciencedirect.com/topics/social-sciences/natural-language-processing) modules from the CoreNLP suite () to produce sets of initially extracted triples $T_{1} . . . T_{n}$. Extracted entities and relationships are further processed in *the entity and relationship handling* stage by, e.g., merging similar entities and discarding generic terms, thus resulting in an integrated set of triples, $T$. Lastly, the triple set is sent for a *validation* aiming to reduce noisy and erroneous triples. The validation stage contains two modules - a transformer-based validator and an ontology-based validator, which we will briefly describe next.

![](https://ars.els-cdn.com/content/image/1-s2.0-S030645732500086X-gr1.jpg)

Download: Download high-res image (168KB)

The *transformer validator* relies on the support of a triple, i.e., the number of textual sources from which the triple was extracted. As such the support-level $s$ can be interpreted as confidence of the correctness of the triple. Following this intuition, the triple set $T$ is split into $T_{r e l i a b l e}$, containing triples with a high support (e.g., $s \geq 5$, that is triples which were extracted from 5 or more documents), and $T_{u n c e r t a i n}$ (e.g., $s \leq 5$). Next, $T_{n e g a t i v e}$ is produced by corrupting triples of $T_{r e l i a b l e}$ and a transformer model is fine-tuned with $T_{r e l i a b l e}$ and $T_{n e g a t i v e}$. Lastly, a prediction is made for each triple from $T_{u n c e r t a i n}$ resulting in two new sets of triples predicted as correct $T_{c o n s i s t e n t}$ and incorrect $T_{t - d i s c a r d e d}$.

The *ontology validator* takes as input $T_{c o n s i s t e n t}$ and $T_{r e l i a b l e}$ and ensures the removal of triples which are not aligned with the [domain ontology](https://www.sciencedirect.com/topics/computer-science/domain-ontology). Thus, a triple containing a subject or object of a type not specified as the domain and range for the triple relation are discarded ($T_{o - d i s c a r d e d}$). For instance, the ontology defines the relation *uses*, indicating that an entity instance of type *Method, Metric, OtherEntity, or Task* uses an instance of type *Method, Metric, OtherEntity, Task, or Material*.

The triple $<$ *dbpedia, uses, core\_nlp* $>$ describes the relation between the entity *dbpedia*, classified as *Material*, and the entity *core\_nlp* of type *Method*. The given triple does not comply to the ontological schema since no entity of type *Material* can use an entity of type *Method*. Thus, it will be discarded.

### Evaluation.

SCICERO and all its components have been evaluated on a subset of $3 . 6 K$ triples. The KG generation achieves a precision of 75%, a recall of 79%, and an F1 score of 77%. The [validation modules](https://www.sciencedirect.com/topics/computer-science/validation-module) contribute to an over 20% increase in precision, highlighting the critical role of the validation stage. Additional information on the implementation of SCICERO and CS-KG is available in and.

In this paper, we aim to further enhance the quality of the generated triples by looking into possible extensions of the SCICERO validation stage with new validation modules based on LLMs and human expertise.

## 4\. Integrating LLMs and HiL into the SCICERO validation

Human validation has frequently been envisioned as an addition to automated KG generation workflows to ensure the quality of the produced knowledge graphs. We investigate possible extensions of the SCICERO pipeline with an additional *human validator* module. Building on recent advances in LLMs research, which have shown expert-level results for KG validation (), we also investigate an additional *LLM validator* module. We explore both workflows, where the LLM validator fully replaces the human validator as well as scenarios where LLMs and human annotators collaborate in the KG validation task.

This section discusses potential SCICERO extension workflows, with a particular focus on the level of collaboration between distinct [validation modules](https://www.sciencedirect.com/topics/computer-science/validation-module). Formally, let $T$ be a set of input triples, $S$ be the SCICERO pipeline, and $V$ the outcome of the triple validation. We want to introduce one or both modules $M_{j}$, where $j \in \left\{H i L , L L M\right\}$, such that the enhanced pipeline $S + M_{j}$ archives better performance in terms of precision, recall, and F1 score, compared to $S$ alone in validating the triples to be added to CS-KG. We build on top of our recent work (), where we perform a [preliminary investigation](https://www.sciencedirect.com/topics/computer-science/preliminary-investigation) of possible SCICERO extensions to select the most meaningful workflows which lead to the best performance scores. In the following section (Section ) we discuss two experiments with concrete implementation details for the LLM and human validator modules.

In, we categorize potential extension workflows based on the level of collaboration between the integrated LLM and the human validator. Specifically, we classify these workflows according to the four categories introduced in: human judgment, AI assistance, human verification, and full automation. Sections,,, provide a detailed description of each workflow and define the expected roles of the corresponding validation modules.

Additionally, we differentiate the types of the incorporated validation methods according to the classification from. In,,,,,,,,, statistics and learning-based methods are displayed in red. Rule-based methods are shown in yellow and human-based methods are displayed in purple.

Table 1. Possible extensions of SCICERO, employing various levels of interaction among human and LLM validations, following the interaction classification from.

<table><thead><tr><th><strong>Collaboration level</strong></th><th><strong>Workflow</strong></th><th><strong>Figure</strong></th><th><strong>Workflow description</strong></th></tr><tr><th>according to</th><th><strong>ID</strong></th><td>Empty Cell</td><td>Empty Cell</td></tr></thead><tbody><tr><td colspan="4"><strong>Human Judgment</strong></td></tr><tr><td><figure></figure></td><td>1</td><td></td><td>Human validation with no automated support.</td></tr><tr><td><figure></figure></td><td>2</td><td></td><td>Human validation as a final step of SCICERO’s validation. Experts are supported in the removal of noisy triples but have full decision control over triple additions to the KG.</td></tr><tr><td><figure></figure></td><td>3</td><td></td><td>Partial human validation for low-support triples (<math><msub is="true"><mrow is="true"><mi is="true">T</mi></mrow> <mrow is="true"><mi is="true">c</mi> <mi is="true">o</mi> <mi is="true">n</mi> <mi is="true">s</mi> <mi is="true">i</mi> <mi is="true">s</mi> <mi is="true">t</mi> <mi is="true">e</mi> <mi is="true">n</mi> <mi is="true">t</mi></mrow></msub></math>) as a final step of SCICERO’s validation. Highly supported triples (<math><msub is="true"><mrow is="true"><mi is="true">T</mi></mrow> <mrow is="true"><mi is="true">c</mi> <mi is="true">o</mi> <mi is="true">n</mi> <mi is="true">s</mi> <mi is="true">i</mi> <mi is="true">s</mi> <mi is="true">t</mi> <mi is="true">e</mi> <mi is="true">n</mi> <mi is="true">t</mi></mrow></msub></math>) are directly added to the KG.</td></tr><tr><td colspan="4"><strong>AI Assistance</strong></td></tr><tr><td><figure></figure></td><td>4</td><td></td><td>Balanced competence partitioning. Human validation for low-support triples (<math><msub is="true"><mrow is="true"><mi is="true">T</mi></mrow> <mrow is="true"><mi is="true">c</mi> <mi is="true">o</mi> <mi is="true">n</mi> <mi is="true">s</mi> <mi is="true">i</mi> <mi is="true">s</mi> <mi is="true">t</mi> <mi is="true">e</mi> <mi is="true">n</mi> <mi is="true">t</mi></mrow></msub></math>) and LLM validation of highly supported triples (<math><msub is="true"><mrow is="true"><mi is="true">T</mi></mrow> <mrow is="true"><mi is="true">c</mi> <mi is="true">o</mi> <mi is="true">n</mi> <mi is="true">s</mi> <mi is="true">i</mi> <mi is="true">s</mi> <mi is="true">t</mi> <mi is="true">e</mi> <mi is="true">n</mi> <mi is="true">t</mi></mrow></msub></math>).</td></tr><tr><td colspan="4"><strong>Human Verification</strong></td></tr><tr><td><figure></figure></td><td>5</td><td></td><td>Human validation triple correctness upon disagreement. LLM validation of <math><msub is="true"><mrow is="true"><mi is="true">T</mi></mrow> <mrow is="true"><mi is="true">t</mi> <mo is="true">−</mo> <mi is="true">d</mi> <mi is="true">i</mi> <mi is="true">s</mi> <mi is="true">c</mi> <mi is="true">a</mi> <mi is="true">r</mi> <mi is="true">d</mi> <mi is="true">e</mi> <mi is="true">d</mi></mrow></msub></math> and <math><msub is="true"><mrow is="true"><mi is="true">T</mi></mrow> <mrow is="true"><mi is="true">c</mi> <mi is="true">o</mi> <mi is="true">n</mi> <mi is="true">s</mi> <mi is="true">i</mi> <mi is="true">s</mi> <mi is="true">t</mi> <mi is="true">e</mi> <mi is="true">n</mi> <mi is="true">t</mi></mrow></msub></math> triples. Human validation whenever the LLM module disagrees with the original SCICERO validators.</td></tr><tr><td><figure></figure></td><td>6</td><td></td><td>Human validation upon triple removal disagreement. LLM validation of <math><msub is="true"><mrow is="true"><mi is="true">T</mi></mrow> <mrow is="true"><mi is="true">t</mi> <mo is="true">−</mo> <mi is="true">d</mi> <mi is="true">i</mi> <mi is="true">s</mi> <mi is="true">c</mi> <mi is="true">a</mi> <mi is="true">r</mi> <mi is="true">d</mi> <mi is="true">e</mi> <mi is="true">d</mi></mrow></msub></math>. Human validation whenever the LLM disagrees with the original SCICERO validators.</td></tr><tr><td colspan="4"><strong>Fully Automated</strong></td></tr><tr><td><figure></figure></td><td>7</td><td></td><td>LLM-based triples verification added to SCICERO’s validation stage. LLMs take the final judgment.</td></tr><tr><td><figure></figure></td><td>8</td><td></td><td>LLM-based triples verification after SCICERO’s original automated validation for <math><msub is="true"><mrow is="true"><mi is="true">T</mi></mrow> <mrow is="true"><mi is="true">c</mi> <mi is="true">o</mi> <mi is="true">n</mi> <mi is="true">s</mi> <mi is="true">i</mi> <mi is="true">s</mi> <mi is="true">t</mi> <mi is="true">e</mi> <mi is="true">n</mi> <mi is="true">t</mi></mrow></msub></math>.</td></tr><tr><td><figure></figure></td><td>9</td><td></td><td>LLM-based triples verification. Replacement of the SCICERO validation through an LLM validation.</td></tr></tbody></table>

### 4.1. Human judgment

We first explore possible positions of the human validator module within the SCICERO pipeline without involving an LLM. Since the original SCICERO pipeline already contains two automated validators, we consider several alternative configurations:

#### Human validation (workflow 1 in ).

For a completely manual annotation process without any tool-support the SCICERO pipeline needs to be modified. This involves replacing the entire SCICERO validation stage with a human validator module as illustrated in. While this workflow ensures full decision control by the human annotators, it is not a scalable solution for the validation of large resources such as CS-KG.

#### Human validation after SCICERO (workflow 2 in ).

An intuitive extension of SCICERO with human validation implies the positioning of the human validator module at the end of the SCICERO pipeline (see ). In this scenario, the automated transformer and ontology validators can be seen as filters that the human judges utilize in order to reduce the pool of triples that need to be verified. The ontology validator relies on expert-defined rules that apply to the domain, while the transformer validator can be adjusted with the desired triple support level. By placing the human validator at the end, humans retain full control of what is included in the final KG while automated tools support the removal of noisy triples. This workflow is particularly useful when the primary validation goal is to further enhance the precision of the resulting KG triples.

![](https://ars.els-cdn.com/content/image/1-s2.0-S030645732500086X-gr2.jpg)

Download: Download high-res image (148KB)

#### Partial human validation after SCICERO (workflow 3 in ).

While sending all triples to the human validator module ensures the highest level of human oversight, this solution does not scale well for large resources since the manual efforts are enormous. Thus, we also consider a version of this workflow, where the human validator is only involved for the annotation of selected triples. Specifically, human annotation is added only for triples with limited literature support (). Although not every triple is manually reviewed before it is added to the KG, human oversight can be ensured by the selection of an appropriate [reliability threshold](https://www.sciencedirect.com/topics/computer-science/reliability-threshold) for the transformer validator and establishing rules, to be followed by the ontology validator, with domain experts.

![](https://ars.els-cdn.com/content/image/1-s2.0-S030645732500086X-gr3.jpg)

Download: Download high-res image (191KB)

Following the task-partitioning idea from, workflow 3 can also be classified as an example of *AI assistance* since human judges take control over $T_{c o n s i s t e n t}$, while the automated validators takes care of $T_{r e l i a b l e}$. However, in this paper we focus on the interaction between the human validator and LLM validator modules and thus consider the interaction in the workflow as *human judgment*. Next, we propose an extension of workflow 3 more closely fitting the AI (LLM) assistance paradigm.

![](https://ars.els-cdn.com/content/image/1-s2.0-S030645732500086X-gr4.jpg)

Download: Download high-res image (195KB)

### 4.2. AI assistance

#### Balanced competence partitioning (workflow 4 in ).

Intuitively, LLMs are likely to be more capable at validating statements that often occur in literature because of the availability of a larger training dataset. In contrast, human judges might struggle reviewing statement extracted from numerous sources, especially if contradictory results are presented. Therefore, we propose a workflow where LLMs deal with triples linked to a higher amount of scientific texts (i.e., triples with high support), while human participants focus on triples for which only a few references are available (i.e., triples with low support). visualizes the capability-based task partitioning between the LLM validator (for $T_{r e l i a b l e}$) and the human validator (for $T_{c o n s i s t e n t}$) after the original SCICERO validation modules.

![](https://ars.els-cdn.com/content/image/1-s2.0-S030645732500086X-gr5.jpg)

Download: Download high-res image (221KB)

### 4.3. Human verification

A typical human verification workflow, where human participants judge the results of an automated approach, does not reduce the number of triples to be verified since all triples would be annotated both within the LLM validator module and the human validator module. Moreover, an over- or under-reliance on the LLM might affect the judgment capabilities of the human participants.

To address this issue, we adopt the “preference-testing” strategy from, and apply it to the triple validation task such that a human judge is involved only whenever a disagreement among automated validation modules occurs.

#### Human validation upon correctness disagreement (workflow 5 in ).

The original SCICERO evaluation revealed that 34% of the triples removed by the transformer validator were in fact correct triples. In contrast, 35% of $T_{c o n s i s t e n t}$ triples, added to the KG, were incorrect (). To address this, as shown in, an additional LLM validator module can be integrated to re-evaluate triples before their removal or addition to the KG. The disagreement paradigm can be employed whenever the LLM validator produces an output different from the original SCICERO validation modules. Following the intuition that triples verified as correct by several distinct automated approaches are likely to be correct, human participants can focus only on annotating triples where no conclusive decision could be established.

#### Human validation upon triple removal disagreement (workflow 6 in ).

The previously proposed workflow can be adopted based on the main KG validation goals to reduce the manual efforts. For instance, workflow 6 () follows the disagreement strategy only for the removal of triples and not for triple additions to the KG. Such an approach is especially useful whenever a higher KG coverage is desired. In comparison, for use cases with high KG precision requirements, such as those in the medical domain, the disagreement strategy might only be added for the addition of triples, to allow human participants to focus on removing misleading information.

![](https://ars.els-cdn.com/content/image/1-s2.0-S030645732500086X-gr6.jpg)

Download: Download high-res image (270KB)

![](https://ars.els-cdn.com/content/image/1-s2.0-S030645732500086X-gr7.jpg)

Download: Download high-res image (242KB)

### 4.4. Fully automated

We propose two integration approaches of the LLM module within the SCICERO framework.

#### SCICERO integration with the LLM validator (workflow 7 in ).

In this setup, the LLM validator is assumed to be better performing than the SCICERO automated validation and is therefore added as a last step of the workflow to ensure no noisy triples are included in the final KG. The transformer and ontology validators are utilized as filters reducing the LLM annotation costs, however, the final decision is taken by the LLM.

#### SCICERO with LLM validator approval for Tuncertain (workflow 8 in ).

An alternative workflow, exploiting the task-partitioning paradigm, is shown in. The LLM validator module is integrated before the removal of triples or addition of triples with lower scientific support (i.e, triples belonging to $T_{u n c e r t a i n}$). This workflow is the fully automated replication of workflow 5, however, instead of involving a HiL on disagreement, the annotation by the LLM is considered reliable and is used as the final decision.

![](https://ars.els-cdn.com/content/image/1-s2.0-S030645732500086X-gr8.jpg)

Download: Download high-res image (180KB)

#### Complete LLM validation (workflow 9 in ).

Building on related work in the field of LLMs (, ), we also propose a workflow in which the original SCICERO validation stage is entirely replaced by an LLM-based validator, as illustrated in. This workflow allows the investigation of the capabilities of LLMs as standalone annotators, compared to the performance achieved with the integration of the LLM within the SCICERO validation stage.

![](https://ars.els-cdn.com/content/image/1-s2.0-S030645732500086X-gr9.jpg)

Download: Download high-res image (230KB)

![](https://ars.els-cdn.com/content/image/1-s2.0-S030645732500086X-gr10.jpg)

Download: Download high-res image (168KB)

## 5\. Experiment design and implementation

To evaluate each of the nine SCICERO validation workflows described in Section, we designed two experiments that differ in the dataset used and the implementation of the validator modules. It is important to emphasize that this study does not aim to evaluate the HiL or LLM validation modules in isolation. Instead, our objective is to assess their integration within an existing KG generation pipeline and to analyze the benefits of incorporating both LLMs and HiL in the validation stage. Therefore, we do not assess these modules separately using standard triple classification benchmarks.

An overview of the experimental investigation is illustrated in. We first conducted a large-scale simulation (Experiment A) using the adopted workflows to validate $3 . 6 K$ triples. In this setting, the human validator module was simulated using the annotations of the original domain experts from the SCICERO evaluation (), who manually classified each triple as either true or false. Our objective was to evaluate these collaborative workflows based on (1) precision, recall, and F1 scores, and (2) scalability, by analyzing the required number of HiL and LLM annotations. In Experiment B, we validated the findings of Experiment A by implementing an actual human validator module, comprising a pool of recruited domain experts. Given the additional manual effort required, this experiment was conducted on a representative subset of 600 triples from the original dataset.

We introduce the used dataset in Section and describe the experimental setups of experiments A and B in Sections, respectively.

![](https://ars.els-cdn.com/content/image/1-s2.0-S030645732500086X-gr11.jpg)

Download: Download high-res image (383KB)

### 5.1. Experimental data

For the experimental investigations we make use of (1) CS-KG-3600: a gold standard created during the original SCICERO () evaluation, and (2) CS-KG-600: a subset of this gold standard allowing for testing of additional validation implementations.

#### CS-KG-3600.

For the SCICERO evaluation, a $3 . 6 K$ triples set was sampled from the generated CS-KG, including equal amounts (600) of triples from each of the following categories:

- •
	triples with very high support levels ($\in T_{r e l i a b l e}$)
- •
	triples with high support levels ($\in T_{r e l i a b l e}$)
- •
	triples with low support levels ($\in T_{c o n s i s t e n t}$)
- •
	triples labeled as incorrect by the transformer validator ($\in T_{t - d i s c a r d e d}$)
- •
	triples removed by the ontology validator ($\in T_{o - d i s c a r d e d}$)
- •
	randomly produced triples ($T_{r a n d o m}$) generated by replacing the head or [tail](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/tail) of CS-KG triples.

The triples were manually evaluated by 3 senior researchers in the Computer Science field and the annotations were aggregated using a majority [voting strategy](https://www.sciencedirect.com/topics/computer-science/voting-strategy) to determine the ground truth value for each triple. Further details are available in.

#### CS-KG-600.

We create a smaller representative dataset for exploration and findings validation purposes. CS-KG-600 is sampled from CS-KG-3600 and consists of 100 randomly selected triples from each of the six subsets contained within the gold standard.

Table 2. Overview of the LLMs employed for the experiment, their version, and the date of the conducted experiment.

| **Model** | **Version** | **Experiment Date** |
| --- | --- | --- |
| GPT-4o | gpt-4o-2024-05-13 | May 22nd, 2024 |
| Claude Sonnet | claude-3-5-sonnet-20241022 | Jan 31st, 2025 |
| Llama 3.3 70B | Llama-3.3-70B-Instruct | Feb 14, 2025 |

a

We utilized the model available on Hugging Fac’s platform accessible at [https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)

### 5.2. Experiment A: Large scale simulation on CS-KG-3600

In this section, we describe the implementation of each newly added validation module for the first experiment (left-hand side of ). This experiment was conducted on the full CS-KG-3600 gold standard.

#### LLM validator.

The LLM module is implemented as follows:

- •
	**Binary triple validation task.** Given a set of triples $T$, where each triple $t$ is represented as $t = \left(s u b j e c t , r e l a t i o n , o b j e c t\right)$, the goal is to classify each triple as true or false, formalized as $V \left(t\right) : T \rightarrow \left\{0 , 1\right\}$.
- •
	**Employed LLMs.** We employed three alternative LLMs in our experiment: GPT-4o, Claude Sonnet, and Llama 3.3. These models are among the highest-performing in the field and have each demonstrated superior performance across a wide range of tasks in previous studies. In particular, the GPT family has demonstrated excellent performance in class membership relation validation (). Similarly, GPT-4o and Claude Sonnet have achieved expert-level ontology axiom validations, exceeding the results of open source models ().
	Additionally, we aimed to include an open model to accommodate scenarios where deploying a local solution is essential for validating private resources. While privacy concerns were not a factor in this study, since CS-KG exclusively extracts information from publicly available scholarly publications, we acknowledge that on-premise LLMs may be necessary in other applications. Since recent studies have shown that Llama 3 70B outperforms other open models in triple consistency validation (), we select its successor – Llama 3.3 – as on open source model for our experiments.
	outlines the specific versions of the models employed in our study, along with the corresponding dates on which each experiment was performed.
- •
	**LLM prompting.** shows the initial instructions sent to the LLM model, introducing the annotation task and specifying the expected format of the response. Initial investigation revealed that requesting only the triple id and a binary judgment often resulted in incomplete or excessive judgments, which was addressed by requiring the complete triples to be included in the response.
	After the behavior of the LLM is defined, batches of 100 triples without any additional contextual information are sent for validation. In cases where the response did not match the required response format, the annotation was ignored and the same batch was sent again. To mimic a typical crowdsourcing experiment, we used the model’s [default parameters](https://www.sciencedirect.com/topics/computer-science/default-parameter) settings (e.g., temperature) and sent each batch of triples three consecutive times. The final judgment for each triple was determined using a majority vote aggregation of all responses.

#### Human validator.

Because of the large size of the dataset ($3 . 6 K$ triples), to reduce the annotation efforts of the experiment, we simulate human-in-the-loop validations for the complete dataset by leveraging the original expert annotations used to create the gold standard. For each triple $t$, the gold standard dataset contains three binary expert annotations and the aggregated final ground truth value $A_{t} = \left\{a_{1} , a_{2} , a_{3} , a_{g t}\right\}$, $a_{i} \in \left\{0 , 1\right\}$. For each triple $t$ we select a single random [expert judgment](https://www.sciencedirect.com/topics/computer-science/expert-judgment) $a_{r} \in \left\{a_{1} , a_{2} , a_{3}\right\}$ to allow the reusability of the previously established gold standard while limiting biases introduced by the usage of the gold standard within the validation stage. Within the evaluation of the proposed SCICERO workflows, the selected random annotation $a_{r}$ is compared against the ground truth value $a_{g t}$.

![](https://ars.els-cdn.com/content/image/1-s2.0-S030645732500086X-gr12.jpg)

Download: Download high-res image (316KB)

### 5.3. Experiment B: Real-life validation of CS-KG-600

The second experiment (right hand-side of ) focuses on a realistic implementation of the human validator module. We perform the experiment on the subset CS-KG-600 to reduce additional manual annotation efforts.

#### LLM validator.

For the LLM validator implementation we reuse the produced LLM annotations previously described in Section. Since CS-KG-600 is sampled from CS-KG-3600, no additional LLM annotation had to be carried out.

#### Human validator.

- •
	**Binary triple validation task.** Given a set of triples $T$, where each triple $t$ is represented as $t = \left(s u b j e c t , r e l a t i o n , o b j e c t\right)$, and triple context $C_{t} = \left(s u b j e c t _ t y p e , o b j e c t _ t y p e , f i l e _ i d s\right)$, containing the types of the subject and object nodes as well the identifiers of the files where the triples were extracted from. The goal is to classify each triple as true or false, formalized as $V \left(t , C t\right) : T \rightarrow \left\{0 , 1\right\}$.
- •
	**Sample size.** To minimize the annotation efforts, only triples which are sent to the human validator module in one of the workflows 2–9 are annotated. In total, 333 triples were reviewed.
- •
	**Annotators background.** The annotators were four advanced PhD researchers with Computer Science (or equivalent) background, who did not have any involvement in the creation of CS-KG, SCICERO or the initial gold standard creation. They were asked to judge whether a triple is correct or incorrect according to their expertise and support in scientific literature.
- •
	**Annotation environment.** The annotations were performed using Google Sheets, where each triple was presented in natural language, displaying the subject, object, and relation, along with the types of the subject and object. During the annotation process, participants had access to the files associated with the articles from which each triple was extracted and could use digital libraries such as Scopus to browse through additional scientific content in order to provide an informed decision.
	Example triples provided to the annotators with contextual information are shown in. The first columns represent the triple elements. Let us consider the validation of the triple $<$ [natural language processing](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/natural-language-processing)*, uses, word segmentation* $>$ as an example. As contextual information, the annotators are provided with the knowledge that both *natural language processing* and *word segmentation* are classified as Task. Additionally, they are given the identifiers of three files from which the triple was extracted. To access the original papers, they were instructed to use OpenAlex. For instance, the file identified as **2110300018** can be accessed at [https://openalex.org/works/w2110300018](https://openalex.org/works/w2110300018).
- •
	**Annotation strategy.** Each triple was first annotated by a single expert. In cases where the expert had doubts about the correctness of a triple, a second expert was asked for a judgment. If the annotations were inconclusive, a discussion among the two experts took place and if no agreement could be reached, a third expert was involved and the final decision was reached through majority vote. Each annotator worked at their own pace, and, following the necessary discussions, the final annotations were completed within a week.

Table 3. Example triples and the provided context in the format presented to the annotators.

<table><thead><tr><th rowspan="1"><strong>Subject</strong></th><th rowspan="1"><strong>Relation</strong></th><th rowspan="1"><strong>Object</strong></th><th><strong>Subject</strong><br><strong>type</strong></th><th><strong>Object</strong><br><strong>type</strong></th><th rowspan="1"><strong>Files</strong></th></tr></thead><tbody><tr><th>natural<br>language<br>processing</th><td rowspan="1">uses</td><td rowspan="1">word<br>segmentation</td><td rowspan="1">Task</td><td rowspan="1">Task</td><td>2110300018,<br>158142204,<br>2146654604</td></tr><tr><th>information<br>integration</th><td rowspan="1">acquires</td><td>patient<br>address</td><td rowspan="1">Task</td><td>Other<br>Entity</td><td rowspan="1">2849896015</td></tr><tr><th>semantic<br>profile<br>representation</th><td rowspan="1">acquires</td><td rowspan="1">document<br>classification</td><td rowspan="1">Method</td><td rowspan="1">Task</td><td rowspan="1">2039759410</td></tr></tbody></table>

## 6\. Results

In this section, we present the results achieved with the nine validation workflows in each of the conducted experiments.

### 6.1. Experiment A - Results of the large scale simulation on CS-KG-3600

For the first experiment, we utilized the SCICERO complete gold standard to simulate the proposed extended SCICERO workflows and implemented the human validator module such that a random expert annotation from the ground truth is used within the workflows. shows an overview of the workflow performance in terms of precision, recall and F1 scores as well as additional efforts added to SCICERO, i.e., the amount of triples to undergo an LLM ($N_{L L M}$) or human ($N_{H u m a n}$) validation. The scores are color-coded for an easy overview of the improvements (in green) and losses (in red), introduced by each workflow with respect to the original SCICERO performance on the datasets. We discuss our results along the four categories of workflows from *Human Judgment* to *Full Automation*.

Notably, the *human judgment* workflows offer precision improvements of 8%–18% with possible recall losses (up to 8%). While the F1 improvements are prominent for this workflow type, the number of triples to be manually evaluated, especially for workflows 1 and 2, are considerably high ($\geq 1 . 8 K$) and as such, these workflows are only suitable for small-size resources. For workflow 3, the amount of manual annotations was significantly reduced by leveraging the capabilities of the SCICERO validators to filter reliable triples. While the precision is lowest compared to other workflows of this type, the F1 score is still increased to 80%, similarly to workflow 2 (81%), in which three times more triples are annotated.

Table 4. Experiment A results on the CS-KG-3600 dataset in terms of precision (P), recall (R), F1 scores and additional resource efforts provided as $N_{L L M}$ and $N_{H u m a n}$. The best score for each workflow across LLMs is shown in **bold** and the best scores per workflow type are underlined.

![](https://ars.els-cdn.com/content/image/1-s2.0-S030645732500086X-fx1001.jpg)

In the *AI assistance* category, workflow 4, which extended the workflow 3 manual validation with an additional LLM validator module, further improves the precision to 90% (＋15% from the SCICERO baseline) when the GPT-4o model is used. Nevertheless, the loss in recall (−13%) results in a small F1 score decrease (−1%). As such, this workflow is suitable for evaluation campaigns where a high precision of the KG is required, while the KG coverage is not a main priority.

The workflows from the *human verification* interaction-level type lead to score improvements in all performance scores while keeping the human annotations to a minimum ($< 13 \%$ of the total triples). Workflow 5 improves the precision by up to 5% by utilizing GPT-4o while workflow 6 reaches up to 8% recall increase when using Claude Sonnet.

The *fully automated* workflows showcase the capabilities of the LLM validator module. Workflow 7 and 8 manage to increase the precision by 3%–12% with no additional manual efforts when using GPT-4o. Workflow 9, which relies solely on LLM-based validation, is the only workflow that leads to an overall decrease in precision and F1 scores. This outcome highlights the crucial role of integrating LLMs with other automated approaches to enhance performance.

The experiment highlighted the strengths and limitations of different automation levels that integrate LLMs with human-in-the-loop approaches. While *human-judgment* workflows yield the most significant improvements over the original SCICERO pipeline, they are labor-intensive and poorly suited for evaluating large-scale knowledge graphs. At the other end of the spectrum, the workflows based on *full automation* exhibited the highest scalability, albeit at the cost of some performance. In contrast, *AI Assistance* workflows can partially address scalability challenges and enhance precision but suffer from low recall. The *human-verification* approach seems to offer the best trade-off between performance and manual effort, as it effectively improves overall results while minimizing human intervention.

### 6.2. Experiment B - Results of the real-life validation of CS-KG-600

For the second experiment, we utilized CS-KG-600, a subset of the SCICERO gold standard, and conducted an additional human-in-the-loop annotation campaign. provides a overview of the performance achieved by the various workflows.

Similarly to Experiment A, the *human judgment* workflows increase the precision results compared to the SCICERO baseline (+ 4%–8%). However, in contrast to the results from Experiment A, the added benefit is not as high and the losses in recall and F1 score are significant (up to −35%). Performance decreases were expected since in Experiment A the ground truth was used within the simulated workflows. These results can further be explained by the domain expertise level of the involved human participants (senior vs junior experts). However, further investigations are needed to explore other factors, which may have influenced the scores.

Table 5. Experiment B results on the CS-KG-600 dataset in terms of precision (P), recall (R), F1 scores and additional resource efforts provided as $N_{L L M}$ and $N_{H u m a n}$. The best score for each workflow across LLMs is shown in **bold** and the best scores per workflow type are underlined. Scores marked with a star ($*$) are estimated based on a subset annotation.

![](https://ars.els-cdn.com/content/image/1-s2.0-S030645732500086X-fx1002.jpg)

It should be noted that because of the high manual efforts in the validation following workflow 1, we do not test this entire workflow in Experiment B. The values in are estimations based on the annotations performed for the remaining workflows (56% of the CS-KG-600 dataset).

Surprisingly, the *fully automated* and *AI-assisted* workflows result in a higher increase in precision (+ 5%–12% when using GPT-4o), compared to the performance obtained using human judgment. As with the previous experiment, there is a trade-off with the recall scores which decrease by up to 20%. An exception is the implementation of workflow 8 with the Claude Sonnet model, which leads to overall improved performance scores. However, these effects are not consistently observed across models, and further investigation is needed to determine whether similar performance can be reliably replicated.

*Human verification* workflows, as in Experiment A, lead to balanced [performance improvements](https://www.sciencedirect.com/topics/computer-science/performance-improvement) across all tested LLMs. The increase is rather small (＋4% precision in workflow 4; +3% recall in workflow 5). However, it is noteworthy that these gains come without any trade-offs in other performance metrics.

The optimal workflow should be selected based on the main evaluation objective and the available resources. As demonstrated in our experiments, precision scores can be enhanced both with and without additional manual intervention. While fully manual or fully automated workflows inherently involve a trade-off between precision and recall, human-in-the-loop verification strategies effectively improve overall performance while minimizing manual effort.

## 7\. Conclusion

The automated generation of knowledge graphs enables extensive content coverage of the represented domains. However, such automatically curated resources often contain quality issues. To ensure the quality of the generated KGs and the success of the applications relying on them, validation is a crucial step in the generation process. This paper explores innovative validation approaches for knowledge graphs that combine human-in-the-loop techniques with LLMs. Specifically, we investigate potential workflows that integrate LLMs and human contributors at varying levels of automation (RQ1) and evaluate their strengths and limitations (RQ2) in terms of both performance metrics (precision, recall, and F1 score) and scalability.

We validate the Computer Science Knowledge Graph (CS-KG) as a use case. CS-KG is a valuable resource that integrates scientific claims from millions of publications, facilitating the analysis of research trends and supporting various [scientometric](https://www.sciencedirect.com/topics/social-sciences/scientometrics) tasks (). Thus, it is fundamental to ensure the quality of the knowledge graph by removing misleading or incorrectly extracted statements. To this end, we extend SCICERO – the pipeline used to produce CS-KG – by integrating LLMs and HiL within its validation stage.

This section presents a summary of the key contributions and findings of our research. Additionally, we discuss the limitations, propose directions for future research, and outline open issues and remaining challenges.

### Contributions.

We extend SCICERO by integrating additional LLMs and human-based validator modules and make the following contributions to the field:

- •
	**Human-LLM collaboration investigation.** We present an overview of possible SCICERO extensions, incorporating LLMs and/or human-in-the-loop validation techniques. We explore a spectrum of collaboration levels, raging from fully manual human judgments and AI-assisted annotations to human verification and full automation. This results in nine different workflows combining HiL and LLMs.
- •
	**LLM-based KG validation.** We propose a concrete implementation of an LLM-sourced KG triple annotation and asses the achieved validation performance of three LLMs.
- •
	**Experimental evaluation.** We conduct two experimental investigations using the SCICERO gold standard, consisting of $3 . 6 K$ triples, to empirically evaluate the strength and limitations of each of the nine proposed collaborative validation workflows. As such, we empirically shed light on the trade-offs of various human-LLM combination possibilities. To the best of our knowledge, we pioneer the empirical exploration of the trade-offs of such hybrid workflows on large-scale datasets for the task of KG validation.
- •
	**Annotation collection.** We publish the collected annotations produced in the LLM and HiL validation modules online to allow the reproducibility of our work as well as the exploration of further workflows and in-depth experiments by fellow researchers.

### Main findings.

Our experimental investigation yields the following key insights, relevant to the community:

- •
	**Weak performance of standalone LLM validation.** LLMs, when used independently, fail to deliver highly accurate KG triple validations (up to 70% precision, workflow 9). However, when combined with other automated validation methods, as in workflows 7 & 8, precision improves significantly, reaching up to 87%.
- •
	**Human-level validation by integrated LLMs.** The integration of LLMs into the SCICERO pipeline produces results comparable to, and in some cases better than, SCICERO workflows, including a human-in-the-loop. Concretely, in Experiment B, workflow 7 achieves 85% precision and outperforms the human judgment workflows by 4%–8%.
- •
	**Superior hybrid human-LLM collaboration.** The integration of LLMs and human annotators successfully balances precision and recall, overcoming trade-off limitations observed in workflows that rely solely on either human expertise or LLM-sourced annotations. These improvements are shown by workflows 5 & 6 in both experimental setups across tested LLMs.
- •
	**LLM disagreement strategy for HiL involvement.** A promising method for reducing human intervention is the disagreement strategy employed by workflows 5 & 6: when two automated validators produce inconsistent annotations, human contributors can resolve the conflict. If both automated methods agree, their validation can be considered reliable and manual checks can be avoided.

### Limitations and outlook.

Despite the valuable insights gained in this study, several limitations and challenges remain:

- •
	**Single use case.** This study focuses on a single KG generation pipeline –SCICERO– to enable a detailed and in-depth analysis of a concrete use case. Since several components of SCICERO are specifically designed for the Computer Science domain, the implementation developed for this study cannot be directly applied to other domains. However, the theoretical framework explored in this study, along with the nine workflows, was designed to be domain-independent and can be readily implemented in various fields with minimal or no modifications. Similarly, the insights gained from our study can inform the development of novel systems that integrate HiL approaches and LLMs. Furthermore, even the specific framework modeled on CS-KG can be adapted to other domains by adjusting the extraction components and incorporating a relevant [domain ontology](https://www.sciencedirect.com/topics/computer-science/domain-ontology). Nevertheless, such adaptations require additional domain expertise and evaluation efforts, which fall beyond the scope of this study. To further validate and generalize our findings, we plan to conduct a series of follow-up experiments to assess the adaptability of the proposed workflows across different domains and KG generation solutions.
- •
	**Further SCICERO integration.** Future work will involve scaling up the evaluation by applying the validation pipelines to a larger subset of CS-KG to further validate the findings of this study. Moreover, we intend to utilize the extended SCICERO pipelines to generate different versions of CS-KG, allowing for a [cross validation](https://www.sciencedirect.com/topics/social-sciences/cross-validation) and analysis of tasks enabled by the KG such as forecasting of research dynamics.
- •
	**LLM (prompt) variability.** While our implementation, which utilized three different LLMs, produces human-level annotations, further studies are necessary to assess the impact of prompt modifications and model selection on overall performance. Future work could explore workflows that integrate retrieval-augmented generation (RAG) and evaluate how relevant contextual information impacts performance.
- •
	**Scalability.** Although the hybrid human-LLM SCICERO extensions reduce manual efforts significantly, scalability remains a challenge for large resources containing millions of triples. Further investigations will explore ways to extend SCICERO with other strategies such as triple annotation priority to prevent bottlenecks while maintaining high validation quality. We also plan to investigate an experimental setup that integrates multiple SCICERO workflows. This approach would enable dynamic selection of the most suitable workflow based on real-time assessments of both human and LLM [resource availability](https://www.sciencedirect.com/topics/computer-science/resource-availability).
- •
	**Evaluating LLM annotations.** In this paper, LLM annotations have solely been compared against human-generated annotations. However, our experiments indicate that LLMs can outperform junior experts. Further research is needed to re-evaluate current ground truth creation methods and explore new measurements to detect cases when LLMs exceed human expertise.

Validating semantic resources using LLMs is a complex challenge. In this work, we contribute to the field by proposing and evaluating various workflows that incorporate HiL methods, LLMs, or a combination of both, applied to a large-scale resource. Our findings underscore the strengths and limitations of each approach, demonstrating the potential of LLMs as a valuable complement for generating high-quality knowledge graphs at scale. Additionally, our insights into hybrid workflows integrating HiL and LLMs are relevant to researchers working on other knowledge-intensive tasks beyond KG validation.

## CRediT authorship contribution statement

**Stefani Tsaneva:** Writing – review & editing, Writing – original draft, Visualization, Validation, Project administration, Methodology, Investigation, Formal analysis, [Data curation](https://www.sciencedirect.com/topics/computer-science/data-curation), Conceptualization. **Danilo Dessì:** Writing – review & editing, Data curation, Conceptualization. **Francesco Osborne:** Writing – review & editing, Data curation, Conceptualization. **Marta Sabou:** Writing – review & editing, Supervision, Project administration, Funding acquisition, Conceptualization.

## Declaration of Generative AI and AI-assisted technologies in the writing process

During the preparation of this work the authors used ChatGPT4 in order to suggest improvements to the [readability](https://www.sciencedirect.com/topics/agricultural-and-biological-sciences/readability) and language of the manuscript. After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

We thank all data annotators for their involvement and contributions.

This research was funded in whole or in part by the Austrian Science Fund (FWF) [BILAI](https://www.bilateral-ai.net/) () and HOnEst (V 745) projects. For open access purposes, the author has applied a CC BY public copyright license to any author accepted manuscript version arising from this submission. Additionally, the work was supported by the [PERKS](https://perks-project.eu/) (101120323) project, co-funded by the European Union. Views and opinions expressed are, however, those of the authors only and do not necessarily reflect those of the European Union. Neither the European Union nor the granting authority can be held responsible for them.

## Data availability

The SCICERO gold standard and collected annotations from the experiments are available at [https://github.com/danilo-dessi/SKG-pipeline/blob/main/eval/](https://github.com/danilo-dessi/SKG-pipeline/blob/main/eval/) and [https://doi.org/10.5281/zenodo.13730203](https://doi.org/10.5281/zenodo.13730203).

## References

These authors contributed equally.

Wine Ontology - [https://www.w3.org/TR/owl-guide/wine.rdf](https://www.w3.org/TR/owl-guide/wine.rdf).

Pizza Ontology - [https://protege.stanford.edu/ontologies/pizza/pizza.owl](https://protege.stanford.edu/ontologies/pizza/pizza.owl).

Computer Science Ontology - [https://scholkg.kmi.open.ac.uk/cskg/ontology](https://scholkg.kmi.open.ac.uk/cskg/ontology).

The gold standard is available under [https://github.com/danilo-dessi/SKG-pipeline/tree/main/eval](https://github.com/danilo-dessi/SKG-pipeline/tree/main/eval).

[^1]

GPT-4o - [https://openai.com/index/gpt-4o-system-card](https://openai.com/index/gpt-4o-system-card).

Claude Sonnet - [https://www.anthropic.com/news/claude-3-5-sonnet](https://www.anthropic.com/news/claude-3-5-sonnet).

Llama 3.3 - [https://www.llama.com/docs/model-cards-and-prompt-formats/llama3\_3](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_3).

[^2]

Scopus - [https://www.scopus.com/](https://www.scopus.com/).

OpenAlex - [https://openalex.org/](https://openalex.org/).

[^3]

Knowledge Graph Triple Validation by LLMs and Human-in-the-Loop \[Data set\]. Zenodo. [https://doi.org/10.5281/zenodo.13730203](https://doi.org/10.5281/zenodo.13730203).

[^1]: •

**Employed LLMs.** We employed three alternative LLMs in our experiment: GPT-4o, Claude Sonnet, and Llama 3.3. These models are among the highest-performing in the field and have each demonstrated superior performance across a wide range of tasks in previous studies. In particular, the GPT family has demonstrated excellent performance in class membership relation validation (). Similarly, GPT-4o and Claude Sonnet have achieved expert-level ontology axiom validations, exceeding the results of open source models ().

Additionally, we aimed to include an open model to accommodate scenarios where deploying a local solution is essential for validating private resources. While privacy concerns were not a factor in this study, since CS-KG exclusively extracts information from publicly available scholarly publications, we acknowledge that on-premise LLMs may be necessary in other applications. Since recent studies have shown that Llama 3 70B outperforms other open models in triple consistency validation (), we select its successor – Llama 3.3 – as on open source model for our experiments.

outlines the specific versions of the models employed in our study, along with the corresponding dates on which each experiment was performed.

[^undefined]: •

**LLM prompting.** shows the initial instructions sent to the LLM model, introducing the annotation task and specifying the expected format of the response. Initial investigation revealed that requesting only the triple id and a binary judgment often resulted in incomplete or excessive judgments, which was addressed by requiring the complete triples to be included in the response.

After the behavior of the LLM is defined, batches of 100 triples without any additional contextual information are sent for validation. In cases where the response did not match the required response format, the annotation was ignored and the same batch was sent again. To mimic a typical crowdsourcing experiment, we used the model’s [default parameters](https://www.sciencedirect.com/topics/computer-science/default-parameter) settings (e.g., temperature) and sent each batch of triples three consecutive times. The final judgment for each triple was determined using a majority vote aggregation of all responses.

[^undefined]: ↩

[^2]: •

**Annotation environment.** The annotations were performed using Google Sheets, where each triple was presented in natural language, displaying the subject, object, and relation, along with the types of the subject and object. During the annotation process, participants had access to the files associated with the articles from which each triple was extracted and could use digital libraries such as Scopus to browse through additional scientific content in order to provide an informed decision.

Example triples provided to the annotators with contextual information are shown in. The first columns represent the triple elements. Let us consider the validation of the triple $<$ [natural language processing](https://www.sciencedirect.com/topics/earth-and-planetary-sciences/natural-language-processing)*, uses, word segmentation* $>$ as an example. As contextual information, the annotators are provided with the knowledge that both *natural language processing* and *word segmentation* are classified as Task. Additionally, they are given the identifiers of three files from which the triple was extracted. To access the original papers, they were instructed to use OpenAlex. For instance, the file identified as **2110300018** can be accessed at [https://openalex.org/works/w2110300018](https://openalex.org/works/w2110300018).

[^undefined]: •

**Annotation strategy.** Each triple was first annotated by a single expert. In cases where the expert had doubts about the correctness of a triple, a second expert was asked for a judgment. If the annotations were inconclusive, a discussion among the two experts took place and if no agreement could be reached, a third expert was involved and the final decision was reached through majority vote. Each annotator worked at their own pace, and, following the necessary discussions, the final annotations were completed within a week.

[^undefined]: ↩

[^3]: •

**Annotation collection.** We publish the collected annotations produced in the LLM and HiL validation modules online to allow the reproducibility of our work as well as the exploration of further workflows and in-depth experiments by fellow researchers.