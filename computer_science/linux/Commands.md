# Linux CLI Commands

## pwd Command

pwd - prints path of the current directory.

## ls Command

ls - lists files in the currect directory.

- -l - shows details about files
- -i - displays the inode number
- -a - shows all files, even hidden ones
- The first character gives the file type, and the next nine characters are the permission mask, or permission bits, that shows (and controls) who can read, write (change), and execute the file and its contents.
- Next comes the link count, which is the number of links to the file’s inode (something that stores the metadata—all of the information about the file except its name). This is followed by the file’s owner’s username, which tells who owns the file and who is most responsible for that file. This can be any user’s name, be it a regular user, a system user or daemon, or even an application name.
- The group name shows the group that the file is associated with and gives the permissions for all of the members in that group.
- The next attribute shown is the file’s size, which is given in either bytes or blocks (in UNIX, the default size for a block of data is 4096 bytes).
- The next attribute is the time stamp for when the file was created or when it was modified or changed. This time stamp is given in a date and a time format, as shown with month (three characters), day (2 characters), and four digits for the time, two for the hour on a 24-hour clock (e.g., 1:00 p.m. = 13, 6:00 p.m. = 18, and so on), and two for the minute, separated by a colon.
- Finally, the name of the file is shown.
- If it is a link file, the name of the file linked to is shown (mtab -> /proc/mounts).

![image](https://user-images.githubusercontent.com/73081144/145730485-4bf9128d-e2a8-4219-9bfb-57fc1ca2fba0.png)

## cd Command

cd 'dir' - move to other directory.

- this is where directory is the name of a directory path to which you want to change. The path could be a full or partial path.

| Command | Description |
| ------- | ----------- |
| cd or cd $HOME or cd ~ | Navigates to your home directory. |
| cd .. | Navigates to a parent directory. |
| cd . | Navigates to the current directory. Although this is not practical, it can still be done. |
| cd / | Navigates to the root directory. |
| cd child | Navigates to a child directory named child. |
| cd ../sibling | Navigates to a sibling directory named sibling. |
| cd ../.. | Navigates to the parent’s parent. Or, navigates up two levels. This would be the “grandparent.” |
| cd ../../.. | Navigates to the parent’s grand-parent. Or, navigates up three levels. |

## cat Command

cat 'file' - used to display the contents of a file, but can be used to create one

## chmod Command

chmod - changes the permissions mask on a file or directory.

- chmod –[options] mode filename
- -R (recursive) - this includes all of the files in the directory and in all subdirectories.
- -f (force) - this forges ahead with all of the objects even if errors occur.
- -v (verbose) - this displays feedback on all of the files processed and the changes made.
  
Symbolic permissions coding allows you to add or remove permissions by specifying the set of permissions (user, group, or other) that you want to change. When using symbolic permissions, the chmod format is as follows:

chmod [references][operator][modes] filename

References refer to the set of permissions: u for user, g for group, o for other, and a for all, which includes all three. Operator refers to adding or removing permissions: + for add, - for remove, and = for changing the set of permissions for that reference. Modes are the permissions themselves: r, w, or x. For example, if you want to add write to the group permissions for the file lotsofun, the chmod command would be as follows:

chmod g+w lotsofun

To remove write permissions (w) for all sets (a), use the following command:

chmod a-w lotsofun

To set the permissions for the owner and the group (ug) to read and execute (rx) only (no write permission), use the following command:

chmod ug=rw lotsofun

## chown Command

chown - this is used for changing the ownership (and group assignment)

- chown [– options] newowner filename
- newowner can be either a log-in name or a user ID, and it can also take the form of newowner:newgroup and change the group as well as the owner.
- h: This changes soft links.
- help: This shows the help message for chown.
- R: This stands for recursive. (i.e., change the owner of all files from this directory down; does not work with filenames)
- V,c: This stands for verbose and displays feedback on all of the files processed and the changes made.

For example, you own willie.txt, but you want to give it to another user on the system named ww543267. You would use the following command:

chown ww543267 willie.txt

You want to change both the owner and the group of willie.txt to that of ww543267 and ww543267's group, lumpagroup. Using chown to change both the owner and group, you would use the following:

chown ww543267: lumpagroup willie.txt

## chgrp Command

chgrp - this is used for just changing the group assignment.

- chgrp [-options] newgroup filenames
- f: This enables silent mode, which means that errors are not printed.
- R: This stands for recursive. (i.e., change the group of all files from this directory down; does not work with file names)
- v: This stands for verbose. Changes are described.
- help: This displays a help message and text.

For example, if you want to change the owning group of the file gloop.txt to the group named bucket, the command would look like the following:

chgrp bucket gloop.txt

To change the owning group of the directory /gobstopper/testing and all of the files and subdirectories inside it to the group slugworth, the following command is used:

chgrp -R slugworth /gobstopper/testing

## mount & unmount Commands

mount - the mount command maps a directory, which can be an entire file system, into the existing directory tree.

- mount [option…] directory or mount [option…] device or mount filesystem mount_point

- -h - prints a help message.
- -V - prints the mount's version information.
- [-t type] - lists all mounted file systems (of file type “type”). The option -l adds labels to this listing ([-l] [-t type]).
- -a - mounts all regular file systems listed in the file system catalog, that is, all the file systems listed in the /etc/<filesystem>. This is usually executed by the startup scripts at boot time.
  
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

unmount - used to disconnect file systems from the directory tree.

- umount /dev/sda3 (unmount device sda3) or umount /usr/empty1 (unmount mount point /usr/empty1)

Both the mount and umount commands require root (superuser) privileges to run successfully.

## mkdir Command

mkdir - makes new directory

- mkdir [-options] directory-name
- -p - used for creating a parent directory that does not exist in the path.

For example, to create a directory named R, you would enter the following:

mkdir R

You can create several directories with a single mkdir command as long as you separate each directory name with a space.

mkdir R S E

For creating both parent and child directory, use -p option. For example, the command mkdir G/C2 will generate an error if the parent “G” is nonexistent. However, the command mkdir -p G/C2 will create the parent, G, first and then its child directory, C2, next.

## rmdir Command

rmdir - removes directories

- rmdir [-options] directory-name
- when using the command to remove a directory, the directory must be empty.
- your current directory position cannot be the directory you are trying to remove.

If you want to remove parent directory and its children, use -p option (v stands for verbose):

rmdir -pv q/w/e/r/t/y

However, it only works if the directories are empty.

## rm Command

rm - removes everything in path

- rm [-options] path
- use -r option if want to remove directory.

## mv Command

mv - used to mode files

- mv source destination

This is where source is the file you want to move and destination is the file the source will be copied to. With cp, you end up with two files (the original and the duplicate), and with mv you end up with one (the newly moved/renamed one). For example, to move a file named f7.dat to f8dat, you would enter the following command:

mv f7.dat f8.dat

## touch Command

touch - create an empty file or to change a file’s modification timestamp.

- touch [-options] file_name

You can also use the command to create an empty file. For example, to create an empty file named FunDay.dat, you would enter the following:

touch FunDay.dat

## echo Command

echo - used to display text on the screen, but can be used to create a file

Although the main use of the echo command is to display (echo) text on the screen, it can be used to create a file by using the following general format:

echo text > filename

This is where text is the text you want to be saved to the file named filename.

So, for example, echo hi > f1.dat would place the text hi in the file name f1.dat.

## cp Command

cp - used to copy files

- cp source destination

This is where source is the file you want to copy and destination is the file the source will be copied to.

For example, to copy a file named f3.dat to f4.dat, you would enter the following command:

cp f3.dat f4.dat

To copy all files of the same type:

cp *.tar \Desktop

To copy all files:

cp -v *.* \Desktop

# pushd and popd Commands

pushd - saves current directory for future use.

- pushd path (path where you want to go)

used with popd

popd - returns you to the last pushd directory.

If you use multiple pushd, it stacks paths (first in last out).

# which Command

which - shows where a file is located

- which filename

# history Command

history - prints commands that you used in a session.

# grep Command

grep - searches line by line for a specified pattern and then outputs any line or word that matches the pattern.

- grep [-options] ‘pattern’ [file]

If the file argument is omitted, grep reads from the standard input. It is best to enclose the pattern within single quotes. For example, the grep command grep ‘apple’ fruitlist.txt will print out (display on the console) all lines containing "apple" from the fruitlist.txt file; therefore, lines with words such as "pineapple" or "apples" are printed, as shown in the following:

![image](https://user-images.githubusercontent.com/73081144/146870393-64771975-dc2b-400a-84aa-cca144f67212.png)
