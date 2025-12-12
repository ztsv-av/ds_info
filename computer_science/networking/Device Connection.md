# Device Connection


When you connect Ethernet devices, it's important that the transmit (Tx) wires from one device are matched with the receive (Rx) wires on the other device. To help understand how to connect devices together, be aware of the following:

- Network interface cards in workstations and routers send data on the transmit pins and expect to receive data on the receive pins.
- Crossing is automatically performed within a hub or the switch between ports used for connecting devices to the hub or a switch.
- Uplink ports on hubs and switches are not crossed.

## Cable Types

1. Straight-Through - A straight-through cable connects each wire to the same pin on each connector (pin 1 to pin 1, pin 2 to pin 2, etc.). A straight-through cable is used when the crossover is performed with a hub or a switch. Use a straight-through cable when connecting the following devices:
- Workstation to a regular port on a hub or switch
- Router to a regular port on a hub or a switch
- Regular port on a hub or switch to an uplink port on a hub or a switch

2. Crossover - 	A crossover cable matches the transmit (Tx) wires on one connector with the receive (Rx) wires on the other connector. A crossover cable is used when crossing is not performed automatically or when crossover is performed twice. Use a crossover cable when connecting the following devices:

- Workstation to a workstation, router to a router, or workstation to a router (in a back-to-back configuration)
- Uplink port on a hub or switch to an uplink port on a hub or a switch
- Workstation or router to the uplink port on a hub or a switch
- Hub or switch using a regular port to a hub or a switch using a regular port

3. Rollover - A rollover cable is a cable with an RJ45 connector on one end and an RS232 (serial) connector on the other end. Use a rollover cable to connect the serial port on a workstation to the console connector on a router or switch, and then run a terminal emulation program on the workstation to connect to the console of the router or switch to perform configuration and management tasks.
A rollover cable might also have an RJ45 connector on both ends, requiring an adapter to convert from the RJ45 connector to the serial cable. When terminated with an RJ45 connector on both ends, the wires within the connectors are rolled over to the opposite connector as follows:

- Pin 1 is connected to pin 8
- Pin 2 is connected to pin 7
- Pin 3 is connected to pin 6
- Pin 4 is connected to pin 5

## Cable Facts

As a general rule, use a crossover cable when connecting two like devices, and use a straight-through cable when connecting different devices or port types.

- If crossover is not performed by either device, use a crossover cable to connect the devices.
- If crossover is performed by both devices, use a crossover cable to perform the crossing three times.
- If crossover is performed by one device, use a straight-through cable.

For most installations, a straight-through cable is used from the hub or switch in the wiring closet to the wall plate in an office, and another straight-through cable is used between the wall plate and the workstation. Crossing is performed at the hub or the switch, not at any of the cables connecting the workstation to the hub or switch.

- To tell the difference between a crossover and a straight-through cable, place the connectors side by side facing the same direction.
- - If the wires are in the same order on both connectors, the cable is a straight-through cable.
- - If the wires are in a different order, the cable is a crossover cable.

Pre-made crossover cables often have a special jacket color (such as red).  However, you cannot rely on the cable color only to tell the difference between a crossover and a straight-through cable.

On some hubs and switches, the uplink port has a button or switch that lets you use it as a regular port (with crossing) or an uplink port (without crossing). On others, the uplink port is shared with one regular port. You can use either port, but not at the same time.

- Some hubs and switches include the letter X in the port labeling to identify ports that perform crossing.
- Most modern switches use Auto-MDI/MDIX, which senses the cable type used and performs crossing based on the cable. For these devices, you do not need to be concerned with which cable you use.
