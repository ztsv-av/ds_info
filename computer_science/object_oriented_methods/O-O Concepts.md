# O-O Concepts

## Composition Relationship

Composition is a 'has a' relationship that demonstrates how a class can have a member variable that contains an instance of another. 'I contain an instance of the class I point to'. Composition is one-way relationship, meaning the contained class knows nothing about the container class.

![image](https://user-images.githubusercontent.com/73081144/202078848-021027ca-02f8-4d26-a194-59d05220b0c5.png)

*Fig. 1. Composition.*

Member variable used for containment is shown next to the diamond.

## Aggregation Relationship

Aggregation is a relationship where the container class only has a reference to the contained object. It does not control the life span of the contained object, compared to composition relationship.

![image](https://user-images.githubusercontent.com/73081144/202079143-3086215c-4749-4a6e-ab52-7c6e323ba97c.png)

*Fig. 2. Aggregation.*


## Inheritance Relationship

Inheritance is 'is a' relationship where a class is derived from another class.

![image](https://user-images.githubusercontent.com/73081144/202079267-ea9ad2c9-f1ea-4655-87aa-36ad9b941cb0.png)

*Fig. 3. Inheritance.*

## Association Relationship

Association is a relationship where a class knows about its owner and needs to reference its owner.

![image](https://user-images.githubusercontent.com/73081144/202079414-956a0ffb-b545-4fae-ba81-988ff856e7eb.png)

*Fig. 4. Association.*

## Dependency

There are times when one class needs to know abou another class. Arguments to member variables are used to communicate these relationships. Dashed lines point from a class to another class it is dependent on.

![image](https://user-images.githubusercontent.com/73081144/202079762-e6b52ec3-9169-460e-bde7-44ac06dcf67e.png)

*Fig. 5. Dependency.*

## Encapsulation

Encapsulation is a way to protect an object's properties from direct outside access. For example, in Java you declare some of the object's properties as private.

## Polymorphism

Polymorphism is the ability of an object to take on many forms. Polymorphism enables different types of objects to respond to the same call in different ways.

## Inheritance

In object-oriented programming, inheritance is the mechanism of basing an object or class upon another object (prototype-based inheritance) or class (class-based inheritance), retaining similar implementation. Also defined as deriving new classes (sub classes) from existing ones such as super class or base class and then forming them into a hierarchy of classes. In most class-based object-oriented languages, an object created through inheritance, a "child object", acquires all the properties and behaviors of the "parent object" , with the exception of: constructors, destructor, overloaded operators and friend functions of the base class. Inheritance allows programmers to create classes that are built upon existing classes, to specify a new implementation while maintaining the same behaviors (realizing an interface), to reuse code and to independently extend original software via public classes and interfaces. The relationships of objects or classes through inheritance give rise to a directed acyclic graph.
