# Script(s) for enabling Horizon DaaS monitoring

### Horizon DaaS monitoring integration
Fetching data from the Horizon platform, outputs metrics in Influx Line Protocol on stdout

#### Usage
```
/opt/horizondaas/venv/bin/python3 /opt/horizondaas/bin/horizondaas --help
Usage: /opt/horizondaas/bin/horizondaas [options]
 
VMware CIM CLI Horizon tool to be used with Telegraf
 
Options:
  -h, --help            show this help message and exit
  -c config.yml, --config config.yml

```

#### Requirements
```
- Pip-package "pywbem, influxdb, PyYAML
```

#### Install
```
Step 1: Update your repositories
sudo apt-get update
# Step 2: Install pip for Python 3
sudo apt-get install build-essential libssl-dev libffi-dev python-dev
sudo apt install python3-pip
# Step 3: Use pip to install virtualenv
sudo pip3 install virtualenv
# Step 4: Launch your Python 3 virtual environment, here the name of my virtual environment will be venv
virtualenv -p python3 venv
# Step 5: Activate your new Python 3 environment. There are two ways to do this
. venv/bin/activate
# or source venv/bin/activate which does exactly the same thing
# you can make sure you are now working with Python 3
python --version
# this command will show you what is going on: the python executable you are using is now located inside your virtualenv repository which python.

# now we are ready to install some required pip modules
sudo pip install pywbem
sudo pip install PyYAML
sudo pip install influxdb
```

#### Example Telegraf configuration
```
File: inputs_daas-sp01.mgmt.local.conf

[[inputs.exec]]
  commands = [
    "/opt/horizondaas/venv/bin/python3 /opt/horizondaas/bin/horizondaas -c /opt/horizondaas/etc/daas-sp01.mgmt.local.yaml",
  ]
  timeout = "180s"
  data_format = "influx"
```

#### Details about what configuration change is possible.

###### Prefix for metric. Do not change this value
```
main:
        prefix: pamola-horizondaas 

```

###### Loglevel 30 is recommended. Will only show warnings, error and critical alerts in logfile
###### Logfile is the location of the logfile. Use one logfile for each host

```
log:
        loglevel: 30
        logfile: /var/log/horizondaas/daas-sp01.mgmt.local.log

```

###### Straight forward. Used a real host as example
```
host:
        url: https://daas-sp01.mgmt.local
        username: username
        password: password.
        insecure_skip_verify: true
```

###### What CIMs to use and what metrics are allowed to collect

```
metrics:
        CIMs:
                - Desktone_ActiveDirectoryStatus

        allowedMetrics:
                - Desktone_ActiveDirectoryStatus_ResponseTime
                - Desktone_ActiveDirectoryStatus_CommunicationStatus
                - Desktone_ActiveDirectoryStatus_OperationalStatus
                - Desktone_ActiveDirectoryStatus_Status
```

###### What additional tags should be collected

```
        additional_tags:
                Desktone_ActiveDirectoryStatus: DcAddress

```

###### For full example check etc/horizondaas-example.yml
