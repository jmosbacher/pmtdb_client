# xepmts.PmtApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_pmts**](PmtApi.md#delete_pmts) | **DELETE** /Pmts | Deletes all Pmts
[**deletepmt_item**](PmtApi.md#deletepmt_item) | **DELETE** /Pmts/{pmtId} | Deletes a pmt document
[**get_pmts**](PmtApi.md#get_pmts) | **GET** /Pmts | Retrieves one or more Pmts
[**getpmt_item**](PmtApi.md#getpmt_item) | **GET** /Pmts/{pmtId} | Retrieves a pmt document
[**getpmt_item_by_serial_number**](PmtApi.md#getpmt_item_by_serial_number) | **GET** /Pmts/{Serial_Number} | Retrieves a pmt document by serial_number
[**post_pmts**](PmtApi.md#post_pmts) | **POST** /Pmts | Stores one or more Pmts.
[**putpmt_item**](PmtApi.md#putpmt_item) | **PUT** /Pmts/{pmtId} | Replaces a pmt document

# **delete_pmts**
> delete_pmts()

Deletes all Pmts

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
api_instance = xepmts.PmtApi(xepmts.ApiClient(configuration))

try:
    # Deletes all Pmts
    api_instance.delete_pmts()
except ApiException as e:
    print("Exception when calling PmtApi->delete_pmts: %s\n" % e)
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

# **deletepmt_item**
> deletepmt_item(pmt_id, if_match)

Deletes a pmt document

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
api_instance = xepmts.PmtApi(xepmts.ApiClient(configuration))
pmt_id = 'pmt_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a pmt document
    api_instance.deletepmt_item(pmt_id, if_match)
except ApiException as e:
    print("Exception when calling PmtApi->deletepmt_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmt_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pmts**
> InlineResponse2002 get_pmts(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more Pmts

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
api_instance = xepmts.PmtApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more Pmts
    api_response = api_instance.get_pmts(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtApi->get_pmts: %s\n" % e)
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

# **getpmt_item**
> Pmt getpmt_item(pmt_id)

Retrieves a pmt document

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
api_instance = xepmts.PmtApi(xepmts.ApiClient(configuration))
pmt_id = 'pmt_id_example' # str | 

try:
    # Retrieves a pmt document
    api_response = api_instance.getpmt_item(pmt_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtApi->getpmt_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmt_id** | **str**|  | 

### Return type

[**Pmt**](Pmt.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpmt_item_by_serial_number**
> Pmt getpmt_item_by_serial_number(serial_number)

Retrieves a pmt document by serial_number

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
api_instance = xepmts.PmtApi(xepmts.ApiClient(configuration))
serial_number = 'serial_number_example' # str | 

try:
    # Retrieves a pmt document by serial_number
    api_response = api_instance.getpmt_item_by_serial_number(serial_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtApi->getpmt_item_by_serial_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**|  | 

### Return type

[**Pmt**](Pmt.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_pmts**
> post_pmts(body)

Stores one or more Pmts.

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
api_instance = xepmts.PmtApi(xepmts.ApiClient(configuration))
body = xepmts.Pmt() # Pmt | A pmt or list of pmt documents

try:
    # Stores one or more Pmts.
    api_instance.post_pmts(body)
except ApiException as e:
    print("Exception when calling PmtApi->post_pmts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pmt**](Pmt.md)| A pmt or list of pmt documents | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putpmt_item**
> putpmt_item(body, if_match, pmt_id)

Replaces a pmt document

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
api_instance = xepmts.PmtApi(xepmts.ApiClient(configuration))
body = xepmts.Pmt() # Pmt | A pmt or list of pmt documents
if_match = 'if_match_example' # str | Current value of the _etag field
pmt_id = 'pmt_id_example' # str | 

try:
    # Replaces a pmt document
    api_instance.putpmt_item(body, if_match, pmt_id)
except ApiException as e:
    print("Exception when calling PmtApi->putpmt_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Pmt**](Pmt.md)| A pmt or list of pmt documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **pmt_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

