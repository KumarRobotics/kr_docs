Sensor
======

=======================================
Calibration
=======================================

A good tutorial on calibration |sensor_calibration|

.. |sensor_calibration| raw:: html

   <a href="https://docs.openvins.com/gs-calibration.html" target="_blank">Sensor Calibration</a>

=======================================
Serial Devices Permission and Ownership
=======================================

Some ROS driver which access resources in ``/dev`` will fail to launch, stating that they cannot open the device or access the resource.

Perform ``ls /dev/tty*`` to see if there is a serial device connected. The default could be ``/dev/ttyACM0`` or ``/dev/ttyUSB0``. If the device is connected, then you probably need to fix a permission issue.

By default, TTY devices in ``/dev`` are owned by the root user. You can do the following to grant yourself access.

Simple fix: giving temporary access to ``<username>``::

  sudo chown <username> /dev/ttyACM0

Permanent fix: adding ``<username>`` to dialout group::

  usermod -a -G dialout <username>
