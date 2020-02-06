# xepmts.StatusChangeApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletestatus_change_item**](StatusChangeApi.md#deletestatus_change_item) | **DELETE** /status_changes/{status_changeId} | Deletes a status_change document
[**deletestatus_changes**](StatusChangeApi.md#deletestatus_changes) | **DELETE** /status_changes | Deletes all status_changes
[**getstatus_change_item**](StatusChangeApi.md#getstatus_change_item) | **GET** /status_changes/{status_changeId} | Retrieves a status_change document
[**getstatus_change_item_by_pmt_no**](StatusChangeApi.md#getstatus_change_item_by_pmt_no) | **GET** /status_changes/{Pmt_No} | Retrieves a status_change document by pmt_no
[**getstatus_changes**](StatusChangeApi.md#getstatus_changes) | **GET** /status_changes | Retrieves one or more status_changes
[**poststatus_changes**](StatusChangeApi.md#poststatus_changes) | **POST** /status_changes | Stores one or more status_changes.
[**putstatus_change_item**](StatusChangeApi.md#putstatus_change_item) | **PUT** /status_changes/{status_changeId} | Replaces a status_change document

# **deletestatus_change_item**
> deletestatus_change_item(status_change_id, if_match)

Deletes a status_change document

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
api_instance = xepmts.StatusChangeApi(xepmts.ApiClient(configuration))
status_change_id = 'status_change_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a status_change document
    api_instance.deletestatus_change_item(status_change_id, if_match)
except ApiException as e:
    print("Exception when calling StatusChangeApi->deletestatus_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_change_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletestatus_changes**
> deletestatus_changes()

Deletes all status_changes

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
api_instance = xepmts.StatusChangeApi(xepmts.ApiClient(configuration))

try:
    # Deletes all status_changes
    api_instance.deletestatus_changes()
except ApiException as e:
    print("Exception when calling StatusChangeApi->deletestatus_changes: %s\n" % e)
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

# **getstatus_change_item**
> StatusChange getstatus_change_item(status_change_id)

Retrieves a status_change document

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
api_instance = xepmts.StatusChangeApi(xepmts.ApiClient(configuration))
status_change_id = 'status_change_id_example' # str | 

try:
    # Retrieves a status_change document
    api_response = api_instance.getstatus_change_item(status_change_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusChangeApi->getstatus_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_change_id** | **str**|  | 

### Return type

[**StatusChange**](StatusChange.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getstatus_change_item_by_pmt_no**
> StatusChange getstatus_change_item_by_pmt_no(pmt_no)

Retrieves a status_change document by pmt_no

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
api_instance = xepmts.StatusChangeApi(xepmts.ApiClient(configuration))
pmt_no = 'pmt_no_example' # str | 

try:
    # Retrieves a status_change document by pmt_no
    api_response = api_instance.getstatus_change_item_by_pmt_no(pmt_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusChangeApi->getstatus_change_item_by_pmt_no: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmt_no** | **str**|  | 

### Return type

[**StatusChange**](StatusChange.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getstatus_changes**
> InlineResponse200 getstatus_changes(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more status_changes

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
api_instance = xepmts.StatusChangeApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more status_changes
    api_response = api_instance.getstatus_changes(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatusChangeApi->getstatus_changes: %s\n" % e)
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

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **poststatus_changes**
> poststatus_changes(body)

Stores one or more status_changes.

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
api_instance = xepmts.StatusChangeApi(xepmts.ApiClient(configuration))
body = xepmts.StatusChange() # StatusChange | A status_change or list of status_change documents

try:
    # Stores one or more status_changes.
    api_instance.poststatus_changes(body)
except ApiException as e:
    print("Exception when calling StatusChangeApi->poststatus_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusChange**](StatusChange.md)| A status_change or list of status_change documents | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putstatus_change_item**
> putstatus_change_item(body, if_match, status_change_id)

Replaces a status_change document

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
api_instance = xepmts.StatusChangeApi(xepmts.ApiClient(configuration))
body = xepmts.StatusChange() # StatusChange | A status_change or list of status_change documents
if_match = 'if_match_example' # str | Current value of the _etag field
status_change_id = 'status_change_id_example' # str | 

try:
    # Replaces a status_change document
    api_instance.putstatus_change_item(body, if_match, status_change_id)
except ApiException as e:
    print("Exception when calling StatusChangeApi->putstatus_change_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusChange**](StatusChange.md)| A status_change or list of status_change documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **status_change_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

