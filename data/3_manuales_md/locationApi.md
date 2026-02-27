Location API - Platform documentation






[Skip to content](#location-api)

# Location API

The **Location API** enables the identification of user location. You can find the Location API endpoints listed below.

To view the additional Location API, go to the [API Documentation](/API), and see the **Historical Location** section.

## GET /location/{venueId}/allLocations

It returns information on all users and their position at the venue which can be displayed in the Device Mapper. The user location is determined in relation to the point (0,0) specified in the Venue configuration.

### Request

Authentication: *Basic Auth*  
Method: *GET*  
URL: */location/{venueId}/allLocations*

URL parameters:

| Name | Type | Description |
| --- | --- | --- |
| venueId | string | ID of the Venue visible in Portal Management / Structure / Venues |

### Responses

#### Success response

Code: *200*

#### Description

Format: JSON object

Response elements:

| Name | Type | Description |
| --- | --- | --- |
| locations | object | keys: macs of devices, values: corresponding positions of devices |

Position element:

| Name | Type | Description |
| --- | --- | --- |
| x | string | User's location against x axis |
| y | string | User's position against the y axis |
| floor | integer | Floor number where Device is located |

#### Example

```
{
 "12:34:56:78:FF:AA": {
   "x": "-37.9",
   "y": "46.5",
   "floor": 1
 },
 "10:30:47:61:12:AF": {
   "x": "-150.5",
   "y": "28.7",
   "floor": 1
 }
}


```

#### Error responses

Code: *404 Not found*

Description: *The provided venueId in the URL parameters does not exist*