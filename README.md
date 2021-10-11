# IRRHound

A simple package to deal with network resources registered into Internet Routing Registries (IRR). [Jump to usage examples](#basic-usage) or read through the documentation.

## Description

As IPv4 prefixes keep being traded around the world, it is become increasingly challenging to track registration details for routing resources (ROUTE objects) in the variously available IRRs. Complete knowledge of these resources is fundamental to provide reliable automatic generation of BGP input filters, expecially in Route Server implementations at Internet Exchange Points.
This package provides a library of functions and some example tools to perform extensive research for a given AS registered resources, research strategy is accomplished as follows:

- Given an input AS number and related AS-SET (both v4/v6 if needed) a recursive research is performed against `whois.radb.net`whois server by means of the `bgpq3` tool, in order to retrieve the full list of main AS and customers'ASes.
- For each AS, related ROUTE objects are retrieved across all available registries
- In case multiple ROUTE objects are registered for the same prefix in different registries, a selection process favours objects in most accessed registries (in order to reduce the number of registries one needs to query)
- Information about duplicate ROUTE objects is kept with the main object selected

## Package functions

Package `irrhound.irrhound` provides two functions:

- `irr_hunt_sources(asn,asmacro,asmacro6)`: returns a minimal set of sources containing resources (ROUTE objects) for the given AS number and related v4/v6 customers' AS-SETs. Return value is a dict with the following structure: `{ 'sources': [list] }` 
- `irr_hunt_routes(asn,asmacro,asmacro6)`: returns a complete set of ROUTE objects for the given AS number and v4/v6 customers' AS-SETs. Each ROUTE object descriptor can carry additional duplicates from different regisitries. Return value is a dict with the following structure: `{ 'routes': [ { 'cidr': network, 'origin': ASN, 'source': IRR source, 'duplicates': [list of routes in dict format] }`

### Basic usage

Getting an IRR sources suggestion:

```
>>>from irrhound.irrhound import irr_hunt_sources
>>>sources = irr_hunt_sources(27320,'AS-FROOT', None)
>>>print(sources)

>>> {'sources': ['RADB', 'ALTDB', 'NTTCOM']}
```

Retrieving all route objects for a given peer:

```
>>>from irrhound.irrhound import irr_hunt_routes
>>>routes = irr_hunt_routes(27320,'AS-FROOT', None)
>>>print(routes)

>>>{'routes': [{'cidr': '192.5.4.0/23', 'origin': 3557, 'source': 'RADB', 'duplicates': [{'cidr': '192.5.4.0/23', 'origin': 3557, 'source': 'RADB'}]}, {'cidr': '192.5.4.0/24', 'origin': 3557, 'source': 'RADB', 'duplicates': [{'cidr': '192.5.4.0/24', 'origin': 3557, 'source': 'RADB'}]}, {'cidr': '192.5.5.0/24', 'origin': 3557, 'source': 'RADB', 'duplicates': [{'cidr': '192.5.5.0/24', 'origin': 3557, 'source': 'RADB'}]}, {'cidr': '202.41.142.0/24', 'origin': 3557, 'source': 'RADB', 'duplicates': [{'cidr': '202.41.142.0/24', 'origin': 3557, 'source': 'RADB'}]}, {'cidr': '199.212.90.0/23', 'origin': 3557, 'source': 'ALTDB', 'duplicates': [{'cidr': '199.212.90.0/23', 'origin': 3557, 'source': 'ALTDB'}]}, {'cidr': '199.212.92.0/23', 'origin': 3557, 'source': 'ALTDB', 'duplicates': [{'cidr': '199.212.92.0/23', 'origin': 3557, 'source': 'ALTDB'}]}, {'cidr': '2001:500:2e::/47', 'origin': 3557, 'source': 'RADB', 'duplicates': [{'cidr': '2001:500:2e::/47', 'origin': 3557, 'source': 'RADB'}]}, {'cidr': '2001:500:2e::/48', 'origin': 3557, 'source': 'RADB', 'duplicates': [{'cidr': '2001:500:2e::/48', 'origin': 3557, 'source': 'RADB'}]}, {'cidr': '2001:500:2f::/48', 'origin': 3557, 'source': 'RADB', 'duplicates': [{'cidr': '2001:500:2f::/48', 'origin': 3557, 'source': 'RADB'}]}, {'cidr': '2001:dd8:1d::/48', 'origin': 3557, 'source': 'RADB', 'duplicates': [{'cidr': '2001:dd8:1d::/48', 'origin': 3557, 'source': 'RADB'}]}, {'cidr': '2001:4f8::/32', 'origin': 3557, 'source': 'NTTCOM', 'duplicates': [{'cidr': '2001:4f8::/32', 'origin': 3557, 'source': 'NTTCOM'}]}, {'cidr': '2001:500::/48', 'origin': 3557, 'source': 'NTTCOM', 'duplicates': [{'cidr': '2001:500::/48', 'origin': 3557, 'source': 'NTTCOM'}]}]}
```

See the available tools for extended examples on how to use these functions and their return values.

## Available tools
In the `tools/` directory you will find some useful tools to deal with IRR resources:

- **suggest_irr_sources.py**: check for IRR sources that contain objects about a network operator, identified by its own Autonomous System and (optional) AS-SET
- **retrieve_irr_resources.py**: retrieve route objects from an IRR source for given AS number and AS-SET.

## Setup

### Requirements 

Requires Python3 and a working version of [bgpq4](https://github.com/bgp/bgpq4) plus the [ipwhois](https://ipwhois.readthedocs.io/en/latest/) Python package.

### Install (quick & dirty)

`pip install -e .` 
