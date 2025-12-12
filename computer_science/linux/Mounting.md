# Mounting

## Mount

To access a directory or file in the UNIX or Linux system, it must be associated with a path in the directory tree. To access a directory, file, or file system in addition to the initial directory tree, it needs to be mounted using the mount command. Most file systems are related to either disk partitions or disk-based logical volumes, but they can be anything from external hard disks to file systems on SD cards, Universal Serial Bus (USB) storage, digital video disks (DVDs), and other removable storage devices across the network.

The mount command maps a directory, which can be an entire file system, into the existing directory tree. The point where the new directory connects into the current directory tree is called the mount point. The previous contents of the mount point become inaccessible once the new directory or file system is mounted and stay inaccessible as long as the other directory or file system is mounted there. Mount points are usually empty directories, even though they do not have to be.

The point where the new directory connects into the current directory tree is called the mount point. The previous contents of the mount point become inaccessible once the new directory or file system is mounted and stay inaccessible as long as the other directory or file system is mounted there. Mount points are usually empty directories, even though they do not have to be.

mount - the mount command maps a directory, which can be an entire file system, into the existing directory tree.

- mount [option…] directory or mount [option…] device or mount filesystem mount_point
  
For example, the following command will connect the file system stored on the disk partition represented by /dev/sda4 to the path /usr/empty1:

mount /dev/sda3 /usr/empty1

The command ls /usr/empty1 will show the file system’s contents as long as it stays mounted.

![image](https://user-images.githubusercontent.com/73081144/145738037-6ec475d9-3672-48e1-a5a5-669a33449484.png)

1. Make a mount point (mkdir /usr/empty1).
Note: Doing an ls -l on the new mount point shows that it is empty.

2. Mount the new file system (mount /dev/sda3 /usr/empty1).

3. Doing an ls -l on the new mount point now shows the file system from /dev/sda1.

To access the files on a CD-ROM, mount the CD-ROM in the following directory tree:

mount /dev/cdrom /media/cdrom

In this command, the CD-ROM is /dev/cdrom, and its mount point is /media/cdrom. After the command is run, any file located on the CD-ROM is now accessible to the system.

## Unmount

unmount - used to disconnect file systems from the directory tree.

- umount /dev/sda3 (unmount device sda3) or umount /usr/empty1 (unmount mount point /usr/empty1)

The umount command unmounts or disconnect the mounted file system when it is no longer needed.

Note that the umount command will complain if the mounted file system is in use when it is being unmounted. For the umount command to work, the file system to be unmounted (or detached from the directory tree) cannot have any open files or processes running

Both the mount and umount commands require root (superuser) privileges to run successfully.

*Note: In most modern Linux system desktop environments, mounting the CD-ROM with the command*

*mount /dev/cdrom /media/cdrom*

*will be done automatically when you insert the CD, and unmounting the CD-ROM with the command umount /dev/cdrom (unmount external device) or*

*umount /media/cdrom (unmount mount point)*

*will also be done automatically when you click on the “Eject” button on the device or the "Safely Remove" widget on the screen*

## Bind Mounts

Bind mounts mount one path (file or directory) into another path, and the bind mount command is as follows:

mount --bind olddir newdir

or

mount -B olddir newdir

This makes the same contents accessible in two places. It is also possible to bind (mount) a single file on a single file. In this case, olddir and newdir are replaced with file paths. However, this attaches only part of the file system, not all the possible submounts (subdirectories). To bind the entire file system’s hierarchy in a second place, it is necessary to use the --rbind or -R (recursive) option, as follows:

mount --rbind olddir newdir

or

mount -R olddir newdir

The file system mount options will remain the same as those of the original mount point. The mount options can only be changed by a separate remount command, such as the following:

mount -o remount,ro newdir
