Setting up your build environment
=================================

======
catkin
======

`Catkin <http://wiki.ros.org/catkin>`_ is the recommended dependency manager for use with ROS. Most packages added to the KR github will be intended for use with catkin. Instructions for setting up a catkin workspace are available on the `ROS wiki <http://wiki.ros.org/catkin/Tutorials>`_. Adding a new package to your catkin workspace is `straightforward <http://wiki.ros.org/catkin/Tutorials/CreatingPackage>`_.

Linking packages into your catkin workspace
-------------------------------------------

When managing a large project with multiple packages, it is usually convenient to keep your workspace separate from the git folder. This is achieved by *symbolically linking* your packages into the catkin ``src`` folder.

**Example**

For the following example we suppose the following directory structure exists::

  ~/Documents/catkin  <-- Root of the catkin workspace
  ~/Documents/code    <-- Folder where you store your git repositories

If you wanted to clone the `bluefox2 <https://github.com/KumarRobotics/bluefox2>`_ package and add it to your catkin workspace, you would do the following::

  $ cd ~/Documents/code
  $ git clone https://github.com/KumarRobotics/bluefox2
  $ ln -s bluefox2 ~/Documents/catkin/src/bluefox2

Of course, you do not *have* to link to the root of a git repository. You can link to any folder which is itself a catkin package, or which contains catkin packages.

===============
Targeting c++11
===============

`c++11 <http://www.stroustrup.com/C++11FAQ.html>`_ is the most recent ISO standard for the c++ language. It adds `numerous features <http://www.codeproject.com/Articles/570638/Ten-Cplusplus-Features-Every-Cplusplus-Developer>`_ which improve the language and the standard library. We recommend adopting c++11. Some packages in the KR github may depend on your compiler having support for the new specification.

Since version 4.8, GCC implements `all of the c++11 features <http://gcc.gnu.org/gcc-4.8/cxx0x_status.html>`_. GCC 4.8 is **pre-installed in Ubuntu 14.04** (Trusty) and works with ROS Indigo out of the box.

Setting up GCC 4.8 on Ubuntu 12.04
----------------------------------

The Ubuntu 12.04 (Precise) repositories do not contain a package for GCC 4.8. PPAs for `toolchain test <https://launchpad.net/~ubuntu-toolchain-r>`_ builds are available. In order to install ``gcc`` and ``g++`` version 4.8, execute the following commands::

  $ sudo add-apt-repository ppa:ubuntu-toolchain-r/test
  $ sudo apt-get update
  $ sudo apt-get install gcc-4.8 g++-4.8

You should then update the links in ``/usr/bin`` so that they point to the newer version of gcc. This is achieved by executing::

  s sudo update-alternatives --remove-all gcc
  $ sudo update-alternatives --remove-all g++
  $ sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 20
  $ sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 20
  $ sudo update-alternatives --config gcc
  $ sudo update-alternatives --config g++

Source: `ubuntuhandbook.org <http://ubuntuhandbook.org/index.php/2013/08/install-gcc-4-8-via-ppa-in-ubuntu-12-04-13-04/>`_

Enabling c++11 in CMake
-----------------------

c++11 features are enabled with the compiler switch: ``-std=c++11``. Adding this option to your CMakeLists.txt file is very simple::

  add_definitions("-std=c++11")
