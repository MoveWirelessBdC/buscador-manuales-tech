Session API - Platform documentation






[Skip to content](#post-accounting-session)

# POST / Accounting Session

## Description

The **Accounting Session API** is a push API that sends accounting session data to an external server on every session
start and end.

It can be used to integrate the platform with services delivered by external providers.

Push Method:  
**POST**

## Push URL

The **Push URL** is the URL of the server which receives the collected data.

* It must start with **https://**
* It is set in **Portal Management → Properties → Advanced properties**: the keys are *sessionPushApiUrl* and
  *sessionPushApiBasicAuthCredential*
  + *sessionPushApiUrl* sets the Push API
  + *sessionPushApiBasicAuthCredential* is **optional**, and when defined, it enables transferring sessions to the URL
    with Basic Authentication.   
    **Note: It must have a specific format: "login:password".**
* When a session starts or ends, the entire path is searched for the above
  properties: from the organisation in which they log in, to root. Then, the profiles are sent to the Push URL.
* It is recommended to use the properties in an organisation which acts as the Data Administrator
* Property *sessionPushApiCustomerRefPropertyName* is optional and stores name of dynamic property storing value of
  customerRef to be sent along with session data

## Message

Format: JSON object  
Message elements:

| Name | Format | Description |
| --- | --- | --- |
| `emailData` | EmailData / null | Email data |
| `createdTime` | Long | Timestamp in milliseconds |
| `updatedTime` | Long | Timestamp in milliseconds |
| `customerRef` | String / null | Customer Ref |
| `bytesDown` | Long | Bytes downloaded |
| `bytesUp` | Long | Bytes uploaded |
| `sessionDuration` | Long | Duration of the session in seconds |
| `eventType` | String | start / stop |
| `deviceID` | String | Device ID |

### EmailData

| Name | Format | Description |
| --- | --- | --- |
| `emailAddress` | String | Email address |
| `confirmationDate` | Long / null | Timestamp in milliseconds. When null, it means the email is not confirmed |

## Example

```
{
  "emailData": {
    "emailAddress": "john.doe@example.com",
    "confirmationDate": 1561982019208
  },
  "createdTime": 1561982019208,
  "updatedTime": 1561982019208,
  "customerRef": "Customer 1",
  "bytesDown": 1000,
  "bytesUp": 2000,
  "sessionDuration": 3600,
  "eventType": "start",
  "deviceID": "AABBCCDDEEFF"
}

```