# xepmts.DarkCountRateApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dark_count_rate_item**](DarkCountRateApi.md#delete_dark_count_rate_item) | **DELETE** /DarkCountRates/{darkcountrateId} | Deletes a DarkCountRate document
[**delete_dark_count_rates**](DarkCountRateApi.md#delete_dark_count_rates) | **DELETE** /DarkCountRates | Deletes all DarkCountRates
[**get_dark_count_rate_item**](DarkCountRateApi.md#get_dark_count_rate_item) | **GET** /DarkCountRates/{darkcountrateId} | Retrieves a DarkCountRate document
[**get_dark_count_rates**](DarkCountRateApi.md#get_dark_count_rates) | **GET** /DarkCountRates | Retrieves one or more DarkCountRates
[**post_dark_count_rates**](DarkCountRateApi.md#post_dark_count_rates) | **POST** /DarkCountRates | Stores one or more DarkCountRates.
[**put_dark_count_rate_item**](DarkCountRateApi.md#put_dark_count_rate_item) | **PUT** /DarkCountRates/{darkcountrateId} | Replaces a DarkCountRate document

# **delete_dark_count_rate_item**
> delete_dark_count_rate_item(darkcountrate_id, if_match)

Deletes a DarkCountRate document

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
api_instance = xepmts.DarkCountRateApi(xepmts.ApiClient(configuration))
darkcountrate_id = 'darkcountrate_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a DarkCountRate document
    api_instance.delete_dark_count_rate_item(darkcountrate_id, if_match)
except ApiException as e:
    print("Exception when calling DarkCountRateApi->delete_dark_count_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **darkcountrate_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dark_count_rates**
> delete_dark_count_rates()

Deletes all DarkCountRates

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
api_instance = xepmts.DarkCountRateApi(xepmts.ApiClient(configuration))

try:
    # Deletes all DarkCountRates
    api_instance.delete_dark_count_rates()
except ApiException as e:
    print("Exception when calling DarkCountRateApi->delete_dark_count_rates: %s\n" % e)
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

# **get_dark_count_rate_item**
> DarkCountRate get_dark_count_rate_item(darkcountrate_id)

Retrieves a DarkCountRate document

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
api_instance = xepmts.DarkCountRateApi(xepmts.ApiClient(configuration))
darkcountrate_id = 'darkcountrate_id_example' # str | 

try:
    # Retrieves a DarkCountRate document
    api_response = api_instance.get_dark_count_rate_item(darkcountrate_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DarkCountRateApi->get_dark_count_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **darkcountrate_id** | **str**|  | 

### Return type

[**DarkCountRate**](DarkCountRate.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dark_count_rates**
> InlineResponse2003 get_dark_count_rates(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more DarkCountRates

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
api_instance = xepmts.DarkCountRateApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more DarkCountRates
    api_response = api_instance.get_dark_count_rates(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DarkCountRateApi->get_dark_count_rates: %s\n" % e)
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

# **post_dark_count_rates**
> post_dark_count_rates(body)

Stores one or more DarkCountRates.

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
api_instance = xepmts.DarkCountRateApi(xepmts.ApiClient(configuration))
body = xepmts.DarkCountRate() # DarkCountRate | A DarkCountRate or list of DarkCountRate documents

try:
    # Stores one or more DarkCountRates.
    api_instance.post_dark_count_rates(body)
except ApiException as e:
    print("Exception when calling DarkCountRateApi->post_dark_count_rates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DarkCountRate**](DarkCountRate.md)| A DarkCountRate or list of DarkCountRate documents | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_dark_count_rate_item**
> put_dark_count_rate_item(body, if_match, darkcountrate_id)

Replaces a DarkCountRate document

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
api_instance = xepmts.DarkCountRateApi(xepmts.ApiClient(configuration))
body = xepmts.DarkCountRate() # DarkCountRate | A DarkCountRate or list of DarkCountRate documents
if_match = 'if_match_example' # str | Current value of the _etag field
darkcountrate_id = 'darkcountrate_id_example' # str | 

try:
    # Replaces a DarkCountRate document
    api_instance.put_dark_count_rate_item(body, if_match, darkcountrate_id)
except ApiException as e:
    print("Exception when calling DarkCountRateApi->put_dark_count_rate_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DarkCountRate**](DarkCountRate.md)| A DarkCountRate or list of DarkCountRate documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **darkcountrate_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

