# pmtdb_client.PmtInstallApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deletepmt_install_item**](PmtInstallApi.md#deletepmt_install_item) | **DELETE** /pmt_installs/{pmt_installId} | Deletes a pmt_install document
[**deletepmt_installs**](PmtInstallApi.md#deletepmt_installs) | **DELETE** /pmt_installs | Deletes all pmt_installs
[**getpmt_install_item**](PmtInstallApi.md#getpmt_install_item) | **GET** /pmt_installs/{pmt_installId} | Retrieves a pmt_install document
[**getpmt_install_item_by_pmt_no**](PmtInstallApi.md#getpmt_install_item_by_pmt_no) | **GET** /pmt_installs/{Pmt_No} | Retrieves a pmt_install document by pmt_no
[**getpmt_installs**](PmtInstallApi.md#getpmt_installs) | **GET** /pmt_installs | Retrieves one or more pmt_installs
[**postpmt_installs**](PmtInstallApi.md#postpmt_installs) | **POST** /pmt_installs | Stores one or more pmt_installs.
[**putpmt_install_item**](PmtInstallApi.md#putpmt_install_item) | **PUT** /pmt_installs/{pmt_installId} | Replaces a pmt_install document

# **deletepmt_install_item**
> deletepmt_install_item(pmt_install_id, if_match)

Deletes a pmt_install document

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
api_instance = pmtdb_client.PmtInstallApi(pmtdb_client.ApiClient(configuration))
pmt_install_id = 'pmt_install_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a pmt_install document
    api_instance.deletepmt_install_item(pmt_install_id, if_match)
except ApiException as e:
    print("Exception when calling PmtInstallApi->deletepmt_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmt_install_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletepmt_installs**
> deletepmt_installs()

Deletes all pmt_installs

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
api_instance = pmtdb_client.PmtInstallApi(pmtdb_client.ApiClient(configuration))

try:
    # Deletes all pmt_installs
    api_instance.deletepmt_installs()
except ApiException as e:
    print("Exception when calling PmtInstallApi->deletepmt_installs: %s\n" % e)
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

# **getpmt_install_item**
> PmtInstall getpmt_install_item(pmt_install_id)

Retrieves a pmt_install document

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
api_instance = pmtdb_client.PmtInstallApi(pmtdb_client.ApiClient(configuration))
pmt_install_id = 'pmt_install_id_example' # str | 

try:
    # Retrieves a pmt_install document
    api_response = api_instance.getpmt_install_item(pmt_install_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtInstallApi->getpmt_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmt_install_id** | **str**|  | 

### Return type

[**PmtInstall**](PmtInstall.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpmt_install_item_by_pmt_no**
> PmtInstall getpmt_install_item_by_pmt_no(pmt_no)

Retrieves a pmt_install document by pmt_no

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
api_instance = pmtdb_client.PmtInstallApi(pmtdb_client.ApiClient(configuration))
pmt_no = 'pmt_no_example' # str | 

try:
    # Retrieves a pmt_install document by pmt_no
    api_response = api_instance.getpmt_install_item_by_pmt_no(pmt_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtInstallApi->getpmt_install_item_by_pmt_no: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmt_no** | **str**|  | 

### Return type

[**PmtInstall**](PmtInstall.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getpmt_installs**
> InlineResponse2002 getpmt_installs(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more pmt_installs

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
api_instance = pmtdb_client.PmtInstallApi(pmtdb_client.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more pmt_installs
    api_response = api_instance.getpmt_installs(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PmtInstallApi->getpmt_installs: %s\n" % e)
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

# **postpmt_installs**
> postpmt_installs(body)

Stores one or more pmt_installs.

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
api_instance = pmtdb_client.PmtInstallApi(pmtdb_client.ApiClient(configuration))
body = pmtdb_client.PmtInstall() # PmtInstall | A pmt_install or list of pmt_install documents

try:
    # Stores one or more pmt_installs.
    api_instance.postpmt_installs(body)
except ApiException as e:
    print("Exception when calling PmtInstallApi->postpmt_installs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PmtInstall**](PmtInstall.md)| A pmt_install or list of pmt_install documents | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **putpmt_install_item**
> putpmt_install_item(body, if_match, pmt_install_id)

Replaces a pmt_install document

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
api_instance = pmtdb_client.PmtInstallApi(pmtdb_client.ApiClient(configuration))
body = pmtdb_client.PmtInstall() # PmtInstall | A pmt_install or list of pmt_install documents
if_match = 'if_match_example' # str | Current value of the _etag field
pmt_install_id = 'pmt_install_id_example' # str | 

try:
    # Replaces a pmt_install document
    api_instance.putpmt_install_item(body, if_match, pmt_install_id)
except ApiException as e:
    print("Exception when calling PmtInstallApi->putpmt_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PmtInstall**](PmtInstall.md)| A pmt_install or list of pmt_install documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **pmt_install_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

