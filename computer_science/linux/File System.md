# Linux File System

The UNIX or Linux file system is a hierarchy that starts at the / (root) directory and continues downward through various levels of directories and subdirectories. The Linux file system is based upon a hierarchy called the tree structure. The topmost directory is called root; it is referenced by the forward slash symbol (/). Note that the root directory differs from the root user. One is the top of the file system tree. The other is a username you use to log in and perform administrative tasks.  
The two main benefits of the hierarchical tree structure are organization and security. In terms of security, you can limit what a user can see and do in a directory by setting permissions at the directory level. This may mean that another user may not have access to the directory itself or the files or other child directories within it.

## System Directories

| Path | Description |
| ---- | ----------- |
| / | The root directory; contains directories that are needed at the top level |
| /bin | Contains the binary (executable) files of the operating system (OS); available to all users |
| /boot | Contains the files for booting the system |
| /dev | Contains the device drivers |
| /etc | Contains supervisory commands, configuration files, disk configuration files, valid user lists, groups, Ethernet files, trusted hosts list, where to send critical messages, and so forth |
| /home | Contains the home directories for users |
| /kernel | 	Contains the kernel files |
| /lib | Contains shared library files and sometimes other kernel-related files |
| /lost+found | Contains files left in an inconsistent state due to a software or hardware bug, unlinked because of an unscheduled system halt (crash, kernel panic, or power failure), or unreferenced data fragments deposited after a file check (fsck) |
| /mnt | Contains the information about other file systems mounted (virtually added or connected) to the main file system, such as other disks and CD/DVD-ROM drives |
| /proc | Virtual file system; contains runtime system information (e.g., system memory, devices mounted, and hardware configuration) |
| /root | Superuser’s home directory (Linux only) |
| /sbin | Contains the binary (executable) files for system administration |
| /tmp | Holds temporary files used between system boots |
| /usr | Contains miscellaneous files for different purposes: administrative command files, shared files, library files, and so forth |
| /var | Contains variable-length files, such as logs and print files |

## Paths

The list of directories need to be passed through to locate a particular file plus its filename form—the pathname. Pathnames can be absolute or relative. Relative pathnames start at the current directory. Absolute pathnames start at / (root) and list every directory along the way. To reach the directory somestuff in the directory mystuff, which is itself inside the directory ringo (whose absolute pathname is /home/ringo), the relative pathname is mystuff/somestuff, which is mystuff, the directory between somestuff and ringo, plus the destination, somestuff. On the other hand, the absolute pathname starts at / (root) and runs through home, ringo, and mystuff before reaching somestuff, so its absolute pathname is /home/ringo/mystuff/sometuff.

![image](https://user-images.githubusercontent.com/73081144/145737454-0f789266-a902-4a23-9e4d-e9e288eb8581.png)

## Disk Drive
Before you learn about file systems, you need to learn about the disk drive. A file system is stored on a disk drive, so it is important to understand what is beneath the file system. Physically, a disk drive has a series of platters, like a stack of dining plates. These platters are divided into sectors and tracks. A sector is a pie-shaped wedge section of the hard drive and a track is a concentric circle on the disk. Data is stored in files on the hard drive at a physical location using sectors and tracks.
![image](https://user-images.githubusercontent.com/73081144/145729232-9d322672-c7fd-4e08-a2a5-36545ea7aa5e.png)

## Blocks
At the logical level, Linux allocates space for data in units called blocks. A block is a group of sectors on disk. The default block size is 1,024 bytes. Blocks have unique identifying numbers associated with them. Linux uses a partition to manage a group of blocks. The file system keeps track of these numbers. This allows you to simply refer to the data by the name of the file it resides in.

For example, assume your resume is stored at sector 10 and track 4 on a particular disk. Instead of referring to the data located at sector 10, track 4 (the physical location), you would open your resume by its name (the logical location). You never even need to know the physical location of the file because the file system keeps track of it.

## Index Table
The file system keeps an index table in memory for locating files. The file system logically retrieves data stored physically on the disk.
Note that the index table is analogous to the index in the back of a book. When you need to look up a term, you go to the index. The index contains terms and the pages they are located on in the book. Once you find the page location, you can then proceed in the book to the appropriate page reference for the term.

## File System Types
Linux supports many file system types. A few of the file system types will be mentioned here. They are as follows:

- ext2: The ext2 file system is supported by Linux. When an improper shutdown occurs however, the file system is required to go through a file system check (with the fsck command). An improper shutdown is an abrupt loss of power resulting in potential file system table corruption. Best practices dictate you go through a proper shutdown using the Linux shutdown command to prevent this corruption.

- ext3: The ext3 file system is a newer, improved version of ext2. It has a disk journaling system that keeps track of changes in the file system. This allows an abrupt loss of power without having to perform a file system integrity check.

- NFS: The Network File System was developed by Sun Microsystems and allows you to use a file system partition from another Linux system as if it were local.

- Msdos: The msdos file system type supports the Microsoft Disk Operating System (MS-DOS) 8.3 file names. With 8.3 file names, you can have only eight characters followed by a dot and then three additional characters called the extension. The extension is used to associate an application to a file.

- UNIX File System (UFS) is also known as the Berkeley Fast File System (BFFS) as it originated from the original UNIX file system. Some of the features are as follows:
- - A superblock containing a magic number. The Magic Number (MN) identifies the filesystem as a UFS type. The MN also contains other data about the file system’s size.
- - A set of book blocks that is located on the disk at the beginning of the UFS partition.
- - A group of blocks containing a backup copy of the superblock, the number of inodes, and the quantity of data blocks.

- UNIX Zettabyte File System (ZFS) is a combination of a filesystem and a Logical Volume Manager (LVM). Some of the ZFS features are as follows:
- - Data protection using an algorithm to provide redundancy.
- - Data compression using an algorithm to store data efficiently.
- - Integration of the filesystem and LVM making management of the partition more efficient compared to a filesystem-only system.
- - Data integrity by protecting user data from hardware spikes and data loss.

- Linux ext4 (EXTended Fourth Filesystem) is essentially version 4 of the ext3 filesystem previously discussed. Features of ext4 include the following:
- - Backward compatibility with ext2 and ext3 filesystems for older systems running these filesystems.
- - Journal check-summing for data reliability.
- - Support of large filesystems exceeding 100 TeraBytes (TB).
- - Quick filesystem checking with the fsck command by skipping unallocated data blocks.
- - More accurate timestamps of data for those applications needing a precise time.

- Linux ReiserFS was developed by Hans Reiser as the first journaling filesystem. Some of the features include the following:
- - Journaling of data to ensure accuracy and reliability by keeping track of data that has not yet been written to disk. Journaling improves reliability of data in case of a system crash.
- - Dynamic disk allocation on allowing you to add to (grow) the filesystem while the system is up and running. Previously, you would backup your data, delete the filesystem, create it with the larger size, and then restore your data.
- - Reducing fragmentation of data thereby speeding up the system’s performance.
