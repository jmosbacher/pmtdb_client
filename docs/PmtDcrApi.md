# xepmts.PmtDcrApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletepmt_dcr_item**](PmtDcrApi.md#deletepmt_dcr_item) | **DELETE** /pmt_dcrs/{pmt_dcrId} | Deletes a pmt_dcr document
[**deletepmt_dcrs**](PmtDcrApi.md#deletepmt_dcrs) | **DELETE** /pmt_dcrs | Deletes all pmt_dcrs
[**getpmt_dcr_item**](PmtDcrApi.md#getpmt_dcr_item) | **GET** /pmt_dcrs/{pmt_dcrId} | Retrieves a pmt_dcr document
[**getpmt_dcrs**](PmtDcrApi.md#getpmt_dcrs) | **GET** /pmt_dcrs | Retrieves one or more pmt_dcrs
[**postpmt_dcrs**](PmtDcrApi.md#postpmt_dcrs) | **POST** /pmt_dcrs | Stores one or more pmt_dcrs.
[**putpmt_dcr_item**](PmtDcrApi.md#putpmt_dcr_item) | **PUT** /pmt_dcrs/{pmt_dcrId} | Replaces a pmt_dcr document

# **deletepmt_dcr_item**
> deletepmt_dcr_item(pmt_dcr_id, if_match)

Deletes a pmt_dcr document

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
api_instance = xepmts.PmtDcrApi(xepmts.ApiClient(configuration))
pmt_dcr_id = 'pmt_dcr_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a pmt_dcr document
    api_instance.deletepmt_dcr_item(pmt_dcr_id, if_match)
except ApiException as e:
    print("Exception when calling PmtDcrApi->deletepmt_dcr_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmt_dcr_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletepmt_dcrs**
> deletepmt_dcrs()

Deletes all pmt_dcrs

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
api_instance = xepmts.PmtDcrApi(xepmts.ApiClient(configuration))

try:
    # Deletes all pmt_dcrs
    api_instance.deletepmt_dcrs()
except ApiException as e:
    print("Exception when calling PmtDcrApi->deletepmt_dcrs: %s\n" % e)
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

# **getpmt_dcr_item**
> PmtDcr getpmt_dcr_item(pmt_dcr_id)

Retrieves a pmt_dcr document

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
api_instance = xepmts.PmtDcrApi(xepmts.ApiClient(configuration))
pmt_dcr_id = 'pmt_dcr_id_example' # str | 

try:
    # Retrieves a pmt_dcr document
    api_response = api_instance.getpmt_dcr_item(pmt_dcr_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtDcrApi->getpmt_dcr_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmt_dcr_id** | **str**|  | 

### Return type

[**PmtDcr**](PmtDcr.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpmt_dcrs**
> InlineResponse2003 getpmt_dcrs(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more pmt_dcrs

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
api_instance = xepmts.PmtDcrApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more pmt_dcrs
    api_response = api_instance.getpmt_dcrs(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtDcrApi->getpmt_dcrs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postpmt_dcrs**
> postpmt_dcrs(body)

Stores one or more pmt_dcrs.

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
api_instance = xepmts.PmtDcrApi(xepmts.ApiClient(configuration))
body = xepmts.PmtDcr() # PmtDcr | A pmt_dcr or list of pmt_dcr documents

try:
    # Stores one or more pmt_dcrs.
    api_instance.postpmt_dcrs(body)
except ApiException as e:
    print("Exception when calling PmtDcrApi->postpmt_dcrs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PmtDcr**](PmtDcr.md)| A pmt_dcr or list of pmt_dcr documents | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putpmt_dcr_item**
> putpmt_dcr_item(body, if_match, pmt_dcr_id)

Replaces a pmt_dcr document

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
api_instance = xepmts.PmtDcrApi(xepmts.ApiClient(configuration))
body = xepmts.PmtDcr() # PmtDcr | A pmt_dcr or list of pmt_dcr documents
if_match = 'if_match_example' # str | Current value of the _etag field
pmt_dcr_id = 'pmt_dcr_id_example' # str | 

try:
    # Replaces a pmt_dcr document
    api_instance.putpmt_dcr_item(body, if_match, pmt_dcr_id)
except ApiException as e:
    print("Exception when calling PmtDcrApi->putpmt_dcr_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PmtDcr**](PmtDcr.md)| A pmt_dcr or list of pmt_dcr documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **pmt_dcr_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

