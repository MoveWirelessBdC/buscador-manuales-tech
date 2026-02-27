Ruckus vSZ - Platform documentation






[Skip to content](#ruckus-vsz-configuration-guide)

# Ruckus vSZ Configuration Guide

## Prerequisites and Basic Configuration

To configure the Ruckus vSZ Access Point with the platform, you should first fulfill specific prerequisites, and prepare the Basic Configuration.

### Configuration Prerequisites

You should ensure that the Ruckus controller:
- Has correctly configured IP settings, and is connected with the DNS server,
- Can resolve the domain address which is ***domain**.com*,
- Is given access to the platform via ports: *80*, *1812* and *1813*,
- Is connected and communicating with Access Points.

You should also make certain that:
- The end device has been given access to the port **9997** of the management plane, cluster plane of vSZ, or in case of Ruckus GRE tunnel - an external IP,
- The firewall for the http and https re-directions should have ports **8090** and **8099** **opened**.

### Basic Configuration

Below, you can find the table providing the data for the **Production Environments**, which are the cloud servers of the platform.

| Name | URL | IP |
| --- | --- | --- |
| Linkyfi UVA | uva.linkyfi.com | 35.245.165.143 |

## Configuring Ruckus vSZ

Before you start the configuration of the platform, you should set up the Ruckus vSZ Access Point. To do this, configure the following parameters successively:
- RADIUS server
- Hotspot
- WLAN group
- WLAN network.

Note

During the configuration process, the end-device web browser may stop at **SIP:9997**. This may be caused by the **9997-post** barrier, or a Ruckus bug. To resolve the problem, you should add a custom **SIP** to the **Control Panel** instead of the **Management Panel**.

## Before You Start the Configuration

Before you start the configuration process, you should disable the IP, and MAC Address’ encryption:

1. First, connect to the **SmartZone CLI** via **SSH**. Then, enter the configuration mode by typing `config`in the console. Press **Enter** on your keyboard to initialise the process..
2. After initialising the `(config)#` command prompt, type `no encrypt-mac-ip` and press **Enter**. As a result, you should get the following response:

   `Do you want to continue to disable (or input 'no' to cancel)? [yes/no].`

   Type `yes` to confirm the desired action, and press **Enter** to initialise it. At that point, you should get the following response: `Successful operation.`
3. To ensure that the encryption of the IP and the MAC address has been disabled::

   * In the configuration mode where
     the `(config)#` command prompt is displayed, type the following command:
     `do show running-config encrypt-mac-ip`
   * If you are not in the configuration mode, type the following command:
     `show running-config encrypt-mac-ip`

   As a result, you should get the following response:
   `Encryption MAC and IP: Disabled.`

## Configuring the RADIUS Server

### Enabling Communication Between the Controller and the RADIUS Server

The RADIUS server must be configured to ensure the authentication of the end users’ devices, and to authorise these devices to use the WiFi network. This configuration process consists of two steps:

* Configuration of the RADIUSserver for authentication, and
* Configuration of the RADIUSserver for accounting.

#### Configuring the RADIUS Server for Authentication

1. Log in to the Ruckus vSZ user interface, and go to the **Services & Profiles \*\* Authentication** section in the menu on the left.
2. In the **Non-Proxy** (AP Authentication) **window, select the** Default Zone **option from the menu tree. Then, click the** Create\*\* button.

   ![ruckus vsz configuration](images/ruckus_vSZ/config_ruckus_vsz_1.png)
3. Now, you can provide the server details in the **Create AAA server** window:

   * In the **Name** field, type the name of the server. For this instruction, it is *Radius Name*,
   * From the **Type** checklist, select the **RADIUS** option,
   * Into the **IP Address** field, enter the **RADIUS Server Address**. For this instruction, it is *35.241.143.144*,
   * Into the **Port** field, enter *1812*,
   * In the **Shared Secret** field, type *bAZev44u*
   * In the **Confirm Secret** field, retype the **Shared Secret** from the previous field.

   After you have finished providing the server details, click **OK** to save the server settings.

![ruckus vsz configuration](images/ruckus_vSZ/config_ruckus_vsz_2.png)

#### Configuring the RADIUS Server for Accounting

This configuration enables the communication with **Domain RADIUS Server** on **port 1813** to enable the RADIUS accounting.

1. Go to the **Services & Profiles \*\* Accounting** section in the menu on the left.
2. In the**Non-Proxy** window, select the **Default Zone** option from the menu tree. Then, click the **Create** button.

   ![ruckus vsz configuration](images/ruckus_vSZ/config_ruckus_vsz_3.png)
3. Now, you can provide the server details in the \**Create New* window:

   * In the **Name** field, type the name of the server for accounting. For this instruction, it is *Radius\_Accounting\_Name*,
   * Into the **IP Address** field, enter the **Server IP Address**. For this instruction, it is *35.241.143.144*,
   * Into the **Port** field, enter *1813*,
   * Into the **Shared Secret** field, enter *bAZev44u*
   * In the **Confirm Secret** field, retype the **Shared Secret** from the previous field.

   After you have finished providing the server details, click **OK** to save the server settings.

![ruckus vsz configuration](images/ruckus_vSZ/config_ruckus_vsz_4.png)

## Configuring the Hotspot Service

The configuration of the hotspot enables establishing the proper network connection, followed by the redirection to the captive portal. You can choose which RADIUS Server should be used for the authorization process, and designate the Walled Garden.

Tip

The Walled Garden is a list of websites that can be accessed by users who have not logged in to the network. It is required for proper functioning of the captive portal.

1. Go to the **Services & Profiles > Hotspot & Portals** and select the \*\* Hotspot(WISPr)\*\* section. Then, choose the desired zone from the menu tree; for this instruction, it is *Default Zone*.
2. Now, click the **Create** button to create a **Hotspot Portal**.

   ![ruckus vsz configuration](images/ruckus_vSZ/config_ruckus_vsz_5.png)
3. Now, you can provide the server details in the **Create Hotspot Portal** window:

   * In the **Portal Name** field, type the name of the Portal. For this instruction, it is ***domain***,
   * From the **Logon URL** checklist, select the **External** option. Then, enter the desired captive portal address into the **Redirect Unauthenticated User to the URL for Authentication** field. For this instruction, it is *http://**domain**.com/login*,
   * From the **Redirected MAC Format** dropdown list, select the desired MAC Format. For this instruction, it is *AABBCCDDEEFF*,
   * From the **Start Page** checklist, select the **Redirect to the URL That Users Intend to Visit** option, and type the desired website address in the below field. For this instruction, it is *http://**domain**.com/welcome*.

   ![ruckus vsz configuration](images/ruckus_vSZ/config_ruckus_vsz_6.png)
4. After you have provided the Hotspot Page details, expand the **Walled Garden** section, and provide its details. To do this, type ***domain**.com* into the **Walled Garden Entry** field. Then, click **Add** to save the entry.

   Repeat this step to add other required website addresses from the **References** section.
5. To finish the configuration process, click the **OK** button.

   ![ruckus vsz configuration](images/ruckus_vSZ/config_ruckus_vsz_7.png)

## Configuring the Wireless LAN Group

The Wireless LAN Group (WLAN Group) configuration requires assigning the existing SSIDs to WLAN Groups which are logical containers for numerous different SSIDs. Those groups can be later used to broadcast multiple SSIDs by using the same Access Point.

1. From the **Wireless LANs** list, select **Default Zone**. Then, click **+** which is located above the WLAN list to add a WLAN Group.

   ![ruckus vsz configuration](images/ruckus_vSZ/config_ruckus_vsz_8.png)
2. In the **Create WLAN Group** window, type the name of the WLAN Group In the **Name** field. For this instruction, it is **Domain**, and click **Next**.

   Then, click the **OK** button to finish creating the WLAN Group.

   ![ruckus vsz configuration](images/ruckus_vSZ/config_ruckus_vsz_9.png)

## Configuring the Wireless LAN Network

The configuration of Wireless LAN requires creating a *SSID Network*\*, which is distributed by Access Points, by assigning the hotspots to the designated SSID and, by that, enabling the correct redirection and communication with RADIUS.

1. From the menu on the left, select the **Wireless LANs** option.
2. From the **Wireless LANs** list, select **Default Zone**. Then, click the **Create** button to add a new network.

   ![ruckus vsz configuration](images/ruckus_vSZ/config_ruckus_vsz_10.png)
3. Now, you can provide the server details in the **Create WLAN Configuration** window:

   * In the **Name** field, type the name of the network. For this instruction, it is *SSID\_NAME*,
   * Into the **SSID** field, enter the broadcasted SSID. For this instruction, it is *SSID\_NAME*.
     Note: This value is also required in the platform configuration process.
   * From the **WLAN Group** dropdown list, select the WLAN group which you have created. For this instruction, it is ***Domain***,
   * In the **WLAN Usage** section, for the **Authentication Type** select *Hotspot (WISPr)*,
   * In the **Authentication Options** section, for the **Method**, select **Open**,
   * In the **Encryption Options** section, for the **Method**, select **None**,
   * In the **Hotspot Portal** section:
     + From the **Hotspot (WISPr) Portal** dropdown list, select the name of the Hotspot Service which you have created. For this instruction, it is ***Domain***,
     + In the **Authentication Server** option, uncheck the **Use the Controller as Proxy** checkbox, and select the name of the Authentication Service, which you have created, from the dropdown list. For this instruction, it is *Radius\_Name*,
     + In the **Accounting Server** option, uncheck the **Use the Controller as Proxy** checkbox, and select the name of the Accounting Service, which you have created, from the dropdown list. For this instruction, it is *Radius Accounting*.
4. When you have finished providing the details, click **OK** to save the settings.

   ![ruckus vsz configuration](images/ruckus_vSZ/config_ruckus_vsz_11.png)

## Configuring the Platform

The platform configuration consists of two steps: adding the access point to the network, and configuring it. You should carry them out successively.

### Adding an Access Point to the Network

Note

Access Points are called **Devices** on the platform.

1. Firstly, log in to the platform. Then, go to the **Portal Management → Structure** section and select **Devices** from the navigation bar.

   Note

   Make sure that you are in the appropriate organisation. To do this, select the desired one from the right panel or the top bar; it should be highlighted in blue.
2. Now, click **+** in the bottom right corner to add a device.

   ![ruckus vsz configuration](images/ruckus_vSZ/ruckus_vsz_1.png)
3. In the **Add Devices** window, enter the device details:

   * From the **Device Type** dropdown list, select the type of the device,
   * Into the **AP MAC** field, enter the device MAC;
   * In the **IP Address** field ,enter the device’s IP address (recommended),
   * In the **Serial Number** field, enter the device’s serial number,
   * Into the **Descriptive Name** field, type a descriptive name of the device,

   Then, click **Save** in the top right corner to confirm the details and proceed further.

   ![ruckus vsz configuration](images/ruckus_vSZ/ruckus_vsz_2.png)
4. The device is now added to your organisation.

### Configuring the Network

To learn how to configure the Network, read the [Creating Access Settings](../user_guide/user_enrollment/create_access_settings.html).

## References

Below, you can find the list of entities which can be added to the Walled Garden during the configuration process. After you have finished adding them, continue configuring the Access Control.

When using the Ruckus GRE tunnel, we recommend adding the **Domain address**, its **IP**, and the social media records which you would like to use to the walled garden rules.

Note

The below entities are **optional** for the configuration. Using them may impact the **Popup** option which may not work as expected. You should also note that all of these entities use the *https* which requires the configuration of an appropriate cert for the proper redirection to the designated web address.

### Domain

```
*.domain.com

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

### Microsoft (required for loging in with Microsoft)

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