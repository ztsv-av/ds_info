# The Unified Process

The Unified Process is a specific methodology that maps out when and how to use the various Unified Modeling Language (UML) techniques for object‐oriented analysis and design. The primary contributors were Grady Booch, Ivar Jacobson, and James Rumbaugh. Whereas the UML provides structural support for developing the structure and behavior of an information system, the Unified Process provides the behavioral support. The Unified Process, of course, is use‐case driven, architecture‐centric, and iterative and incremental. Furthermore, the Unified Process is a two‐dimensional systems development process described by a set of phases and workflows. The phases are inception, elaboration, construction, and transition. The workflows include business modeling, requirements, analysis, design, implementation, test, deployment, configuration and change management, project management, and environment.23 Figure 1‐3 depicts the Unified Process.

## Phases

The phases of the Unified Process support an analyst in developing information systems in an iterative and incremental manner. The phases describe how an information system evolves through time. Depending on which development phase the evolving system is currently in, the level of activity varies over the workflows. The curve in Figure 1‐3 associated with each workflow approximates the amount of activity that takes place during the specific phase. For example, the inception phase primarily involves the business modeling and requirements workflows, while practically ignoring the test and deployment workflows. Each phase contains a set of iterations, and each iteration uses the various workflows to create an incremental version of the evolving system. As the system evolves through the phases, it improves and becomes more complete. Each phase has objectives, a focus of activity over the workflows, and incremental deliverables. Each of the phases is described next.

### Inception

In many ways, the inception phase is very similar to the planning phase of a traditional SDLC approach. In this phase, a business case is made for the proposed system. This includes feasibility analysis that should answer questions such as the following:

- Do we have the technical capability to build it (technical feasibility)?
- If we build it, will it provide business value (economic feasibility)?
- If we build it, will it be used by the organization (organizational feasibility)?

![image](https://user-images.githubusercontent.com/73081144/176343475-1d5a4308-c957-4194-baee-2713a1b2fa16.png)

To answer these questions, the development team performs work related primarily to the business modeling, requirements, and analysis workflows. In some cases, depending on the technical difficulties that could be encountered during the development of the system, a throwaway prototype is developed. This implies that the design, implementation, and test workflows could also be involved. The project management and environment supporting workflows are very relevant to this phase. The primary deliverables from the inception phase are a vision document that sets the scope of the project; identifies the primary requirements and constraints; sets up an initial project plan; and describes the feasibility of and risks associated with the project, the adoption of the necessary environment to develop the system, and some aspects of the problem domain classes being implemented and tested.

### Elaboration

When we typically think about object‐oriented systems analysis and design, the activities related to the elaboration phase of the Unified Process are the most relevant. The analysis and design workflows are the primary focus during this phase. The elaboration phase continues with developing the vision document, including finalizing the business case, revising the risk assessment, and completing a project plan in sufficient detail to allow the stakeholders to be able to agree with constructing the actual final system. It deals with gathering the requirements, building the UML structural and behavioral models of the problem domain, and detailing how the problem domain models fit into the evolving system architecture. Developers are involved with all but the deployment engineering workflow in this phase. As the developers iterate over the workflows, the importance of addressing configuration and change management becomes apparent. Also, the development tools acquired during the inception phase become critical to the success of the project during this phase.24 The primary deliverables of this phase include the UML structure and behavior diagrams and an executable of a baseline version of the evolving information system. The baseline version serves as the foundation for all later iterations. By providing a solid foundation at this point, the developers have a basis for completing the system in the construction and transition phases.

### Construction

The construction phase focuses heavily on programming the evolving information system. This phase is primarily concerned with the implementation workflow. However, the requirements workflow and the analysis and design workflows also are involved with this phase. It is during this phase that missing requirements are identified and the analysis and design models are finally completed. Typically, there are iterations of the workflows during this phase, and during the last iteration, the deployment workflow kicks into high gear. The configuration and change management workflow, with its version‐control activities, becomes extremely important during the construction phase. At times, an iteration has to be rolled back. Without good version controls, rolling back to a previous version (incremental implementation) of the system is nearly impossible. The primary deliverable of this phase is an implementation of the system that can be released for beta and acceptance testing.

### Transition

Like the construction phase, the transition phase addresses aspects typically associated with the implementation phase of a traditional SDLC approach. Its primary focus is on the testing and deployment workflows. Essentially, the business modeling, requirements, and analysis workflows should have been completed in earlier iterations of the evolving information system. Furthermore, the testing workflow should have been executed during the earlier phases of the evolving system. Depending on the results from the testing workflow, some redesign and programming activities on the design and implementation workflows could be 

## Workflows

The workflows describe the tasks or activities that a developer performs to evolve an information system over time. The workflows of the Unified Process are grouped into two broad categories: engineering and supporting.

### Engineering Workflows

Engineering workflows include business‐modeling, requirements, analysis, design, implementation, test, and deployment workflows. The engineering workflows deal with the activities that produce the technical product (i.e., the information system).

#### Business Modeling Workflow

The business modeling workflow uncovers problems and identifies potential projects within a user organization. This workflow aids management in understanding the scope of the projects that can improve the efficiency and effectiveness of a user organization. The primary purpose of business modeling is to ensure that both developer and user organizations understand where and how the to‐be‐developed information system fits into the business processes of the user organization. This workflow is primarily executed during the inception phase to ensure that we develop information systems that make business sense. The activities that take place on this workflow are most closely associated with the planning phase of the traditional SDLC; however, requirements gathering, and use‐case and business process modeling techniques also help us to understand the business situation.

#### Requirements Workflow

In the Unified Process, the requirements workflow includes eliciting both functional and nonfunctional requirements. Typically, requirements are gathered from project stakeholders, such as end users, managers within the end user organization, and even customers. The requirements workflow is used the most during the inception and elaboration phases. The identified requirements are very helpful for developing the vision document and the use cases used throughout the development process. Additional requirements tend to be discovered throughout the development process. In fact, only the transition phase tends to have few, if any, additional requirements identified.

#### Analysis Workflow

The analysis workflow primarily addresses the creation of an analysis model of the problem domain. In the Unified Process, the analyst begins designing the architecture associated with the problem domain; using the UML, the analyst creates structural and behavior diagrams that depict a description of the problem domain classes and their interactions. The primary purpose of the analysis workflow is to ensure that both the developer and user organizations understand the underlying problem and its domain without overanalyzing. If they are not careful, analysts can create analysis paralysis, which occurs when the project becomes so bogged down with analysis that the system is never actually designed or implemented. A second purpose of the analysis workflow is to identify useful reusable classes for class libraries. By reusing predefined classes, the analyst can avoid reinventing the wheel when creating the structural and behavior diagrams. The analysis workflow is predominantly associated with the elaboration phase, but like the requirements workflow, it is possible that additional analysis will be required throughout the development process.

#### Design Workflow

The design workflow transitions the analysis model into a form that can be used to implement the system: the design model. Whereas the analysis workflow concentrates on understanding the problem domain, the design workflow focuses on developing a solution that will execute in a specific environment. Basically, the design workflow simply enhances the description of the evolving system by adding classes that address the environment of the system to the evolving analysis model. The design workflow uses activities such as detailed problem domain class design, optimization of the evolving information system, database design, user‐interface design, and physical architecture design. The design workflow is associated primarily with the elaboration and construction phases of the Unified Process.

#### Implementation Workflow

The primary purpose of the implementation workflow is to create an executable solution based on the design model (i.e., programming). This includes not only writing new classes but also incorporating reusable classes from executable class libraries into the evolving solution. As with any programming activity, the new classes and their interactions with the incorporated reusable classes must be tested. Finally, in the case of multiple groups performing the implementation of the information system, the implementers also must integrate the separate, individually tested modules to create an executable version of the system. The implementation workflow is associated primarily with the elaboration and construction phases.

#### Testing Workflow

The primary purpose of the testing workflow is to increase the quality of the evolving system. Testing goes beyond the simple unit testing associated with the implementation workflow. In this case, testing also includes testing the integration of all modules used to implement the system, user acceptance testing, and the actual alpha testing of the software. Practically speaking, testing should go on throughout the development of the system; testing of the analysis and design models occurs during the elaboration and construction phases, whereas implementation testing is performed primarily during the construction and, to some degree, transition phases. Basically, at the end of each iteration during the development of the information system, some type of testing should be performed.

#### Deployment Workflow

The deployment workflow is most associated with the transition phase of the Unified Process. The deployment workflow includes activities such as software packaging, distribution, installation, and beta testing. When actually deploying the new system into a user organization, the developers might have to convert the current data, interface the new software with the existing software, and train the end user to use the new system.

### Supporting Workflows

The supporting workflows include the project management, configuration and change management, and environment workflows. The supporting workflows focus on the managerial aspects of information systems development.

#### Project Management Workflow

Whereas the other workflows associated with the Unified Process are technically active during all four phases, the project management workflow is the only truly cross‐phase workflow. The development process supports incremental and iterative development, so information systems tend to grow or evolve over time. At the end of each iteration, a new incremental version of the system is ready for delivery. The project management workflow is quite important owing to the complexity of the two‐dimensional development model of the Unified Process (workflows and phases). This workflow's activities include identifying and managing risks, managing scope, estimating the time to complete each iteration and the entire project, estimating the cost of the individual iteration and the whole project, and tracking the progress being made toward the final version of the evolving information system.

#### Configuration and Change Management Workflow

The primary purpose of the configuration and change management workflow is to keep track of the state of the evolving system. In a nutshell, the evolving information system comprises a set of artifacts (e.g., diagrams, source code, and executables). During the development process, these artifacts are modified. A substantial amount of work—and, hence, money—is involved in developing the artifacts. The artifacts themselves should be handled as any expensive asset would be handled—access controls must be put into place to safeguard the artifacts from being stolen or destroyed. Furthermore, because the artifacts are modified on a regular, if not continuous, basis, good version control mechanisms should be established. Finally, a good deal of project management information needs to be captured (e.g., author, time, and location of each modification). The configuration and change management workflow is associated mostly with the construction and transition phases.

#### Environment Workflow

During the development of an information system, the development team needs to use different tools and processes. The environment workflow addresses these needs. For example, a CASE tool that supports the development of an object‐oriented information system via the UML could be required. Other tools necessary include programming environments, project management tools, and configuration management tools. The environment workflow involves acquiring and installing these tools. Even though this workflow can be active during all of the phases of the Unified Process, it should be involved primarily with the inception phase.

## Extensions to the Unified Process

As large and as complex as the Unified Process is, many authors have pointed out a set of critical weaknesses. First, the Unified Process does not address staffing, budgeting, or contract management issues. These activities were explicitly left out of the Unified Process. Second, the Unified Process does not address issues relating to maintenance, operations, or support of the product once it has been delivered. Thus, it is not a complete software process; it is only a development process. Third, the Unified Process does not address cross‐ or inter‐project issues. Considering the importance of reuse in object‐oriented systems development and the fact that in many organizations employees work on many different projects at the same time, leaving out inter‐project issues is a major omission.

To address these omissions, Ambler and Constantine suggest adding a production phase and two workflows: the operations and support workflow and the infrastructure management workflow (see Figure 1‐4).25 In addition to these new workflows, the test, deployment, and environment workflows are modified, and the project management and the configuration and change management workflows are extended into the production phase. These extensions are based on alternative object‐oriented software processes: the OPEN process (Object‐oriented Process, Environment, and Notation) and the Object‐Oriented Software Process.26

![image](https://user-images.githubusercontent.com/73081144/176343515-78e9104b-456f-4881-9aea-7fa3374f8ae4.png)

### Production Phase

The production phase is concerned primarily with issues related to the software product after it has been successfully deployed. This phase focuses on issues related to updating, maintaining, and operating the software. Unlike the previous phases, there are no iterations or incremental deliverables. If a new release of the software is to be developed, then the developers must begin a new run through the first four phases. Based on the activities that take place during this phase, no engineering workflows are relevant. The supporting workflows that are active during this phase include the configuration and change management workflow, the project management workflow, the new operations and support workflow, and the infrastructure management workflow.

### Operations and Support Workflow

The operations and support workflow, as you might guess, addresses issues related to supporting the current version of the software and operating the software on a daily basis. Activities include creating plans for the operation and support of the software product once it has been deployed, creating training and user documentation, putting into place necessary backup procedures, monitoring and optimizing the performance of the software, and performing corrective maintenance on the software. This workflow becomes active during the construction phase; its level of activity increases throughout the transition and, finally, the production phase. The workflow finally drops off when the current version of the software is replaced by a new version. Many developers are under the false impression that once the software has been delivered to the customer, their work is finished. In most cases, the work of supporting the software product is much more costly and time consuming than the original development. At that point, the developer's work may have just begun. When considering the newer DevOps approaches, it is obvious that operations personnel should be actively involved with this workflow.

### Infrastructure Management Workflow

The infrastructure management workflow's primary purpose is to support the development of the infrastructure necessary to develop object‐oriented systems. Activities such as development and modification of libraries, standards, and enterprise models are very important. When the development and maintenance of a problem‐domain architecture model goes beyond the scope of a single project and reuse is going to occur, the infrastructure management workflow is essential. Another very important set of cross‐project activities is the improvement of the software development process. Because the activities on this workflow tend to affect many projects and the Unified Process focuses only on a specific project, the Unified Process tends to ignore these activities (i.e., they are simply beyond the scope and purpose of the Unified Process).

### Existing Workflow Modifications and Extensions

In addition to the workflows that were added to address deficiencies contained in the Unified Process, existing workflows had to be modified and/or extended into the production phase. These workflows include the test, deployment, environment, project management, and configuration and change management workflows.

#### Test Workflow

For high‐quality information systems to be developed, testing should be done on every deliverable, including those created during the inception phase. Otherwise, less than high‐quality systems will be delivered to the customer.

#### Deployment Workflow

Legacy systems exist in most corporations today, and these systems have databases associated with them that must be converted to interact with the new systems. Owing to the complexity of deploying new systems, the conversion requires significant planning. Therefore, the activities on the deployment workflow need to begin in the inception phase instead of waiting until the end of the construction phase, as suggested by the Unified Process.

#### Environment Workflow

The environment workflow needs to be modified to include activities related to setting up the operations and production environment. The actual work performed is similar to the work related to setting up the development environment that was performed during the inception phase. In this case, the additional work is performed during the transition phase.

#### Project Management Workflow

Even though the project management workflow does not include staffing the project, managing the contracts among the customers and vendors, and managing the project's budget, these activities are crucial to the success of any software development project. We suggest extending project management to include these activities. This workflow should additionally occur in the production phase to address issues such as training, staff management, and client relationship management.

#### Configuration and Change Management Workflow

The configuration and change management workflow is extended into the new production phase. Activities performed during the production phase include identifying potential improvements to the operational system and assessing the potential impact of the proposed changes. Once developers have identified these changes and understood their impact, they can schedule the changes to be made and deployed with future releases.

Figure 1‐5 shows the chapters in which the Enhanced Unified Process phases and workflows are covered. Given the offshore outsourcing and automation of information technology,27 in this textbook, we focus primarily on the elaboration phase and the business modeling, requirements, analysis, design, and project management workflows of the Enhanced Unified Process. However, as Figure 1‐5 shows, the other phases and workflows are covered. 

![image](https://user-images.githubusercontent.com/73081144/176343545-10d9dea6-42f5-439d-a324-9b0c100a7ef6.png)
