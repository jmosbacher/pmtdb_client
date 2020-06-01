# xepmts.AccountApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_account_item**](AccountApi.md#delete_account_item) | **DELETE** /Accounts/{accountId} | Deletes a Account document
[**get_account_item**](AccountApi.md#get_account_item) | **GET** /Accounts/{accountId} | Retrieves a Account document
[**get_account_item_by_username**](AccountApi.md#get_account_item_by_username) | **GET** /Accounts/{Username} | Retrieves a Account document by username
[**get_accounts**](AccountApi.md#get_accounts) | **GET** /Accounts | Retrieves one or more Accounts
[**post_accounts**](AccountApi.md#post_accounts) | **POST** /Accounts | Stores one or more Accounts.
[**put_account_item**](AccountApi.md#put_account_item) | **PUT** /Accounts/{accountId} | Replaces a Account document

# **delete_account_item**
> delete_account_item(account_id, if_match)

Deletes a Account document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.AccountApi(xepmts.ApiClient(configuration))
account_id = 'account_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a Account document
    api_instance.delete_account_item(account_id, if_match)
except ApiException as e:
    print("Exception when calling AccountApi->delete_account_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_item**
> Account get_account_item(account_id)

Retrieves a Account document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.AccountApi(xepmts.ApiClient(configuration))
account_id = 'account_id_example' # str | 

try:
    # Retrieves a Account document
    api_response = api_instance.get_account_item(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

### Return type

[**Account**](Account.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_item_by_username**
> Account get_account_item_by_username(username)

Retrieves a Account document by username

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.AccountApi(xepmts.ApiClient(configuration))
username = 'username_example' # str | 

try:
    # Retrieves a Account document by username
    api_response = api_instance.get_account_item_by_username(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account_item_by_username: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**Account**](Account.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounts**
> InlineResponse20010 get_accounts(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more Accounts

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.AccountApi(xepmts.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more Accounts
    api_response = api_instance.get_accounts(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **where** | **str**| the filters query parameter (ex.: {\&quot;number\&quot;: 10}) | [optional] 
 **sort** | **str**| the sort query parameter (ex.: \&quot;city,-lastname\&quot;) | [optional] 
 **page** | **int**| the pages query parameter | [optional] 
 **max_results** | **int**| the max results query parameter | [optional] 

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_accounts**
> post_accounts(body)

Stores one or more Accounts.

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.AccountApi(xepmts.ApiClient(configuration))
body = xepmts.Account() # Account | A Account or list of Account documents

try:
    # Stores one or more Accounts.
    api_instance.post_accounts(body)
except ApiException as e:
    print("Exception when calling AccountApi->post_accounts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Account**](Account.md)| A Account or list of Account documents | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_account_item**
> put_account_item(body, if_match, account_id)

Replaces a Account document

### Example
```python
from __future__ import print_function
import time
import xepmts
from xepmts.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = xepmts.AccountApi(xepmts.ApiClient(configuration))
body = xepmts.Account() # Account | A Account or list of Account documents
if_match = 'if_match_example' # str | Current value of the _etag field
account_id = 'account_id_example' # str | 

try:
    # Replaces a Account document
    api_instance.put_account_item(body, if_match, account_id)
except ApiException as e:
    print("Exception when calling AccountApi->put_account_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Account**](Account.md)| A Account or list of Account documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **account_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

