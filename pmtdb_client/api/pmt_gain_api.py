# coding: utf-8

"""
    PMT API

    API for the XenonnT PMT database  # noqa: E501

    OpenAPI spec version: 0.1
    Contact: joe.mosbacher@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from pmtdb_client.api_client import ApiClient


class PmtGainApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def deletepmt_gain_item(self, pmt_gain_id, if_match, **kwargs):  # noqa: E501
        """Deletes a pmt_gain document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletepmt_gain_item(pmt_gain_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pmt_gain_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletepmt_gain_item_with_http_info(pmt_gain_id, if_match, **kwargs)  # noqa: E501
        else:
            (data) = self.deletepmt_gain_item_with_http_info(pmt_gain_id, if_match, **kwargs)  # noqa: E501
            return data

    def deletepmt_gain_item_with_http_info(self, pmt_gain_id, if_match, **kwargs):  # noqa: E501
        """Deletes a pmt_gain document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletepmt_gain_item_with_http_info(pmt_gain_id, if_match, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pmt_gain_id: (required)
        :param str if_match: Current value of the _etag field (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pmt_gain_id', 'if_match']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deletepmt_gain_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pmt_gain_id' is set
        if ('pmt_gain_id' not in params or
                params['pmt_gain_id'] is None):
            raise ValueError("Missing the required parameter `pmt_gain_id` when calling `deletepmt_gain_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `deletepmt_gain_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pmt_gain_id' in params:
            path_params['pmt_gainId'] = params['pmt_gain_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pmt_gains/{pmt_gainId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def deletepmt_gains(self, **kwargs):  # noqa: E501
        """Deletes all pmt_gains  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletepmt_gains(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.deletepmt_gains_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.deletepmt_gains_with_http_info(**kwargs)  # noqa: E501
            return data

    def deletepmt_gains_with_http_info(self, **kwargs):  # noqa: E501
        """Deletes all pmt_gains  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.deletepmt_gains_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method deletepmt_gains" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pmt_gains', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getpmt_gain_item(self, pmt_gain_id, **kwargs):  # noqa: E501
        """Retrieves a pmt_gain document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getpmt_gain_item(pmt_gain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pmt_gain_id: (required)
        :return: PmtGain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getpmt_gain_item_with_http_info(pmt_gain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.getpmt_gain_item_with_http_info(pmt_gain_id, **kwargs)  # noqa: E501
            return data

    def getpmt_gain_item_with_http_info(self, pmt_gain_id, **kwargs):  # noqa: E501
        """Retrieves a pmt_gain document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getpmt_gain_item_with_http_info(pmt_gain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str pmt_gain_id: (required)
        :return: PmtGain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['pmt_gain_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getpmt_gain_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'pmt_gain_id' is set
        if ('pmt_gain_id' not in params or
                params['pmt_gain_id'] is None):
            raise ValueError("Missing the required parameter `pmt_gain_id` when calling `getpmt_gain_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pmt_gain_id' in params:
            path_params['pmt_gainId'] = params['pmt_gain_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pmt_gains/{pmt_gainId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PmtGain',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def getpmt_gains(self, **kwargs):  # noqa: E501
        """Retrieves one or more pmt_gains  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getpmt_gains(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.getpmt_gains_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.getpmt_gains_with_http_info(**kwargs)  # noqa: E501
            return data

    def getpmt_gains_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieves one or more pmt_gains  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.getpmt_gains_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str where: the filters query parameter (ex.: {\"number\": 10})
        :param str sort: the sort query parameter (ex.: \"city,-lastname\")
        :param int page: the pages query parameter
        :param int max_results: the max results query parameter
        :return: InlineResponse2006
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['where', 'sort', 'page', 'max_results']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method getpmt_gains" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'where' in params:
            query_params.append(('where', params['where']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'max_results' in params:
            query_params.append(('max_results', params['max_results']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pmt_gains', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InlineResponse2006',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def postpmt_gains(self, body, **kwargs):  # noqa: E501
        """Stores one or more pmt_gains.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postpmt_gains(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PmtGain body: A pmt_gain or list of pmt_gain documents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.postpmt_gains_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.postpmt_gains_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def postpmt_gains_with_http_info(self, body, **kwargs):  # noqa: E501
        """Stores one or more pmt_gains.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.postpmt_gains_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PmtGain body: A pmt_gain or list of pmt_gain documents (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method postpmt_gains" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `postpmt_gains`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pmt_gains', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def putpmt_gain_item(self, body, if_match, pmt_gain_id, **kwargs):  # noqa: E501
        """Replaces a pmt_gain document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putpmt_gain_item(body, if_match, pmt_gain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PmtGain body: A pmt_gain or list of pmt_gain documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str pmt_gain_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.putpmt_gain_item_with_http_info(body, if_match, pmt_gain_id, **kwargs)  # noqa: E501
        else:
            (data) = self.putpmt_gain_item_with_http_info(body, if_match, pmt_gain_id, **kwargs)  # noqa: E501
            return data

    def putpmt_gain_item_with_http_info(self, body, if_match, pmt_gain_id, **kwargs):  # noqa: E501
        """Replaces a pmt_gain document  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.putpmt_gain_item_with_http_info(body, if_match, pmt_gain_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param PmtGain body: A pmt_gain or list of pmt_gain documents (required)
        :param str if_match: Current value of the _etag field (required)
        :param str pmt_gain_id: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'if_match', 'pmt_gain_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method putpmt_gain_item" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `putpmt_gain_item`")  # noqa: E501
        # verify the required parameter 'if_match' is set
        if ('if_match' not in params or
                params['if_match'] is None):
            raise ValueError("Missing the required parameter `if_match` when calling `putpmt_gain_item`")  # noqa: E501
        # verify the required parameter 'pmt_gain_id' is set
        if ('pmt_gain_id' not in params or
                params['pmt_gain_id'] is None):
            raise ValueError("Missing the required parameter `pmt_gain_id` when calling `putpmt_gain_item`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'pmt_gain_id' in params:
            path_params['pmt_gainId'] = params['pmt_gain_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'if_match' in params:
            header_params['If-Match'] = params['if_match']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/pmt_gains/{pmt_gainId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
