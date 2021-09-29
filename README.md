# IRRHound

A simple package to deal with network resource registered into Internet Routing Registries (IRR).
Currently checks for IPv4 resources only.

## Setup

### Requirements 

Requires Python3 and a working version of [bgpq3](https://github.com/snar/bgpq3)

### Install (quick & dirty)

`pip install -e .` 

## Available tools
In the `tools/` directory you will find some useful tools to deal with IRR resources:

- **suggest_irr_sources.py**: check for IRR sources that contain objects about a network operator, identified by its own Autonomous System and (optional) AS-SET

- **retrieve_irr_resources.py**: retrieve route objects from an IRR source for given AS number and AS-SET.
