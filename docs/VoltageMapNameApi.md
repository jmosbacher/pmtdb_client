# xepmts.VoltageMapNameApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_voltage_map_name_item**](VoltageMapNameApi.md#get_voltage_map_name_item) | **GET** /VoltageMaps/names/{voltagemapnameId} | Retrieves a VoltageMapName document
[**get_voltage_mapsnames**](VoltageMapNameApi.md#get_voltage_mapsnames) | **GET** /VoltageMaps/names | Retrieves one or more VoltageMaps/names

# **get_voltage_map_name_item**
> VoltageMapName get_voltage_map_name_item(voltagemapname_id)

Retrieves a VoltageMapName document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.VoltageMapNameApi(xepmts.ApiClient(configuration))
voltagemapname_id = 'voltagemapname_id_example' # str | 

try:
    # Retrieves a VoltageMapName document
    api_response = api_instance.get_voltage_map_name_item(voltagemapname_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoltageMapNameApi->get_voltage_map_name_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voltagemapname_id** | **str**|  | 

### Return type

[**VoltageMapName**](VoltageMapName.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_voltage_mapsnames**
> InlineResponse2008 get_voltage_mapsnames(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more VoltageMaps/names

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.VoltageMapNameApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more VoltageMaps/names
    api_response = api_instance.get_voltage_mapsnames(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoltageMapNameApi->get_voltage_mapsnames: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

