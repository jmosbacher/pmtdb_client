# xepmts.InstallApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_install_item**](InstallApi.md#delete_install_item) | **DELETE** /Installs/{installId} | Deletes a Install document
[**delete_installs**](InstallApi.md#delete_installs) | **DELETE** /Installs | Deletes all Installs
[**get_install_item**](InstallApi.md#get_install_item) | **GET** /Installs/{installId} | Retrieves a Install document
[**get_install_item_by_uid**](InstallApi.md#get_install_item_by_uid) | **GET** /Installs/{Uid} | Retrieves a Install document by uid
[**get_installs**](InstallApi.md#get_installs) | **GET** /Installs | Retrieves one or more Installs
[**post_installs**](InstallApi.md#post_installs) | **POST** /Installs | Stores one or more Installs.
[**put_install_item**](InstallApi.md#put_install_item) | **PUT** /Installs/{installId} | Replaces a Install document

# **delete_install_item**
> delete_install_item(install_id, if_match)

Deletes a Install document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.InstallApi(xepmts.ApiClient(configuration))
install_id = 'install_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a Install document
    api_instance.delete_install_item(install_id, if_match)
except ApiException as e:
    print("Exception when calling InstallApi->delete_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_installs**
> delete_installs()

Deletes all Installs

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.InstallApi(xepmts.ApiClient(configuration))

try:
    # Deletes all Installs
    api_instance.delete_installs()
except ApiException as e:
    print("Exception when calling InstallApi->delete_installs: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_install_item**
> Install get_install_item(install_id)

Retrieves a Install document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.InstallApi(xepmts.ApiClient(configuration))
install_id = 'install_id_example' # str | 

try:
    # Retrieves a Install document
    api_response = api_instance.get_install_item(install_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallApi->get_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_id** | **str**|  | 

### Return type

[**Install**](Install.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_install_item_by_uid**
> Install get_install_item_by_uid(uid)

Retrieves a Install document by uid

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.InstallApi(xepmts.ApiClient(configuration))
uid = 'uid_example' # str | 

try:
    # Retrieves a Install document by uid
    api_response = api_instance.get_install_item_by_uid(uid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallApi->get_install_item_by_uid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uid** | **str**|  | 

### Return type

[**Install**](Install.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_installs**
> InlineResponse2009 get_installs(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more Installs

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.InstallApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more Installs
    api_response = api_instance.get_installs(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InstallApi->get_installs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_installs**
> post_installs(body)

Stores one or more Installs.

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.InstallApi(xepmts.ApiClient(configuration))
body = xepmts.Install() # Install | A Install or list of Install documents

try:
    # Stores one or more Installs.
    api_instance.post_installs(body)
except ApiException as e:
    print("Exception when calling InstallApi->post_installs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Install**](Install.md)| A Install or list of Install documents | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_install_item**
> put_install_item(body, if_match, install_id)

Replaces a Install document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.InstallApi(xepmts.ApiClient(configuration))
body = xepmts.Install() # Install | A Install or list of Install documents
if_match = 'if_match_example' # str | Current value of the _etag field
install_id = 'install_id_example' # str | 

try:
    # Replaces a Install document
    api_instance.put_install_item(body, if_match, install_id)
except ApiException as e:
    print("Exception when calling InstallApi->put_install_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Install**](Install.md)| A Install or list of Install documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **install_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

