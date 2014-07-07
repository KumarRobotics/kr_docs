Developing in ROS using an IDE
==============================

`IDEs <http://stackoverflow.com/questions/208193/why-should-i-use-an-ide>`_ offer a number of features which can improve your productivity when developing complex software. Autocomplete is particularly useful when using a complicated SDK like ROS. The ROS wiki `includes documentation <http://wiki.ros.org/IDEs>`_ on employing various IDEs with ROS. This page aims to document useful setup instructions to consider when configuring an IDE with ROS.

==========
Qt Creator
==========

`Qt Creator <http://qt-project.org/wiki/category:tools::qtcreator>`_ is a fast, powerful and, cross-platform c++ development IDE. It is actively maintained by the `Digia <http://www.digia.com/>`_ corporation, and is freely available under the LGPL licensing scheme. Qt integrates easily with cmake projects, and offers an elegant GUI development toolkit for Qt - `the recommended platform <http://wiki.ros.org/rqt>`_ for building graphical ROS applications.

Launching Qt Creator
--------------------

In order to access the necessary environment variables (``ROS_PACKAGE_PATH``, ``ROS_MASTER_URI``, etc) Qt Creator must be started from the command line. Alternatively, you can make a desktop launcher by following the instructions `here <http://wiki.ros.org/IDEs#QtCreator>`_.

rosmake packages in Qt Creator
------------------------------

catkin packages in Qt Creator
-----------------------------
