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

  cd ~/Documents/code
  git clone https://github.com/KumarRobotics/bluefox2
  ln -s bluefox2 ~/Documents/catkin/src/bluefox2

Of course, you do not *have* to link to the root of a git repository. You can link to any folder which is itself a catkin package, or which contains catkin packages.

===============
Targeting c++11
===============

`c++11 <http://www.stroustrup.com/C++11FAQ.html>`_ is the most recent ISO standard for the c++ language. It adds `numerous features <http://www.codeproject.com/Articles/570638/Ten-Cplusplus-Features-Every-Cplusplus-Developer>`_ which improve the language and the standard library. We recommend adopting c++11. Some packages in the KR github may depend on your compiler having support for the new specification.

Since version 4.8, GCC implements `all of the c++11 features <http://gcc.gnu.org/gcc-4.8/cxx0x_status.html>`_. GCC 4.8 is **pre-installed in Ubuntu 14.04** (Trusty) and works with ROS Indigo out of the box.

Setting up GCC 4.8 on Ubuntu 12.04
----------------------------------

The Ubuntu 12.04 (Precise) repositories do not contain a package for GCC 4.8. PPAs for `toolchain test <https://launchpad.net/~ubuntu-toolchain-r>`_ builds are available. In order to install ``gcc`` and ``g++`` version 4.8, execute the following commands::

  sudo add-apt-repository ppa:ubuntu-toolchain-r/test
  sudo apt-get update
  sudo apt-get install gcc-4.8 g++-4.8

You should then update the links in ``/usr/bin`` so that they point to the newer version of gcc. This is achieved by executing::

  sudo update-alternatives --remove-all gcc
  sudo update-alternatives --remove-all g++
  sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-4.8 20
  sudo update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-4.8 20
  sudo update-alternatives --config gcc
  sudo update-alternatives --config g++

You will then need to update boost to 1.54 in order to use the new compiler.

Source: `ubuntuhandbook.org <http://ubuntuhandbook.org/index.php/2013/08/install-gcc-4-8-via-ppa-in-ubuntu-12-04-13-04/>`_

Enabling c++11 in CMake
-----------------------

c++11 features are enabled with the compiler switch: ``-std=c++11``. Adding this option to your CMakeLists.txt file is very simple::

  add_definitions("-std=c++11")

==========
Qt Creator
==========

`Qt Creator <http://qt-project.org/wiki/category:tools::qtcreator>`_ is a fast, powerful and, cross-platform c++ development IDE. It is actively maintained by the `Digia <http://www.digia.com/>`_ corporation, and is freely available under the LGPL licensing scheme. Qt integrates easily with cmake projects, and offers an elegant GUI development toolkit for Qt - `the recommended platform <http://wiki.ros.org/rqt>`_ for building graphical ROS applications.

Launching Qt Creator
--------------------

In order to access the necessary environment variables (``ROS_PACKAGE_PATH``, ``ROS_MASTER_URI``, etc) Qt Creator must be started from the command line. Alternatively, you can make a desktop launcher by following the instructions `here <http://wiki.ros.org/IDEs#QtCreator>`_.

ROS Packages in Qt Creator
--------------------------

To use Qt Creator with your ROS package. Create a new project with the ``File -> New File or Project`` action. Select the ``Import Project -> Import Existing Project``, as illustrated below:

.. image:: ../images/qt_step1.png

Assign your project a sensible name, and select the location as the package directory (in which your ``src`` directory resides):

.. image:: /images/qt_step2.png

You will be asked to import files. Select directories which contain headers and source files. When prompted to select project options, you should **NOT** add the IDE files to version control - these are specific to your machine.

.. image:: /images/qt_step3.png

Lastly, you must configure the Qt Creator build settings correctly. Navigate to  the ``Projects`` menu in the mode selector (accessible from ``Window -> Show Mode Selector``).

Append ``build`` to the build directory (you may need to create this directory yourself). Then add a custom build step which performs the operation ``cmake ..`` (.. is the argument). You may also optionally add ``-j4`` to the make arguments in order to parallelize builds. See the image below for an example of valid settings.

.. image:: /images/qt_step4.png

If you wish for Qt Creator to index a set of headers that are not on the default path, add them to your ``.includes`` file in QtCreator. For example::

  include
  build/devel/include

will index your project headers and generated project headers (such as messages).

Better Qt Creator
-----------------

Themes
~~~~~~

Qt creator ships with aweful color schemes. You should change it to increase your productivity. Go get `qtcreator-themes <https://github.com/gareth-cross/qtcreator-themes>`_ for better color schemes.

Beautifier
~~~~~~~~~~

Beautifier is QtCreator plugin that helps you format your code. It supports astyle, clang-format and uncrustify. We recommend using clang-format. To get clang-format, just do::

    sudo apt-get install clang-format-3.5

Go to ``Help`` -> ``About Plugins...``, under ``C++`` click ``Beautifier``. Then restart.

After restart, go to ``Tools`` -> ``Options`` -> ``Beautifier``, and setup your clang-format.
