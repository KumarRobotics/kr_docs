Intel NUC
=========

`Intel NUC <http://www.intel.com/content/www/us/en/nuc/overview.html>`_ is a common computation platform being used at KumarRobotics. They are usually mounted on bigger platform such as `Pelican <http://www.asctec.de/en/uav-uas-drone-products/asctec-pelican/>`_ and `DJI S900/1000 <http://www.dji.com/product/spreading-wings-s900>`_.

This page is dedicated to record problems and solutions that we encountered while working with the NUC.

=================
Improper Shutdown
=================

If your NUC shutdowns due to low battery power, then it may not boot up properly the next time. This is described in detail `here <https://bugs.launchpad.net/ubuntu/+source/grub2/+bug/872244>`_.

The reason why this is happening is because in ``/boot/grub/grub.cfg``, the following logic sets the ``timeout`` to ``-1`` after a power failure. ::

    if [ "${recordfail}" = 1 ] ; then
        set timeout=-1
    else
        ...

But we don't want to modify this file directly because it will be overwritten after every kernel update. The workaround to fix this problem is by setting a config variable ``GRUB_RECORDFAIL_TIMEOUT`` which will be read by ``/etc/grub.d/00_header``.

Open ``/etc/default/grub``, add the following line in the file. ::

    GRUB_RECORDFAIL_TIMEOUT=5

Here ``5`` is just a random number I picked. After this modification run ::

    sudo update-grub

Then reboot and verify that in ``boot/grub/grub.cfg`` the ``set timeout=-1`` has been successfully changed to ``set timeout=5``.

=================================
Waiting for Network Configuration
=================================

Sometimes when you boot up Ubuntu, it will stuck at the booting screen for a long time saying it is waiting for network configuration. This can be annoying. Here's how to disable it.

1. Open ``/etc/init/failsafe.conf``

2. Change the first 3 ``sleep`` command to ``sleep x`` where ``x`` is some small value, like ``5``.

3. Or if you don't want to wait at all, simply comment out the following lines. ::

    $PLYMOUTH message --text="Waiting for network configuration..." || :
    sleep 40

    $PLYMOUTH message --text="Waiting up to 60 more seconds for network configuration..." || :
    sleep 59
