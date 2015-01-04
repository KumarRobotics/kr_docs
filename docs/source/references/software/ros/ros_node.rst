ROS Node
========

Here we describe common practice for writing a ROS node. Driver node will be discussed in a different section.

This article assumes that the reader has gone through the basic `ros tutorial <http://wiki.ros.org/ROS/Tutorials>`_ and:

* Knows conceptually what is a `ROS node <http://wiki.ros.org/Nodes>`_
* Be able to write simple `publisher and subscriber <http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber(c%2B%2B)>`_
* Knows how to build ROS packages with `catkin <http://wiki.ros.org/catkin>`_

====
Node
====


==========
Nodehandle
==========

According to `NodeHandles <http://wiki.ros.org/roscpp/Overview/NodeHandles>`_, ``ros::NodeHandle`` manages an internal reference count to start and shutdown a node. This means that you can safely pass ``ros::NodeHandle`` around by const references without worrying about its lifetime and cleaning up. This also means that passing ``ros::NodeHandle`` via raw pointer or wrapping it around a ``shared_pointer`` is unnecessary.

The fact that ``ros::NodeHandle`` manages a reference count also means that it is non-trivial to construct such objects. Generally, you should avoid creating/destroying a ``ros::NodeHandle`` in a loop.

Thus, we recommend using the following constructor to construct a ROS node::

    class MyNode {
        MyNode(const ros::NodeHandle& nh, const ros::NodeHandle& pnh);

        // Disallow copy constructor and copy-assignment operator
        MyNode(const MyNode&) = delete;
        MyNode& operator=(const MyNode&) = delete;
    }

Here, ``nh`` is a global ``NodeHandle`` while ``pnh`` is a private ``NodeHandle``.
Usually, we use gloabal ``NodeHandle`` for topic publishing and subscribing and private ``NodeHandle`` to get and set parameters. But depening on the type of the node, there will be exceptions, which will be discussed in later sections.

=========
Callbacks
=========

==========
Remappings
==========

=======
Nodelet
=======

Implementing your node in a class also has the advantage of easily converting it to a `nodelet <http://wiki.ros.org/nodelet>`_.

=======
Drivers
=======
