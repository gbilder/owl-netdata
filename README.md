

Assuming netdata is already installed...

## Make, install and run eagle-owl driver

first install required dev headers

`sudo apt-get install libusb-dev`

cd to `owl-driver` and

`make clean && make`

copy resulting `cm160` to `/usr/local/lib`

TODO: autostart driver on boot

start driver 

`/usr/local/bin/cm160`

this will peridociay update the file `/tmp/eagle-owl-live.txt`

## Install the two netdata files and turn on in config

copy `owl.chart.py` to `/usr/libexec/netdata/python.d/`
copy `ow.html` to `/usr/share/netdata/web`

add the following line to `/etc/netdata/python.d.conf`

`owl: yes`

## restart netdata

`sudo killall netdata ; sleep 1 ; sudo netdata`

