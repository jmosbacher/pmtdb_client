# xepmts.PmtErrorApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pmt_error_item**](PmtErrorApi.md#delete_pmt_error_item) | **DELETE** /PmtErrors/{pmterrorId} | Deletes a PmtError document
[**get_pmt_error_item**](PmtErrorApi.md#get_pmt_error_item) | **GET** /PmtErrors/{pmterrorId} | Retrieves a PmtError document
[**get_pmt_errors**](PmtErrorApi.md#get_pmt_errors) | **GET** /PmtErrors | Retrieves one or more PmtErrors
[**post_pmt_errors**](PmtErrorApi.md#post_pmt_errors) | **POST** /PmtErrors | Stores one or more PmtErrors.
[**put_pmt_error_item**](PmtErrorApi.md#put_pmt_error_item) | **PUT** /PmtErrors/{pmterrorId} | Replaces a PmtError document

# **delete_pmt_error_item**
> delete_pmt_error_item(pmterror_id, if_match)

Deletes a PmtError document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.PmtErrorApi(xepmts.ApiClient(configuration))
pmterror_id = 'pmterror_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a PmtError document
    api_instance.delete_pmt_error_item(pmterror_id, if_match)
except ApiException as e:
    print("Exception when calling PmtErrorApi->delete_pmt_error_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmterror_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pmt_error_item**
> PmtError get_pmt_error_item(pmterror_id)

Retrieves a PmtError document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.PmtErrorApi(xepmts.ApiClient(configuration))
pmterror_id = 'pmterror_id_example' # str | 

try:
    # Retrieves a PmtError document
    api_response = api_instance.get_pmt_error_item(pmterror_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtErrorApi->get_pmt_error_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmterror_id** | **str**|  | 

### Return type

[**PmtError**](PmtError.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pmt_errors**
> InlineResponse200 get_pmt_errors(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more PmtErrors

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.PmtErrorApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more PmtErrors
    api_response = api_instance.get_pmt_errors(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtErrorApi->get_pmt_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pmt_errors**
> post_pmt_errors(body)

Stores one or more PmtErrors.

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.PmtErrorApi(xepmts.ApiClient(configuration))
body = xepmts.PmtError() # PmtError | A PmtError or list of PmtError documents

try:
    # Stores one or more PmtErrors.
    api_instance.post_pmt_errors(body)
except ApiException as e:
    print("Exception when calling PmtErrorApi->post_pmt_errors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PmtError**](PmtError.md)| A PmtError or list of PmtError documents | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_pmt_error_item**
> put_pmt_error_item(body, if_match, pmterror_id)

Replaces a PmtError document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.PmtErrorApi(xepmts.ApiClient(configuration))
body = xepmts.PmtError() # PmtError | A PmtError or list of PmtError documents
if_match = 'if_match_example' # str | Current value of the _etag field
pmterror_id = 'pmterror_id_example' # str | 

try:
    # Replaces a PmtError document
    api_instance.put_pmt_error_item(body, if_match, pmterror_id)
except ApiException as e:
    print("Exception when calling PmtErrorApi->put_pmt_error_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PmtError**](PmtError.md)| A PmtError or list of PmtError documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **pmterror_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

