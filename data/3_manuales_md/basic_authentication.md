Basic Authentication - Platform documentation






[Skip to content](#basic-authentication)

# Basic authentication

## Description

The authentication described here is required by some endpoints in order to give access to stored data. It is a standard implementation based on RFC7235 and RFC2617.

## Request

When you pass your credentials in the header, you must Base64-encode them in UTF8 and use the following format:   
`Authorization: Basic Base64(login:password)`

**Example:**  
`Authorization: Basic bXlMb2dpbjpteVBhc3N3b3Jk`

## Response

**Error responses**  
Code: 401 Unauthorized  
Description: The Authorization header or credentials are invalid.  
Header: `WWW-Authenticate: Basic realm=Linkyfi`

Note

In most cases, the `realm` is **Linkyfi**, which means that you should use your Linkyfi credentials. Exact information about credentials are provided in specific endpoint section.