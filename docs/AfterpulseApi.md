# xepmts.AfterpulseApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_afterpulse_item**](AfterpulseApi.md#delete_afterpulse_item) | **DELETE** /Afterpulses/{afterpulseId} | Deletes a Afterpulse document
[**delete_afterpulses**](AfterpulseApi.md#delete_afterpulses) | **DELETE** /Afterpulses | Deletes all Afterpulses
[**get_afterpulse_item**](AfterpulseApi.md#get_afterpulse_item) | **GET** /Afterpulses/{afterpulseId} | Retrieves a Afterpulse document
[**get_afterpulses**](AfterpulseApi.md#get_afterpulses) | **GET** /Afterpulses | Retrieves one or more Afterpulses
[**post_afterpulses**](AfterpulseApi.md#post_afterpulses) | **POST** /Afterpulses | Stores one or more Afterpulses.
[**put_afterpulse_item**](AfterpulseApi.md#put_afterpulse_item) | **PUT** /Afterpulses/{afterpulseId} | Replaces a Afterpulse document

# **delete_afterpulse_item**
> delete_afterpulse_item(afterpulse_id, if_match)

Deletes a Afterpulse document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.AfterpulseApi(xepmts.ApiClient(configuration))
afterpulse_id = 'afterpulse_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a Afterpulse document
    api_instance.delete_afterpulse_item(afterpulse_id, if_match)
except ApiException as e:
    print("Exception when calling AfterpulseApi->delete_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **afterpulse_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_afterpulses**
> delete_afterpulses()

Deletes all Afterpulses

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.AfterpulseApi(xepmts.ApiClient(configuration))

try:
    # Deletes all Afterpulses
    api_instance.delete_afterpulses()
except ApiException as e:
    print("Exception when calling AfterpulseApi->delete_afterpulses: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_afterpulse_item**
> Afterpulse get_afterpulse_item(afterpulse_id)

Retrieves a Afterpulse document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.AfterpulseApi(xepmts.ApiClient(configuration))
afterpulse_id = 'afterpulse_id_example' # str | 

try:
    # Retrieves a Afterpulse document
    api_response = api_instance.get_afterpulse_item(afterpulse_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AfterpulseApi->get_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **afterpulse_id** | **str**|  | 

### Return type

[**Afterpulse**](Afterpulse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_afterpulses**
> InlineResponse2006 get_afterpulses(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more Afterpulses

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.AfterpulseApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more Afterpulses
    api_response = api_instance.get_afterpulses(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AfterpulseApi->get_afterpulses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_afterpulses**
> post_afterpulses(body)

Stores one or more Afterpulses.

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.AfterpulseApi(xepmts.ApiClient(configuration))
body = xepmts.Afterpulse() # Afterpulse | A Afterpulse or list of Afterpulse documents

try:
    # Stores one or more Afterpulses.
    api_instance.post_afterpulses(body)
except ApiException as e:
    print("Exception when calling AfterpulseApi->post_afterpulses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Afterpulse**](Afterpulse.md)| A Afterpulse or list of Afterpulse documents | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_afterpulse_item**
> put_afterpulse_item(body, if_match, afterpulse_id)

Replaces a Afterpulse document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.AfterpulseApi(xepmts.ApiClient(configuration))
body = xepmts.Afterpulse() # Afterpulse | A Afterpulse or list of Afterpulse documents
if_match = 'if_match_example' # str | Current value of the _etag field
afterpulse_id = 'afterpulse_id_example' # str | 

try:
    # Replaces a Afterpulse document
    api_instance.put_afterpulse_item(body, if_match, afterpulse_id)
except ApiException as e:
    print("Exception when calling AfterpulseApi->put_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Afterpulse**](Afterpulse.md)| A Afterpulse or list of Afterpulse documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **afterpulse_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

