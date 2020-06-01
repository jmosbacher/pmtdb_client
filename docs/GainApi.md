# xepmts.GainApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_gain_item**](GainApi.md#delete_gain_item) | **DELETE** /Gains/{gainId} | Deletes a Gain document
[**delete_gains**](GainApi.md#delete_gains) | **DELETE** /Gains | Deletes all Gains
[**get_gain_item**](GainApi.md#get_gain_item) | **GET** /Gains/{gainId} | Retrieves a Gain document
[**get_gains**](GainApi.md#get_gains) | **GET** /Gains | Retrieves one or more Gains
[**post_gains**](GainApi.md#post_gains) | **POST** /Gains | Stores one or more Gains.
[**put_gain_item**](GainApi.md#put_gain_item) | **PUT** /Gains/{gainId} | Replaces a Gain document

# **delete_gain_item**
> delete_gain_item(gain_id, if_match)

Deletes a Gain document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.GainApi(xepmts.ApiClient(configuration))
gain_id = 'gain_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a Gain document
    api_instance.delete_gain_item(gain_id, if_match)
except ApiException as e:
    print("Exception when calling GainApi->delete_gain_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gain_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_gains**
> delete_gains()

Deletes all Gains

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.GainApi(xepmts.ApiClient(configuration))

try:
    # Deletes all Gains
    api_instance.delete_gains()
except ApiException as e:
    print("Exception when calling GainApi->delete_gains: %s\n" % e)
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

# **get_gain_item**
> Gain get_gain_item(gain_id)

Retrieves a Gain document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.GainApi(xepmts.ApiClient(configuration))
gain_id = 'gain_id_example' # str | 

try:
    # Retrieves a Gain document
    api_response = api_instance.get_gain_item(gain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GainApi->get_gain_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gain_id** | **str**|  | 

### Return type

[**Gain**](Gain.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gains**
> InlineResponse2002 get_gains(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more Gains

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.GainApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more Gains
    api_response = api_instance.get_gains(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GainApi->get_gains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_gains**
> post_gains(body)

Stores one or more Gains.

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.GainApi(xepmts.ApiClient(configuration))
body = xepmts.Gain() # Gain | A Gain or list of Gain documents

try:
    # Stores one or more Gains.
    api_instance.post_gains(body)
except ApiException as e:
    print("Exception when calling GainApi->post_gains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Gain**](Gain.md)| A Gain or list of Gain documents | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_gain_item**
> put_gain_item(body, if_match, gain_id)

Replaces a Gain document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.GainApi(xepmts.ApiClient(configuration))
body = xepmts.Gain() # Gain | A Gain or list of Gain documents
if_match = 'if_match_example' # str | Current value of the _etag field
gain_id = 'gain_id_example' # str | 

try:
    # Replaces a Gain document
    api_instance.put_gain_item(body, if_match, gain_id)
except ApiException as e:
    print("Exception when calling GainApi->put_gain_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Gain**](Gain.md)| A Gain or list of Gain documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **gain_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

