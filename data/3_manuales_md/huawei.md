Huawei - Platform documentation






[Skip to content](#huawei-configuration-guide)

# Huawei Configuration Guide

## Introduction

Welcome to the **Linkyfi Configuration Guide**.

This guide will help you configure the Huawei so that it works with the Linkyfi platform.

## Prerequisites and basic configuration

To start with your Huawei configuration, you need to fulfil certain prerequisites and prepare your basic configuration.

### Prerequisites

Make sure that:

* Huawei:
  + has correctly configured IP settings with a correct DNS server.
  + resolves the domain address – **linkyfi.com**.
  + has access to the Linkyfi platform using ports **80**, **1812**, and **1813**.
* You are logged in to the Agile Controller-Campus.

Noted working firmware version:

| Software Mapping | Software Version |
| --- | --- |
| Agile Controller-Campus | V300R019C00SPC310 |
| AP | V200R010C00SPCa00 |

### Basic configuration

Below, you can find the table providing the data for the **Production Environments**, which are the cloud servers of the platform.

| Name | URL | IP |
| --- | --- | --- |
| Linkyfi UVA | uva.linkyfi.com | 35.245.165.143 |

## Configuring Huawei

During the configuration of Huawei, you need to:

* [Make an access point online](#making-an-access-point-online),
* [Connect the access point to the Agile Controller-Campus](#connecting-access-points-to-the-agile-controller-campus),
* [Integrate the access point with Linkyfi](#integrating-the-access-point-with-linkyfi).

Proceed with each configuration and then [configure the Linkyfi platform](#configuring-the-linkyfi-platform).

### Making an access point online

This stage of the configuration consists of two steps:

* [Finding the device's IP address](#Finding-the-device's-IP-address),
* Configuring the access point either in the [web interface](#Configuring-the-access-point-in-the-web-interface) or in the [command line interface](#Configuring-the access-point-in-the-CLI) (CLI).

#### Finding the device's IP address

Begin the configuration by finding the device's IP address in the CLI.

To find the device's IP address in the CLI:

1. Power up the access point.
2. If the device is connected to a network:

   * Find a PC which is at the same network segment.
   * In the CLI, run the command:

     `arp -a | find /i "18-de-d7-ba-52-e0"`

     where `18-de-d7-ba-52-e0` is **the MAC address of the device**.

     ![Device's IP address in the CLI](images/huawei/huawei_01.png)
3. If the device is not connected to any network, then connect a PC to the interface GE0 or GE1, the IP of network card on PC should be configured as 169.254.1.100, at the same segment. According to the product manual, the default IP address might be 169.254.1.1.

**What to do next:** [Configure the access point](#configuring-the-access-point)

#### Configuring the access point

The second step is to configure the access point, you can either do it in the web interface or in the CLI.

##### Configuring the access point in the web interface

The first of the option of the configuration of the access point is to configure it in the web interface.

To configure the access point in the web interface:

1. In a web browser, go to the *https://{device\_ip}* website and log in.
2. Expand **Deployment Configuration**:

![Deployment Configuration](images/huawei/huawei_02.png)

* For **Working mode**, select the **Cloud AP** option.
* For **Address mode**, select the **IP** option.
* Into the **IP address** field, type your Controller Address. For example in this instruction, it is: *114.115.200.167*.
* Into the **Port number** field, type **10020**.

![Deployment Configuration Port Number](images/huawei/huawei_03.png)

* Click **Apply**.

Note

If you access the web GUI and it returns no login page but this information:

![FIT](images/huawei/huawei_04.png)

Then the work mode is not set to cloud, and you need to [configure the device using the CLI](#configuring-the-access-point-in-the-cli).

##### Configuring the access point in the CLI

The access points can be also configured in the command line interface.

To configure the access point in the CLI:

1. Connect the device through the SSH2 protocol.
   ![Connect the device through the SSH2 protocol](images/huawei/huawei_05.png)
2. Run the command: `<Huawei>display version`. If the work mode is FIT or FAT rather than CLOUD, you need to switch mode to CLOUD.
   ![Work mode](images/huawei/huawei_06.png)
3. Switch the work mode to CLOUD by running the commands: `system` and then `ap-mode-switch cloud`. Confirm the switch. As a result, the device will reboot.
   ![Cloud work mode](images/huawei/huawei_07.png)
4. Register the device to the controller by running the commands: `system` and then `cloud-mng controller ip-address 114.115.200.167 port 10020` and then `display cloud-mng info`.
   ![cloud-mng controller ip-address](images/huawei/huawei_08.png)

Note

Remember to use your controller's IP address

**What to do next:** [Connect access point to the Agile Controller-Campus](#connecting-access-points-to-the-agile-controller-campus)

### Connecting access points to the Agile Controller-Campus

The second stage of the Huawei configuration is the connection of the access point to the Agile Controller-Campus. It consists of:

* [Accessing the access point in the CLI](#accessing-the-access-point-in-the-cli)
* [Adding and authorizing the access point](#adding-and-authorizing-the-access-point)
* [Registering the access point in the CLI](#registering-the-access-point-in-the-cli)
* [Checking the status of the access point in the CLI](#checking-the-status-of-the-access-point-in-the-agile-controller-campus)

#### Accessing the access point in the CLI

The first step is accessing the access point in the CLI.

| **Before you begin**: Set the console baud rate to **9600**. If it is set correctly, then the login authentication appears. |
| --- |
| Login authentication |

To access an access point in the command line interface:

1. Enter the password.
2. Check the current system software version, by running the command:
   `<Huawei>display startup`
3. Check the ESN number, by running the command:
   `<Huawei>display esn`
4. Check whether the AP can ping the controller and ensure that the public
   network is used, by running the command:
   `ping <controller_southbound_service_IP>`

Note

Copy the ESN number, as it is going to be used later in the configuration.

For this instruction, the `controller_southbound_service_IP` is `114.115.200.167`.

Note

Remember to use your controller's IP address.

![Ping](images/huawei/Huawei_10.png)

**What to do next:** [Add and authorize the access point](#adding-and-authorizing-the-access-point)

#### Adding and authorizing the access point

The next step is to add and authorize access points in the Agile Controller-Campus.

To add and authorize access points:

1. In the Agile Controller-Campus, go to **Plan > Network > Device List** , and click **Add Device**:
   * Into the **Device ESN** field, type the ESN of the access point. For this instruction it is *2150 0829 352S H190 4086*.
     ![Plan > Network > Device List](images/huawei/huawei_11.png)
   * Click **Select** and select the corresponding device group.
2. Go to **System > License Management** **>** **License Information** :
   * Click **Authorize device**.
     ![License information](images/huawei/huawei_12.png)
   * Select the ESN of the access point to be connected.
     ![ESN](images/huawei/huawei_13.png)

**What to do next:** [Register the access point](#registering-the-access-point-in-the-cli)

#### Registering the access point in the CLI

The next step is to register the added and authorized access points.

To configure the access point in the CLI:

1. In the command line, log in to the access point.
2. Enter the system view by running the `system-viewcommand`.
3. To configure the IP address of the Agile Controller-Campus, run the command:

   `cloud-mng controller ip-address <ip_address> port <port_number>`
   ![IP address of the Agile Controller-Campus](images/huawei/huawei_14.png)
4. To configure the IP address of the Agile Controller-Campus, run the command:
   `cloud-mng controller url \<url\_string\> port \<port\_number\>`
5. Make sure the configuration was successful, by running the command:
   `display cloud-mng info`

   ![display cloud-mng info](images/huawei/huawei_15.png)

**What to do next:** [Check the status of the access point](#checking-the-status-of-the-access-point-in-the-agile-controller-campus)

#### Checking the status of the access point in the Agile Controller-Campus

This stage of the configuration ends with checking the status of the device in the web interface.

To check the status of the access point in the web interface:

1. Go to **Plan > Network > Device List**.
2. Make sure that in the **Status** column, **Normal** is displayed .

![Device list](images/huawei/huawei_16.png)

**What to do next:** [Integrate the access point with Linkyfi](#integrating-the-access-point-with-linkyfi)

### Integrating the access point with Linkyfi

The next stage of the configuration is the integration of the access point with Linkyfi. It consists of the following procedures:

* [Adding the ACL template](#adding-the-acl-template)
* [Adding RADIUS relay server](#adding-radius-relay-server)
* [Adding the URL template](#adding-the-url-template)
* [Configuring SSID](#configuring-ssid)
* [Setting a portal page](#setting-a-portal-page)

#### Adding the ACL template

The first step of the integration is the addition of the ACL template.

To add the ACL template:

1. Go to **Tenant > Configure > Template** and then go to the **Policy Template** tab.
2. From the **Template** menu, select **ACL**.
3. Into the **Name** field, type a name of the template. For this instruction it is *ACL6000*.
4. For **Rule List**:

   * Click **Add**.
   * Add following entries:

   |  |  |
   | --- | --- |
   | IP | 13.228.254.255/32 |
   | domain | \*linkyfi.com |

   ![Rule list](images/huawei/huawei_17.png)

   * Also add the domain and name and IP addresses of the Agile Controller-Campus.

   |  |  |
   | --- | --- |
   | domain | *.huaweicloud.com* |
   | IP | **(your controller IP)**\* |

   ![Rule list](images/huawei/huawei_18.png)
5. For the full list of entries (e.g. to allow social media login), go to the [References](#references) chapter.

**What to do next:** [Add RADIUS relay server](#adding-radius-relay-server)

#### Adding RADIUS relay server

The next step is to add RADIUS relay server.

To add RADIUS relay server:

1. Go to the **Radius Relay Server** tab.
2. Into the **Name** field, type a name of the server. For this instruction it is *LinkyfiRadius*.
3. For **Authentication server** address, click **Add**:
   * Into the **Host IP Address** field, type your Linkyfi server address. For this instruction it is *13.228.254.255*.
   * Into the **Port** field, type **1812**.
   * Into the **Key** field, type **bAZev44u**.
4. For **Accounting server address** , click **Add**:
   * Into the **Host IP Address** field, type your Linkyfi server address. For this instruction it is *13.228.254.255*.
   * Into the **Port** field, type **1813**.
   * Into the **Key** field, type **bAZev44u**.
5. Into the **Timeout period(s)** field, type **30**.
6. Into the **Retransmission times** field, type **2**.
7. For **Load balancing** mode, select the **Strict accordance with priority** option.

![RADIUS relay server](images/huawei/huawei_19.png)

**What to do next:** [Add the URL template](#_Adding_the_URL)

#### Adding the URL template

This chapter will help you add the URL template.

To add the URL template:

1. Go to the **URL Template** tab.
2. Name the Template. For this instruction, it is *LinkyfiURL*.
3. For **Template Type**, select the **Cloud platform-based relay authentication** option.

   ![URL template](images/huawei/huawei_20.png)
   4. For **Parameters** in template, click **Create** and add the following entries:

| **Value Assignment Mode** | **Parameter Content** | **Parameter Name** |
| --- | --- | --- |
| User-defined | login | cmd |
| User-defined | 4c-fa-ca-f4-45-40 | apname |
| Replace Existing Value | redirect-url | url |
| Replace Existing Value | user-ip | ip |
| Replace Existing Value | user-mac | mac |
| Replace Existing Value | loginurl | loginurl |
| Replace Existing Value | ssid | essid |

Note

Replace your AP's own MAC address with apname.

![Parameters in template](images/huawei/huawei_21.png)

**What to do next:** [Configure SSID](#configuring-ssid)

#### Configuring SSID

The next step is to configure SSID. Read this chapter to learn how to do it.

To configure SSID:

1. Go to **Network Configuration > AP**.
2. In the **Basic Settings** pane:

   * Into the **SSID Name** field, type a name for the SSID. Remember it, as it is going to be used later. For this instruction it is *Linkyfi*.
   * Switch the **Working status** slider to the **ON** position (it lights green).
   * For **Effective radio** , select the radio channels on which it must work. For this instruction it is *2.4G/5G*.
   * For **Network connection** mode, select the **NAT** option.

   ![Basic settings](images/huawei/huawei_22.png)

   * Click **Next**.
3. In the **Security Authentication** pane:

   * For **Authentication mode** , select the **Open network** option.
   * Switch the **Push pages** slider to the **ON** position (it lights green).
   * For **Page pushing mode**, select **Relay authentication by cloud platform**.
   * For **Interconnection** mode, select the **RADIUS relay** option.

   ![Security authentication](images/huawei/huawei_23.png)

   * For **Third-Party Portal page authentication parameters**:
     + Into the **User name** field, type **username**.
     + Into the **Password** field, type **password**.
     + Into the **Success page URL** field, type **redirect\_URL**.
     + Next to the **RADIUS relay server** field, click **Select Server** and select the created server. For this instruction it is *LinkyfiRadius*.
   * Switch the **Real-time accounting** slider to the **ON** position (it lights green).
   * For **Default permit rule**, select the created ACL template. For this instruction it is *ACL6000*.
   * For **Escape policy**, select the proper check boxes.

   ![Third-party Portal page authentication parameters](images/huawei/huawei_24.png)

   * Click **Next**.
4. In the **Policy Control** pane, click **OK**.

![Policy control](images/huawei/huawei_25.png)

**What to do next:** [Set a portal page](#setting-a-portal-page)

#### Setting a portal page

The last step of the integration is the setting of a portal page.

To set a portal page:

1. Go to **Site > Configure > Access Policy** > **Portal Page Push Policy**.
2. Type a Name for the portal.
3. Turn on **SSID Matching**.
4. For **SSID**, select the SSID that was created previously. For this instruction it is *Linkyfi*.

   ![Portal Page Push Policy](images/huawei/huawei_26.png)
5. Turn on **Device Matching**.
6. Add your Devices.
7. In the **Push Page Rule** section:

   * For **Authentication mode**, select the **Cloud platform-based relay authentication**.
   * For **Interconnection** mode, select **RADIUS Relay**.
   * For **URL template**, select the template created previously. For this instruction it is *LinkyfiURL*.
   * In the **Third-party authentication URL** field, type your welcome page address. For this instruction it is *<http://linkyfi.com/login>.*
   * Click **Apply**.

![Push Page rule](images/huawei/huawei_27.png)

**What to do next:** [Configure the Linkyfi platform](#configuring-the-linkyfi-platform)

## Configuring the Linkyfi platform

### Adding the access point

To add the access point:

1. Click **Portal Management**.
2. Go to **Structure** and then **Devices**.
3. Click the ![plus icon](images/huawei/huawei_28.png) button to add a new device.

   ![Add new device](images/huawei/huawei_29.png)
   4. In the **Add a new device** pane:

   * From the **Device type** list, select **Huawei**.
   * Into the **AP MAC** field, type a MAC address of your device. For this instruction it is *4c-fa-ca-f4-45-40*.

   ![Device settings](images/huawei/huawei_30.png)   
   5. Click **Save**.

**What to do next:** [Create a portal](#creating-portals).

### Creating Portals

To create a portal:

1. Go to **User Enrollment > User Journey > Portal.**
2. Configure portal settings:

   * Into the **Name** field, type the portal name. For this instruction it is **new\_linkyfi\_portal**.
   * From the **Language selection** list, select the portal language.

   ![Create a portal](images/huawei/huawei_31.png)

   * In the top right corner, click **Next**.
3. In the left menu, select category and component, drag it and drop onto the working space.

![Portal editor](images/huawei/huawei_32.png)
4. Click **Save**.

**What to do next:** [Adding the Portal node](#adding-the-portal-node).

### Adding the Portal node

**After creating the portal, next thing you should do is to attach the portal to a flow.**

To add the portal node:

1. Go to **User Enrollment > User Journey > Page Flow**
2. Configure portal settings
   * Into the **Name** field, type the flow name. For this instruction it is **new\_linkyfi\_flow**.
     ![Flow](images/huawei/huawei_33.png)
3. In the Page Flow editor, depending on whether it is the first node added to the flow or a consecutive one, click the available button, either ![plus icon](images/huawei/huawei_34.png) or ![three dots](images/huawei/huawei_35.png). From the list, select **Portal**.

![Flow editor](images/huawei/huawei_36.png)
4. If you have a portal that is already created, in the portals available in the panel, click the portal tile and then click **Select**.

![New portal node](images/huawei/huawei_37.png)
5. As a result, the Portal node is added to the flow.

![New portal node added](images/huawei/huawei_38.png)
6. Then, click ![three dots](images/huawei/huawei_35.png) to add internet access.

![Add Internet access](images/huawei/huawei_39.png)
7. Set the **Network parameters**.

![Network parameters](images/huawei/huawei_40.jpg)  
8. Lastly, remember to add a **Landing page**. It can be a portal or a website.

![Landing page](images/huawei/huawei_41.png)
9. Click **Save**.

**What to do next:** [Publishing a Page Flow](#publishing-a-page-flow).

### Publishing a Page Flow

**In order for a Page Flow to be made public, you need to create access settings and attach a Page Flow to it.**

To publish a Page Flow:

1. Go to **User Enrollment > User Journey > Access settings**.
2. Click ![plus icon](images/huawei/huawei_28.png) to add your network name/SSID. For this instruction it is *Linkyfi*.  
   ![Publish a page flow](images/huawei/huawei_42.png)

   Note

   Into the **Name** field, type the exact network name or SSID that you set on AP. This is case sensitive.
3. In the **Network manager**, click **Attach flow** on the tile of the created access settings.

![Attach flow](images/huawei/huawei_43.png)
4. If you already have a Page Flow created, in the Page Flows available panel, click it and then click **Select**.

![Published page flow](images/huawei/huawei_44.png)
5. As a result, the Page Flow is published. You can see it in the Access settings tile in the Attached Flow section.

![Attached flow](images/huawei/huawei_45.png)

## References

In this section, there is a list of all entries that you may need to add to the walled garden. When you finish adding them, continue with the [Adding the ACL template](#adding-the-acl-template) procedure.

### Linkyfi

```
*.linkyfi.com

```

```
IPs:
For Linkyfi Europe:                   94.23.89.14
For Linkyfi North and South America:  52.2.225.2
For Linkyfi Asia:                     13.228.254.255

```

### iOS

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

```

### Microsoft

```
msftncsi.com

*.msftncsi.com

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

IPs:

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

IPs:

```
199.16.156.0/22

199.59.148.0/22

199.96.56.0/21

192.133.76.0/22

```

### Instagram

```
instagram.com

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

*.gstatic.com

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