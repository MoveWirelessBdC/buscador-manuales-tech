Meraki - Platform documentation






[Skip to content](#meraki-configuration-guide)

# Meraki Configuration Guide

## Prerequisites and Basic Configuration

To configure the Meraki Access Point with the platform, you should first fulfill specific prerequisites, and prepare the Basic Configuration.

### Configuration Prerequisites

You should ensure that:

* You have created and configured the account in the Meraki Management Platform. In this account, you should **enable** the following options:

  + The **Domain-Based Walled Garden**,
  + The **RADIUS Accounting For Splash** page,
* The Meraki Access Point is connected to the Meraki Management Platform which you can access via this link: <https://account.meraki.com/secure/login/dashboard_login>, and are online.

After you have finished these steps, prepare the basic configuration of the device (SSID, association with APs, etc.).

### Basic Configuration

Below, you can find the table providing the data for the **Production Environments**, which are the cloud servers of the platform.

| Name | URL | IP |
| --- | --- | --- |
| Linkyfi UVA | uva.linkyfi.com | 35.245.165.143 |

## Configuring the Meraki Management System

The configuration of the Meraki Management System requires setting up successively: the **Access Control**, the **Splash Page**, and **This Platform**.

### Configuring the Access Control

To configure the Access Control:

1. To go to the **Access Control**, hover your mouse over the **Wireless** section in the menu. Then, in the dropdown menu, select the **Access Control** option which is located under the *Configure*\* category.

   ![meraki configuration](images/meraki/config_meraki_1.png)
2. Now, from the **SSID** dropdown list, you can select the SSID on which this platform’s access should be configured. For this instruction, it is *SSID\_NAME*.
3. In the **Network Access** section, select the **Pre-Shared Key With** option, and choose **WPA2** from the dropdown list. Then, define the key which users should enter to associate.

   ![meraki configuration](images/meraki/config_meraki_2.png)
4. To set up the **Splash Page**, select the **Sign-On With** option from the checklist and choose *My RADIUS Server* from the dropdown list.

   ![meraki configuration](images/meraki/config_meraki_3.png)
5. Now, to configure the **RADIUS** for the **Splash Page**, click the **Add a Server** link. Then, enter the **Server** details:

   a) Into the **Host Field**, enter the **RADIUS Server IP Address**. For this instruction, it is *35.241.143.144*.  
   b) In the **Port Field**, type *1812*.  
   c) Into the **Secret Field**, enter your **Shared Secret**. For this instruction, it is *bAZev44u*

   ![meraki configuration](images/meraki/config_meraki_4.png)

   Note

   If you need to configure the **RADIUS Backup Servers**, repeat step 4. In such case, into the **Host** field, type your **Backup RADIUS Server Address**.
6. Now, to configure the **RADIUS Accounting** function:

   Note

   Currently, due to the security policy, the Accounting for Splash Page/Captive Portal is blocked by defalut, even if enabled in the user interface. To enable this option, you should contact the Cisco support.

   a) From the **RADIUS Accounting** dropdown list, select the **RADIUS Accounting Is Enabled** option.  
   Tip: In case the **RADIUS Accounting Is Enabled** option is not available, the **RADIUS Accounting** function is not used on the Splash Page. To solve this, contact the Meraki Help Desk by creating a new case. To do this, go to the **Help \*\* Cases** section, and type "Please enable RADIUS accounting for the Splash Page." in the appropriate field.

   b) To set up the **RADIUS Accounting Servers** panel, click the **Add a Server** link, and provide the **Server** details:  
   - In the **Host** field, type the **RADIUS Server IP Address**. For this instruction, it is *35.241.143.144*.
   - Into the **Port** field, enter the **Port**. For this instruction, it is *1813*.
   - Into the **Secret** field, enter your **Shared Secret**. For this instruction, it is *bAZev44u*

   ![meraki configuration](images/meraki/config_meraki_5.png)

   Note

   If you need to configure the **RADIUS Backup Servers**, repeat step 6. In such case, into the **Host** field, enter the **Backup RADIUS Server Address**.
7. Now, in the **Enable Data-Carrier Detect?** section, select the **DCD Is Disabled** from the dropdown list, and from the **Captive Portal Strength** list choose **Block All Access Until the Sign-On Is Complete**.

   ![meraki configuration](images/meraki/config_meraki_6.png)

   ![meraki configuration](images/meraki/config_meraki_7.png)
8. Then, continue to configure the **Walled Garden**:

   a) From the **Walled Garden** dropdown list, select the **Walled Garden Is Enabled** option.  
   b) Into the **Walled Garden Ranges** field, type the entries from the **References** section according to your preferences

   Tip

   In case of problems with setting up the **Domain Addresses** in the **Walled Garden** ranges field, the **Domain-Based Walled Garden** function may be disabled. To solve this, contact the Meraki Help Desk by creating a new case. To do this, go to the **Help \*\* Cases** and type "Please enable the Domain-Based Walled Garden for the Splash Page." in the appropriate field.

   ![meraki configuration](images/meraki/config_meraki_8.png)
9. To finish the configuration of the Access Control, click the **Save Changes** button.

### Configuring the Splash Page

To configure the Splash Page:

1. To go to the **Splash Page**, hover your mouse over the **Wireless** section in the menu. Then, in the dropdown menu, select the **Splash Page** option which is located under the **Configure** category.

   ![meraki configuration](images/meraki/config_meraki_9.png)
2. From the **SSID** dropdown list, select the **SSID** on which the platform access should be configured. For this instruction, it is *SSID\_NAME*.

   ![meraki configuration](images/meraki/config_meraki_10.png)
3. In the **Custom Splash URL** section, select the **Or Provide a URL Where Users Will Be Redirected** option from the checklist, and enter the website address to which the users should be redirected into the empty field. Such address should have the following format:
   *<http://domainname.com/login?essid=>***\*Name of SSID***\**.

   ![meraki configuration](images/meraki/config_meraki_11.png)
4. In the **Splash Behavior > Where Should Users Go After the Splash Page?** section, choose the **A Different URL** option from the checklist, and type the website address into the empty field. Such address should have the following format:
   *<http://domainname.com/welcome?essid=>***\*Name of SSID***\**.

   ![meraki configuration](images/meraki/config_meraki_12.png)
5. To finish the configuration process, click the **Save Changes** button.

### Configuring a Meraki Device on This Platform

Note

To configure the Platform, you need the **SSIDs** from the Splash Page configuration.

This Platform’s configuration consists of two steps: **adding the device to the Platform**, and **configuring the Network**.

#### Adding the Device to the Platform

To add the Meraki device to the platform:

1. Firstly, log in to the platform. Then, go to the **Portal Management → Structure** section and select **Devices** from the navigation bar.

   Note

   Make sure that you are in the appropriate organisation. To do this, select the desired one from the right panel or the top bar; it should be highlighted in blue.
2. Now, click **+** in the bottom right corner to add a device.

   ![meraki configuration](images/meraki/meraki_1.png)
3. In the **Add Devices** window, enter the device details:

   * From the **Device Type** dropdown list, select the type of the device,
     Into the **Device Name** field, type the device name; in most cases, it is a device’s MAC address,
   * In the **IP Address** field ,enter the device’s IP address (recommended),
   * In the **Serial Number** field, enter the device’s serial number,
   * Into the **Descriptive Name** field, type a descriptive name of the device,
     Then, click **Save** in the top right corner to confirm the details and proceed further.

   ![meraki configuration](images/meraki/meraki_2.png)
4. The device is now added to your organisation.

#### Configuring the Network

To learn how to configure the Network, read the [Creating Access Settings](../user_guide/user_enrollment/create_access_settings.html)

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