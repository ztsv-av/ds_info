# Data Storages

The following are a few ways to store computer data:

- Hard disks
- - IDE
- - ATA or PATA
- - SATA
- - SCSI
- - Fibre Channel
- Solid state disks (SSDs)
- Flash memory (i.e., read–write memory chips also used in RAM memory cards and USB flash drives)
- Magnetic tapes
- Optical media (CDs and DVDs)

## Hard Drive

![image](https://user-images.githubusercontent.com/73081144/145735222-71943b2a-7d23-4643-9ffc-f3b62a86e8d5.png)

A typical hard drive contains several, rotating aluminum platters coated with magnetic film. Data are read and written by tiny skating heads that are mounted on a metal arm (or armature) that swings out and back to position them above the correct track of the disk. The heads float just above the surface of the platters, but never actually touch them. If the heads come in contact with the platter, both the head and the platter are destroyed. Reading from the platter is quick, but the mechanical maneuvering to find the particular sector with the particular data is not, and this slows down the throughput.

There are two main sources of delay:

 - seek delay: The time it takes for the head armature to swing into position over the appropriate track
 - rotational latency: The time the system has to wait for the right sector to pass underneath the head as the platter rotates

![image](https://user-images.githubusercontent.com/73081144/145735060-5e21285c-b8c5-4d52-8559-b37989ad49e6.png)

A track is a storage channel, and on a disk the tracks are concentric circles. A set of tracks on different platters but all the same distance from the spindle is called a cylinder. The data on the cylinder can be read without any additional movement of the arm. The heads move fast, but not as fast as the disks spin (i.e., 7,200 revolutions per minute or RPM is standard, but 10,000-RPM and 15,000-RPM drives are available), so any disk access that does not require the heads to move (or seek) a new position is faster. Higher rotational speeds decrease latency and increase the bandwidth of data transfers.

The disk is also divided into sectors, which physically look like wedges, or pieces of pizza, but are actually the divisions of the tracks (i.e., each sector holds the same amount of data bits, with the speed of the disk making the inner sectors run by the disk head slower than the outer ones, meaning that the data density of the outer tracks is less than that of the inner ones). Every piece of data on the disk is defined by an address that is composed of a track, a cylinder, and a sector, where the heads are moved together to the corresponding cylinder and then fine-tuned to the track, and they wait for the sector(s) to move underneath.

Laptops and many desktop Linux systems have only a single disk, whereas most of the larger corporate systems that use Linux or UNIX have many more. They will have two to eight disks connected locally and tens or hundreds of disks connected as RAID, NAS, or SAN storage systems. RAID stands for Redundant Arrays of Inexpensive (or Independent) Disks (Nemeth et al., 2011), whereas NAS stands for Network Attached Storage and SAN for Storage Array Networks (Brown & Kerns, 2017). When the data of a single file are spread across multiple storage devices, the disks are said to be “striped.” The disk striping process divides the file into data blocks and writes those blocks to multiple disks at the same time, providing the advantage of letting the system have extremely large databases or tablespaces while using only one logical device.

## Hard drive types

### IDE

![image](https://user-images.githubusercontent.com/73081144/145735344-0ba53457-cf0a-4e41-8dbe-9acf758fca83.png) - Back of IDE/EIDE Hard Drive
![image](https://user-images.githubusercontent.com/73081144/145735350-311bdeed-9029-4634-9231-22c6ed5ca109.png) - IDE/EIDE Ribbon Cable

Integrated Drive Electronics (IDE) also known as Advanced Technology Attachment (ATA) or Parallel ATA (PATA) and its updated or enhanced version (EIDE) are the standard for IBM-compatible (i.e., PC-compatible), hard drives, and CD and DVD drives. These drives have their controllers on each drive, which allows them to be connected directly to the motherboard.
Each IDE/EIDE connector (channel) can support two drives, and the cables are designed to have three connectors—one for the motherboard and two for drives. The drives do not have to be the same type, and small personal computers (PCs) usually connect one hard drive and one CD/DVD drive. Floppy drives are no longer in much use. PATA disks are medium to fast in speed, capable of huge capacities, and cheap in cost.

### SATA

![image](https://user-images.githubusercontent.com/73081144/145735311-86de93df-605c-4767-9e90-ead76b8d5510.png) - SATA Drive and Connectors
![image](https://user-images.githubusercontent.com/73081144/145735336-59113755-6b5c-4c5f-9007-0b672a5d9d00.png) - SATA Cables

Serial ATA (SATA) drives support much higher transfer rates (3 Gb/s versus Mb/s). SATA simplifies connectivity with only 7 conductors for the data cable and a 15-pin power cable (there are usually separate cables for data and power, but a single 22-conductor connector is available). The smaller data cable allows connectivity to smaller connectors on the motherboard as well (Saypoint, n.d.).

SATA has native support for hot-swapping, the ability to add or replace one hard drive with another without powering down, and command queuing, a function that allows the hard drives to optimize the order in which the received read and write commands are executed. This reduces unnecessary head movement and leads to better performance. Optical drives are also available with SATA connections. SATA drives are more expensive than ATA/IDE drives, but this is expected to change over time.

### SCSI

![image](https://user-images.githubusercontent.com/73081144/145735372-f8871f0b-3d9c-48b9-b5c7-61fea5b9c34a.png)  - SCSI Drive and Cable

The Small Computer System Interface (SCSI) defines a generic data pipe that can be used by all kinds of peripherals. In the past, it was used for disks, tape drives, scanners, and printers, but recently its use has been mostly abandoned, except for drives. SCSI uses parallel cabling. Figure 7 shows an SCSI drive with its connectors and a ribbon cable. Note that the cable has more than three connectors on an IDE/EIDE cable.

Each SCSI bus channel can support 16 devices, although the controller itself counts as a device. Each device has an SCSI address or “target number” that distinguishes it from the other devices on the bus. Target numbers start at 0 and go up to 15, and the SCSI controller is usually target 7 (Disctech, 2018).

Unfortunately, through the years, as the SCSI technology changed, its names also changed, becoming “fast,” “wide,” and even “ultra”, then Ultra2, Ultra3, Ultra-320, and Ultra-640 SCSI. The connectors that were used changed as well. The one that is still being used is the SCA-2, an 80-pin connector with both power and bus connections.

![image](https://user-images.githubusercontent.com/73081144/145735397-04a43f86-14c2-46b3-bb45-bb1b54b325a8.png)  - SCSI Bus Daisy Chain

The SCSI buses use a daisy chain configuration, and though daisy chaining is the common description, it is a bit misleading. Despite being physically wired as a chain, it is electrically a single bus. Figure 9 shows a simple, workstation installation of an SCSI controller and multiple terminators.

The end (last device on the chain) of a parallel SCSI bus must have a terminating resistor (or terminator).

![image](https://user-images.githubusercontent.com/73081144/145735412-5de285b3-8705-4f58-a42a-faeecf45545f.png)  - Internal SCSI Terminator
![image](https://user-images.githubusercontent.com/73081144/145735422-7d7d471c-46b8-4e88-a7b6-f55cb7b37528.png)  - External SCSI Terminator

These terminators absorb signals as they reach the end of the bus and prevent noise from reflecting back onto the bus. This is because the data pulses propagating along the SCSI bus will reflect from an open connector, and those reflections can add and subtract in bits and cause the original data to be corrupted, causing data loss. The terminators absorb the energy from the pulses, eliminating reflections.

Terminators come in four types—internal, external, active, and pass-through. A pass-through can be used at the beginning of the cable for a limited chain of SCSI drives. External SCSI devices have two SCSI ports—identical and interchangeable (i.e., either one can be the input or output, with the external terminator attached to the final device in the chain). Internal SCSI devices are attached via a ribbon cable, so only one port is needed on the device, and the internal terminator is a pass-through.

### SAS

![image](https://user-images.githubusercontent.com/73081144/145735473-f118d013-cdd5-4d91-b546-95501e44c988.png)

Recent versions of SCSI (such as Serial Attached SCSI or SAS, SCSI-over-Fibre Channel Protocol or FCP, and USB Attached SCSI or UAS) are not parallel SCSI, but they use serial communications. Serial Attached SCSI (SAS) is the SCSI version of SATA. It is a point-to-point system and does not use terminators and target IDs. Each SAS device has a Fibre Channel-style 64-bit World Wide Name (WWN), such as those used by storage area network (SAN) systems, assigned by the manufacturer, instead of a Media Access Control (MAC) address that is assigned to each Network Interface Controller (NIC).
The number of devices in a SAS SCSI bus (or SAS domain) is no longer limited to 16 and allows up to 16,384 devices to be connected.

### RAID

RAID (Redundant Array of Independent Disks) is a bunch of disks that operate like one big disk and does two things, as follows:

- improve performance by striping data across multiple drives to work together to read or write data stream
- replicate or mirror data to multiple drives, which decreases the risk of data loss as compared to having a single-disk failure

Mirroring can be done either with or without parity bits. Parity allows the system to check for errors. In its simplest form, a single bit is added to each byte. If the parity is even, the parity bit makes sure that an even number of binary 1s are in the byte. For example, a byte of 10011010 has four 1s, so its parity bit will be 0. However, if the byte were 10111010, it would have five 1s, so the parity bit will be 1 to make an even number of six 1s (Pinder, 2011).

Mirroring writes data blocks bit-for-bit to different drives; if there is a parity scheme, it also writes a parity bit or a multibit checksum for error-correcting. Mirroring is faster but uses twice the disk space, whereas adding parity schemes reduces data throughput because the parity has to be calculated and included during the write and checked and removed during the read.

RAID is described in levels, defining operation and redundancy. An almost-a-RAID configuration called just a bunch of disks (JBOD) allows more than one disk to be combined into a single, larger, virtual drive—no redundancy, parity, or performance gains but lots of disk space.

Types of RAID:
- RAID 0 - uses two or more disks of the same capacity, and it reads and writes the data alternately on each of the drives. Figure 14 shows the data being written to two disks, with the first data block going to Disk 1, the second to Disk 2, the third to Disk 1, the fourth to Disk 2, and so forth.  
![image](https://user-images.githubusercontent.com/73081144/145735689-0d4ee1f0-306a-45d4-89a6-2cfd98dd1e8d.png) - RAID 0

- RAID 1 - uses mirroring, with the data being written to two or more disks at the same time.  
![image](https://user-images.githubusercontent.com/73081144/145735711-476285dd-b514-4ec3-8619-c4e0ceaf90d3.png) - RAID 1
- RAID 10 and RAID 01 - RAID 1+0 (10) and 0+1 (01) combine RAID 1 and RAID 0 in the same system.
RAID 1+0 has two pairs of disks, with the first pair mirrored to the second pair (RAID 1) and the internal data alternated within the pair (RAID 0). RAID 0+1 has two pairs of disks, with the pairs mirrored to each other and the internal data mirrored on each disk.  
![image](https://user-images.githubusercontent.com/73081144/145735727-b569162e-17b5-4085-8d5a-9670d18ef598.png) - RAID 10 and RAID 01
- RAID 5 - adds parity bits, striping both data and parity information across the disks, adding data redundancy and improving performance. It also uses disk space more efficiently than RAID 1, giving a space efficiency of at least 67%, whereas the space efficiency of RAID 1 cannot be higher than 50%.  
![image](https://user-images.githubusercontent.com/73081144/145735742-0d512c0f-8a64-42d2-8e79-56d0e37e663b.png) - RAID 5
- RAID 6 - is similar to RAID 5, but it uses two parity blocks, allowing it to survive the failure of two drives without losing data.  
![image](https://user-images.githubusercontent.com/73081144/145735751-d25e043b-a669-4a22-8a03-cba717f6c2de.png) - RAID 6

## Partitions

![image](https://user-images.githubusercontent.com/73081144/145736109-e467e41c-3077-48ac-a5d3-85b0d4745018.png)

Partitions are logical divisions of physical hard-disk drives that the operating system (OS) treats as independent disks and file systems. Information on each partition is managed as though it is a distinct and separate hard drive. This allows multiple drives to operate as one big drive, or one physical drive to operate as several smaller drives for better efficiency. This was especially important in the earlier versions of UNIX, Linux, and Windows that could not handle large data drives. Dividing a large drive into several, smaller ones reduces the available space on the hard disk because each new logical disk has to be formatted by the OS, which adds overhead the same as on a true physical one. Under UNIX and Linux, a disk cannot be formatted until the disk itself is partitioned (Rouse, n.d.).

A disk partition, or just a partition, is a section or piece of a computer’s hard drive, which is treated as though it were separate from every other segment. Partitions allow users and system administrators to divide a single hard drive into multiple drives of various sizes for a variety of reasons, such as organizing data or data files for more convenient backup and recovery, reducing possible data loss, or even encryption.

Each partition is fixed-size, with its own device file in /etc/dev, and is implemented by the same driver handling the physical device. The actual partitioning scheme uses only a few data blocks at the beginning of the device’s storage area to record the different ranges of data blocks used to make up the different partitions. Partitions are not as common as they used to be; Linux and Solaris (SUN UNIX) use partitions to maintain compatibility with Windows, whereas HP-UX (Hewlett-Packard UNIX) and AIX (IBM UNIX) hardly use them at all, preferring to use logical volume management (LVM).

Although adding a disk, formatting it, and adding it to your file system on a Linux desktop or laptop can be as simple as on a Windows PC, enterprise-level servers using UNIX and Linux have a more complex storage management system; hence, they are reliable, as well as easy to back up and adapt as needs change, and provide high-performance for multiple users (i.e., local and remote).
