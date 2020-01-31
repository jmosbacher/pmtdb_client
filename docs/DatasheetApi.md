# pmtdb_client.DatasheetApi

All URIs are relative to *https://api.xepmts.yossisprojects.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_datasheet_item**](DatasheetApi.md#delete_datasheet_item) | **DELETE** /datasheets/{datasheetId} | Deletes a Datasheet document
[**deletedatasheets**](DatasheetApi.md#deletedatasheets) | **DELETE** /datasheets | Deletes all datasheets
[**get_datasheet_item**](DatasheetApi.md#get_datasheet_item) | **GET** /datasheets/{datasheetId} | Retrieves a Datasheet document
[**get_datasheet_item_by_pmt_no**](DatasheetApi.md#get_datasheet_item_by_pmt_no) | **GET** /datasheets/{Pmt_No} | Retrieves a Datasheet document by pmt_no
[**getdatasheets**](DatasheetApi.md#getdatasheets) | **GET** /datasheets | Retrieves one or more datasheets
[**postdatasheets**](DatasheetApi.md#postdatasheets) | **POST** /datasheets | Stores one or more datasheets.
[**put_datasheet_item**](DatasheetApi.md#put_datasheet_item) | **PUT** /datasheets/{datasheetId} | Replaces a Datasheet document

# **delete_datasheet_item**
> delete_datasheet_item(datasheet_id, if_match)

Deletes a Datasheet document

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
api_instance = pmtdb_client.DatasheetApi(pmtdb_client.ApiClient(configuration))
datasheet_id = 'datasheet_id_example' # str | 
if_match = 'if_match_example' # str | Current value of the _etag field

try:
    # Deletes a Datasheet document
    api_instance.delete_datasheet_item(datasheet_id, if_match)
except ApiException as e:
    print("Exception when calling DatasheetApi->delete_datasheet_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasheet_id** | **str**|  | 
 **if_match** | **str**| Current value of the _etag field | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deletedatasheets**
> deletedatasheets()

Deletes all datasheets

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
api_instance = pmtdb_client.DatasheetApi(pmtdb_client.ApiClient(configuration))

try:
    # Deletes all datasheets
    api_instance.deletedatasheets()
except ApiException as e:
    print("Exception when calling DatasheetApi->deletedatasheets: %s\n" % e)
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

# **get_datasheet_item**
> Datasheet get_datasheet_item(datasheet_id)

Retrieves a Datasheet document

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
api_instance = pmtdb_client.DatasheetApi(pmtdb_client.ApiClient(configuration))
datasheet_id = 'datasheet_id_example' # str | 

try:
    # Retrieves a Datasheet document
    api_response = api_instance.get_datasheet_item(datasheet_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasheetApi->get_datasheet_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datasheet_id** | **str**|  | 

### Return type

[**Datasheet**](Datasheet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasheet_item_by_pmt_no**
> Datasheet get_datasheet_item_by_pmt_no(pmt_no)

Retrieves a Datasheet document by pmt_no

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
api_instance = pmtdb_client.DatasheetApi(pmtdb_client.ApiClient(configuration))
pmt_no = 'pmt_no_example' # str | 

try:
    # Retrieves a Datasheet document by pmt_no
    api_response = api_instance.get_datasheet_item_by_pmt_no(pmt_no)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasheetApi->get_datasheet_item_by_pmt_no: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pmt_no** | **str**|  | 

### Return type

[**Datasheet**](Datasheet.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **getdatasheets**
> InlineResponse2003 getdatasheets(where=where, sort=sort, page=page, max_results=max_results)

Retrieves one or more datasheets

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
api_instance = pmtdb_client.DatasheetApi(pmtdb_client.ApiClient(configuration))
where = 'where_example' # str | the filters query parameter (ex.: {\"number\": 10}) (optional)
sort = 'sort_example' # str | the sort query parameter (ex.: \"city,-lastname\") (optional)
page = 56 # int | the pages query parameter (optional)
max_results = 56 # int | the max results query parameter (optional)

try:
    # Retrieves one or more datasheets
    api_response = api_instance.getdatasheets(where=where, sort=sort, page=page, max_results=max_results)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DatasheetApi->getdatasheets: %s\n" % e)
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

# **postdatasheets**
> postdatasheets(body)

Stores one or more datasheets.

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
api_instance = pmtdb_client.DatasheetApi(pmtdb_client.ApiClient(configuration))
body = pmtdb_client.Datasheet() # Datasheet | A Datasheet or list of Datasheet documents

try:
    # Stores one or more datasheets.
    api_instance.postdatasheets(body)
except ApiException as e:
    print("Exception when calling DatasheetApi->postdatasheets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Datasheet**](Datasheet.md)| A Datasheet or list of Datasheet documents | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_datasheet_item**
> put_datasheet_item(body, if_match, datasheet_id)

Replaces a Datasheet document

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
api_instance = pmtdb_client.DatasheetApi(pmtdb_client.ApiClient(configuration))
body = pmtdb_client.Datasheet() # Datasheet | A Datasheet or list of Datasheet documents
if_match = 'if_match_example' # str | Current value of the _etag field
datasheet_id = 'datasheet_id_example' # str | 

try:
    # Replaces a Datasheet document
    api_instance.put_datasheet_item(body, if_match, datasheet_id)
except ApiException as e:
    print("Exception when calling DatasheetApi->put_datasheet_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Datasheet**](Datasheet.md)| A Datasheet or list of Datasheet documents | 
 **if_match** | **str**| Current value of the _etag field | 
 **datasheet_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

