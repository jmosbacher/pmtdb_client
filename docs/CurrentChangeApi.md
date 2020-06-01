# xepmts.CurrentChangeApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_current_change_item**](CurrentChangeApi.md#delete_current_change_item) | **DELETE** /CurrentChanges/{currentchangeId} | Deletes a CurrentChange document
[**get_current_change_item**](CurrentChangeApi.md#get_current_change_item) | **GET** /CurrentChanges/{currentchangeId} | Retrieves a CurrentChange document
[**get_current_changes**](CurrentChangeApi.md#get_current_changes) | **GET** /CurrentChanges | Retrieves one or more CurrentChanges
[**post_current_changes**](CurrentChangeApi.md#post_current_changes) | **POST** /CurrentChanges | Stores one or more CurrentChanges.
[**put_current_change_item**](CurrentChangeApi.md#put_current_change_item) | **PUT** /CurrentChanges/{currentchangeId} | Replaces a CurrentChange document

# **delete_current_change_item**
> delete_current_change_item(currentchange_id, if_match)

Deletes a CurrentChange document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.CurrentChangeApi(xepmts.ApiClient(configuration))
currentchange_id = 'currentchange_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a CurrentChange document
    api_instance.delete_current_change_item(currentchange_id, if_match)
except ApiException as e:
    print("Exception when calling CurrentChangeApi->delete_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentchange_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_change_item**
> CurrentChange get_current_change_item(currentchange_id)

Retrieves a CurrentChange document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.CurrentChangeApi(xepmts.ApiClient(configuration))
currentchange_id = 'currentchange_id_example' # str | 

try:
    # Retrieves a CurrentChange document
    api_response = api_instance.get_current_change_item(currentchange_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentChangeApi->get_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **currentchange_id** | **str**|  | 

### Return type

[**CurrentChange**](CurrentChange.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_changes**
> InlineResponse2004 get_current_changes(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more CurrentChanges

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.CurrentChangeApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more CurrentChanges
    api_response = api_instance.get_current_changes(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrentChangeApi->get_current_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_current_changes**
> post_current_changes(body)

Stores one or more CurrentChanges.

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.CurrentChangeApi(xepmts.ApiClient(configuration))
body = xepmts.CurrentChange() # CurrentChange | A CurrentChange or list of CurrentChange documents

try:
    # Stores one or more CurrentChanges.
    api_instance.post_current_changes(body)
except ApiException as e:
    print("Exception when calling CurrentChangeApi->post_current_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CurrentChange**](CurrentChange.md)| A CurrentChange or list of CurrentChange documents | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_current_change_item**
> put_current_change_item(body, if_match, currentchange_id)

Replaces a CurrentChange document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.CurrentChangeApi(xepmts.ApiClient(configuration))
body = xepmts.CurrentChange() # CurrentChange | A CurrentChange or list of CurrentChange documents
if_match = 'if_match_example' # str | Current value of the _etag field
currentchange_id = 'currentchange_id_example' # str | 

try:
    # Replaces a CurrentChange document
    api_instance.put_current_change_item(body, if_match, currentchange_id)
except ApiException as e:
    print("Exception when calling CurrentChangeApi->put_current_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CurrentChange**](CurrentChange.md)| A CurrentChange or list of CurrentChange documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **currentchange_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

