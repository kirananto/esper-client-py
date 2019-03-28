# esper
This is a read only Esper SDK.  You can find out more about Esper at [https://shoonya.io](https://shoonya.io).

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.0.1
- Package version: 0.0.1
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import esper 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import esper
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import esper
from esper.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic_security
configuration = esper.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = esper.DeviceApi(esper.ApiClient(configuration))
enterprise_id = 'enterprise_id_example' # str | ID of the enterprise

try:
    # Find devices in an enterprise
    api_response = api_instance.get_all_devices(enterprise_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DeviceApi->get_all_devices: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://127.0.0.1:8000/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DeviceApi* | [**get_all_devices**](docs/DeviceApi.md#get_all_devices) | **GET** /enterprise/{enterprise_id}/device/ | Find devices in an enterprise

## Documentation For Models

 - [Device](docs/Device.md)
 - [DeviceListResponse](docs/DeviceListResponse.md)
 - [EmmDevice](docs/EmmDevice.md)

## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: api_key
- **Location**: HTTP header

## basic_security

- **Type**: HTTP basic authentication


## Author

developer@shoonya.io