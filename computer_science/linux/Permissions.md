# File Permissions

When using ls -l, it lists files and their permissions.

![image](https://user-images.githubusercontent.com/73081144/145730485-4bf9128d-e2a8-4219-9bfb-57fc1ca2fba0.png)

The first character gives the file type, and the next nine characters are the permission mask, or permission bits, that shows (and controls) who can read, write (change), and execute the file and its contents. These permissions are divided into three three-character sets: the first three show the permissions for the file’s user or owner (OWNER), the next three show the permissions for the file’s group (GROUP) (usually the same group as the user’s), which are the permissions for anyone that is a member of that group, and the last three show the permissions for every other user on the system that is neither the user nor a member of the designated group (WORLD). Note that there are three more hidden bits associated with each set of permissions. These characters set the way that the file operates, called the file’s mode.

| Character | Name | Permission |
|-----------|------|------------|
| r | read | Read or access the contents of the file or list or show the contents of the directory |
| w | write | Write, change, or modify the contents of the file or directory, and create or delete a file in the directory|
| x | execute | Execute or run the file as a program, script, or process, or allow access into the directory |
| - | denied | That permission is denied | 

| Binary | Octal | Permission Set |	Permissions |
|--------|-------|----------------|-------------|
| 000 |	0 |	--- | All permission denied |
| 001 |	1 |	--x | Execute only |
| 010 |	2 |	-w- | Write only |
| 011 |	3 |	-wx | Write and execute only |
| 100 |	4 |	r-- | Read only |
| 101 |	5 |	r-x | Read and execute only |
| 110 |	6 |	rw- | Read and write only |
| 111 |	7 |	rwx | Read, write, and execute all |

## chmod, chown, chgrp

You convert the permissions field to binary and octal because you can change the mode of the file or directory with the chmod (change mode) command. The chmod command is used to change the permissions mask on a file or directory, and there are several ways to code it: numeric, symbolic, or absolute.

chmod - changes the permissions mask on a file or directory.
chmod [-options] mode filename

For example, if you want to change the permissions for the file named charlie.sh to read, write, and execute for the user and to simply read for both the group and the other users, making it -rwxr--r--, which converts to octal 744, the chmod command can be configured as follows:

chmod 744 charlie.sh
chmod rwxr—r—charlie.sh


![image](https://user-images.githubusercontent.com/73081144/145730624-61d4c6da-2d3b-4cb6-b5a4-7a2b22300dbd.png)

chown - this is used for changing the ownership (and group assignment)
chown [–options] newowner filename

For example, you own willie.txt, but you want to give it to another user on the system named ww543267. You would use the following command:

chown ww543267 willie.txt

You want to change both the owner and the group of willie.txt to that of ww543267 and ww543267's group, lumpagroup. Using chown to change both the owner and group, you would use the following:

chown ww543267: lumpagroup willie.txt

chgrp - this is used for just changing the group assignment.
chgrp [-options] newgroup filenames

For example, if you want to change the owning group of the file gloop.txt to the group named bucket, the command would look like the following:

chgrp bucket gloop.txt

To change the owning group of the directory /gobstopper/testing and all of the files and subdirectories inside it to the group slugworth, the following command is used:

chgrp -R slugworth /gobstopper/testing

## Extended File Attributes

There are other special permissions apart from the normal file permissions of read, write, and execute. These are also set with the chmod and chown commands. These permissions are the Set owner User ID up on execution (SUID), Set Group ID up on execution (SGID), and the sticky bit.

### The SUID Bit

The SUID is a special type of file permission. Normally in Linux or UNIX, when you execute a program or script file, it inherits the permissions of the user that executed it. The SUID gives temporary permission to a user to execute a program or script file with the permissions of the file owner rather than his or her own. This means that the user executing the program or script gets to do so using the file owner’s permissions, his or her UID, and his or her GID, allowing the user to execute the file, program, script, or command as though he or she were the owner. The SUID is used under the following circumstances:

- when root login is required to execute some commands, programs, or scripts;
- when giving permissions to a particular user or users is not warranted;
- when some programs need to be run as the owner.

The SUID can be set with a numeric or symbolic chmod command. The SUID replaces the x in the user permissions with an s. The symbolic format is the simplest and appears as follows:

chmod u+s jimfile1.txt

When using the numeric format, the SUID is set with a number 4 in front of the permissions number. For example, if you want to set the permissions of the file jimfile1.txt to 766 with the SUID set, the chmod command looks like the following:

chmod 4766 jimfile1.txt

When the SUID is set, the ls -l command will show the x in the owner permissions field replaced by s or S.

-rwsrw-rw- 1 jim jimgroup 148 Dec 22 03:46 jimfile1.txt

-rwSrw-rw- 1 jim jimgroup 148 Dec 22 03:46 jimfile1.txt

A capital S indicates that the file or directory did not have x permissions when the SUID was set. To convert the capital S to a little s, you must first add an execute permission to the file or directory and then set the SUID by adding the s again, as follows:

chmod u+x jimfile1.txt

chmod u+s jimfile1.txt

After that, the ls –l command will show the x in the owner permissions field replaced by s:

-rwsrwxr-x 1 jim jimgroup 0 Dec 27 11:24 jimfile1.txt

### The SGID Bit

The SGID is a special type of file permission given to a file or directory. Normally in Linux or UNIX, when you execute a program or script file, it inherits the permissions of the user that executed it. The SGID gives temporary permission to a user to execute a program or script file with the permissions of the file’s group, essentially making the user a member of that group. The SGID is similar to the SUID. The difference between them is that the SUID provides owner permissions, while the SGID provides group permissions, allowing the user to execute a program or script file with the permissions of the file group rather than his or her own (Nemeth et al., 2011).

The SGID can be set with a numeric or symbolic chmod command. The SGID replaces the x in the group permissions with an s. The symbolic format is the simplest and appears as follows:

chmod g+s jimfile1.txt

When using the numeric format, the SUID is set with a number 2 in front of the permissions number. For example, if you want to set the permissions of the file jimfile1.txt to 766 with the SGID set, the chmod command looks like the following:

chmod 2766 jimfile1.txt

When the SGID is set, the ls -l command will show the x in the owner permissions field replaced by s or S.

-rwsrwSrw- 1 jim jimgroup 148 Dec 22 03:46 jimfile1.txt

A capital S indicates that the file or directory did not have x permissions when the SGID was set. To convert the capital S to a little s, you must first add an execute permission to the file or directory and then set the SUID by adding the s again, as follows:

chmod g+x jimfile1.txt

chmod g+s jimfile1.txt

After that, the ls -l command will show the x in the group permissions field replaced by an s, as follows:

-rwxrwsrx- 1 jim jimgroup 0 Dec 27 11:24 jimfile1.txt

### The Sticky Bit

The sticky bit is a special permission that is mainly used on directories to avoid the deletion of the directory and its contents by other users, even though they have write permission on the directory. If the sticky bit is enabled on a directory, the directory’s contents can only be deleted by its owner and the root user (superuser). No one else that is an other (someone that is neither the owner nor a group member) can delete anything in a directory where the sticky bit is set. This is used as a security measure to avoid the deletion of critical directories and their contents, files, and subdirectories, even though the other permission set gives them full rwx permissions. The sticky bit can be set for files, but most of the time, it is not required.

The sticky bit can be set with a numeric or symbolic chmod command. The sticky bit replaces the x in the other permission set with a t or T. The symbolic format is the simplest and appears as follows:

chmod o+t /home/jimsfiles

Because it does not change anything inside the permissions field and only affects the other permission set, it is not necessary to specify the o, so the chmod can be as follows:

chmod +t /home/jimsfiles

When using the numeric format, the sticky bit is set with a number 1 in front of the permissions number. For example, if you want to set the permissions of the directory /home/jimsfiles to 757 with the sticky bit set, the chmod command looks like the following:

chmod 1757 /home/jimsfiles

When the sticky bit is set, the ls -l command will show a t or T at the end of the permissions field, as follows:

drwsrw-rwt 1 jim jimgroup 148 Dec 22 03:46 /home/jimsfiles

A capital T at the end of the file permissions field indicates that the directory did not have executable permission for other users when the sticky bit was set. To convert the capital T to a little t, you must first add an execute permission for others in the directory and then set the sticky bit by adding the t again, as follows

chmod o+x /home/jimsfiles

chmod o+s /home/jimsfiles

After that, the ls -l command will show the x in the other permissions field replaced by a t, as follows:

drwxrw-rxt 1 jim jimgroup 0 Dec 27 11:24 /home/jimsfiles
