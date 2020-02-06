# xepmts.PmtAfterpulseApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletepmt_afterpulse_item**](PmtAfterpulseApi.md#deletepmt_afterpulse_item) | **DELETE** /pmt_afterpulses/{pmt_afterpulseId} | Deletes a pmt_afterpulse document
[**deletepmt_afterpulses**](PmtAfterpulseApi.md#deletepmt_afterpulses) | **DELETE** /pmt_afterpulses | Deletes all pmt_afterpulses
[**getpmt_afterpulse_item**](PmtAfterpulseApi.md#getpmt_afterpulse_item) | **GET** /pmt_afterpulses/{pmt_afterpulseId} | Retrieves a pmt_afterpulse document
[**getpmt_afterpulses**](PmtAfterpulseApi.md#getpmt_afterpulses) | **GET** /pmt_afterpulses | Retrieves one or more pmt_afterpulses
[**postpmt_afterpulses**](PmtAfterpulseApi.md#postpmt_afterpulses) | **POST** /pmt_afterpulses | Stores one or more pmt_afterpulses.
[**putpmt_afterpulse_item**](PmtAfterpulseApi.md#putpmt_afterpulse_item) | **PUT** /pmt_afterpulses/{pmt_afterpulseId} | Replaces a pmt_afterpulse document

# **deletepmt_afterpulse_item**
> deletepmt_afterpulse_item(pmt_afterpulse_id, if_match)

Deletes a pmt_afterpulse document

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
api_instance = xepmts.PmtAfterpulseApi(xepmts.ApiClient(configuration))
pmt_afterpulse_id = 'pmt_afterpulse_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a pmt_afterpulse document
    api_instance.deletepmt_afterpulse_item(pmt_afterpulse_id, if_match)
except ApiException as e:
    print("Exception when calling PmtAfterpulseApi->deletepmt_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmt_afterpulse_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletepmt_afterpulses**
> deletepmt_afterpulses()

Deletes all pmt_afterpulses

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
api_instance = xepmts.PmtAfterpulseApi(xepmts.ApiClient(configuration))

try:
    # Deletes all pmt_afterpulses
    api_instance.deletepmt_afterpulses()
except ApiException as e:
    print("Exception when calling PmtAfterpulseApi->deletepmt_afterpulses: %s\n" % e)
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

# **getpmt_afterpulse_item**
> PmtAfterpulse getpmt_afterpulse_item(pmt_afterpulse_id)

Retrieves a pmt_afterpulse document

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
api_instance = xepmts.PmtAfterpulseApi(xepmts.ApiClient(configuration))
pmt_afterpulse_id = 'pmt_afterpulse_id_example' # str | 

try:
    # Retrieves a pmt_afterpulse document
    api_response = api_instance.getpmt_afterpulse_item(pmt_afterpulse_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtAfterpulseApi->getpmt_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmt_afterpulse_id** | **str**|  | 

### Return type

[**PmtAfterpulse**](PmtAfterpulse.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpmt_afterpulses**
> InlineResponse2002 getpmt_afterpulses(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more pmt_afterpulses

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
api_instance = xepmts.PmtAfterpulseApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more pmt_afterpulses
    api_response = api_instance.getpmt_afterpulses(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtAfterpulseApi->getpmt_afterpulses: %s\n" % e)
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

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postpmt_afterpulses**
> postpmt_afterpulses(body)

Stores one or more pmt_afterpulses.

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
api_instance = xepmts.PmtAfterpulseApi(xepmts.ApiClient(configuration))
body = xepmts.PmtAfterpulse() # PmtAfterpulse | A pmt_afterpulse or list of pmt_afterpulse documents

try:
    # Stores one or more pmt_afterpulses.
    api_instance.postpmt_afterpulses(body)
except ApiException as e:
    print("Exception when calling PmtAfterpulseApi->postpmt_afterpulses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PmtAfterpulse**](PmtAfterpulse.md)| A pmt_afterpulse or list of pmt_afterpulse documents | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putpmt_afterpulse_item**
> putpmt_afterpulse_item(body, if_match, pmt_afterpulse_id)

Replaces a pmt_afterpulse document

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
api_instance = xepmts.PmtAfterpulseApi(xepmts.ApiClient(configuration))
body = xepmts.PmtAfterpulse() # PmtAfterpulse | A pmt_afterpulse or list of pmt_afterpulse documents
if_match = 'if_match_example' # str | Current value of the _etag field
pmt_afterpulse_id = 'pmt_afterpulse_id_example' # str | 

try:
    # Replaces a pmt_afterpulse document
    api_instance.putpmt_afterpulse_item(body, if_match, pmt_afterpulse_id)
except ApiException as e:
    print("Exception when calling PmtAfterpulseApi->putpmt_afterpulse_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PmtAfterpulse**](PmtAfterpulse.md)| A pmt_afterpulse or list of pmt_afterpulse documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **pmt_afterpulse_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

