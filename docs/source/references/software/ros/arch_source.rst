Arch Linux Source Build
=======================

.. note::

   The following instructions are for building ROS noetic from source on Arch Linux. They were written on 9/28/21 based on Arch Linux kernel 5.14.8-arch1-1 and associated packages; things may have changed by the time you are reading this.

=======================
Installing Dependencies
=======================

Loosly following steps 1.1 - 2.1 from the `source install instructions <http://wiki.ros.org/noetic/Installation/Source>`_:

Install build dependencies from AUR: ::

  yay -S python-rosdep python-rosdep python-rosinstall_generator python-vcstool python-catkin_tools

and initialize rosdep: ::

  sudo rosdep init

By default, rosdep does resolve a few keys to pacman dependencies but not nearly enough to be useful. `ros-arch/rosdep-with-aur <https://github.com/ros-arch/rosdep-with-aur>`_ provides the missing keys: ::

  git clone https://github.com/ros-arch/rosdep-with-aur
  sudo cp rosdep-with-aur/10-arch.list /etc/ros/rosdep/sources.list.d/
  sudo rosdep update

Follow step 2.1 (up to but excluding 2.1.1) from the `source installation instructions <http://wiki.ros.org/noetic/Installation/Source>`_ to set up a ROS workspace and fetch the rosinstall file of your choice. The remaining instructions are for ROS noetic desktop full and specific steps to resolve dependency and build issues may vary for other installations (e.g. desktop, base, etc).

Next, install package dependencies using rosdep. While rosdep is only configured to work with pacman, many of the keys provided by ``rosdep-with-aur`` map to AUR packages. To get around this issue, use rosdep to get the list of system libraries to install and manually complete the installation command yourself. Note that I found ``orocos-kdl-python2`` to be listed as a dependency but is superseded by ``orocos-kdl-python`` and thus can safely be removed from the list. Additionally, when building desktop-full ``gazebo`` is not actually listed as a dependency but is certainly required and must be added to the list manually::

  rosdep keys --from-paths src --ignore-src --rosdistro noetic | ROS_PYTHON_VERSION=3 xargs rosdep resolve | grep -Ev '^$|^#.*' | sort | uniq > arch-libs.txt
  bash -c 'yay -S $(cat arch-libs.txt)'

=========================
Fixing Compilation Issues
=========================

.. note::

   I have assembled all the changes I needed to make into a single :download:`patch <noetic-desktop-full.patch>`. The rest of this section details those changes and why they were made.

If the installed version of ``log4cxx`` on your machine is >=0.12 you need to patch ``rosconsole`` as noted `here <https://github.com/ros-noetic-arch/ros-noetic-rosconsole/issues/6>`_. This issue can be solved by changing the backend to be something besides ``log4cxx`` or applying this `patch <https://patch-diff.githubusercontent.com/raw/ros/rosconsole/pull/51.patch>`_ (included in the patch below).

Beyond the above patch, various libraries that include ``rosconsole`` and thus ``log4cxx`` headers in turn have to be compiled with C++17. Some of these packages explicitly declare the C++ version to be less than 17 in their CMakeLists.txt causing errors. The included patch fixes these issues for the packages contained in the ``desktop_full`` collection of ROS noetic.

=========
Compiling
=========

The official instructions use ``catkin_make_isolated`` but you could just as easily use catkin tools: ::

  catkin init --install --cmake-args -DCMAKE_BUILD_TYPE=Release -DCMAKE_CXX_STANDARD=17
  catkin build

Install to a different location as you see fit.
