Cisco with Catalyst WC - Platform documentation






[Skip to content](#cisco-with-catalyst-wireless-controller-guide)

# Cisco with Catalyst Wireless Controller Guide

## Introduction

This guide will help you configure your Cisco Catalyst Wireless Controller to work with platform.

Instruction and screens were based on Cisco Catalyst C9800-CL version 17.9.4.

## Prerequisites and basic configuration

To start with your Cisco configuration, you need to fulfil certain prerequisites and prepare your basic configuration.

### Prerequisites

You should verify that Cisco Catalyst Wireless Controller:

* has correctly configured IP settings with a correct DNS server;
* resolves the platform domain address;
* has access to the platform using ports *80*, *1812*, and *1813*;
* runs software version 17.3 or higher (recommended at least 17.9.4 for best stability).

### Basic configuration

Below, you can find the table providing the data for the **Production Environments**, which are the cloud servers of the
platform.

| Name | URL | IP |
| --- | --- | --- |
| Linkyfi UVA | uva.linkyfi.com | 35.245.165.143 |

## Configuration

### Configuring the AAA

#### Configure Radius

1. Go to the **Configuration > Security > AAA**.
2. Select the **Servers/Groups** tab.
3. Choose **RADIUS > Servers** and click the **+Add** button.
4. Configure **Edit AAA Radius Server**:
   1. Into the **Name** field, type any name for your RADIUS server. For this instruction, it is **Testmaster**.
   2. Into the **Server Address** field, enter the server’s IP address.
   3. From the **Key Type** dropdown list, select the **Clear Text**.
   4. Into the **Key** field, enter the RADIUS password. For this instruction, it is **bAZev44u**.
   5. Into the **Confirm Key** field, enter again the RADIUS password. For this instruction, it is **bAZev44u**.
   6. Into the **Auth Port** field, enter the Authorization server port. For this instruction, it is **1812**.
   7. Into the **Acct Port** field, enter the Accounting server port. For this instruction, it is **1813**.
   8. Into the **Server Timeout (seconds)** field, enter the desired number of seconds. For this instruction, it is
      **10**.
   9. Into the **Retry Count** field, enter the desired number. For this instruction, it is **3**.
      ![Cisco AAA Radius Server](images/cisco_catalyst/cisco_1.png)
5. Then, click the **Update & Apply to Device** button to save the configuration.
6. Now go to **RADIUS > Server Groups** and click the **+Add** button.
7. Configure **Edit AAA Radius Server Group**:
   1. Into the **Name** field, type any name for your RADIUS server group. For this instruction, it is **Testmaster**.
   2. From the **MAC-Delimiter** dropdown list, select the **hyphen**.
   3. From the **MAC-Filtering** dropdown list, select the **mac**.
   4. Move the configured server group from **Available Servers** to **Assigned Servers**.
      ![Cisco AAA Radius Server Group](images/cisco_catalyst/cisco_2.png)
8. Then, click the **Update & Apply to Device** button to save the configuration.

#### Configure Authentication

1. Go to the **AAA Method List** tab.
2. Choose **AAA Method List > Authentication** and click the **+Add** button.
3. Configure **Quick Setup: AAA Authentication**:
   1. Into the **Method List Name** field, type any name for your method list. For this instruction, it is
      **Testmaster\_authe**.
   2. From the **Type** dropdown list, select the **login**.
   3. From the **Group Type** dropdown list, select the **group**.
   4. Move the configured server from **Available Servers** to **Assigned Servers**.
      ![Cisco AAA Authentication](images/cisco_catalyst/cisco_3.png)
4. Then, click the **Update & Apply to Device** button to save the configuration.

#### Configure Authorization

1. Choose **AAA Method List > Authorization** and click the **+Add** button.
2. Configure **Quick Setup: AAA Authorization**:
   1. Into the **Method List Name** field, type any name for your method list. For this instruction, it is
      **Testmaster\_autho**.
   2. From the **Type** dropdown list, select the **network**.
   3. From the **Group Type** dropdown list, select the **group**.
   4. Move the configured server from **Available Servers** to **Assigned Servers**.
      ![Cisco AAA Authorization](images/cisco_catalyst/cisco_4.png)
3. Then, click the **Update & Apply to Device** button to save the configuration.

#### Configure Accounting

1. Choose **AAA Method List > Accounting** and click the **+Add** button.
2. Configure **Quick Setup: AAA Accounting**:
   1. Into the **Method List Name** field, type any name for your method list. For this instruction, it is
      **Testmaster\_acc**.
   2. From the **Type** dropdown list, select the **identity**.
   3. Move the configured server from **Available Servers** to **Assigned Servers**.
      ![Cisco AAA Accounting](images/cisco_catalyst/cisco_5.png)
3. Then, click the **Update & Apply to Device** button to save the configuration.

#### Configure AAA Advanced:

1. Go to the **AAA Advanced** tab.
2. Configure **Global Config**:
   1. Expand **Show Advanced Settings**
   2. In the **Radius Attributes**:
      * Called-station-id: Accounting > macaddress
      * Called-station-id: Authentication > ap-macaddress
        ![Cisco AAA Advanced](images/cisco_catalyst/cisco_6.png)

### Configuring the Captive Portal

1. Go to the **Configuration > Security > Web Auth**.
2. Modify the preconfigured Web Auth Parameter by selecting **global**.
3. Configure **Web Auth Parameter**.
4. In the **General** tab:
   1. Select the **Captive Bypass Portal** checkbox.
   2. Select the **Disable Success Window** checkbox.
   3. Select the **Disable Logout Window** checkbox.
      ![Cisco Web Auth Parameter 1](images/cisco_catalyst/cisco_7.png)
5. Go back to the **Web Auth** window and click the **+Add** button.
6. Configure **Web Auth Parameter**.
7. Select the **General** tab:
   1. Into the **Parameter-map Name** field, type any name for your Parameter-map. For this instruction, it is
      **Testmaster**.
   2. Into the **Maximum HTTP connections** field, enter **200**.
   3. Into the **Init-State Timeout(secs)** field, enter **60**.
   4. From the **Type** dropdown list, select the **webauth**.
   5. Select the **Captive Bypass Portal** checkbox.
   6. Select the **Disable Success Window** checkbox.
   7. Select the **Disable Logout Window** checkbox.
   8. Select the **Disable Cisco Logo** checkbox.
      ![Cisco Web Auth Parameter 2](images/cisco_catalyst/cisco_8.png)
8. Select the **Advanced** tab:
   1. Into the **Redirect URL for login** field, enter the captive portal address `https://platform.com/login`
   2. Into the **Redirect Append for AP MAC Address** field, enter **apname**.
   3. Into the **Redirect Append for Client MAC Address field**, enter **mac**.
   4. Into the **Redirect Append for WLAN SSID** field, enter **essid**.
   5. Into the **Portal IPV4 Address** field, enter the platform server’s IP address.
      ![Cisco Web Auth Parameter 3](images/cisco_catalyst/cisco_9.png)
9. Then, click the **Update & Apply** button to save the configuration.

### Configuring the URL Filters

1. Go to **Configuration > Security > URL Filters** and click the **+Add** button.
2. Configure the **URL Filter**:
   1. Into the **List Name** field, type any name for your List. For this instruction, it is **Testmaster**.
   2. From the **Type** dropdown list, select the **PRE-AUTH**.
   3. Into the **Action**, select the **PERMIT**.
   4. Into the URLs, add the following:
      * platform.com
      * server DNS
   5. For the full list of entries (e.g. to allow social media login), go to the [References](#references) chapter.
      ![Cisco URL Filter](images/cisco_catalyst/cisco_10.png)
3. Then, click the **Update & Apply to Device** button to save the configuration.

### Configuring the WLAN

1. Go to **Configuration > Tags & Profiles > WLANs** and click the **+Add** button.
2. Configure the **WLAN**.
3. Select the **General** tab:
   1. Into the **Profile Name** field, type any name for your profile. For this instruction, it is **Testmaster**.
   2. Into the **SSID** field, type any name for your SSID. For this instruction, it is **Testmaster**.
   3. Into the **Status**, select the **ENABLED**.
      ![Cisco WLAN General](images/cisco_catalyst/cisco_11.png)
4. Select the **Security** tab:
   1. Go to **Layer2** tab.
   2. Under Layer2, you will see the available wireless securities, select **None**.
   3. Select the **Mac Filtering** checkbox.
   4. From the **Authorization List** dropdown list, select your created list. For this instruction, it is
      **Testmaster**.
   5. Unselect the **OWE Transition Mode** checkbox.
      ![Cisco WLAN Security Layer2](images/cisco_catalyst/cisco_12.png)
   6. Go to **Layer3** tab
   7. Select the **Web Policy** checkbox.
   8. From the **Web Auth Parameter Map** dropdown list, select your created web auth. For this instruction, it is
      **Testmaster**.
   9. From the **Authentication List** dropdown list, select your created list. For this instruction, it is
      **Testmaster\_authe**.
   10. Select the **On MAC Filter Failure** checkbox.
       ![Cisco WLAN Security Layer3](images/cisco_catalyst/cisco_13.png)
5. Then, click the **Update & Apply to Device** button to save the configuration.

### Configuring the Policy

1. Go to the **Configuration > Tags & Profiles > Policy** and click the **+Add** button.
2. Configure the **Policy Profile**.
3. Select the **General** tab:
   1. Into the **Name** field, type any name for your policy. For this instruction, it is **Testmaster**.
   2. Into the **Status**, select the **ENABLED**.
   3. Into the **IP MAC Binding**, select **DISABLED**.
   4. Into the **Central Switching**, select **DISABLED**.
   5. Into the **Central DHCP**, select **DISABLED**.
      ![Cisco Policy Profile General](images/cisco_catalyst/cisco_14.png)
4. Select the **Access Policies** tab:
   1. Select the **Radius Profiling** checkbox.
   2. Select the **HTTP TLV Caching** checkbox.
   3. Select the **DHCP TLV Caching** checkbox.
   4. Into the **VLAN/VLAN Group** field, assign VLAN ID between 0-4095. For this instruction, it is **123**.
   5. From the **Pre Auth dropdown** list, select the created URL Filters. For this instruction, it is **Testmaster**.
      ![Cisco Policy Profile Access Policies](images/cisco_catalyst/cisco_15.png)
5. Select the **Advanced** tab:
   1. Select the **Allow AAA Override** checkbox.
   2. From the **Accounting List** dropdown list, select the created AAA policy. For this instruction, it is
      **Testmaster\_acc**.
      ![Cisco Policy Profile Advanced](images/cisco_catalyst/cisco_16.png)
6. Then, click the **Update & Apply to Device** button to save the configuration.

### Configuring the Certificates

**Important**: For production environments, always use a trusted SSL certificate from a well-known Certificate Authority
(CA). Self-signed certificates will cause security warnings on client devices and may prevent automatic captive portal
detection.

#### Uploading a p12 certificate

1. Go to the **Configuration > Security > PKI Management > Add Certificate > Import PKCS12 Certificate**
2. Select the protocol for uploading the certificate: TFTP, SFTP, FTP, SCP, or Desktop (HTTPS) to the controller's
   memory.
3. Specify the certificate file with the CA certificate generated for the authorizing point in the controller.
4. Enter the certificate password.
   ![Cisco PKI Management](images/cisco_catalyst/cisco_17.png)
5. Click **Import** button.

#### Modifying Web Auth Parameters

1. Go to the **Configuration > Security > Web Auth**
2. In the **General settings** tab, modify the following:
   1. Set the **Virtual IPv4 Address** used for Captive Portal redirection. For this instruction its **192.0.2.1**.
   2. In **Trustpoint** section, select the uploaded certificate.
   3. In **Virtual IPv4 Hostname** section, input the domain name from the certificate.
      * Configure the DNS used by clients to resolve the domain specified as the Virtual IPv4 Hostname to the IP
        address assigned as the Virtual IPv4 Address.
   4. Check boxes to enable **Web Auth intercept HTTPS** and **Enable HTTP server for Web Auth**.
   5. **Disable HTTP secure server for Web Auth** should be unchecked.  
      ![Cisco Web Auth Parameter](images/cisco_catalyst/cisco_18.png)
3. Then, click the **Update & Apply to Device** button to save the configuration.

## Configuring the Platform

To configure an access point on the Platform, you should first add it to the Platform. Then, you should configure the
network in which the access point will be used.

### Adding an Access Point to The Platform

To add an Access Point, you should first log in to the Platform. Then, go to the **Portal Management > Structure**
section, and select the **Devices** tab from the upper bar.

1. Now, click the **+** button in the bottom right corner to add a new device.
   ![Platform configuration](images/aruba_central/aruba_platform_config_1.png)
2. Now, in the new window:
   1. From the **Device type** list, select **Cisco with Catalyst WC**.
   2. In the **AP MAC** field, type the access point's **Radio MAC** address.
   3. Into the **IP address** field, enter the controller IP address.
   4. Into the **CoA Port** field, enter the controller CoA Port.
   5. Into the **Serial number** field, enter the access point’s serial number.
   6. In the **Descriptive name**, you can type the name that would help you differentiate this access point from the
      other ones.
      ![Platform add Cisco 1](images/cisco_catalyst/cisco_20.png)
      ![Platform add Cisco 2](images/cisco_catalyst/cisco_21.png)
3. After you have finished providing the details, click Save in the top right corner to finish adding the access point
   to the Platform.

## References

In this section, there is a list of all entries that you may need to add to the walled garden. When you finish adding
them, continue with the [Configuring the URL Filters](#configuring-the-url-filters) procedure.

### Domain

```
domain.com

```

#### IP

For Domain Europe: `35.241.143.144`  
For Domain North and South America: `35.245.165.143`  
For Domain Asia: `35.240.186.103`

### iOS (optional)

```
www.appleiphonecell.com  
captive.apple.com  
www.apple.com  
www.itools.info  
www.ibook.info  
www.airport.us  
www.thinkdifferent.us

```

### Android

```
connectivitycheck.android.com  
*.gstatic.com  
clients3.google.com

```

### Microsoft

```
msftncsi.com  
*.msftncsi.com
login.microsoftonline.com
aadcdn.msftauth.net
aadcdn.msauth.net
login.live.com  

```

### Facebook

```
facebook.com  
facebook.net  
akamaihd.net  
digicert.com  
fbcdn.net  
fb.com  
fbsbx.com  
*.facebook.com  
*.facebook.net  
*.akamaihd.net  
*.digicert.com  
*.fbcdn.net  
*.fb.com  
*.fbsbx.com  

```

#### IP

```
5.178.32.0/20  
195.27.154.0/24  
80.150.192.0/24  
77.67.96.0/22  
212.119.27.0/25  
2.16.0.0/13  
66.171.231.0/24  
31.13.24.0/21  
31.13.64.0/18  
212.245.45.0/24  
213.254.17.0/24  
46.33.70.0/24  

```

### Twitter

```
twitter.com  
twimg.com  
abs.twitter.com  
*.twitter.com  
*.twimg.com  
*.abs.twitter.com 

```

#### IP

```
199.16.156.0/22  
199.59.148.0/22  
199.96.56.0/21  
192.133.76.0/22  

```

### VKontakte

```
vk.com  
oauth.vk.com  
vk.me  
*.vk.com  
*.oauth.vk.com  
*.vk.me

```

### PayPal

```
paypal.com  
omtrdc.net  
mediaplex.com  
paypalobjects.com  
abmr.net  
dotomi.com  
*.paypal.com  
*.omtrdc.net  
*.mediaplex.com  
*.paypalobjects.com  
*.abmr.net  
*.dotomi.com  

```

### Instagram

```
instagram.com

```

### YouTube

```
youtube.com  
ytimg.com  
gstatic.com  
google.com  
googlevideo.com  
*.youtube.com  
*.ytimg.com  
*.gstatic.com  
*.google.com  
*.googlevideo.com 

```

### Google

```
accounts.google.com  
gstatic.com  
googleusercontent.com  
google.com  
googleapis.com  
accounts.youtube.com  
*.accounts.google.com  
*.googleusercontent.com  
*.google.com  
*.googleapis.com  
*.accounts.youtube.com 

```

### Line.me

```
*.line.me  
*.line-apps.com  
*.line-scdn.net  

```

### Kakao

```
*.kakao.com  
*.google.com  
*.m2.daumcdn.net  

```