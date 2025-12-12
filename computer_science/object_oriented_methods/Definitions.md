# Definitions

## Objects

An object is an instantiation of a class, i.e., an actual person, place, or thing about which we want to capture information. If we were building an appointment system for a doctor's office, classes might include doctor, patient, and appointment. The specific patients, such as Jim Maloney, Mary Wilson, and Theresa Marks, are considered objects—i.e., instances of the Patient class.

## Operations

Each object has attributes that describe information about the object, such as a patient's name, birth date, address, and phone number. Each object also has behaviors. At this point in the development of the evolving system, the behaviors are described by operations. An operation is nothing more than an action that an object can perform. For example, an appointment object can probably schedule a new appointment, delete an appointment, and locate the next available appointment. Later on during the development of the evolving system, the operations will be implemented as methods.

# Messages

Each object also can send and receive messages. Messages are information sent to objects to tell an object to execute one of its operations. Essentially, a message is a function or procedure call from one object to another object. For example, if a patient is new to the doctor's office, the system sends an insert message to the application. The patient object receives the instruction (the message) and does what it needs to do to insert the new patient into the system (the behavior).

# Interface

Interface is a class that only have virtual functions that are meant to be overrident in classes that use the interface. Interface is represented like a normal class except the $"<<type>>"$ notation is shown above the name of the class.
