# Read Ruuvi tag beacons in Ubuntu

This project aims to provide a script for reading ruuvitag beacons on raspberrypi 3 running
Ubuntu 20.04 server. The script in this directory is fully functiona, except that the
provided configuration is a dummy. You need to change the values to match your setup. The script
has also a few major dependencies.

## Dependencies

The hardware must have bluetooth capability and must be in the proximity of the ruuvitag emiting
the beacon. Note that you have to specify the MAC address of the tag in the configuration.

### pi-bluetooth

Since I'm not running Rasbian OS, I don't have the bluetooth drivers installed. Luckily the dirvers
can be installed via standard packet manager.

```shell
apt -y install pi-bluetooth
```

### ruuvitag_sensor

This is the actual work horse of the show. I'll be leveraging this libarary to read the
Ruuvitag beacons. I used pip3 to install the library, but the
[GitHub](https://github.com/ttu/ruuvitag-sensor) of the project provides guides for other methods
as well.

```shell
pip3 install ruuvitag_sensor
```

### Bleson

ruuvitag\_sensor library leverages [Bleson](https://github.com/TheCellule/python-bleson) under
the hood. The quide in the [ruuvitag\_sensor](https://github.com/ttu/ruuvitag-sensor) GitHub says
that Bleson does not come in when you
install the ruuvitag\_sensor package, but pip3 certainly installed it without a separate command.

I encountered weird issue where the ruuvitag\_sensor library failed without any indication. I was
able to get it working by explicitly enabling Bleson:

```shell
export RUUVI_BLE_ADAPTER="Bleson"
```

Weirdly, this was only issue on 32 bit version of Ubuntu server.

## Testing

```python3
from ruuvitag_sensor.ruuvi import RuuviTagSensor

def handle_data(found_data):
    print('MAC ' + found_data[0])
    print(found_data[1])

RuuviTagSensor.get_datas(handle_data)
```

like describe on in the [ruuvitag-sensor](https://pypi.org/project/ruuvitag-sensor/) pypi page.
