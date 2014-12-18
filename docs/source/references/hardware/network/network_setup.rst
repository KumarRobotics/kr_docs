Network Setup
=============

========================
Network Setup for Robots
========================

To ensure your robot has continuous and reliable network connection, you should use ``wpa_supplicant`` if you don't have a display for the robot.

Here are the steps for setting up ``wpa_supplicant``.

0. First of all, ask for a static ip for your robot in the mrsl network.

1. add ``wpa_supplicant.conf`` to ``/etc/wpa_supplicant/``::

    ctrl_interface=/var/run/wpa_supplicant
    ctrl_interface_group=0
    ap_scan=1
    fast_reauth=1

    network={
        ssid="mrsl_airrouterhp"
        scan_ssid=1
        key_mgmt=NONE
    }

2. modify ``/etc/network/interfaces`` so that it looks like::

    auto lo
    iface lo inet loopback

    auto wlan0  # auto start wlan0 interface
    iface wlan0 inet static  # use static ip for wlan0
    address 192.168.129.xyz  # your desired ip
    gateway 192.168.129.1    # mrsl gateway
    netmask 255.255.255.0
    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
