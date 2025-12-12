# Software Design Patterns

## Creational Design Patterns

1. Abstract factory: Provides an interface for creating families of related or dependent objects without specifying their concrete classes. Clients only have to commit to an interface (method call) defined by an abstract class, not a particular concrete class. An example would be an application that is written to use GUI widgets, like a scrollbar or a textbox for the Motif look and feel. It could also be used for a program manager look and feel. The client makes the call for the scrollbar, and under the covers, the abstract widget factory supplies the appropriate widget: a scrollbar.
2. Builder: Separates the construction of a complex object from its representation so that the same construction process can create different representations. An RTFReader class has a TextConverter object, which has a number of different implementations. One implementation is an ASCIITextConverter, while another might be UnicodeTextConverter. Each kind of converter is separate from the more complex converter, which is responsible for parsing an RTF document.
3. Factory method: Defines an interface for creating an object but lets subclasses decide which class to instantiate. Factory methods let a class defer instantiation to subclasses. A framework of applications creates applications with different implementations. A drawing application, which creates drawing documents as well as a spreadsheet application, could be an implementation of the same application framework.
4. Prototype: Specify the kinds of objects to create using a prototypical instance and create new objects by copying this prototype. If an existing graphical tool palette is to be adapted for use with a different set of graphical forms, it can be adapted quite easily by creating the palette with a prototype of the graphical form that the tools are meant to support.
5. Singleton: Ensure a class has only one instance and provide a global point of access to it. Every system may have multiple printers assigned to it; however, there can only be one print spooler that knows about every request that is headed for every printer.


## Structural Design Patterns

1. Adapter: Converts the interface of a class into another interface that clients expect. It lets classes work together that could not otherwise do so because of incompatible interfaces. Another term for such a class is a wrapper, where the wrapper provides the appropriate interface to the calling class and adapts method calls to the called class.
2. Bridge: Decouples an abstraction from its implementation so the two can vary independently. A JavaBean can serve as a bridge between a GUI screen and a data store. This enables the data store to change independently from the GUI and vice versa.
3. Composite: Composes objects into tree structures to represent part-whole hierarchies. Composites let clients treat individual objects and compositions of objects uniformly.
4. Decorator: Attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality. A textView object is decorated with a border and the border is decorated with a scroll. The resulting object enables a border around a large set of text that is scrollable.
5. Façade: Provides a unified interface to a set of interfaces in a subsystem. Façade defines a higher-level interface that makes the subsystem easier to use. All the client sees is the face (or façade) of the underlying subsystem. The more complex subsystem sits behind the face and is detached from the client.
6. Flyweight: Uses sharing to support large numbers of fine-grained objects efficiently. A folder tree has only two objects—an open folder and multiple instances of a closed folder. The closed folder is actually only one instance shared across the tree.
7. Proxy: Provides a surrogate placeholder for another object to control access to it.

## Behavioral Design Patterns

1. Chain of responsibility: Avoid coupling the sender of a request to its receiver by giving more than one object a chance to handle the request. Chain the receiving objects and pass the request along the chain until an object handles it.
2. Command: Encapsulate a request as an object, thereby letting you parameterize clients with different requests, queue, or log requests, and support undoable operations. Each MenuItem is configured with a concrete Command subclass. When a MenuItem is selected, it calls an Execute method on its Command subclass and Execute carries out the operation. The MenuItem is decoupled from the actual receiver of the command.
3. Interpreter: Given a language, define a representation for its grammar, along with an interpreter that uses the representation to interpret sentences in the language. If a particular kind of problem occurs often enough, then it might be worthwhile to express instances of the problem as sentences in a simple language.
4. Iterator: Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation. There are all kinds of collections of data, and you simply want to iterate over the collection without worrying about what kind of collection is used.
5. Mediator: Defines an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly, and it lets you vary their interaction independently.
6. Memento: Without violating encapsulation, capture and externalize an object’s internal state so that the object can be restored to this state later.
7. Observer: Defines a one-to-many dependency among objects so that when on object changes state, all its dependents are notified and updated automatically.
8. State: Allows an object to alter its behavior when a change occurs in its internal state. An order object may move from an initial state of shipped to a filled state as the order is filled.
9. Strategy: Define a family of algorithms, encapsulate each one, and make them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
10. Template method: Define the skeleton of an algorithm in an operation, deferring some steps to subclasses. A template method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure. Upon opening a document, all of the basic algorithms are implemented for a generic document. Implementation details for different kinds of documents are deferred to actual implementations of the types of documents.
11. Visitor: Represent an operation to be performed on the elements of an object structure. Visitor lets one define a new operation without changing the classes of the elements on which it operates.
Question 4: Is there an example of how patterns can be combined to describe a larger software

## Model-view Controller (MVC) Design Pattern

Model-view controller (MVC) design pattern, or architecture, embodies the interaction of three design patterns: observer, composite, and strategy design patterns. It can also use the factory method or decorator design patterns, depending on the implementation requirements.

Model-view controller is built on a model that identifies the business problem domain, all of the data and the business rules for updates, and it inserts and deletes on the data. The view is the component, which is visible to the user and can take the form of GUI screens or HTML pages. The view must ensure that its appearance reflects the current state of the model. The controller defines the way the user interface reacts to user input.

## E-business Design Patterns

Each pattern identifies the parties involved in the business interaction and the structure the interaction assumes. Industry examples are provided for each of the patterns so developers can easily match their own business needs with the solutions each pattern offers. The following are the five core e-business patterns:

1. User-to-business (U2B):
   - Locating a nearby insurance office or agent
   - Online billing
   - Buying and selling stocks online
   - Accessing, reviewing, and editing account information
   - Submitting business requests, forms, applications, and orders
   - Tracking order fulfillment and delivery
2. User-to-online buying (U2OB): The U2OB pattern is actually a subset of the U2B pattern that deals more specifically with e-business transactions in which packaged goods are sold online through a catalog using a shopping cart, electronic wallet, or similar tool. U2OB can also include links to back-end systems for inventory updates and credit checking.
3. Business-to-business integration (B2Bi): The B2Bi pattern complements and extends U2OB through programmatic business-to-business interactions. Automating B2B e-business across corporate boundaries requires a shared business process where two or more disparate business processes might be present.
4. Business-to-business e-marketplace (eMP): The eMP pattern combines elements from several patterns to create hub applications that bring together multiple buyers and sellers to provide efficient electronic trading of goods and services.
5. User-to-data (U2D): The user-to-data pattern provides the user access to, and manipulation of, data. U2D establishes a set of requirements and system environments known as the informational environment, which supports the management and control of business activities over time. This informational environment is populated with data from the operational environment through which business activities are recorded on a minute-to-minute basis as the original source of much of the information needed to manage and control the business.
6. Future planned expansion of the patterns includes the development of the following patterns as well:
    - User-to-user (U2U)
    - Application integration
