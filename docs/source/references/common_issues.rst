Common Issues
=============

===================
Common ROS Problems
===================

GCC fails to find headers for generated messages
------------------------------------------------

You may wish to compile a package (in catkin) which contains **msg** files to be used by other packages (or a package which depends on said messages). The order of compilation is important here. If dependencies are improperly specified, GCC may fail to compile when you include generated message headers.

For example, you might have the package structure::

    my_workspace/
      my_library/
        msg/MyMessage.msg
        src/my_library.cpp
        CMakeLists.txt
        package.xml
        ...
      my_node/
        src/my_node.cpp
        CMakeLists.txt
        package.xml
        ...

Evidently, ``my_node`` must declare a dependency on ``my_library`` in both ``CMakeLists.txt`` and ``package.xml``. However, ``my_library`` and ``my_node`` should **also** both declare a dependency on the exported targets of ``my_library``. Otherwise, catkin may attempt to compile ``my_library.cpp`` and ``my_node.cpp`` before the header for ``MyMessage.msg`` has been generated, causing build failure. Exported targets include the messages and services defined by a package.

This additional dependency is specified by adding the following to both make files::

    add_dependencies(${PROJECT_NAME} ${catkin_EXPORTED_TARGETS})

You may optionally specify the exported targets of only one package, like so::

    add_dependencies(${PROJECT_NAME} ${my_library_EXPORTED_TARGETS})

See `here <ttp://answers.ros.org/question/52744/how-to-specify-dependencies-with-foo_msgs-catkin-packages/>`_ for details.
