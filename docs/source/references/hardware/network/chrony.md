# Chrony

Chrony lets you syncronize the clocks of multiple devices so you can have consistent timestamps.

To install chrony run `sudo apt install chrony`

If you don't know where chrony.conf is run `whereis chrony`

### Setting up chronyd (server)

To allow devices with all ip adress in the network `192.168.1.`, add the following line to `chrony.conf`:


```
allow 192.168.1.1/24
```

### Setting up chronyc (client)

Assuming master's ip `192.168.1.55` and client ip will be `192.168.1.115`

### chrony.conf

```
server 192.168.1.55 iburst
makestep 0.0001 10
maxchange 1000000.000001 1 1
rtcsync
```

### /etc/network/interfaces

```
source /etc/network/interfaces.d/*

auto lo
iface lo inet loopback

# auto eth0
iface eth0 inet dhcp
iface default inet dhcp
auto wlan0
#iface wlan0 inet dhcp
iface wlan0 inet static
       address 192.168.1.115
       netmask 255.255.255.0
       gateway 192.168.1.1
       dns-nameservers 192.168.129.5
       wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf
```

### /etc/wpa_supplicant/wpa_supplicant.conf
```
ctrl_interface=/var/run/wpa_supplicant
ctrl_interface_group=ssh
ap_scan=1

network={
        ssid="windy"
        proto=RSN
        key_mgmt=NONE
        pairwise=CCMP TKIP
        group=CCMP TKIP
}
```
