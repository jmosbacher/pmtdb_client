# pmtdb_client.PmtGainApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletepmt_gain_item**](PmtGainApi.md#deletepmt_gain_item) | **DELETE** /pmt_gains/{pmt_gainId} | Deletes a pmt_gain document
[**deletepmt_gains**](PmtGainApi.md#deletepmt_gains) | **DELETE** /pmt_gains | Deletes all pmt_gains
[**getpmt_gain_item**](PmtGainApi.md#getpmt_gain_item) | **GET** /pmt_gains/{pmt_gainId} | Retrieves a pmt_gain document
[**getpmt_gains**](PmtGainApi.md#getpmt_gains) | **GET** /pmt_gains | Retrieves one or more pmt_gains
[**postpmt_gains**](PmtGainApi.md#postpmt_gains) | **POST** /pmt_gains | Stores one or more pmt_gains.
[**putpmt_gain_item**](PmtGainApi.md#putpmt_gain_item) | **PUT** /pmt_gains/{pmt_gainId} | Replaces a pmt_gain document

# **deletepmt_gain_item**
> deletepmt_gain_item(pmt_gain_id, if_match)

Deletes a pmt_gain document

### Example
```python
from __future__ import print_function
import time
import pmtdb_client
from pmtdb_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = pmtdb_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pmtdb_client.PmtGainApi(pmtdb_client.ApiClient(configuration))
pmt_gain_id = 'pmt_gain_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a pmt_gain document
    api_instance.deletepmt_gain_item(pmt_gain_id, if_match)
except ApiException as e:
    print("Exception when calling PmtGainApi->deletepmt_gain_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmt_gain_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletepmt_gains**
> deletepmt_gains()

Deletes all pmt_gains

### Example
```python
from __future__ import print_function
import time
import pmtdb_client
from pmtdb_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = pmtdb_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pmtdb_client.PmtGainApi(pmtdb_client.ApiClient(configuration))

try:
    # Deletes all pmt_gains
    api_instance.deletepmt_gains()
except ApiException as e:
    print("Exception when calling PmtGainApi->deletepmt_gains: %s\n" % e)
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

# **getpmt_gain_item**
> PmtGain getpmt_gain_item(pmt_gain_id)

Retrieves a pmt_gain document

### Example
```python
from __future__ import print_function
import time
import pmtdb_client
from pmtdb_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = pmtdb_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pmtdb_client.PmtGainApi(pmtdb_client.ApiClient(configuration))
pmt_gain_id = 'pmt_gain_id_example' # str | 

try:
    # Retrieves a pmt_gain document
    api_response = api_instance.getpmt_gain_item(pmt_gain_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtGainApi->getpmt_gain_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmt_gain_id** | **str**|  | 

### Return type

[**PmtGain**](PmtGain.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpmt_gains**
> InlineResponse2006 getpmt_gains(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more pmt_gains

### Example
```python
from __future__ import print_function
import time
import pmtdb_client
from pmtdb_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = pmtdb_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pmtdb_client.PmtGainApi(pmtdb_client.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more pmt_gains
    api_response = api_instance.getpmt_gains(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtGainApi->getpmt_gains: %s\n" % e)
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

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postpmt_gains**
> postpmt_gains(body)

Stores one or more pmt_gains.

### Example
```python
from __future__ import print_function
import time
import pmtdb_client
from pmtdb_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = pmtdb_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pmtdb_client.PmtGainApi(pmtdb_client.ApiClient(configuration))
body = pmtdb_client.PmtGain() # PmtGain | A pmt_gain or list of pmt_gain documents

try:
    # Stores one or more pmt_gains.
    api_instance.postpmt_gains(body)
except ApiException as e:
    print("Exception when calling PmtGainApi->postpmt_gains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PmtGain**](PmtGain.md)| A pmt_gain or list of pmt_gain documents | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putpmt_gain_item**
> putpmt_gain_item(body, if_match, pmt_gain_id)

Replaces a pmt_gain document

### Example
```python
from __future__ import print_function
import time
import pmtdb_client
from pmtdb_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = pmtdb_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = pmtdb_client.PmtGainApi(pmtdb_client.ApiClient(configuration))
body = pmtdb_client.PmtGain() # PmtGain | A pmt_gain or list of pmt_gain documents
if_match = 'if_match_example' # str | Current value of the _etag field
pmt_gain_id = 'pmt_gain_id_example' # str | 

try:
    # Replaces a pmt_gain document
    api_instance.putpmt_gain_item(body, if_match, pmt_gain_id)
except ApiException as e:
    print("Exception when calling PmtGainApi->putpmt_gain_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PmtGain**](PmtGain.md)| A pmt_gain or list of pmt_gain documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **pmt_gain_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

