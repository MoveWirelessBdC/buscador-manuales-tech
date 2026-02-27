Aruba Instant - Platform documentation






[Skip to content](#aruba-instant-configuration-guide)

# Aruba Instant Configuration Guide

## Prerequisites and Basic Configuration

To configure the Aruba controller Access Point with the platform, you should first fulfill specific prerequisites, and prepare the Basic Configuration.

### Configuration Prerequisites

You should ensure that:

* You have correctly configured the Aruba Controller IP pools (including a valid DNS server address)
* Your Aruba Central devices resolve the platform domain address and have access to the Platform through ports: *80*, *1812* and *1813*.

### Basic Configuration

Below, you can find the table providing the data for the **Production Environments**, which are the cloud servers of the platform.

| Name | URL | IP |
| --- | --- | --- |
| Linkyfi UVA | uva.linkyfi.com | 35.245.165.143 |

## Configuring Aruba Instant

The configuration of the Aruba Central requires setting up successively: the network, and **the Platform**.

## Configuring Aruba Controller

Before you start configuring the Aruba Instant, you should first log in to the Aruba user interface, and upgrade the software.

The configuration of Aruba Instant consists of three steps. Firstly, you should add a new network to the system. Secondly, you should create the necessary user roles. Finally, you must configure your access points in the Platform.

### Logging In To the Aruba User Interface

Go to the *https://* website, and provide your login credentials:
- Into the **Username** field, type your username. For this instruction it is *admin*.
- Into the **Password** field, type your password.

Then, click the **Log In** button to log in to the user interface.

Note

When you log in to the interface for the first time, you should select the country code of your country from the additional dropdown list. For this instruction it is *PL - Poland* Click the **OK** button to confirm your selection.

![aruba instant configuration](images/aruba_instant/aruba_instant_1.png)

![aruba instant configuration](images/aruba_instant/aruba_instant_2.png)

### Upgrading the Software

#### Automatic Upgrade

1. In the Aruba user interface, select the **Maintenance** option in the upper right corner.

   ![aruba instant configuration](images/aruba_instant/aruba_instant_3.png)
2. In the new window, select the **Firmware** tab, and click the **Check for New Version** button in the **Automatic** section.

   ![aruba instant configuration](images/aruba_instant/aruba_instant_4.png)
3. When the software must be updated, you can see the appropriate notification. Then, click the **Upgrade Now** button.

   When the upgrade process is finished, click **OK** to finish.

   Note

   The software upgrade will reboot all of the access points.

#### Manual Upgrade

1. Go to the Aruba website, and log in to your account. Then, download the image of the new software, and save it on your computer.
2. Now, select the **Maintenance** tab in the upper right corner.

   ![aruba instant configuration](images/aruba_instant/aruba_instant_3.png)
3. In the new window, select the **Firmware** tab, and click the *Browse* *button next to the* *Image File for New Version* *field in the* *Manual*\* section.

   ![aruba instant configuration](images/aruba_instant/aruba_instant_5.png)
4. If you do **not** wish to reboot your access points, unselect the **Reboot All APs After Upgrade** checkbox. Then, click the **Upgrade Now** button to start upgrading your devices.

### Adding a Network

1. In the **Network** column, click the **New** button. You will get redirected to the new window, where you can configure your network step by step.
2. In the first **WLAN Settings** step, provide your network details:

   * Into the **Name (SSID)** field, enter the unique name of your network. For this instruction it is *Platform*
   * For the **Primary Usage**, select the **Guest** option from the selectors list.

   Click **Next** in the lower right corner of the window to proceed to the next step.

   ![aruba instant configuration](images/aruba_instant/aruba_instant_6.png)
3. In the second **VLAN** step:

   * For the **Client IP Assignment**, select the appropriate method of assigning clients’ IPs from the selectors list. For this instruction it is *Virtual Controller Managed*.
   * For the **Client VLAN Assignment**, select the appropriate method of assigning clients’ VLANs. For this instruction, it is *Default*.

   Click **Next** in the lower right corner of the window to proceed further.

   ![aruba instant configuration](images/aruba_instant/aruba_instant_7.png)
4. In the third **Security** step, you can set up your network’s security:

   * From the **Splash Page Type** dropdown list, select *External*.
   * From the **Captive Portal Profile** dropdown list, select *New*. Then, in the popup box, provide the details of the portal:
   * In the **Name** field, type the name of your captive portal. For this instruction it is *Platform*.
   * From the **Type** dropdown list, select *Radius Authentication*.
   * Into the **IP or Hostname** field, enter the address of the Platform server. For this instruction it is *platform.com*.
   * Into the **URL** field, enter the captive portal address starting from */*. For this instruction it is */login*.
   * From the **Use Https**\* dropdown list, select either:
     + the **Enabled** option; then, into the **Port** field, type *443*.
     + the **Disabled** option; then, into the **Port** field, type *80*. For this instruction, it is **Disabled** and the **Port** is *80*.
   * Into the **Redirect URL** field, enter the welcome page website address. For this instruction it is *<http://platform.com/welcome>*.

   When you have finished providing the details, click **OK** in the lower right corner of the popup box to confirm them.

   ![aruba instant configuration](images/aruba_instant/aruba_instant_8.png)

   * From the **Auth Server 1** dropdown list, select *New*. Then, in the popup box:
     + From the selector options, choose *RADIUS*.
     + Into the **Name** field, enter the name of the server. For this instruction it is *platform*.
     + Into the **IP Address** field, enter the IP address of the RADIUS server. For this instruction it is \_ 35.241.143.144\_. You should note, however, that the IP Address depends on the platform in which you configure the device.
     + Into the **Auth Port Field**, type *1812*.
     + Into the **Accounting Port** field, enter *1813*.
     + Into the **Shared Key** and the **Retype Key** fields, enter your shared secret. For this instruction it is *bAZev44u*
     + In the **Timeout** field, specify the number of seconds. For this instruction it is *5*.
     + In the **Retry Count** field, specify the number of retry attempts. For this instruction it is *3*.

   To confirm the details, click **OK** in the lower right corner of the popup box.

   ![aruba instant configuration](images/aruba_instant/aruba_instant_9.png)

   * Into the **Reauth Interval** field, type the desired number of minutes. Otherwise, the AP configuration may not work correctly. For this instruction it is *3* minutes.
   * From the **Accounting** dropdown list, select the *Use Authentication Servers* option.
   * From the **Accounting Mode** list, select *Authentication*.

   Then, click the **Next** button to proceed to the next step.

   ![aruba instant configuration](images/aruba_instant/aruba_instant_10.png)
5. Finally, in the **Access** step, you can configure your network’s access. To do this, move the slider on the left to the **Role-Based** position.

   Note

   The default role is created automatically, and it has the same name as your network. It is assigned to network users after they have successfully logged in to the network. For this instruction, the name of the role is *Platform*.

   ![aruba instant configuration](images/aruba_instant/aruba_instant_11.png)

   In this step, you can edit role settings according to your preferences. To do this:
   - In the **Roles** table, select the desired role.
   - Then, in the **Access Rules For** table, select the name of the role again, and click the **Edit** button below the table.

   Now, you can amend the role’s settings. To confirm them, click **OK**.

   ![aruba instant configuration](images/aruba_instant/aruba_instant_12.png)
6. To confirm creating the role, click **Finish**.

## Configuring the Platform

To configure an access point on the Platform, you should first add it to the Platform. Then, you should configure the network in which the access point will be used.

### Adding an Access Point to The Platform

To add an Access Point, you should first log in to the Platform. Then, go to the **Portal Management > Structure** section, and select the **Devices** tab from the upper bar.

1. Now, click the **+** button in the bottom right corner to add a new device.

   ![aruba instant configuration](images/aruba_central/aruba_platform_config_1.png)
2. Now, in the new window:

   * From the **Device Type** list, select **Aruba Stand-Alone 6.5 and Newer**.
   * In the **NAS-ID** field, type the access point's NAS-ID;
   * Into the **IP Address** field, enter the access point’s IP address (recommended);
   * Into the **Serial Number** field, enter the access point’s serial number;
   * In the **Descriptive Name**, you can type the name that would help you differentiate this access point from the other ones;
   * Into the **MAC** field, enter the access point’s MAC address.

   ![aruba instant configuration](images/aruba_instant/aruba_instant_platform_2.png)

   ![aruba instant configuration](images/aruba_instant/aruba_instant_platform_3.png)

   After you have finished providing the details, click **Save** in the top right corner to finish adding the access point to the Platform.

## References

Below, you can find the list of entities which can be added to the Walled Garden during the configuration process. After you have finished adding them, continue configuring the Access Control.

Note

The below entities are **optional** for the configuration. Using them may impact the **Popup** option which may not work as expected. You should also note that all of these entities use the *https* which requires the configuration of an appropriate cert for the proper redirection to the designated web address.

### Domain

`* .domain.com`

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

## PayPal

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

`instagram.com`

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