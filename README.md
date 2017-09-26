pyslice - OpenStack Python Automation
=====================================

*Pre-requisites: python 2.7 or 3.x*

1. To setup, do:
```
virtualenv venv
source venv/bin/activate
pip install -r requirements
```
2. Copy config.conf.default to config.conf
3. Change config.conf to match your configuration
4. `./slice | sudo puppet apply`
5. Profit!
