#!/bin/bash

# Start resin-wifi-connect
export DBUS_SYSTEM_BUS_ADDRESS=unix:path=/host/run/dbus/system_bus_socket
sleep 1
node /AstroBox/resin-wifi-connect/src/app.js --clear=false

# At this point the WiFi connection has been configured and the device has
# internet - unless the configured WiFi connection is no longer available.

# Make Pi cam available
modprobe v4l2_common
modprobe bcm2835-v4l2

cd /opt/janus/share/janus/demos && python -m SimpleHTTPServer 8000 &&
python /AstroBox/run --config /etc/astrobox/config.yaml
