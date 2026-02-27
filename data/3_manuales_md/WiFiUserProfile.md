WiFiUserProfile - Platform documentation






[Skip to content](#post-wifiuserprofile)

# POST / WiFiUserProfile

## Description

The **WiFiUserProfile** API is a push API that sends user data about users who successfully log in to WiFi or change
their data in the GDPR panel. It is sent every time a WiFi user gets access to the Internet, and/or makes changes to
their data.

It can be used to integrate the platform with services delivered by external providers, for instance, CRM software.

Push Method:  
**POST**

## Push URL

The **Push URL** is the URL of the server which receives the collected data.

* It must start with **https://**
* It is set in **Portal Management → Properties → Advanced properties**: the keys are *wiFiUserProfilePushApiUrl* and
  *wiFiUserProfilePushApiBasicAuthCredential*
  + *wiFiUserProfilePushApiUrl* sets the Push API
  + *wiFiUserProfilePushApiBasicAuthCredential* is **optional**, and when defined, it enables transferring user
    profiles to the URL with Basic Authentication.   
    **Note: It must have a specific format: "login:password".**
* When a user logs in to WiFi or changes their data in the GDPR panel, the entire path is searched for the above
  properties: from the organisation in which they log in, to root. Then, the profiles are sent to the Push URL.
* It is recommended to use the properties in an organisation which acts as the Data Administrator

**Note:** If the notification option is **enabled** in the parent organisation, then, when a user logs in to the network
in a sub-organization, this sub-organisation will also trigger a notification.

## Message

Format: JSON object  
Message elements:

| Name | Format | Description |
| --- | --- | --- |
| `firstName` | String / null | First name |
| `lastName` | String / null | Last name |
| `dateOfBirth` | Long / null | Timestamp in milliseconds |
| `gender` | String / null | Gender |
| `photoUrl` | String / null | Photo URL |
| `locale` | String / null | Localisation |
| `devicesIds` | List of strings | Device IDs |
| `activeOrganization` | ActiveOrganizationData / null | ID of organization into which user has logged in |
| `visitedOrganizationIds` | OrganizationData / null | IDs of visited organisations |
| `address` | AddressData / null | Address |
| `emailData` | EmailData / null | Email data |
| `phoneData` | PhoneData / null | Phone data |
| `socialMediaProfileActivity` | SocialMediaProfileActivity / null | Social Media profile activity |
| `termsSettings` | TermsSettings / null | Term settings |
| `isProfileRestricted` | True / false | When true, it means the user’s data is not used |
| `dateRegistered` | Long | Timestamp in milliseconds of profile creation date |

### ActiveOrganizationData

| Name | Format | Description |
| --- | --- | --- |
| `id` | Long | Organisation ID |
| `name` | String | When name is not reachable for some reason, the value is “ORGANIZATION\_NAME\_NOT\_FOUND” |
| `dynamicProperties` | Map (String -> String) | Map containing list of dynamically set properties for this organization. Keys are property names and values are property values. |

### OrganizationData

| Name | Format | Description |
| --- | --- | --- |
| `id` | Long | Organisation ID |
| `name` | String | When name is not reachable for some reason, the value is “ORGANIZATION\_NAME\_NOT\_FOUND” |

### AddressData

| Name | Format | Description |
| --- | --- | --- |
| `addressLine1` | String / null | Address line 1 |
| `addressLine2` | String / null | Address line 2 |
| `building` | String / null | Building details |
| `postCode` | String / null | Postal Code |
| `city` | String / null | City |
| `region` | String / null | Region |
| `country` | String / null | Country |

### EmailData

| Name | Format | Description |
| --- | --- | --- |
| `emailAddress` | String | Email address |
| `confirmationDate` | Long / null | Timestamp in milliseconds. When null, it means the email is not confirmed |

### PhoneData

| Name | Format | Description |
| --- | --- | --- |
| `phoneNumber` | String | Phone number |
| `confirmationDate` | Long / null | Timestamp in milliseconds. When null. it means the phone is not confirmed. |

### SocialMediaProfileActivity

| Name | Format | Description |
| --- | --- | --- |
| `socialMediaType` | String | Type of Social Media |
| `socialMediaProfileId` | String | Social Media Profile |

### TermsSettings

| Name | Format | Description |
| --- | --- | --- |
| `termsDetails` | List of TermsDetailsData | Lists detailed Terms data |
| `categoryDetails` | List of CategoryDetailsData | Lists detailed category data |
| `communicationChannelsDetails` | List of CommunicationChannelsDetailsData | Lists detailed communication channels data |

### TermsDetailsData

| Name | Format | Description |
| --- | --- | --- |
| `versionId` | String | Document version |
| `tag` | String | When tag name is not reachable for some reason, value is "TERMS\_NAME\_NOT\_FOUND” |
| `isAccepted` | Boolean | User accepted terms |
| `modificationTimestamp` | Long | Timestamp in milliseconds |
| `deviceId` | String / null | Device ID |
| `organization` | OrganizationData / null | Organisation details |

### CategoryDetailsData

| Name | Format | Description |
| --- | --- | --- |
| `versionId` | String | Document version |
| `tag/code>` | String | When tag name is not reachable for some reason, the value is "MARKETING\_CATEGORY\_NAME\_NOT\_FOUND” |
| `isAccepted` | Boolean | User accepted marketing categories |
| `modificationTimestamp` | Long | Timestamp in milliseconds |
| `deviceId` | String / null | Device ID |
| `organization` | OrganizationData / null | Organisation details |

### CommunicationChannelsDetailsData

| Name | Format | Description |
| --- | --- | --- |
| `versionId` | String | Document version |
| `modificationTimestamp` | Long | Timestamp in milliseconds |
| `deviceId` | String / null | Device ID |
| `selectedCommunicationMethods` | List of strings | Lists selected communication methods |
| `organization` | OrganizationData / null | Organisation details |

## Example

```
{
  "firstName": "Jon",
  "lastName": "Doe",
  "dateOfBirth": 57888000000,
  "gender": "Male",
  "photoUrl": null,
  "locale": null,
  "devicesIds": [
    "5d19bc43dc366538e2cc0340"
  ],
  "activeOrganization": {
    "id": 2137,
    "name": "OrganizationWhereLoggedIn",
    "dynamicProperties": {
      "customPropertyName1": "customPropertyValue1",
      "otherProperty": "customPropertyValue2"
    }
  },
  "visitedOrganizationIds": [
    {
      "id": 10015,
      "name": "TestOrganization"
    }
  ],
  "address": {
    "addressLine1": "My Address Line 1",
    "addressLine2": "My Address Line 2",
    "building": "31A",
    "postCode": "11-111",
    "city": "Krakow",
    "region": null,
    "country": "Poland"
  },
  "emailData": {
    "emailAddress": "test@test.test",
    "confirmationDate": null
  },
  "phoneData": null,
  "socialMediaProfileActivity": [
    {
      "socialMediaType": "Twitter",
      "socialMediaProfileId": "123"
    }
  ],
  "termsSettings": {
    "termsDetails": [
      {
        "versionId": "5cb0b1e449d7485cb39a439b",
        "tag": "Terms 1",
        "isAccepted": true,
        "modificationTimestamp": 1561967718724,
        "deviceId": "5d19bc43dc366538e2cc0340",
        "organization": {
          "id": 10015,
          "name": "TestOrganization"
        }
      }
    ],
    "categoryDetails": [
      {
        "versionId": "5d19f4e4dc366554ca6a847d",
        "tag": "category details",
        "isAccepted": true,
        "modificationTimestamp": 1561982286114,
        "deviceId": "5d19f545dc366554ca6a8490",
        "organization": {
          "id": 10015,
          "name": "TestOrganization"
        }
      },
      {
        "versionId": "5d0a20f18c86197b3e6e0cb6",
        "tag": "category details 2",
        "isAccepted": false,
        "modificationTimestamp": 1561982286114,
        "deviceId": "5d19f545dc366554ca6a8490",
        "organization": {
          "id": 10015,
          "name": "TestOrganization"
        }
      }
    ],
    "communicationChannelsDetails": [
      {
        "versionId": "5d19f360dc3665431e90a6b4",
        "modificationTimestamp": 1561982019208,
        "deviceId": "5d19f43bdc366554ca6a8457",
        "selectedCommunicationMethods": [
          "E-mail",
          "SMS",
          "On-screen message",
          "Social media",
          "Custom method"
        ],
        "organization": {
          "id": 10015,
          "name": "TestOrganization"
        }
      }
    ]
  },
  "isProfileRestricted": true,
  "dateRegistered": 1551982019208
}

```