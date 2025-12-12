# Disk Managment

In Linux, drives have the following names:
- all drives names start with 's' if it is SATA, SSD, Scsi;
- all other drives names start with 'h', like ide.

## Partitions
If you want to have multiple drives from one drive, you partition it.
- if drive has 1 partition, it will have the following name: Sda1 (path: /dev/Sda1)
- if drive has 2 partitions, it will have the following names: Sdb1, Sdb2 (paths: /dev/Sdb1, /dev/Sdb2)
- etc.
