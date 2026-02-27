Ruckus ZD - Platform documentation






[Skip to content](#ruckus-zonedirector-configuration-guide)

# Ruckus ZoneDirector Configuration Guide

## Prerequisites and Basic Configuration

To configure the Ruckus ZoneDirector Access Point with the platform, you should first fulfill specific prerequisites, and prepare the Basic Configuration.

### Configuration Prerequisites

You should ensure that the Ruckus ZoneDirector controller:
- Has correctly configured IP settings and is connected with the DNS server,
- Can resolve the domain address which is *linkyfi.com*,
- Is given access to the platform via ports *80*, *1812* and *1813*,
- Is connected and communicating with Access Points,

You should also make certain that:
- The Ruckus ZoneDirector firmware version is **9.13.1** (9.10 for https redirection).
- You are logged in to the Ruckus ZoneDirector web interface.

### Basic Configuration

Below, you can find the table providing the data for the **Production Environments**, which are the cloud servers of the platform.

| Name | URL | IP |
| --- | --- | --- |
| Linkyfi UVA | uva.linkyfi.com | 35.245.165.143 |

## Configuring Ruckus ZoneDirector

Before you start the configuration of the platform, you should set up the Ruckus ZD Access Point. To do this, configure the following parameters successively:
- RADIUS server
- Hotspot
- WLAN
- WLAN groups
- Access point
- Access point groups.

## Configuring the RADIUS Server

### Enabling Communication Between the Controller and the RADIUS Server

The RADIUS server must be configured to ensure the authentication of the end users’ devices, and to authorise these devices to use the WiFi network. This configuration process consists of two steps:

* Configuration of the Radius server for authentication, and
* Configuration of the Radius server for accounting.

#### Configuring the RADIUS Server for Authentication

1. Log in to the Ruckus ZoneDirector user interface, and go to the **Services&Profiles > AAA Servers** section in the menu on the left.
2. Now, click the **Create New** button in the **Authentication/Accounting Servers** pane to add a new RADIUS server.
3. Now, you can provide the server details in the \**Create New* window:

   * Into the **Name** field, type the name of the server. For this instruction, it is *Your\_Radius\_Name*,
   * From the **Type** checklist, select the **RADIUS** option,
   * Into the **IP Address** field, enter the **RADIUS Server Address**. For this instruction, it is *35.241.143.144*,
   * Into the **Port** field, enter *1812*,
   * In the **Shared Secret** and **Confirm Secret** field, type *bAZev44u*

   After you have finished providing the server details, click **OK** to save the server settings.

   ![configuration ruckus zd](images/ruckus_zd/config_ruckus_zd_1.png)

#### Configuring the RADIUS Server for Accounting

This configuration enables the communication with **Linkyfi RADIUS Server** on **port 1813** to enable the RADIUS accounting.

1. Go to the **Services&Profiles> AAA Servers** section in the menu on the left. Then, click the **Create New** button in the **Authentication/Accounting Servers** pane to add a new RADIUS server.
2. Now, you can provide the server details in the \**Create New* window:

   * In the **Name** field, type the name of the server. For this instruction, it is *Your\_Accounting\_Radius*,
   * From the **Type** checklist, select the **RADIUS Accounting** option,
   * Into the **IP Address** field, enter the **IP Address** for the RADIUS for Accounting server. For this instruction, it is *35.241.143.144*,
   * Into the **Port** field, enter *1813*,
   * In the **Shared Secret** and the **Confirm Secret** fields, type *bAZev44u*

   After you have finished providing the server details, click **OK** to save the server settings.

   ![configuration ruckus zd](images/ruckus_zd/config_ruckus_zd_2.png)

### Configuring the Hotspot

The configuration of the hotspot enables establishing the proper network connection, followed by the redirection to the captive portal. You can choose which RADIUS Server should be used for the authorization process, and designate the Walled Garden.

Tip

The Walled Garden is a list of websites that can be accessed by users who have not logged in to the network. It is required for proper functioning of the captive portal.

1. Go to the *Service&Profiles > Hotspot Services* *section, and click the* *Create New*\* button to create a new hotspot.
2. Now, you can provide the server details in the \**Create New* window.

   * Select the **General** tab at the top of the window and provide appropriate details:
   * In the **Name** field, type the name for the service. For this instruction, it is *Hotspot\_Name*,
   * Into the **Login Page** field, enter the captive portal address. For this instruction, it is *<http://yourdomainname.com/login>*,
   * From the **Start Page** checklist, select the **Redirect to the URL That the User Intends to Visit** option,
   * In the **Session Timeout** option, select the **Terminate User Session** checkbox. Then, determine the number of minutes after which the session is terminated in the empty field. For this instruction, it is *1440* minutes,
   * In the **Intrusion Prevention** section, check the **Temporarily Block Hotspot Clients With Repeated Authentication Attempts**.

   ![configuration ruckus zd](images/ruckus_zd/config_ruckus_zd_3.png)

   Now, continue to the **Authentication** tab:  
   - From the **Authentication Server** dropdown list, select the name of the RADIUS for Authentication server which you have created. For this instruction, it is *Your\_Radius\_Name*,  
   - From the **Accounting Server** dropdown list, select the name of the RADIUS for Accounting server which you have created. Then,determine the number of minutes after which the interim-update is sent. For this instruction, it is respectively *Your\_Accounting\_Radius* and *5* minutes.   
   - In the **Wireless Client Isolation** section, select the **Isolate Wireless Client Traffic From Their Clients On the Same AP** checkbox.  
   - In the “Location Information” type the ID of device location in the **Location ID** field. For this instruction, it is *Ruckus\_AP*

   Note

   You can also choose the **Isolate Wireless Client Traffic From All Hosts On the Same VLAN/subnet** option, but you should note that it requires creating an independent whitelist for the captive portal for the gateway to communicate, and to gain internet access.

   ![configuration ruckus zd](images/ruckus_zd/config_ruckus_zd_4.png)

   Next, select the **Walled Garden** tab, and provide its details. To do this, type your domain address into the *Destination Address* *field. Then, click* *Save*\* to save the entry.

   For a list of other entries which you may find useful, go to the **References** sub-chapter.

   ![configuration ruckus zd](images/ruckus_zd/config_ruckus_zd_5.png)
3. To finish the Hotspot configuration and save the changes, click **OK** in the lower right corner of the window.

### Configuring the Wireless LAN

The configuration of Wireless LAN (WLAN) requires creating a *SSID Network*\*, which is distributed by Access Points, by assigning the hotspots to the designated SSID and, by that, enabling the correct redirection and communication with RADIUS.

1. In the menu on the left, go to the **Wireless LANs** section. Then, click the **Create** button in the **WLAN List** panel to create a new WLAN.

   ![configuration ruckus zd](images/ruckus_zd/config_ruckus_zd_6.png)
2. Now, you can provide the WLAN details in the \**Create WLAN* window:

   * In the **Name** and the **ESSID** fields, type the name of the network. For this instruction, it is *Your\_SSID\_Name*,

   Note

   This value is also required in the platform configuration process,

   * From the **Type** checklist in the **WLAN Usages** section, select the **Hotspot Service (WISPr)** option,
   * In the **Authentication** section, it is recommended to select the **Open** option for the **Method** of authentication,
   * In the **Encryption Options** section, it is recommended to select the **None** option for the **Method** of encryption,
   * From the **Hotspot Services** dropdown list, select the name of the Hotspot which you have created. For this instruction, it is *Hotspot\_Name*.

   To finish the WLAN configuration and save the changes, click **OK** in the lower right corner of the window.

   ![configuration ruckus zd](images/ruckus_zd/config_ruckus_zd_7.png)

### Configuring Wireless LAN groups

The Wireless LAN Group (WLAN Group) configuration requires assigning the existing SSIDs to WLAN Groups which are logical containers for numerous different SSIDs. Those groups can be later used to broadcast multiple SSIDs by using the same Access Point.

1. In the menu on the left, go to the **Wireless LANs** section. Then, click the **+** button at the top of the **WLAN Groups** list to create a new WLAN Group.
2. Now, you can provide the WLAN Group details in the **Create WLAN Group** window:

   * In the **General Section > Name** field, type the name of a new network group. For this instruction, it is *Your\_New\_Group*,
   * From the **Group Settings** checklist, select the desired networks, the one with the hotspot connection included. For this instruction, it is *Your\_SSID\_Name*.

   To finish the WLAN Group configuration and save the changes, click **OK**.

   ![configuration ruckus zd](images/ruckus_zd/config_ruckus_zd_8.png)

### Configuring an Access Point

This step enables the proper configuration of Access Points with the platform and must be carried out for each device. After you have provided the appropriate details, the platform should recognise the devices as related to your organisation.

1. In the menu on the left, go to the **Access Points** section. Then, click **Configure** next to the desired Access Point to configure it.
2. Now, provide the device details in the **Edit AP** window:

   * In the **Device Name** field, type in the name of the device,
   * Into the **Location** field, enter the MAC address of the device. For this instruction, it is *1c:3a:60:27:6f:10*,
   * From the **Group** dropdown list, select **System Default**.
3. To assign a WLAN Group to this device, select the **Override System Default** option from the WLAN Group checklist. Then, select the name of the WLAN Group which you have created from the dropdown list. For this instruction, it is *Your\_New\_Group*.
4. To finish the configuration process and save the Access Points settings, click **OK** in the lower right corner of the window.

   ![configuration ruckus zd](images/ruckus_zd/config_ruckus_zd_9.png)

### Configuring an Access Point Group

The Access Points Groups allow you to determine the Access Points which should distribute the designated SSID. It also requires specifying frequencies which are used by these devices. The configuration process requires assigning an Access Point Group with a WLAN Group.

1. In the menu on the left, go to the **Configure > Access Points** Then, click the **+** button at the top of the **Access Point Group** panel.
2. Now you can provide the Access Point Group details in the **Create New** window:

   * In the **Name** field, type a name for the new Access Point Group. For this instruction, it is *AP\_Group*.
   * To assign a WLAN Group to the Access Point Group, in the **Radio Settings** section, for both the **Radio B/G/N (2.4 GHz)** and the **Radio A/N/AC (5.0 GHz)** sections, select the **Override System Default** checkboxes. Then, select the name of the WLAN Group which you have created from the dropdown list. For this instruction, it is *Your\_New\_Group*.

   ![configuration ruckus zd](images/ruckus_zd/config_ruckus_zd_10.png)
3. To assign Access Points to the newly created Access Point Group:

   * In the **Group Settings** section, click the **Add More Access Points from System Default Group to This Group** button,
   * Then, select the desired Access Points which you would like to add to the Group from the checkbox list,
   * Finally, click the **Add to This Group** button to assign the selected Access Points to the Group.

   To finish adding the APs to the group, click **OK** in the lower right corner of the window.

   ![configuration ruckus zd](images/ruckus_zd/config_ruckus_zd_11.png)

## Configuring the Platform

The platform configuration consists of two successive steps: adding an access point to the network, and configuring it.

### Adding an Access Point to the Network

Note: Access Points are called **Devices** in the platform.

1. Firstly, log in to the platform. Then, go to the **Portal Management → Structure** section and select **Devices** from the navigation bar.

   Note

   Make sure that you are in the appropriate organisation. To do this, select the desired one from the right panel or the top bar; it should be highlighted in blue.
2. Now, click **+** in the bottom right corner to add a device.
3. Now, in the **Add Device** window:

   * From the **DeviceType**, select **Ruckus Controller**,
   * Into the **Hotspot Location ID** field, enter the Location ID from the Hotspot Configuration. For this instruction, it is *Ruckus\_AP*
   * In case each device has a different Location configured, into the **AP Location**, enter the Location from the **Access Point Configuration**. .For this instruction, it is `1c:3a:60:27:6f:10`.
   * Fill other fields with the Device specification details (optional).
     After you have finished providing the device details, click **Save** in the top right corner to finish adding the device.

   ![configuration ruckus zd](images/ruckus_zd/ruckus_zd_1.png)

### Configuring the Network

To learn how to configure the Network, read the [Creating Access Settings](../user_guide/user_enrollment/create_access_settings.html).

## References

Below, you can find the list of entities which can be added to the Walled Garden during the configuration process. After you have finished adding them, continue configuring the Access Control.

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