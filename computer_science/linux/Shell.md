# Linux Shell

The shell is a command line interpreter, which means that it is a program and has its own programming language.

All of the shells in the C Shell family (csh, tcsh, and so on) are more structured and follow the same basic formatting as the C programming language. All the shells in the Bourne family (sh, ksh, bash, and so on) are pretty much free-form and do not require any particular structure.

| Name | Abbreviation | Info |
| ---- | ------------ | ---- |
|Bourne Shell | sh | This is the oldest of the shells and was designed by Steve Bourne. It is considered to be a bit primitive but is very good for scripting. |
| C Shell |	csh | This is probably the most popular shell. However, even though it adds many nice features that are unavailable in the Bourne shell (e.g., history and job control), it is quite buggy for heavy users. |
| KornShell | ksh | David Korn wrote this shell to be compatible with the Bourne shell but included the cool features introduced by the C Shell. However, it went one step further beyond the C Shell and introduced history editing. |
| Bourne Again Shell | bash | This is similar to the KornShell but with some additional features, such as a built-in help command. |
| TC Shell | tsch |	This is an extended version of the C Shell with the features introduced by ksh and bash. |

The most common and supported shells on most UNIX systems are the following:

- Bourne shell (sh)
- C shell (csh)
- Korn shell (ksh)
- Bourne-again shell (bash)
All of these operate pretty much the same from the command line, but they have differences in syntax, especially in relation to scripts.

1. The Bourne shell (sh), the original and standard UNIX shell, is found on every UNIX (and most Linux) system, and so is used to administer most of the systems, because a Bourne shell script can be run on any flavor of UNIX without any changes. The Bourne shell was first provided in UNIX V7 (the seventh edition of UNIX developed at AT&T) in 1979, and it was named after Stephen Bourne, its developer. For example, the rc start, stop, and shutdown scripts are Bourne shell scripts. The default Bourne shell prompt is the dollar sign "$" (Milo, 2014).

2. The C shell (csh) was developed later on, created by Bill Joy at the University of California, Berkeley. It has been widely distributed, beginning in 1978 with the second release of the Berkeley Software Distribution (BSD). At that time, Joy, a C-programmer, wanted a shell with scripting rules that more closely resembled those of C. The csh added the following features:

- Command line history (which stores a list of entered commands that can be accessed by pressing the up and down arrow keys)
- Aliasing (which allows the substitution of one command for another)
- Built-in arithmetic functions
- Filename completion (like modern word completion applications)
- Job control commands
- Although popular, particularly with system administrators who are also programmers, Bourne shell scripts are simpler, run faster than the same scripts written in csh, and are not used often. The default C shell prompt is the percent sign "%" (Milo, 2014).

3. The Korn shell (ksh) is an updated version of the Bourne shell, which was developed by David Korn of AT&T. The Korn shell added features like those of the C shell (e.g., aliasing, wildcards, built-in arithmetic, and job control), plus a few more, such as making the history editable, coprocessing, and some special debugging functions. The Bourne shell is upward-compatible with the Korn shell, allowing Bourne shell scripts to run just fine. The default Korn shell prompt is the dollar sign "$," similar to that of the Bourne shell.

| Facility | Bourne | C | TC | Korn | Bash |
| -------- | ------ | - | -- | ---- | ---- |
| command history | No | | Yes | Yes | Yes | Yes |
| command aliases | No | | Yes | Yes | Yes | Yes |
| shell scripts | Yes | | Yes | Yes | Yes | Yes |
| filename completion | No | | Yes* | Yes | Yes* | Yes |
| command line editing | No | | No | Yes | Yes* | Yes |
| job control | No | | Yes | Yes | Yes	 | Yes |
(* = Not default setting)

Although often called Linux shells, Bourne-again (bash) and Tenex C or TC (tcsh) shells are free and available and can be compiled into any UNIX system, and more and more modern flavors of UNIX, such as Sun’s Solaris, have bash and tcsh bundled in already. However, it is important to remember that modern Linux distributions include a choice of graphical user interfaces (GUIs), such as GNU’s GNOME and KDE. In Linux, the Bourne-again shell (bash) and the TC shell (tcsh) are the most popular, but bash is the default for Debian and Ubuntu. Bash was written by Brian Fox in 1989 for the GNU Project as a free replacement for the Bourne shell. The “t” in tcsh comes from Tenex, an early UNIX-like OS. Ken Greer at Carnegie Mellon University developed tcsh, first as a standalone shell, and finally, in 1981, merged it with the C shell. In 1983, the tcsh was later added to by Mike Ellis of the Fairchild Laboratory for Artificial Intelligence Research (Milo, 2014).

Bash is an expanded and updated version of the Bourne shell, just as the TC shell is of the C shell. Although these are the most common shells, there are literally dozens more available. Many programmers and system administrators have developed shells that are specific to their personal requirements, but Bourne and C are considered the two main branches of shells.
