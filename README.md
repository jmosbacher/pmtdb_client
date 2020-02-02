# pmtdb_client
API for the XenonnT PMT database

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://github.com/jmosbacher](https://github.com/jmosbacher)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/jmosbacher/pmtdb_client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/jmosbacher/pmtdb_client.git`)

Then import the package:
```python
import pmtdb_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pmtdb_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import pmtdb_client
from pmtdb_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = pmtdb_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pmtdb_client.DatasheetApi(pmtdb_client.ApiClient(configuration))
datasheet_id = 'datasheet_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a Datasheet document
    api_instance.delete_datasheet_item(datasheet_id, if_match)
except ApiException as e:
    print("Exception when calling DatasheetApi->delete_datasheet_item: %s\n" % e)
# Configure HTTP basic authorization: BasicAuth
configuration = pmtdb_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pmtdb_client.DatasheetApi(pmtdb_client.ApiClient(configuration))

try:
    # Deletes all datasheets
    api_instance.deletedatasheets()
except ApiException as e:
    print("Exception when calling DatasheetApi->deletedatasheets: %s\n" % e)
# Configure HTTP basic authorization: BasicAuth
configuration = pmtdb_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pmtdb_client.DatasheetApi(pmtdb_client.ApiClient(configuration))
datasheet_id = 'datasheet_id_example' # str | 

try:
    # Retrieves a Datasheet document
    api_response = api_instance.get_datasheet_item(datasheet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasheetApi->get_datasheet_item: %s\n" % e)
# Configure HTTP basic authorization: BasicAuth
configuration = pmtdb_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pmtdb_client.DatasheetApi(pmtdb_client.ApiClient(configuration))
pmt_no = 'pmt_no_example' # str | 

try:
    # Retrieves a Datasheet document by pmt_no
    api_response = api_instance.get_datasheet_item_by_pmt_no(pmt_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasheetApi->get_datasheet_item_by_pmt_no: %s\n" % e)
# Configure HTTP basic authorization: BasicAuth
configuration = pmtdb_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pmtdb_client.DatasheetApi(pmtdb_client.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more datasheets
    api_response = api_instance.getdatasheets(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasheetApi->getdatasheets: %s\n" % e)
# Configure HTTP basic authorization: BasicAuth
configuration = pmtdb_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pmtdb_client.DatasheetApi(pmtdb_client.ApiClient(configuration))
body = pmtdb_client.Datasheet() # Datasheet | A Datasheet or list of Datasheet documents

try:
    # Stores one or more datasheets.
    api_instance.postdatasheets(body)
except ApiException as e:
    print("Exception when calling DatasheetApi->postdatasheets: %s\n" % e)
# Configure HTTP basic authorization: BasicAuth
configuration = pmtdb_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pmtdb_client.DatasheetApi(pmtdb_client.ApiClient(configuration))
body = pmtdb_client.Datasheet() # Datasheet | A Datasheet or list of Datasheet documents
if_match = 'if_match_example' # str | Current value of the _etag field
datasheet_id = 'datasheet_id_example' # str | 

try:
    # Replaces a Datasheet document
    api_instance.put_datasheet_item(body, if_match, datasheet_id)
except ApiException as e:
    print("Exception when calling DatasheetApi->put_datasheet_item: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DatasheetApi* | [**delete_datasheet_item**](docs/DatasheetApi.md#delete_datasheet_item) | **DELETE** /datasheets/{datasheetId} | Deletes a Datasheet document
*DatasheetApi* | [**deletedatasheets**](docs/DatasheetApi.md#deletedatasheets) | **DELETE** /datasheets | Deletes all datasheets
*DatasheetApi* | [**get_datasheet_item**](docs/DatasheetApi.md#get_datasheet_item) | **GET** /datasheets/{datasheetId} | Retrieves a Datasheet document
*DatasheetApi* | [**get_datasheet_item_by_pmt_no**](docs/DatasheetApi.md#get_datasheet_item_by_pmt_no) | **GET** /datasheets/{Pmt_No} | Retrieves a Datasheet document by pmt_no
*DatasheetApi* | [**getdatasheets**](docs/DatasheetApi.md#getdatasheets) | **GET** /datasheets | Retrieves one or more datasheets
*DatasheetApi* | [**postdatasheets**](docs/DatasheetApi.md#postdatasheets) | **POST** /datasheets | Stores one or more datasheets.
*DatasheetApi* | [**put_datasheet_item**](docs/DatasheetApi.md#put_datasheet_item) | **PUT** /datasheets/{datasheetId} | Replaces a Datasheet document
*PmtAfterpulseApi* | [**deletepmt_afterpulse_item**](docs/PmtAfterpulseApi.md#deletepmt_afterpulse_item) | **DELETE** /pmt_afterpulses/{pmt_afterpulseId} | Deletes a pmt_afterpulse document
*PmtAfterpulseApi* | [**deletepmt_afterpulses**](docs/PmtAfterpulseApi.md#deletepmt_afterpulses) | **DELETE** /pmt_afterpulses | Deletes all pmt_afterpulses
*PmtAfterpulseApi* | [**getpmt_afterpulse_item**](docs/PmtAfterpulseApi.md#getpmt_afterpulse_item) | **GET** /pmt_afterpulses/{pmt_afterpulseId} | Retrieves a pmt_afterpulse document
*PmtAfterpulseApi* | [**getpmt_afterpulses**](docs/PmtAfterpulseApi.md#getpmt_afterpulses) | **GET** /pmt_afterpulses | Retrieves one or more pmt_afterpulses
*PmtAfterpulseApi* | [**postpmt_afterpulses**](docs/PmtAfterpulseApi.md#postpmt_afterpulses) | **POST** /pmt_afterpulses | Stores one or more pmt_afterpulses.
*PmtAfterpulseApi* | [**putpmt_afterpulse_item**](docs/PmtAfterpulseApi.md#putpmt_afterpulse_item) | **PUT** /pmt_afterpulses/{pmt_afterpulseId} | Replaces a pmt_afterpulse document
*PmtDcrApi* | [**deletepmt_dcr_item**](docs/PmtDcrApi.md#deletepmt_dcr_item) | **DELETE** /pmt_dcrs/{pmt_dcrId} | Deletes a pmt_dcr document
*PmtDcrApi* | [**deletepmt_dcrs**](docs/PmtDcrApi.md#deletepmt_dcrs) | **DELETE** /pmt_dcrs | Deletes all pmt_dcrs
*PmtDcrApi* | [**getpmt_dcr_item**](docs/PmtDcrApi.md#getpmt_dcr_item) | **GET** /pmt_dcrs/{pmt_dcrId} | Retrieves a pmt_dcr document
*PmtDcrApi* | [**getpmt_dcrs**](docs/PmtDcrApi.md#getpmt_dcrs) | **GET** /pmt_dcrs | Retrieves one or more pmt_dcrs
*PmtDcrApi* | [**postpmt_dcrs**](docs/PmtDcrApi.md#postpmt_dcrs) | **POST** /pmt_dcrs | Stores one or more pmt_dcrs.
*PmtDcrApi* | [**putpmt_dcr_item**](docs/PmtDcrApi.md#putpmt_dcr_item) | **PUT** /pmt_dcrs/{pmt_dcrId} | Replaces a pmt_dcr document
*PmtGainApi* | [**deletepmt_gain_item**](docs/PmtGainApi.md#deletepmt_gain_item) | **DELETE** /pmt_gains/{pmt_gainId} | Deletes a pmt_gain document
*PmtGainApi* | [**deletepmt_gains**](docs/PmtGainApi.md#deletepmt_gains) | **DELETE** /pmt_gains | Deletes all pmt_gains
*PmtGainApi* | [**getpmt_gain_item**](docs/PmtGainApi.md#getpmt_gain_item) | **GET** /pmt_gains/{pmt_gainId} | Retrieves a pmt_gain document
*PmtGainApi* | [**getpmt_gains**](docs/PmtGainApi.md#getpmt_gains) | **GET** /pmt_gains | Retrieves one or more pmt_gains
*PmtGainApi* | [**postpmt_gains**](docs/PmtGainApi.md#postpmt_gains) | **POST** /pmt_gains | Stores one or more pmt_gains.
*PmtGainApi* | [**putpmt_gain_item**](docs/PmtGainApi.md#putpmt_gain_item) | **PUT** /pmt_gains/{pmt_gainId} | Replaces a pmt_gain document
*PmtInstallApi* | [**deletepmt_install_item**](docs/PmtInstallApi.md#deletepmt_install_item) | **DELETE** /pmt_installs/{pmt_installId} | Deletes a pmt_install document
*PmtInstallApi* | [**deletepmt_installs**](docs/PmtInstallApi.md#deletepmt_installs) | **DELETE** /pmt_installs | Deletes all pmt_installs
*PmtInstallApi* | [**getpmt_install_item**](docs/PmtInstallApi.md#getpmt_install_item) | **GET** /pmt_installs/{pmt_installId} | Retrieves a pmt_install document
*PmtInstallApi* | [**getpmt_install_item_by_pmt_no**](docs/PmtInstallApi.md#getpmt_install_item_by_pmt_no) | **GET** /pmt_installs/{Pmt_No} | Retrieves a pmt_install document by pmt_no
*PmtInstallApi* | [**getpmt_installs**](docs/PmtInstallApi.md#getpmt_installs) | **GET** /pmt_installs | Retrieves one or more pmt_installs
*PmtInstallApi* | [**postpmt_installs**](docs/PmtInstallApi.md#postpmt_installs) | **POST** /pmt_installs | Stores one or more pmt_installs.
*PmtInstallApi* | [**putpmt_install_item**](docs/PmtInstallApi.md#putpmt_install_item) | **PUT** /pmt_installs/{pmt_installId} | Replaces a pmt_install document
*StatusChangeApi* | [**deletestatus_change_item**](docs/StatusChangeApi.md#deletestatus_change_item) | **DELETE** /status_changes/{status_changeId} | Deletes a status_change document
*StatusChangeApi* | [**deletestatus_changes**](docs/StatusChangeApi.md#deletestatus_changes) | **DELETE** /status_changes | Deletes all status_changes
*StatusChangeApi* | [**getstatus_change_item**](docs/StatusChangeApi.md#getstatus_change_item) | **GET** /status_changes/{status_changeId} | Retrieves a status_change document
*StatusChangeApi* | [**getstatus_change_item_by_pmt_no**](docs/StatusChangeApi.md#getstatus_change_item_by_pmt_no) | **GET** /status_changes/{Pmt_No} | Retrieves a status_change document by pmt_no
*StatusChangeApi* | [**getstatus_changes**](docs/StatusChangeApi.md#getstatus_changes) | **GET** /status_changes | Retrieves one or more status_changes
*StatusChangeApi* | [**poststatus_changes**](docs/StatusChangeApi.md#poststatus_changes) | **POST** /status_changes | Stores one or more status_changes.
*StatusChangeApi* | [**putstatus_change_item**](docs/StatusChangeApi.md#putstatus_change_item) | **PUT** /status_changes/{status_changeId} | Replaces a status_change document
*VoltageMapApi* | [**deletevoltage_map_item**](docs/VoltageMapApi.md#deletevoltage_map_item) | **DELETE** /voltage_maps/{voltage_mapId} | Deletes a voltage_map document
*VoltageMapApi* | [**deletevoltage_maps**](docs/VoltageMapApi.md#deletevoltage_maps) | **DELETE** /voltage_maps | Deletes all voltage_maps
*VoltageMapApi* | [**getvoltage_map_item**](docs/VoltageMapApi.md#getvoltage_map_item) | **GET** /voltage_maps/{voltage_mapId} | Retrieves a voltage_map document
*VoltageMapApi* | [**getvoltage_map_item_by_name**](docs/VoltageMapApi.md#getvoltage_map_item_by_name) | **GET** /voltage_maps/{Name} | Retrieves a voltage_map document by name
*VoltageMapApi* | [**getvoltage_maps**](docs/VoltageMapApi.md#getvoltage_maps) | **GET** /voltage_maps | Retrieves one or more voltage_maps
*VoltageMapApi* | [**postvoltage_maps**](docs/VoltageMapApi.md#postvoltage_maps) | **POST** /voltage_maps | Stores one or more voltage_maps.
*VoltageMapApi* | [**putvoltage_map_item**](docs/VoltageMapApi.md#putvoltage_map_item) | **PUT** /voltage_maps/{voltage_mapId} | Replaces a voltage_map document

## Documentation For Models

 - [Datasheet](docs/Datasheet.md)
 - [Error](docs/Error.md)
 - [ErrorError](docs/ErrorError.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [InlineResponse2001](docs/InlineResponse2001.md)
 - [InlineResponse2002](docs/InlineResponse2002.md)
 - [InlineResponse2003](docs/InlineResponse2003.md)
 - [InlineResponse2004](docs/InlineResponse2004.md)
 - [InlineResponse2005](docs/InlineResponse2005.md)
 - [InlineResponse2006](docs/InlineResponse2006.md)
 - [PmtAfterpulse](docs/PmtAfterpulse.md)
 - [PmtDcr](docs/PmtDcr.md)
 - [PmtGain](docs/PmtGain.md)
 - [PmtInstall](docs/PmtInstall.md)
 - [StatusChange](docs/StatusChange.md)
 - [VoltageMap](docs/VoltageMap.md)
 - [VoltageMapVoltages](docs/VoltageMapVoltages.md)

## Documentation For Authorization


## BasicAuth

- **Type**: HTTP basic authentication


## Author

joe.mosbacher@gmail.com
