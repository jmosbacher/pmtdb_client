# xepmts.VoltageMapApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletevoltage_map_item**](VoltageMapApi.md#deletevoltage_map_item) | **DELETE** /voltage_maps/{voltage_mapId} | Deletes a voltage_map document
[**deletevoltage_maps**](VoltageMapApi.md#deletevoltage_maps) | **DELETE** /voltage_maps | Deletes all voltage_maps
[**getvoltage_map_item**](VoltageMapApi.md#getvoltage_map_item) | **GET** /voltage_maps/{voltage_mapId} | Retrieves a voltage_map document
[**getvoltage_map_item_by_name**](VoltageMapApi.md#getvoltage_map_item_by_name) | **GET** /voltage_maps/{Name} | Retrieves a voltage_map document by name
[**getvoltage_maps**](VoltageMapApi.md#getvoltage_maps) | **GET** /voltage_maps | Retrieves one or more voltage_maps
[**postvoltage_maps**](VoltageMapApi.md#postvoltage_maps) | **POST** /voltage_maps | Stores one or more voltage_maps.
[**putvoltage_map_item**](VoltageMapApi.md#putvoltage_map_item) | **PUT** /voltage_maps/{voltage_mapId} | Replaces a voltage_map document

# **deletevoltage_map_item**
> deletevoltage_map_item(voltage_map_id, if_match)

Deletes a voltage_map document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = xepmts.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = xepmts.VoltageMapApi(xepmts.ApiClient(configuration))
voltage_map_id = 'voltage_map_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a voltage_map document
    api_instance.deletevoltage_map_item(voltage_map_id, if_match)
except ApiException as e:
    print("Exception when calling VoltageMapApi->deletevoltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voltage_map_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletevoltage_maps**
> deletevoltage_maps()

Deletes all voltage_maps

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = xepmts.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = xepmts.VoltageMapApi(xepmts.ApiClient(configuration))

try:
    # Deletes all voltage_maps
    api_instance.deletevoltage_maps()
except ApiException as e:
    print("Exception when calling VoltageMapApi->deletevoltage_maps: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getvoltage_map_item**
> VoltageMap getvoltage_map_item(voltage_map_id)

Retrieves a voltage_map document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = xepmts.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = xepmts.VoltageMapApi(xepmts.ApiClient(configuration))
voltage_map_id = 'voltage_map_id_example' # str | 

try:
    # Retrieves a voltage_map document
    api_response = api_instance.getvoltage_map_item(voltage_map_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoltageMapApi->getvoltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **voltage_map_id** | **str**|  | 

### Return type

[**VoltageMap**](VoltageMap.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getvoltage_map_item_by_name**
> VoltageMap getvoltage_map_item_by_name(name)

Retrieves a voltage_map document by name

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = xepmts.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = xepmts.VoltageMapApi(xepmts.ApiClient(configuration))
name = 'name_example' # str | 

try:
    # Retrieves a voltage_map document by name
    api_response = api_instance.getvoltage_map_item_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoltageMapApi->getvoltage_map_item_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 

### Return type

[**VoltageMap**](VoltageMap.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getvoltage_maps**
> InlineResponse2001 getvoltage_maps(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more voltage_maps

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = xepmts.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = xepmts.VoltageMapApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more voltage_maps
    api_response = api_instance.getvoltage_maps(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VoltageMapApi->getvoltage_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postvoltage_maps**
> postvoltage_maps(body)

Stores one or more voltage_maps.

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = xepmts.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = xepmts.VoltageMapApi(xepmts.ApiClient(configuration))
body = xepmts.VoltageMap() # VoltageMap | A voltage_map or list of voltage_map documents

try:
    # Stores one or more voltage_maps.
    api_instance.postvoltage_maps(body)
except ApiException as e:
    print("Exception when calling VoltageMapApi->postvoltage_maps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VoltageMap**](VoltageMap.md)| A voltage_map or list of voltage_map documents | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putvoltage_map_item**
> putvoltage_map_item(body, if_match, voltage_map_id)

Replaces a voltage_map document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = xepmts.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = xepmts.VoltageMapApi(xepmts.ApiClient(configuration))
body = xepmts.VoltageMap() # VoltageMap | A voltage_map or list of voltage_map documents
if_match = 'if_match_example' # str | Current value of the _etag field
voltage_map_id = 'voltage_map_id_example' # str | 

try:
    # Replaces a voltage_map document
    api_instance.putvoltage_map_item(body, if_match, voltage_map_id)
except ApiException as e:
    print("Exception when calling VoltageMapApi->putvoltage_map_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VoltageMap**](VoltageMap.md)| A voltage_map or list of voltage_map documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **voltage_map_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

