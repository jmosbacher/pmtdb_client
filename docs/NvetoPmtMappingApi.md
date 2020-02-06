# xepmts.NvetoPmtMappingApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletenveto_pmt_mapping_item**](NvetoPmtMappingApi.md#deletenveto_pmt_mapping_item) | **DELETE** /nveto_pmt_mappings/{nveto_pmt_mappingId} | Deletes a nveto_pmt_mapping document
[**deletenveto_pmt_mappings**](NvetoPmtMappingApi.md#deletenveto_pmt_mappings) | **DELETE** /nveto_pmt_mappings | Deletes all nveto_pmt_mappings
[**getnveto_pmt_mapping_item**](NvetoPmtMappingApi.md#getnveto_pmt_mapping_item) | **GET** /nveto_pmt_mappings/{nveto_pmt_mappingId} | Retrieves a nveto_pmt_mapping document
[**getnveto_pmt_mappings**](NvetoPmtMappingApi.md#getnveto_pmt_mappings) | **GET** /nveto_pmt_mappings | Retrieves one or more nveto_pmt_mappings
[**postnveto_pmt_mappings**](NvetoPmtMappingApi.md#postnveto_pmt_mappings) | **POST** /nveto_pmt_mappings | Stores one or more nveto_pmt_mappings.
[**putnveto_pmt_mapping_item**](NvetoPmtMappingApi.md#putnveto_pmt_mapping_item) | **PUT** /nveto_pmt_mappings/{nveto_pmt_mappingId} | Replaces a nveto_pmt_mapping document

# **deletenveto_pmt_mapping_item**
> deletenveto_pmt_mapping_item(nveto_pmt_mapping_id, if_match)

Deletes a nveto_pmt_mapping document

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
api_instance = xepmts.NvetoPmtMappingApi(xepmts.ApiClient(configuration))
nveto_pmt_mapping_id = 'nveto_pmt_mapping_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a nveto_pmt_mapping document
    api_instance.deletenveto_pmt_mapping_item(nveto_pmt_mapping_id, if_match)
except ApiException as e:
    print("Exception when calling NvetoPmtMappingApi->deletenveto_pmt_mapping_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nveto_pmt_mapping_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletenveto_pmt_mappings**
> deletenveto_pmt_mappings()

Deletes all nveto_pmt_mappings

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
api_instance = xepmts.NvetoPmtMappingApi(xepmts.ApiClient(configuration))

try:
    # Deletes all nveto_pmt_mappings
    api_instance.deletenveto_pmt_mappings()
except ApiException as e:
    print("Exception when calling NvetoPmtMappingApi->deletenveto_pmt_mappings: %s\n" % e)
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

# **getnveto_pmt_mapping_item**
> NvetoPmtMapping getnveto_pmt_mapping_item(nveto_pmt_mapping_id)

Retrieves a nveto_pmt_mapping document

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
api_instance = xepmts.NvetoPmtMappingApi(xepmts.ApiClient(configuration))
nveto_pmt_mapping_id = 'nveto_pmt_mapping_id_example' # str | 

try:
    # Retrieves a nveto_pmt_mapping document
    api_response = api_instance.getnveto_pmt_mapping_item(nveto_pmt_mapping_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NvetoPmtMappingApi->getnveto_pmt_mapping_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nveto_pmt_mapping_id** | **str**|  | 

### Return type

[**NvetoPmtMapping**](NvetoPmtMapping.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getnveto_pmt_mappings**
> InlineResponse2005 getnveto_pmt_mappings(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more nveto_pmt_mappings

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
api_instance = xepmts.NvetoPmtMappingApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more nveto_pmt_mappings
    api_response = api_instance.getnveto_pmt_mappings(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NvetoPmtMappingApi->getnveto_pmt_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **postnveto_pmt_mappings**
> postnveto_pmt_mappings(body)

Stores one or more nveto_pmt_mappings.

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
api_instance = xepmts.NvetoPmtMappingApi(xepmts.ApiClient(configuration))
body = xepmts.NvetoPmtMapping() # NvetoPmtMapping | A nveto_pmt_mapping or list of nveto_pmt_mapping documents

try:
    # Stores one or more nveto_pmt_mappings.
    api_instance.postnveto_pmt_mappings(body)
except ApiException as e:
    print("Exception when calling NvetoPmtMappingApi->postnveto_pmt_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NvetoPmtMapping**](NvetoPmtMapping.md)| A nveto_pmt_mapping or list of nveto_pmt_mapping documents | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putnveto_pmt_mapping_item**
> putnveto_pmt_mapping_item(body, if_match, nveto_pmt_mapping_id)

Replaces a nveto_pmt_mapping document

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
api_instance = xepmts.NvetoPmtMappingApi(xepmts.ApiClient(configuration))
body = xepmts.NvetoPmtMapping() # NvetoPmtMapping | A nveto_pmt_mapping or list of nveto_pmt_mapping documents
if_match = 'if_match_example' # str | Current value of the _etag field
nveto_pmt_mapping_id = 'nveto_pmt_mapping_id_example' # str | 

try:
    # Replaces a nveto_pmt_mapping document
    api_instance.putnveto_pmt_mapping_item(body, if_match, nveto_pmt_mapping_id)
except ApiException as e:
    print("Exception when calling NvetoPmtMappingApi->putnveto_pmt_mapping_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NvetoPmtMapping**](NvetoPmtMapping.md)| A nveto_pmt_mapping or list of nveto_pmt_mapping documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **nveto_pmt_mapping_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

