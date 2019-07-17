Suggested Readings
==================

For running experiments on real robotics platforms a lot of tools can come in handy. Following are some of the software/tools to get familarized with before diving into running robots in the lab.

Please follow it thoroughly and enjoy the learning!

===================
Ubuntu
===================

Most software for UAVs and robots in lab runs on Ubuntu 18.04 LTS. Please install this particular version, a lot of other software specifically depends on it. We strongly suggest to install a native system, don't virtualize. Do not use Virtual Box, although it works fine, the drop in performance is really noticeable, especially when simulating a real-time flying drone.

===================
Bash
===================

Bash is the standard/default shell in Ubuntu.
Most of the time, when you work in the terminal, you use bash to run programs, for scripting and to manage your file system.

**Skills needed:**

- moving through a file system
- writing and running simple shell scripts
- mounting devices (``fdisk``, ``mount``, ``sync``, ``umount``)
- common commands:
    - ``grep``, ``|``, ``echo``, ``ssh``, ``scp``, ``rsync``, ``cat``


======================================
GIT - code versioning system
======================================

GIT is a powerful versioning system. All our code is stored and versioned using GIT. It allows collaborative work between many people and can be managed completely from the terminal.
Our repositories are hosted at |kumar_git_link|

.. |kumar_git_link| raw:: html

   <a href="https://github.com/KumarRobotics" target="_blank">KumarRobotics</a>

**Tutorials:**

- |git_tut1_link|
- |git_tut2_link|

.. |git_tut1_link| raw:: html

   <a href="https://git-scm.com/docs/gittutorial" target="_blank">Introduction</a>

.. |git_tut2_link| raw:: html

   <a href="https://try.github.io/levels/1/challenges/1" target="_blank">Challenges</a>

**Skills needed:**

- cloning repositories
- committing changes
- pushing and pulling changes to a server
- branching
- merging
- fixing conflicts (will come as they appear :-))

======================================
TMUX - terminal multiplexer
======================================

Tmux is a command line utility that allows splitting a terminal to multiple panels and creating windows (tabs).
It is similar to e.g. Terminator, but runs completely in the command line. Thus it can be used over ssh.

It is scriptable, which makes it ideal for automating simulations, where multiple programs are running in parallel.

- |tmux_tut1_link|
- |tmux_tut2_link|

.. |tmux_tut1_link| raw:: html

   <a href="https://github.com/tmux/tmux" target="_blank">Tmux</a>

.. |tmux_tut2_link| raw:: html

   <a href=https://gist.github.com/MohamedAlaa/2961058" target="_blank">Tmux Cheatsheet</a>

======================================
Tmuxinator - automating tmux
======================================

Tmux itself is very powerful, tmuxinator is just adding some cream on it.
Tmuxinator uses .xml files containing the description of a tmux session.
It allows to define and automate complex multi-terminal setups for e.g. development (one session per program) and simulations.

- |tmuxi_tut_link|

.. |tmuxi_tut_link| raw:: html

   <a href="https://github.com/tmuxinator/tmuxinator" target="_blank">Tmuxinator</a>

===================
Vim
===================

Everyone should use a tool that is right for the job.
Well, for our purposes (C++, ROS, python, bash), Vim is very well suited.
A lot of the time, you will find yourself in need of editing a code remotely (over ssh), and Vim can provide IDE-like features even in that situation.

Learning Vim is about changing the paradigm of programming - it's more about controlling a machine (synthesizer) that edits a text, rather than moving a cursor with a mouse and then typing the text.

Working in the terminal, using e.g. tmux and vim can also help you put away your mouse. Yes, a mouse is not an ideal tool for programming, though it has its use in gaming, 3D modeling, video editing and so on. Without a mouse, you will become much more productive, and your carpal tunnels will thank you.

Give it a chance, have a look at following videos:

- |vim_tut1_link|
- |vim_tut2_link|

.. |vim_tut1_link| raw:: html

   <a href="https://www.youtube.com/watch?v=_NUO4JEtkDw" target="_blank">Learning Vim in a Week</a>

.. |vim_tut2_link| raw:: html

   <a href="https://www.youtube.com/watch?v=5r6yzFEXajQ" target="_blank">Vim + Tmux</a>

======================================
ROS - Robot Operating System
======================================

ROS is a middleware between Ubuntu and C++.
Thanks to it, our programs can talk to each other asynchronously, even though they don't have to "know" each other necessarily.
It also allows simple control of your software from the terminal.
A lot of robotic stuff has been already programmed in ROS, including sensor drivers, visualization, planning, etc., thus we don't need to reinvent the wheel.
Getting into ROS is simple, just follow tutorials on their webpage and don't be afraid to experiment. You can't break the drone in simulation :-).

**Tutorials:** |ros_tut_link|

.. |ros_tut_link| raw:: html

   <a href="http://wiki.ros.org/ROS/Tutorials" target="_blank">ROS</a>

**Required skills:** The more, the better, most of it will come as your start working on a project.