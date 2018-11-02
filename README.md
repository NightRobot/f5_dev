# F5 test

​	testing api use in f5

## iControl REST

test REST API from **iControl User guide ver. 13.1** 

Discovering modules and companents**

GET https://192.168.25.42/mgmt/tm/ltm on browser

Or

```bash
curl -k -u admin:admin -X GET https://192.168.25.42/mgmt/tm/ltm
```

> Note** : A module that is not provisioned on a BIG-IP ystem will not appear in the OUTPUT.



Can use Query parameter in API

```bash
curl -k -u admin:admin -X GET https://localhost/mgmt/tm/ltm/pool/?$select=name
```

that show name of member in pool

->Open Data Protocal (OData)

API referance : [https://devcentral.f5.com/wiki/iControlREST.APIRef.ashx](https://devcentral.f5.com/wiki/iControlREST.APIRef.ashx)

**Node** and **Member** in pool separate configuration



API form -> https://<management-ip>/mgmt/[Child-Namespace](https://devcentral.f5.com/wiki/iControlREST.APIRef.ashx)





## Python SDK

install python sdk from pip python

```
pip install f5-sdk
```

In f5-SDK **Collection** object are **plural** usually,while **Resource** object are **singular**

​	When the [`Resource`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource) object’s corresponding URI is already plural, we append the name of the [collection](https://f5-sdk.readthedocs.io/en/latest/userguide/endpoints/collection.html#collection-section) with `_s`.

**Example:**

| URI                         | Collection            | Resource                      |
| --------------------------- | --------------------- | ----------------------------- |
| `/mgmt/tm/net/tunnels/`     | tm.net.tunnels        | tm.net.tunnels.tunnel         |
| `/mgmt/tm/ltm/pool`         | tm.ltm.pools          | tm.ltm.pools.pool             |
| `/mgmt/tm/ltm/pool/members` | tm.ltm.pool.members_s | tm.ltm.pool.members_s.members |

## REST URIs

You can directly infer REST URIs from the python expressions, and vice versa.

### Examples

```
Expression:     mgmt = ManagementRoot('<ip_address>', '<username>', '<password>')
URI Returned:   https://<ip_address>/mgmt/
```

```
Expression:     cm = mgmt.cm('<ip_address>', '<username>', '<password>')
URI Returned:   https://<ip_address>/mgmt/cm
```

```
Expression:     tm = mgmt.tm('<ip_address>', '<username>', '<password>')
URI Returned:   https://<ip_address>/mgmt/tm
```

```
Expression:     ltm = mgmt.tm.ltm('<ip_address>', '<username>', '<password>')
URI Returned:   https://<ip_address>/mgmt/tm/ltm/
```

```
Expression:     pools1 = mgmt.tm.ltm.pools
URI Returned:   https://<ip_address>/mgmt/tm/ltm/pool
```

```
Expression:     pool_a = pools1.create(partition="Common", name="foo")
URI Returned:   https://<ip_address>/mgmt/tm/ltm/pool/~Common~foo
```

## REST Endpoints

### iControl REST `kind` Parameter

kind parameter provide information about object that let you know what you should expect.

The iControl® REST API uses three types of `kind`: `collectionstate`, `state`, and `stats`.

| Kind              | Associated Objects                                           | Methods                                                      |
| ----------------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `collectionstate` | [`OrganizingCollection`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.OrganizingCollection)[`Collection`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Collection) | [`exists()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.exists) |
| `state`           | [`Resource`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource) | [`create()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.create)[`update()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.update)[`refresh()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.refresh)[`delete()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.delete)[`load()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.load)[`exists()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.exists) |
| `state`           | [`UnnamedResource`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.UnnamedResource) | [`update()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.update)[`refresh()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.refresh)[`load()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.load)[`exists()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.exists) |
| `stats`           | [`Resource`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource) | [`refresh()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.refresh)[`load()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.load)[`exists()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.exists) |

### Method

| Method                                                       | HTTP Command | Action(s)                                                    |
| ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ |
| [`create()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.create) | POST         | creates a new resource on the device with its own URI        |
| [`exec_cmd()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.mixins.CommandExecutionMixin.exec_cmd) | POST         | executes commands on applicable unnamed resources            |
| [`update()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.update) | PUT          | submits a new configuration to the device resource; sets theResource attributes to the state reported by the device |
| [`modify()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.ResourceBase.modify) | PATCH        | submits a new configuration to the device resource; sets onlythe attributes specified in modify method. This is differentfrom update because update will change all the attributes, notonly the ones that you specify. |
| [`refresh()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.refresh) | GET          | obtains the state of a device resource; sets the representingPython Resource Object; tracks device state via its attributes |
| [`delete()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.delete) | DELETE       | removes the resource from the device, sets `self.__dict__`to `{'deleted': True}` |
| [`load()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.load) | GET          | obtains the state of an existing resource on the device; setsthe Resource attributes to match that state |
| [`exists()`](https://f5-sdk.readthedocs.io/en/latest/apidoc/f5.bigip.html#f5.bigip.resource.Resource.exists) | GET          | checks for the existence of an object on the BIG-IP®         |



## Referance

LTM pool and node in load balance

- https://devcentral.f5.com/wiki/iControlREST.APIRef_tm_ltm_pool.ashx
- https://devcentral.f5.com/wiki/iControlREST.APIRef_tm_ltm_pool_members.ashx
- https://devcentral.f5.com/wiki/iControlREST.APIRef_tm_ltm_node.ashx

working with pool and members

- https://devcentral.f5.com/articles/icontrol-rest-working-with-pool-members

Example code not use library

- https://devcentral.f5.com/wiki/iControlREST.Python-Virtual-Server-Pool-Create.ashx

Example code use library

- https://f5-sdk.readthedocs.io/en/latest/userguide/basics.html#dynamic-attributes

lab f5

- https://clouddocs.f5.com/training/community/programmability/html/class1/module1/lab1.html

Cookbook

- https://devcentral.f5.com/articles/icontrol-rest-cookbook-24575

Wiki iControl

- https://devcentral.f5.com/wiki/iControlREST.HomePage.ashx

python-SDK

- https://f5-sdk.readthedocs.io/en/latest/userguide/basics.html#dynamic-attributes
- https://github.com/F5Networks/f5-common-python

