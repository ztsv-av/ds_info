# Documenting Requirements

The goal of documenting a requirement is to communicate (to eventual software developers as well as to the project’s stakeholders) that the requirement is correct and complete. Describing each requirement, therefore, is a critical process. To improve that communication, the requirements engineers may use words, pictures, diagrams, and more. 

When you write requirements, you can either write them from the perspective of the system or from that of the users. There are many ways to write requirements, and two good examples are as follows:

1. From a system perspective, a good way to write requirements is as follows:
   - [Optional precondition] [optional trigger event] the system shall [expected system response].

2. From the users’ perspective, a good way to write requirements is as follows:
   - The [user class or actor name] shall be able to [do something] [to some object] [qualifying conditions, response time, or quality statement].

In general, software requirements can be captured in one of the following ways:

- Carefully crafted and well-organized natural language;
- Visual models to capture the different states of the system, the data flow, the communication among the different components, logic flow, and so on;
- Formal specifications that use mathematical-based, precise language.

A combination of the first two methods is the most common approach to represent requirements, although some critical systems (e.g., a software that will control the operation of a nuclear reactor) may need to have precise requirements to prevent any errors or confusion.

Ways to document requirements:

- Data flow diagrams: These illustrate the movement of data throughout the system or process. Such data movement (flow) can be from one process to another, to or from a data store (file or database), or to or from a user via an input/output (I/O) operation. Unlike a flowchart, the DFD does not describe processing flow and sequence (such as a sequential, conditional, or iterative construct). Instead, it exists only to show the flow of data. Requirements engineers and systems analysts often refer to a DFD as logical or physical. A logical DFD represents only the data flows required for the system to operate. In contrast, a physical DFD shows how the system is currently or will be implemented. Because a physical DFD may represent a system that has evolved over time, the logical and physical DFDs may differ in terms of the number and type of data stores used, the flow of data throughout the system, and more.

![image](https://user-images.githubusercontent.com/73081144/193981805-b133d70d-c516-4170-a6ee-51c117139b3c.png)

*Fig. 1. DFD components.*

![image](https://user-images.githubusercontent.com/73081144/193981938-691f37e3-b2bd-4cea-8971-3f6e3a449359.png)

*Fig. 2. DFD example.*

- Swim lane diagrams or cross-functional diagrams: These not only show a component’s processing, but also who or what is performing the processing. Software engineers often describe a swim lane diagram as a flowchart with specific task assignments.

![image](https://user-images.githubusercontent.com/73081144/193982069-735f28ec-3036-496e-b63b-4b07649e4d01.png)

*Fig. 3. Swim lane diagram example 1.*

![image](https://user-images.githubusercontent.com/73081144/193982220-dcd4b2dc-b662-430b-bf24-caa792fe4a4c.png)

*Fig. 4. Swim lane diagram example 2.*

- UML diagrams:
- - Class diagram: Systems are made of things or objects. This diagram describes the structure of an object and often also shows the relationships between objects.
- - Package diagram: This illustrates the components that make up a subsystem or combine to create a larger system.
- - Object diagram: This illustrates the attributes of an object and their relationship to object instances.
- - Component diagram: This is a big picture diagram that illustrates how the components of a system combine to create the overall system.
- - Composite structure diagram: This illustrates the internal structure (make up) of a class and the collaborations between the components.
- - Deployment diagram: This illustrates the physical components that will be involved in the real-world (deployed) system.
- - Activity diagram: This illustrates the flow of control within a system by showing sequences and conditions that drive action.
- - Sequence diagram: This describes the interactions between classes (messages) that occur over time.
- - Use case diagram: This illustrates an interaction between the system users (often referred to as the actor of the interaction).
- - State diagram: This illustrates the various states within which a system may reside and the activities that drive the transition from one state to another.
- - Communication diagram: This shows the exchange of data (messages) between system components.
- - Interaction overview diagram: This illustrates how the flow of control within a system drives interactions between components.
- - Timing diagram: The events within a system are often time-based. This diagram illustrates the sequence of such events across a time line.

- Dialog map: This provides a way to improve and document communication and brainstorming (the dialog) between attendees of a meeting. The goal of using a dialog map to capture ideas, questions, and concerns.

![image](https://user-images.githubusercontent.com/73081144/193983310-8a990b38-32fb-43a3-bc16-67e1eb3db714.png)

*Fig. 5. Dialog map example.*

- Decision tree: This is a graph that shows the decision points within a process and the consequences (or results) based on specific choices. Each node within the graph specifies a condition that the system will test. The test is often a simple yes or no question, but it does not have to be. The test could examine different range of ages and perform specific processing for each range.

![image](https://user-images.githubusercontent.com/73081144/193983514-7a64ec7d-270b-47ac-82fd-138ae7e777ae.png)

*Fig. 6. Decision tree example 1.*

![image](https://user-images.githubusercontent.com/73081144/193983568-2af8f481-98b2-4395-9373-f8ddb9d70bb3.png)

*Fig. 7. Decision tree example 2.*

- Decision table: This provides a visual representation of actions to take when a specific decision is made. Decision tables normally present a set of conditions that corresponds to a business rule. Based upon the business rule, a decision table will direct the system to perform one or more related operations.

![image](https://user-images.githubusercontent.com/73081144/193983672-79587fbc-c1a9-4bb8-b5b5-b1510b24bd67.png)

*Fig. 8. Decision table example 1.*

![image](https://user-images.githubusercontent.com/73081144/193983786-cdd9d10a-30ab-41de-8e11-3ef152773bff.png)

*Fig. 9. Decision table example 2.*

- Basic flowchart: A basic flowchart is a simple diagram of the step-by-step process of the lowest level of business model description. Basic flowcharts are commonly used in the different areas of businesses or systems. Simplicity and clarity are the advantages of basic flowcharts. However, they do not include what role performs the actions. The following are some areas where a basic flowchart can be helpful:

    - Planning a new project
    - Documenting a basic process 
    - Analysis and design
    - Managing a process
    - Visualizing the solution to a problem
    - Showing actions or operations

- Business process modeling : Business process modeling (BPM) is the visual form of business processes in a workflow. The Business Process Management Initiative (BPMI) established standards to help all business users easily understand each other using the unified standard for design and implementation of business processes. The following are some uses of BPM flowcharts:

    - Visualizing the business processes
    - Showing the organization of the business processes
    - Process improvement
    - Having unified standards for better communication between the business and its technical staff
    - Showing internal processes within a business entity
    - Presenting the interaction between business entities

- Screen mockups;
  
- Flowcharts;
  
- Pseudocode.

## Requirements Template

The purpose or goal of a requirements template is to improve the quality of each and every requirement and to increase consistency across the requirements document. For a large project, the requirements may be gathered and written by many different requirements document. Using a requirements template will significantly improve the quality and consistency of the requirements document.

Key items that should appear within the requirements template include the following:

- Unique identifiers for each requirement that can later be used to reference or trace the requirement. Enter the value that will uniquely identify the requirement throughout the requirements document.
- Meaningful title for the requirement. Assign a meaningful (unique) title that describes the underlying processing that the requirement specifies or the underlying constraint for a nonfunctional requirement.
- Complete description of the requirement. Enter the requirement description. Use the active voice to describe the requirement’s who, what, where, how, and when. Conjunctions such as and or or indicate that the requirement should be further decomposed into two or more requirements.
- Source of the requirement. Enter the source or origin of the requirement.
- Date and time the requirement was written and last modified. Enter the date (and time) the requirement was written or last changed. When a requirement changes, it should have a matching entry in the change management log.
- Any dependencies or relationships that the requirement may have with other requirements. Enter any relationships to other requirements or dependencies on other requirements. For an electronic document, you should provide hyperlinks to the related requirements to make it easy and fast for the reader to move from one requirement to the next.
- Confirmation that the requirement is feasible. Enter the date (and time) the development team approved the requirement’s feasibility.
- Supporting material or diagrams. Insert any related documents, such as a data flow diagram (DFD) or Unified Modeling Language (UML) diagram.
- Business owners or stakeholders (contact information) associated with the requirement. Specify the name of the business owner responsible for the requirement.
- Requirement’s category (functional or nonfunctional), which may include the following:
    - Business requirement or rule
    - User requirement
    - Customer requirement
    - Contract requirement
- Stakeholder approval (date, time, and by who). Enter the date (and time) the business owner approved the requirement specification.
- Any additional notes. Enter any related notes or diagrams.

### Requirement Documentation Example

- Unique requirement ID: BR-0001
- Requirement title: Landing Page Icons
- Requirement description: Upon loading, the mobile application will display a landing page (main screen) with logos and text for the following operations:
    - Update Profile
    - Logout
    - Sell a Product
    - Shop
    - View Today’s Deals
- Requirement source: Mobile Project Statement of Work Dated 1 September 2018
- Date written or modified: 4/15/2019 by Jim Brewer, Business Analyst for ACME Software
- Dependencies or relationships: See notes on responsive design.
- Feasibility approval: 4/25/2019 approved by Ken Lewis, Lead Architect for ACME Software
- Supporting diagrams: See user-interface mockup diagrams.
- Business owner: Jason Stream, Project Manager for New Solutions
- Category: User interface
- Stakeholder approval: 4/30/2019 Jason Stream, Project Manager for New Solutions
- Notes: Screen will be implemented with a responsive user interface (UI) per requirement UI-0030.

## Software Requirements Specification (SRS) Document

A system’s requirements provide the specifics that programmers follow during the implementation phase to write the code that builds the system. During the program-development process, the details that the requirements engineers provide for each requirement will provide the specifics that the programmers will need to write the corresponding programming statements.

The requirements document combines all of the system requirements—both functional and nonfunctional. Within the requirements document, you will find written specifications, visual diagrams, and possibly pseudocode descriptions of the underlying processing.

The following are some key pieces that should exist in an SRS document:

- List of capabilities and functions that the system should offer;
- Key characteristics of the system;
- Constraints that the system should comply with;
- List of all of the different qualities for the system (nonfunctional attributes).

It is very critical to be able to uniquely refer to any requirements, which means that you need to have a unique and consistent identifier for each requirement. This will facilitate the communication between the team members in activities related to change requests, the traceability matrix, and cross-referencing. There are multiple ways to assign such an identifier to each requirement, as follows:

- Sequence numbering: The easiest way is to assign a unique number for each requirement. You can take that one step further by having a prefix to allow for more context. For example, you can have FR-xx to indicate functional requirements. This approach is quite easy, but it lacks any hierarchical or logical grouping. Thus, it is not easy to relate requirements to each other. The numbering system does not give any indication about the order of the requirement or what the requirement is all about.
- Hierarchical numbering: In this approach, you have requirements listed in a hierarchical order with each digit indicating lower level requirements (e.g., 1.2.1 is a child to 1.2 but with more details). This approach is simple, compact, and logical. Most word-processing applications will generate such numbering automatically for you. Just be careful because you can run into trouble if you come back and modify your document; the ordering can change and affect other portions of the project that refer to that particular requirement (consistency can be an issue).
- Hierarchical textual tags: A better approach is to use hierarchical textual tags. The naming should be descriptive to tell the meaning for such requirements. Imagine that you have a set of requirements related to how you will print a document. You can have a parent Print requirement, and under that, you can have multiple children for each requirement. “Print.confirmcopies” can be the label for a requirement that asks users to confirm their selection if they want to print more than five copies. On the other hand, “print.documenttype” can be the label for the requirement that restricts the types of documents that can be printed. This approach is more logical and groups related requirements together. In addition, it can be easy to guess what a requirement is about just from the label. However, it may be difficult to enforce uniqueness, especially if you have a large team. You need to come up with a meaningful name for each requirement, which can be tedious if you have hundreds of them (numbering will be easier).

The requirements document is normally a word-processing document.	Table of Contents
The general form of the requirements document is as follows:

- Preface
- Introduction
- Glossary
- Architectural Designs
- System Modules or Components
- Requirement Specifics and Details
- System Evolution
- Appendices
- Index

### The Preface

The preface provides an overview of the requirements document. Within the preface, you may find a description of the anticipated readers, a description of the document writers, specifics about the date the document was written, as well as the document’s version number if multiple editions of the document exist.

### The Introduction

The introduction of the requirements document should describe the system, its purpose, and the need. The introduction should detail the system’s business purpose as well as the system’s expected interactions with other systems (internal or external to the business). Also, the introduction may describe the anticipated users and their needs. You can think of the interface as an executive summary of the planned system.

### The Glossary

A key attribute of a good requirements document is that it uses consistent terminology across all requirements. The Glossary section of a requirements document should specify the appropriate system terms and provide definitions for those terms. The glossary contents are often identified and written early during the requirements phase so that the requirements engineers can apply the standardized terminology throughout the requirements.

### The Architectural Diagram

The Architectural Diagrams section of the requirements document provides a visual representation of the entire system and its key components. The diagrams should also illustrate how the system will interact with other systems. Depending on the complexity of a system, there may be many layers of architectural diagrams. Within the architectural diagrams, you may also find information about underlying platforms, such as the system’s use of the cloud.	

### The System Modules or Components

The System Modules or Components section of the requirements document is similar to the architectural diagrams in that the section provides a visual representation of key system components and the relationships between them. Should, for example, a system use an e-commerce framework, you might find specifics about the framework and its interfaces within this section.

### The Requirements

The Requirements section of the requirements document is an ordered list of each and every system requirement, including both functional and nonfunctional. Within this section, each requirement should have a unique identifier that stakeholders can use to reference the requirement. To better organize the requirements, the document may categorize and group requirements according to the following:

- Business Requirements
- Performance Requirements
- Security Requirements
- User Requirements
- Customer Requirements
- Quality Requirements
- External API or Interface Requirements
- Infrastructure Requirements

### The System Evolution

The System Evolution section should describe how the system is expected to evolve over time and how such considerations affected the current system requirements.

### The Appendices

The Appendices section of the requirements document may contain a variety of things, from working notes to additional diagrams that detail the system processing and the key documents, such as the original request for proposal. In addition, the appendices may contain requirements for earlier versions of the software. Finally, the appendices may include any agreed-upon change requests between the customer and the company that is building the system.

### The Index

The index should provide readers with a quick way to locate specific content. Within a PDF or Web-based version of a document, the index should include hyperlinks to the underlying content.
