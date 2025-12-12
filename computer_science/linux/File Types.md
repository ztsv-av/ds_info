# File Types

| ls -l | Type             | Description                                            |
|-------|------------------|--------------------------------------------------------|
| d     | directory        | Container for other files                              |
| l     | symbolic link    | Reference to another file                              |
| c     | character device | Represents character-based hardware (e.g. serial port) | 
| b     | block device     | Represents block-based hardware (e.g. floppy dist)     | 
| p     | pipe (FIFO)      | Communcations file                                     |

- Regular files: These include text files, data files, executable (program) files, and shared libraries.
- Directories: These are special files that have information about the files that they contain. These also organize the files. Each directory also contains two special references, “.” and “..”, which refer to the directory itself and its parent directory respectively and cannot be deleted. Note that in reality, only the names and metadata of the files are stored in the directory file, not the file itself.
- Character and block device files: These files provide standard interfaces to the kernel drivers for the various internal and external peripherals of the computer. Block devices read and write whole blocks of data (a data block here is equivalent to an entire sector, or 64KB, of the old disk drives). Character devices read and write only one character (8 bits, or a byte) at a time.
- Link files: Although they are not really a separate file type, these types of files, also known as links, connect (link) one file inside one directory to a file inside another directory, providing a symbolic path to the location of that other file. Links create the illusion that a file exists in more than one place at the same time. There are two types of links, as follows:
- - Hard links: These are limited to files inside a single file system (i.e., a disk partition or a logical volume).
- - Soft links: These are not limited to files in a single file system and can, for example, link to another file system on another partition or logical volume on the disks.

There are three types of executable files: binaries, which the system runs directly, scripts, which must be interpreted by a shell, and compiled files, which must be interpreted by some particular program.
