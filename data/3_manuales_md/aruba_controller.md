Aruba Controller - Platform documentation






[Skip to content](#aruba-controller-configuration-guide)

# Aruba Controller Configuration Guide

## Prerequisites and Basic Configuration

To configure the Aruba controller Access Point with the platform, you should first fulfill specific prerequisites, and prepare the Basic Configuration.

### The Configuration Prerequisites

You should ensure that:

* You have correctly configured the Aruba Controller IP pools (including a valid DNS server address)
* You have **enabled** the Policy Enforcement Firewall option must To verify it, go to Configuration > Network > Controller > Licenses section

You should also verify that:

* The Aruba Controller resolves the domain address – platform.com, and can access the platform using the following ports – 80, 1812 and 1813,
* Your Access Points correctly communicate with the controller, and are set to the **Tunnel** mode

### The Basic Configuration

Below, you can find the table providing the data for the **Production Environments**, which are the cloud servers of the platform.

| Name | URL | IP |
| --- | --- | --- |
| Linkyfi UVA | uva.linkyfi.com | 35.245.165.143 |

## Configuring Aruba Controller

To properly set up the aruba controller, you must follow the below steps:
1. Set up the RADIUS server
2. Configure a group of servers
3. Set up AAA profiles
4. Add whitelists
5. Configure your network

### Logging in to the Aruba Controller

To begin the configuration process, you should first log in to the Aruba Controller. To do this, go to the *https://* page. Into the login fields, enter your username and password, and click the **Log In** button.

![aruba controller configuration](images/aruba_controller/aruba_controller_0.png)

### Setting Up the RADIUS server

1. Go to the **Configuration > WLAN** section and click the blue **+** icon to add a new WLAN.
2. In the first **General** step:

   * In the **Name (SSID)** field, type the name of the WLAN. For this instruction, it is *Platform*.
   * In the **Primary Usage** section, select the **Guest** option.
   * From the **Broadcast On** dropdown list, select \**All APs*.
   * From the **Forwarding Mode** dropdown list, select **Tunnel**.

   After you have finished providing the details, click **Submit** to continue to the next step.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_1.jpg)
3. In the **VLANs** step, select the desired VLAN, from the dropdown list. For this instruction, it is *VLAN\_200*.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_2.jpg)

Then, click **Submit** to proceed further.

1. In the **Security** step. Swipe the slider to the **ClearPass or Other External Captive Portal** option, and click the blue **+** icon in the bottom left corner of the **Auth Servers** field to create a new server.

   For this instruction, a server has already been created. However, if you configure the Aruba Controller for the first time, the **Auth Server** field is empty.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_3.jpg)
2. Now, in the **Create New Server** window:

   * Choose the **RADIUS** selector.
   * In the **Name** field, type the name of the server. For this instruction, it is *Platform*.
   * Into the **IP Address** field, enter the server’s IP address. For this instruction, it is *35.241.143.144*.
   * Into the **Auth Port** field, enter the server’s authentication port. For this instruction, it is *1812*.
   * In the **Accounting Port** field, type the server’s accounting port. For this instruction, it is *1813*.
   * Into the **Shared Key** field, enter the server’s shared key. For this instruction, it is *bAZev44u*.
   * In the \**Retype Key* field, retype the shared key.
   * In the **Timeout** field, set up the server’s timeout by entering the desired number. By default, it is *5*.

   After you have provided the server’s details, click **Submit** in the bottom right corner.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_4.jpg)
3. Now, back in the **Security** step, provide the details of the captive portal:

   * In the **CPPM Host** field, type the domain of the Platform server. For this instruction, it is *platform.com*.
   * In the **CPPM Page** field, type the captive portal address. For this instruction, it is */login*.  
     **Note:** If your Aruba Controller has a custom domain, change `/login` to `/login?switch_url=customdomain.com` in the **CPPM Page** field, where `customdomain.com` is a URL address of the desired domain.
   * Into the **Redirect URL** field, enter the address to which users will be redirected after gaining internet access. For this instruction, it is *platform.com/welcome*.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_5.jpg)
4. In the **Access** step, click **submit** in the bottom right corner to finish setting up the RADIUS server.

### Adding Whitelists

1. Go to the **Authentication > L3 Authentication > Captive Portal Authentication** section, and select the captive portal which you have just created from the **L3** Authentication left menu. For this instruction, it is *Platform*.
2. Now, scroll down the **Captive Portal Authentication Profile** section to the **Whitelist** field, and click the blue **+** icon in the bottom left corner to add a whitelisted site. For this instruction, it is *platform.com*. You can also add other websites, such as social media platforms, according to your preferences.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_6.jpg)

### Configuring a Captive Portal

1. Go again to the **Authentication > L3 Authentication > Captive Portal Authentication** section, and select the captive portal which you have just created from the **L3** Authentication left menu. For this instruction, it is *Platform*..
2. In this section:

   * For the **Default Role**, select **guest** from the dropdown menu.
   * For the **Default Guest Role**, select **guest** as well.
   * Specify the number of seconds for the **Redirect Pause**. For this instruction, it is *10*.
   * Select the **User Login**, **Guest Login**, and Logout Popup Window\*\* checkboxes.
   * Specify the number of seconds for **Logon Wait Minimum Wait** and the **Logon Wait Maximum Wait** options. For this instructions, these are *5* and *10*, respectively.
   * Set the **Logon Wait CPU Utilization Treshold**. For this instruction, it is *60*.
   * Set the number of **Max Authentication Failures**. For this instruction, it is *0*.
   * For the **Authentication Protocol**, select **PAP** from the dropdown list.
   * In the **Login Page** field, enter the website address. For this instruction, it is *<https://platform.com>*.
   * In the **Welcome Page** field, enter the web address of the page which the users see after logging in to your network. For this instruction, it is *<https://platform.com/welcome>*.
   * To enable the welcome page, select the **Show Welcome Page** checkbox.

   After you have finished providing all the details, click **Submit** to save them.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_7.png)

### Adding User Roles

1. Go to the **Configuration > Security > Access Control > User Roles** section, and click the **+** button to create a role:
2. Now, in the **New Role** window, type the Name of the Role in the **Name** field. For this instruction, it is *Platform*. Afterwards, click the **Submit** button.

   Then, click **Apply** in the bottom right corner to confirm adding the role.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_8.jpg)
3. The Role named *Platform* is now created. Now, click the blue **+** button in the bottom left corner.to create a new Policy.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_9.jpg)
4. Now, in the **New Policy** window:

   * From the top checkboxes, select the **Add an Existing Policy** option.
   * From the **Policy Type** dropdown list, select **Session**.
   * From the **Policy Name** dropdown list, select the Policy’s name. For this instruction, it is *apprf-internal\_cp-guest-logon-sacl...*.

   Afterwards, click **Submit** to finish creating the new Policy.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_10.jpg)

### Configuring AAA Profiles

1. Go to the **Authentication > AAA Profiles** section, and click the blue **+** button to add a new AAA Profile.
2. Now, in the **AAA Profile: New Profile** window:

   * In the **Profile Name** field, type the name of the AAA Profile. For this instruction, it is *Platform*.
   * From the **Initial Role** dropdown list, select **Platform-guest-Logon**.
   * From the **MAC Authentication Default Role**, select **guest**.
   * From the **802.1X Authentication Default Role**, also select **guest**.
   * Specify the number of the **Max IPv4 for Wireless User**. For this instruction, it is *2*.
   * Select the **RADIUS Roaming Accounting** and **RADIUS Interim Accounting** checkboxes.
   * From the **User Derivation Rules** dropdown list, select **-None-**.
   * From the following checkboxes, select the **Wired to Wireless Roaming**, **Device Type Classification**, and **Enforce DHCP** options.

   Afterwards, click **Submit** to save the settings.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_11.png)
3. Next, expand the AAA Profile section which you are currently configuring in the **AAA Profiles List**. For this instruction, it is *Platform*. Then, from the sub-list, select the **RADIUS Accounting Server group** section.
4. In the **Server Group** window, select the name of the server group from the **Server group** dropdown list. For this instruction, it is *Platform*.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_12.png)

## Configuring the Network

When you have finished all the above configuration steps, you can now start configuring your Network. To do this, you should add an AP Group, and Remote AP Whitelists.

### Adding an AP Group

1. Go to the **Configuration > AP Group** section and click the blue **+** button to add a new AP Group.
2. In the **New AP group** window, type the name of the new AP group in the **Name** field. For this instruction, it is *Platform,*.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_13.png)
3. Now, select the **WLANs** tab in the **AP groups** window, and click the blue **+** cutton in the bottom left corner to assign a WLN to it.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_14.png)
4. In the **Select WLAN** window, select the AP from the **Virtual-AP** dropdown list. For this instruction, it is *Platform*.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_15.png)

### Adding APs to an AP Group

Note

Before you begin to add an AP to an AP Group, you should ensure that the AP is configured in the RAP mode, and is assigned the correct Controller address.

#### Adding APs to an AP Group in the Remote AP (RAP) Mode

1. Go to the **Configuration > Access Points > Whitelist** section, select the **Remote AP Whitelists** tab, and click the blue **+** button in the bottom left corner.
2. In the **Add New Remote AP Whitelists** window:

   * Into the **MAC Address** field, enter the MAC address of the AP.
   * In the **AP Name** field, type the name of the AP.
     **Note:** It is a good practice to enter the MAC address as the AP name as well.
   * From the **AP Group** dropdown list, select the group to which you would like to add the AP. For this instruction, it is **Platform**.

   To confirm adding a whitelist, click **Submit**.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_16.png)

#### Adding APs to an AP Group in the Campus AP (CAP) Mode

To add APs to an AP Group in the Campus AP **(CAP)** Mode, follow the same steps from the above \_ Adding APs to an AP Group in the Remote AP (RAP) Mode\_ chapter.

**Important:** After you have finished configuring the whitelists, you should make sure the **Admin State** is **enabled**. To do this:

1. Select the desired VLAN in the **VLANs** tab.
2. In the **VLAN** window, select the VLANs On **tab, and check the state in the** Admin State\*\* column.

   ![aruba controller configuration](images/aruba_controller/aruba_controller_17.jpg)

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