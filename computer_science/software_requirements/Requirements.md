# Requirements

What is a requirement? There are many definitions, but the following are a few of them that are discussed in this lesson:

- “Requirement is anything that drives design choices” (Wiegers & Beatty, 2013). The good thing about this definition is that it links requirements to design, which is the ultimate realization of any requirement.
- A requirement is anything that a product should have to provide value to a stakeholder. This definition is good because it links the requirements to the stakeholder.
- “Requirements are a specification of what should be implemented. They are descriptions of how the system should behave, or of a system property or attribute. They may be a constraint on the development process of the system” (Sommerville & Sawyer, 1997). This particular definition acknowledges the diverse nature of the requirements and also looks at requirements from user and developer perspectives.

## Characteristics of a Good Requirement

Systems are complex, and even a simple system can have hundreds, if not thousands, of requirements. The requirements gathering process, similar to the software development process, must often be completed under time and resource constraints. As such, to improve the resulting requirements, it is important that the engineers begin with the quality requirements in mind. The attributes of a good requirement include the following:

- Complete: Each requirement must have all of the details that will allow the reader to understand it. If a requirement describes a function, it should contain all of the details that will allow the development team to implement it. If details are not known, to-be-defined (TBD) should be assigned to that requirement. TBDs should be traced, and construction for any release should not start if any of the requirements needed for that release are TBDs.
- Correct: Each requirement should accurately describe a function or a capability needed by the consumers. The source for each requirement should be known and consulted to ensure the correctness of the requirement.
- Feasible: It must be possible to implement each requirement within the constraints and capabilities available to the project in terms of budget, staff, and time. Developers should verify that technology can support the implementation of each requirement. Incremental development and prototyping are techniques to test the feasibility of any requirements. If any requirement proves to be impossible to implement or if the cost will be too high, an impact analysis should be done to understand the effect on the project.
- Necessary: Each requirement should be presented to provide a business value, market differentiation, conformance with a regulation, and so on. Each requirement should come from someone who is authorized to provide requirements. Each requirement should also be traced back to something such as a user story or a use case.
- Prioritized: Each requirement should have a priority assigned to it to signify its importance to a specific release or for the project in general. This priority should be assigned with the collaboration of multiple stakeholders to ensure that different perspectives are considered.
- Unambiguous: Natural language is prone to ambiguity. Different readers can read the same requirement statement but end up with two different interpretations. A good way to address this is to do a formal review, where different stakeholders explain to each other their understanding and come to a consensus as to what a particular requirement means; the stakeholders can also change the wording to make it more concise.
- Verifiable: Can the testing team develop a test that will verify whether the code implements the requirement? This is a critical question to ensure that you can judge the correctness of the software objectively. Inconsistent, incomplete, infeasible, or ambiguous requirements can be difficult to verify. Make sure to include the testing for requirement reviews because they are efficient when used for this purpose. 

Once you have high-quality individual requirements, you still need to enforce the following qualities for the set of requirements that makes up a release or the total set of requirements for a project:

- Complete: Your set of requirements should capture everything that should be known about the system. Determining if a requirement is complete can be difficult because you cannot know if there are missing details or not. This lesson will discuss techniques for detecting missing requirements.
- Consistent: Consistent requirements entail that no requirements will conflict with each other or with higher level users or business requirements. If you do not resolve conflicts at this stage, developers may need to do that based on their discretion (this may not be what the customer wants). Being able to link each requirement to an originator will allow you to direct questions to the right person to resolve these conflicts. Keep in mind that it may be difficult to spot these conflicts if requirements are stored in different places (software requirements specification [SRS] versus scope or vision documents).
- Modifiable: You should be able to modify any requirements, but you still need to maintain a history for these changes, especially if a requirement has been baselined. In addition, you need to know the dependencies between requirements to understand how a modification will affect other requirements. It is also critical to be able to refer to any requirement uniquely without ambiguity. Repeating the same or related requirements in different places will make it harder to modify these requirements; otherwise, you may end up with inconsistent requirements.
- Traceable: A traceable requirement can be traced backward to its originator and forward to its derived requirements, the design elements, the code that implements it, and the test that will verify it. It is important to avoid combining different requirements under one label to make it easier to build a traceability network.

## Levels and Types of Requirements

Requirements come with different types and levels, and it is important to agree on terminology. Please review the following concepts:

- Business requirement: High-level objective for the organization that needs that system. This requirement normally comes from the sponsor of the project, the marketing team, or the acquiring customers. It is a good practice to collect these business requirements into a vision and scope document. Examples of business requirements include the following:
- - All customer invoices must be paid net 90 days from the date of purchase.
- - Part-time employees cannot work more than 40 hours per week.
- - The system must use an Oracle database for all data storage operations.

- Business rule: A standard, a regulation, or a constraint that relates to the business for which the system is developed.

- Constraint: Anything that can limit the options for the developer when it comes to design or development.

- External interface requirement: A description of a connection between the system and another system, user, or a hardware.

- Feature: A capability or a set of capabilities that provide a value to the end user.

- Functional requirement: A behavior for the system under specific conditions. Functional requirements will normally be captured by the business analyst and will be documented in the software requirement specification (SRS) document. This SRS will be the references for the follow-up phases including design, development, testing, and quality assurance.

- Nonfunctional requirement: A property or a constraint that the system must observe or meet. Nonfunctional requirements are normally referred to as the “ilities,” like portability, availability, maintainability, readability, and so forth.

- Quality attribute: A nonfunctional requirement that describes a performance aspect of the system.

- System requirement: A high-level requirement for a product that is made up of different subsystems. These subsystems can be a mix of software and hardware.

- User requirement: A task that should be done by a group of users. There are good ways to capture these requirements that include use cases, user stories, and even-response tables.

- Performance requirements: These specify a capability that must be met with respect to speed or throughput. Examples of performance requirements include the following:
- - All mobile screens must render in 3 seconds or less.
- - The maximum network throughput must be less than 3 Gbs.
- - The monthly financial report must print in less than 10 minutes.

- Security requirements: These requirements specify data protection or privacy constraints that the system must satisfy. Examples of security requirements include the following:
- - All form-based user input operations must use HyperText Transfer Protocol Secure (https) to transmit data between the user or client system and the remote server.
- - All Ajax transactions must use Secure Sockets Layer (SSL) to securely exchange data between the client and the server.
- - Within the Linux system, the admin or root account must be disabled at all times.

- External application programming interface (API) or interface requirements: These specify an API that the system must provide for external access or consume or resource access. Examples of external API or interface requirements include the following:
- - The system will use MuleSoft as middleware to all external APIs.
- - All payment processing should be done using the PayPal API.

- Infrastructure requirements: These specify a hardware or system software constraint that the system must satisfy. Examples of infrastructure requirements include the following:
- - The mobile app must run on the Android and iOS operating systems.
- - The system will use Amazon Web Services (AWS) or Azure for cloud hosting.

- Customer requirements: These specify a customer request that the system must satisfy. Examples of customer requirements include the following:
- - The software must pass a customer-provided user-acceptance test.
- - The software must be delivered (made available on the customer servers) by July 1st.

## Functional vs Non-functional

A functional requirement specifies a task that the system must provide or perform. For example, functional requirements might include: the system will allow a user to register, log in, and manage his or her profile. A nonfunctional requirement, in contrast, specifies a constraint that the system must satisfy. For example, nonfunctional requirements might include the following:

- All screens will render in 3 seconds or less.
- All data at rest or in transit will be encrypted.
- All server-side code will be written in Python.

## Product Versus Project Requirements

Whatever you store in your SRS document are requirements that users will expect from your system, and these requirements can be called product requirements. However, there are other types of requirements that are not related to the product itself but they are important to the success for the project.

The following are few requirements that relate to your project:

- Physical resources needed in terms of hardware, software, office space, and so forth
- Staff training
- Requirements and procedure for software release, installation, and configuration
- Requirements for the transition from the current system to the new system
- Sourcing and licensing third-party products
- Customer service-level agreements

## Requirements Development and Management

The whole activities related to requirements can be called requirements engineering (that goes well with the whole concept of software engineering). Requirements engineering can be further broken into requirements management and requirements development. Requirements development can be then further broken into elicitation, analysis, specification, and validation.

### Elicitation

This is when you start the process of discovering your requirements through interviews, workshops, prototyping, and document analysis. Key actions during that phase include the following:

- Identify the key stakeholders and users
- Understand users’ tasks and business objectives
- Learn the environment in which the product will be used
- Work with different users to understand their functional requirements and quality expectations 

A typical requirements engineering process begins with the gathering of the requirements. This step is called requirements elicitation. At this stage of a project, the scope of the project and project boundaries should already be defined. A well-defined set of boundaries should include the budget limit, project time line, and available resources that would guide the systems analyst to stay within the boundaries when managing the business expectations. A well-defined statement of the problem should be available to serve as the guideline for elicitation. Various methods are used to glean the requirements from the users, customers, or other project stakeholders. As a result, one must know the users, customers, and stakeholders to interview. Common approaches for requirements elicitation include user scripts, surveys, focus groups, interviews, and observation. Regardless of the method used, the scope of the project should always be kept in mind. In addition, the business analyst must have excellent interviewing skills to capture the user’s requirements. Be open-minded, and make sure not to commit to any solution until you gather all of the requirements and your analysis is completed.

### Analysis

During the analysis phase, you try to develop a better understanding of the requirements gathered during the elicitation phase. Key activities during that phase include the following:

- Analyze the requirements gathered and categorize them per the right categorization (business requirements, constraints, functional requirements vs. nonfunctional requirements)
- Decompose high-level requirements into more detailed requirements
- Understanding the importance of different quality attributes
- Negotiate the priorities
- Identify gaps in requirements or requirements that are unnecessary

### Specification

During the specification phase, you try to represent the collected and analyzed requirements into a persistent and organized way. The key action is to translate the requirements into written document and different kind of diagrams to allow for better reviews and understanding by different stakeholders.

### Validation

The validation phase will confirm that you have the right requirements that will allow you to develop the system expected by your customers. Key activities during this phase include the following:

- Review all documented requirements to correct any issue before proceeding with these requirements
- Develop acceptance test based on the requirements to ensure that the final product will meet the needs of the customer

The way that these phases (elicitation, analysis, development, specification, and validation) were presented should not indicate that it is pure sequential process, but it is actually recommended that you use an iterative approach until you finalize these requirements to a point that all stakeholders feel confident you captured everything relevant about the project.

### Requirements Management

Key activities for requirements management include the following:

- Capture the requirements baseline, which is a snapshot at a particular point when you have an approved set of functional and nonfunctional requirements. This is normally done for a particular release or version of the product.
- Evaluate the impact for any requirement change and document the process of that change.
- Keep the project plan synchronized with the latest changes for the requirements.
- Negotiate contingency plans based on requirements changes.
- Define the dependencies and relationships among the different requirements.
- Trace each requirement to design, source code, and testing.
- Track the status for each requirement throughout the project.

Requirements may change multiple times, and that is a very critical aspect during the requirements-gathering phase. The idea is not to disallow changes but to go through a managed and controlled process to understand the impact of each change to the project and ensure that all relevant stakeholders are part of the decision making to accept or reject any change.

## SDLC Types

The effort and time allocated to requirement development will depend on which software development life cycle you use.

- Waterfall projects: In these projects, you plan to have one major release at the end of the project. The majority of the requirements development happens at the beginning of the project with some minor effort throughout the project to handle some changes.
- Iterative projects: Projects that use approaches such as the rational unified process (RUP) will work on requirements for each iteration with more emphasis on the first iteration.
- Agile projects: These projects break down the project into small releases with requirements development happening for each of these small releases. In these projects, you start by collecting user requirements in the form of user stories. You try to know enough about these stories to estimate the effort and the priority as that will help you schedule these stories for the different releases.

## Good Practices for Requirements Development Cycles

### Elicitation

Requirements have three key levels: business, user, and functional. Each level will come from different sources at different times of the project, targeted for different audience, and documented in different ways. You also need to elicit different nonfunctional requirements for different quality attributes. The following are some good practices that can help you during that phase:

- Define product vision and project scope:
The vision of the project which should be stable throughout the project should give a common understanding to everybody involved in the project about the general outcome of the project. The scope, which can be for the whole product or for a particular release, will define what will be included and what will be left out. The scope can be more fluent compared to the vision.

- Identify user classes and their characteristics:
To ensure that the product addresses the needs for all users, it is important to identify the different groups of users that will be using the system. These groups may differ in the use frequency, the features used, the privilege level, or experience. Capture these groups in terms of tasks done by them, location, attitude, or any characteristics that can affect the use of the system.

- Select a product champion for each user class:
It is important to identify people that can represent classes of customers and speak on their behalf. When you develop a product for a specific customer, it will be easy to do that. However, developing a commercial product will make that tricky. The best approach is to use customers that you have a strategic relationship with or use something like beta version to solicit some input.

- Conduct focus groups with typical users:
Get users from previous products or similar products to the one under development and collect their feedback. This approach is very effective for commercial software. These members of focus groups are different from user champions in that they do not have any decision-making authority.

- Work with user representatives to identify user requirements:
Explore with these champions the key requirements for that product and what they want to achieve. User requirements can be captured in terms of user stories, use cases, or scenarios. You also need to capture how users will interface with the system.

- Identify system events and responses:
List all of the expected external events that the system can experience what are the responses expected from the system. These events can be of three different types, including the following:

- - Data, control events, or signal events that can be received from an external device
- - Time-based events trigger a response (e.g., a data feed that the software will generate every night)
- - Business events that trigger use cases for business applications

- Hold elicitation interviews:
Get one-on-one interviews with the different users or interview a small group at once. This can be very effective to get what you need without wasting their time as each user will just discuss the requirements from his or her perspective or the ones he or she needs. Once you are done with that, you can hold workshops for larger group to discuss any conflict among these requirements.

- Hold facilitated elicitation workshops:
These workshops (also called joint application design or JAD) will allow for collaboration between the business analyst and users and will allow to resolve any conflict of requirements and allow to draft the requirements document.

Other good practices will include the following:

- Observe users performing their jobs
- Distribute questionnaires
- Perform document analysis
- Examine problem reports of current systems for requirement ideas
- Reuse existing requirements

### Analysis

Requirements analysis means the refinement of the requirements to make sure it is clear and understood by everybody. Basically, requirements analysis includes the following:

- Break down high-level requirements into low-level ones
- Build prototypes
- Evaluate feasibility
- Negotiate priority

The goal is to come up with well-defined requirements that will allow for good project planning. You normally present the results of this analysis using multiple formats and from different views to allow looking at the requirements from different lenses. The following are some of the good practices for that phase:

- Model the application environment:
Creating a context model is a good way to capture how the new system will fit within the whole environment. This model defines the boundaries and the interface between the system and other external entities in your environment.

- Create user interface and technical prototypes:
If something is not clearly understood, it will be a good idea to develop a prototype to allow for better communication among the different stakeholders.

- Analyze requirement feasibility:
Requirements should be evaluated from feasibility standpoints. Developers should be able to determine the cost, performance, and technical feasibility for the different requirements. If one requirement proves to be unfeasible, this should be communicated back to the customer to either eliminate or simplify.

- Create a data dictionary:
A data dictionary contains the definition of data items and structure. This should help in communication between customers and the development team.

- Model the requirements:
It is always good to use graphical representations to model requirements from different perspectives. This may help to show any missing, inconsistent, or conflicting requirements. Some of the most common models used are the following:

- - Data flow diagrams
- - State transition diagrams
- - Dialog maps
- - Decision trees
- - Entity relationship diagrams
- - State tables
Other good requirements analysis practices include the following:

- Analyze interfaces between your system and the outside world
- Allocate requirements to subsystems
- Prioritize the requirements

### Specification

The goal of requirements specification is to record the requirements in an accessible, reviewable, and consistent method. You can do that through the software requirement specification (SRC) document or through a requirement management tool.

- Adopt requirement document templates:
Use a consistent template when you document requirements to make it easy to manage.

- Identify requirement origins:
It is critical to link each requirement with its origin in terms of business rule, customer, user stories, and who will be affected by that requirement. This can be of a great help when it comes to make any changes to that requirement to make sure that all of the right people are consulted.

- Uniquely label each requirement:
Define a consistent convention that can be used to assign a label for each requirement to allow for easier reference.

- Record business rules:
Business rules should be recorded at the enterprise level as they are not related to that particular project. Examples of these rules include corporate policies, government regulation, and standards. These rules will be enforced through some specific requirements, so it is good to have traceability links between these requirements and the rules they implement.

- Specify nonfunctional requirements:
You can build a system that does exactly what the customer needs, but it will not be acceptable for them if the system is too slow, goes down a lot, is very hard to change, and so forth. These qualities are referred to as nonfunctional requirements, and it is very critical to capture these the same way you capture other requirements.

### Validation

Requirements validation ensures that requirements are correct, consistent, and with no clear gaps. This step is very important to make sure the project start with a reliable set of requirements.

- Review the requirements:
Assemble a small team of people that represent different types of users, and go through a thorough review for everything collected and analyzed related to requirements to ensure you captured the complete and correct requirements.

- Test the requirements:
Write tests that will ensure the system produces the expected output under all different stimulations. Also, make sure that every requirement captured has a test that will test that particular requirement.

- Define acceptance criteria:
Ask users how they are planning to test the system to see if it meets their expectations in terms of functional and nonfunctional requirements.

### Management

It is inevitable that your requirements will change at certain points during the project, and for that you need to have a sound management process and version control the same way you do for your source code or use one of the dedicated requirements management tools.

- Establish a requirements change control process:
Instead of resisting changes, try to manage them through a clear and well-defined process. This process should be able to define how changes are proposed, analyzed, and resolved. There should be a change control board (CCB) made of key stakeholder representatives that will decide for each change to be accepted or rejected based on sound analysis.

- Perform impact analysis on requirements changes:
Impact analysis is very critical to be able to decide on any proposed change. This should determine the impact on the project for that particular change. The traceability matrix should be a good tool to understand the dependency of other requirements on that particular change and who from the users will be affected by that.

- Establish baselines and control versions of requirements sets:
Once requirements are agreed upon, this will constitute the requirement baseline. Any changes to this baseline should be done through the change control process. You should use version control for each new set of requirements for better tracking.

- Maintain a requirements traceability matrix:
It is very good practice and sometimes it can be mandatory to link each requirement with the piece of code that implements that particular requirement and the test(s) to test that requirements. This will ensure that nothing goes without testing and can also help when you need to change one of the requirement and to understand the impact of that change.

- Use a requirements management tool:
There are commercial tools that can help you store and manage most of the tasks listed above.

Other good requirements management good practices include the following:

- Maintain a history of requirements changes
- Track the status of each requirement
- Track requirements issues
