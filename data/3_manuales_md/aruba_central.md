Aruba Central - Platform documentation






[Skip to content](#aruba-central-configuration-guide)

# Aruba Central Configuration Guide

## Prerequisites and Basic Configuration

To configure the Aruba Central Access Point with the platform, you should first fulfill specific prerequisites, and prepare the Basic Configuration.

### Configuration Prerequisites

You should ensure that:

* You have configured the IP settings with the correct DNS server, and are logged in to the Aruba Central configuration platform;
* Your Aruba Central devices resolve the platform domain address and have access to the Platform through ports: *80*, *1812* and *1813*.

After you have finished these steps, prepare the basic configuration of the device (SSID, association with APs, etc.).

### Basic Configuration

Below, you can find the table providing the data for the **Production Environments**, which are the cloud servers of the platform.

| Name | URL | IP |
| --- | --- | --- |
| Linkyfi UVA | uva.linkyfi.com | 35.245.165.143 |

## Configuring Aruba Central

The configuration of the Aruba Central requires setting up successively: the network, and **This Platform**.

### Configuring the Network

To properly configure your network, you should first log in to the Aruba Central platform. Then, you should follow three steps:

* Firstly, set up the general settings
* Secondly, configure security
* Finally, set up the network access.

#### Configuring the General Settings

To set up general settings:

1. Select the **Global** option and from the **Groups** list, choose the desired group. For this instruction, it is *Home-lab*.

   ![aruba central configuration](images/aruba_central/aruba_central_0a.png)
2. Once you have selected the group, click on the **Config** icon.

   ![aruba central configuration](images/aruba_central/aruba_central_0b.png)

   Then, select **WLAN** and click the **+ Add SSID** option.
3. Now, in the new window, enter the name of the network into the **Name (SSID)** field. For this instruction it is *Platform SSID*.

   Note

   You will need these details further in the configuration process.

   Click **Next** in the bottom right corner to proceed further.

   ![aruba central configuration](images/aruba_central/aruba_central_1.png)
4. In the following **WLANs** section, click **Next** in the bottom right corner.

   ![aruba central configuration](images/aruba_central/aruba_central_2.png)
5. Now, in the **Security** section, move the **Security Level** slider to the **Captive Portal**. Next, to configure the **Captive Portal Profile**, click the **+** button next to the **Captive Portal Profile** dropdown list.

   ![aruba central configuration](images/aruba_central/aruba_central_3.png)
6. In the new window, provide the Captive Portal details:

   * In the **Name** field, type the name of the Portal. For this instruction, it is *Platform*.
   * From the **Authentication Type** dropdown list, select \*\*RADIUS authentication.
   * Into the **IP or Hostname** field, enter the IP address or host name of the Portal. For this instruction, it is *platform.com*.
   * Into the **URL** field, enter the URL address. For this instruction, it is */login*.
   * Into the **Port** field, enter the Port. For this instruction, it is *80*.
   * Into the **Redirect URL** field, enter the URL address for redirection. For this instruction, it is *<http://platform.com/welcome>*.

   To confirm the details, click **OK** in the bottom right corner of the window.

   ![aruba central configuration](images/aruba_central/aruba_central_4.png)

   ![aruba central configuration](images/aruba_central/aruba_central_5.png)
7. Now, to configure the server, you should click the **+** button next to the **Primary Server** dropdown list.

   ![aruba central configuration](images/aruba_central/aruba_central_6.png)
8. In the new window, provide your server details:

   * For the **Server Type**, select **RADIUS** from the dropdown list. - In the **Name** field, type the name of the server. For this instruction, it is *Platform*.
   * Into the \**IP Address* field, enter the IP address of the server.
   * In to the \**Shared Key* field, enter the Shared Secret of the server.
   * Specify the **Dwell Time**, **Timeout**, and **Retry Count**.
   * Into the **Auth Port** field, ener the Port number. For this instruction, it is *1813*.

   To confirm the details, click **OK** in the bottom right corner.

   ![aruba central configuration](images/aruba_central/aruba_central_7.png)

   ![aruba central configuration](images/aruba_central/aruba_central_8.png)
9. To set up the Accounting options, expand the **Advanced Settings** option in the **Security** section, and select **Accounting**. Then, provide the details:

   * For **Accounting**m, select the **Use Authentication Servers** option from the dropdown list.
   * In the **Accounting Interval** field, type the desired number of minutes. For this instruction, it is *10*.

   ![aruba central configuration](images/aruba_central/aruba_central_9.png)
10. To determine the Walled Garden, select the **Walled Garden** option in the **Advanced Settings** section. By clicking the **Add** option at the bottom of the table, you can add the necessary details which you can find in the **References** subchapter of this instruction.

    ![aruba central configuration](images/aruba_central/aruba_central_10.png)

#### Configuring the Network Access

To configure the network access, you either::
**Set the unrestricted network access**, in case you do not need to use additional walled garden entries, such as social media, or
**Set the role-based network access**, in case you need to use additional walled garden entries, such as social media.

**Setting up the Unrestricted Network Access**

To set up the unrestricted network access, go to the **Access** tab and set the **Access Rules** slider to **Unrestricted**. Then, click the **Next** button to proceed further.

![aruba central configuration](images/aruba_central/aruba_central_11.png)

**Setting up the Role-Based Network Access**

To set up the Role-Based Network Access

1. Go to the **Access** tab and set the **Access Rules** slider to **Role Based**.

   ![aruba central configuration](images/aruba_central/aruba_central_12.png)
2. If you have already created a before-authentication role, then skip the following steps directly to step **6**

   If you have not created any before-authentication role yet, click the blue **+** button in the **Roles** table.
3. In the **Roles** table, select the role, and click the blue **+** button in the **Access Rules For Selected Roles** table.
4. Now, in the **Access Rule** window:

   * From the **Rule Type** dropdown list, select **Access Control**,
   * For **Service**, select **Network**, and from the list of protocols select **Any**,
   * From the **Action** list, select **Allow**,
   * From the **Destination** list, select **To a Domain Name**,
   * Into the **Domain Name** field, enter the domain address. For this instruction it is *platform.com*.
     **Note:** Repeat points **d** and **e** for all entries from the Reference\*\* section, which you find relevant/

   Then, click **Save** to confirm the setup.

   ![aruba central configuration](images/aruba_central/aruba_central_13.png)

   ![aruba central configuration](images/aruba_central/aruba_central_14.png)
5. Now, Modify the default role:

   Note

   The default role has the same name as the network and is used after logging in to the network through a captive portal.

   a) In the **Role** table, click the role named as your network. For this instruction, it is *PlatformSSID*.  
   b) In the **Access Rules For Selected Roles** table, click the **Add Role** icon.
   c) In the **Access Rule** window:
   - From the **Rule Type** dropdown list, select **Access Control**,
   - For **Service**, select **Network**, and choose **Any** from the list of protocols,
   - From the **Action** dropdown list, select **Allow**,
   - From the **Destination** dropdown list, select **To All Destinations**.

   Then, click **Save** to confirm the settings.

   ![aruba central configuration](images/aruba_central/aruba_central_15.png)
6. Finally, below the **Role Assignment Rules** section, select the **ASSIGN PRE-AUTHENTICATION ROLE** checkbox, and select the name of the before-authentication role from the dropdown list.. For this instruction it is *PlatformSSID*.

   Then, click the **Finish** button to finish configuring the roles.

   ![aruba central configuration](images/aruba_central/aruba_central_16.png)

### Checking the Aruba Central Access Point Configuration

Before you begin configuring the devices on the Platform, you should set up the device name in its interface. To do this, go to the **Configuration > Access Points** section:

1. In the **Name** field, check the name of the access point. **It is recommended to use the device’s MAC address as the access point's name.**

   Note

   You will need this name when configuring the access point on the Platform.
2. (Optional) To set the MAC address as the device’s name:

   a) Click the **+** button on the right side of the device which name you would like to change.

   ![aruba central configuration](images/aruba_central/aruba_central_17.png)

   b) In the **Name field**, type the device’s MAC address.

   ![aruba central configuration](images/aruba_central/aruba_central_18.png)

   After you have finished providing the MAC address, click **Save** to confirm your changes.

## Configuring the Platform

To configure an access point on the Platform, you should first add it to the Platform. Then, you should configure the network in which the access point will be used.

### Adding an Access Point to The Platform

To add an Access Point, you should first log in to the Platform. Then, go to the **Portal Management > Structure** section, and select the **Devices** tab from the upper bar.

1. Now, click the **+** button in the bottom right corner to add a new device.

   ![aruba central configuration](images/aruba_central/aruba_platform_config_1.png)
2. From the **Device Type** list, select **Aruba Stand-Alone 6.5 and Newer**. Then, provide the access point details:

   * In the **NAS-ID** field, type the access point's NAS-ID,
   * Into the **IP Address** field, enter the access point’s IP address (recommended),
   * Into the **Serial Number** field, enter the access point’s serial number,
   * In the **Descriptive Name**, you can type the name that would help you differentiate this access point from the other ones,
   * Into the **MAC** field, enter the access point’s MAC address.

   ![aruba central configuration](images/aruba_central/aruba_platform_config_2.png)

   ![aruba central configuration](images/aruba_central/aruba_platform_config_3.png)

   After you have finished providing the details, click **Save** in the top right corner to finish adding the access point to the Platform.

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