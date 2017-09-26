pyslice - OpenStack Python Automation
=====================================

*Pre-requisites: python 2.7 or 3.x*

1. To setup, do:
```
virtualenv venv
source venv/bin/activate
pip install -r requirements
```
2. Change the config file (openstack auth url is of the form: `$openstack-endpoint:5000/v2.0`)
3. `./slice | sudo puppet apply`
4. Profit!
