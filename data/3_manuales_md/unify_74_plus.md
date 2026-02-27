Unifi 7.4+ - Platform documentation






[Skip to content](#unify-network-controller-configuration-guide-v74-or-above)

# Unify Network Controller Configuration Guide (v7.4 or above)

## Prerequisites

To configure Unifi V7.4 and above access point controllers with the platform, you should fulfill specific prerequisites and prepare the basic configuration.

## The Configuration Prerequisites

* For Unifi V7.4 and above make sure to prepare the following:
* Check the version of Unifi Controller. It must be version 7.4 or the latest version.
* Make sure that **https://<controller\_domain>:<port>** or **http://<controller\_ip>:<port>** of the controller is in Public and able to reach Platform’s corresponding cloud server.
* Prepare a user credential with “Site Administrator” role in Unifi. Please take note of Username and Password.

## Configuring WLAN

1. Go to **Settings>WiFi>Create New**
2. Fill-up the name for the SSID in the **Name field**.
3. Under **Broadcasting APs**, make sure the WLAN will be broadcast to the proper Access points or Group of Access points.
4. In the **Hotspot 2.0** section, select **Captive Portal**.
5. In the **Security Protocol**, select **Open**.
6. Click **Save** or apply changes.
   ![unify_74_plus](images/unify_74_plus/images_0.jpg)

## Configuring the Hotspot Manager

The configuration of the hotspot enables establishing the proper network connection, followed by the redirection to the captive portal.

Go to Unifi Web UI, on the left menu click **Insights** then **Hotspot Manager** icon and then click **Landing Page**.

1. Click **Branding>Success Landing Page** then under **Custom URL** set https://<platform\_domain>/welcome
   ![unify_74_plus](images/unify_74_plus/img_1.png)
2. Click **Authentication>One Way Methods** then under **External Portal Server** set the IP Address of Platform then click **Save**.
   ![unify_74_plus](images/unify_74_plus/img_2.png)
3. Click **Settings Check** the following settings:
   * Enable **Show Landing Page**
   * Enable **Secure Portal**
   * Enable **Domain** and set to **<platform\_domain>** (e.g. platform.com) (Don’t include http/https)
     ![unify_74_plus](images/unify_74_plus/img_3.png)
4. **Settings>Authorization Access>Pre-Authorization Allowances**, add the following entries:
   * **<platform\_domain>** (domain of corresponding Platform server installation)
   * x.x.x.x/32 (IP Address of corresponding Platform installation)
   * Other domains and IPs that need to be whitelisted if needed.
   * Click **Save** to confirm your settings.

## Adding the Access Point

To add the access point:

1. Log in to the Platform.
2. Click **Portal Management**, and then **Structure**.
3. Go to the **Devices** tab.
4. Click the **(+)** button to add the device.
   ![unify_74_plus](images/unify_74_plus/img_5.png)
5. In the **Add a new device** panel:
   * From the **AP Type list**, select **Unifi v7.4 or Above**.
   * Into the **AP MAC** field, type the MAC Address of the AP.
     ![unify_74_plus](images/unify_74_plus/img_6.png)
   * Click **Next**
   * Into the **API Domain field**, type *https://<controller\_domain>:<port>* or *http://<controller\_ip>:<port>* of the Unifi Controller.
   * Into the **API Username and Password**, type the Admin Username and Password that has **Site Admin Access** to Unifi Controller.
     ![unify_74_plus](images/unify_74_plus/img_7.png)
6. Click the **Save** button.

## Configuring the Network

To configure the network:

1. Click **User Enrollment>User Journey>Access Settings**.
2. Click the **Create a new network** button:

   * In the **Network Name** field, enter the SSID configured during the WLAN setup.
     ![unify_74_plus](images/unify_74_plus/img_8.png)
   * Click **Save**.
   * Click the three dots, then select **Attach Flow**.
   * **Select the Flow** (The flow depends on customer requirements. Typically, we use a test flow for connection testing.)
   * Click **Select**

   ![unify_74_plus](images/unify_74_plus/img_9.png)
   ![unify_74_plus](images/unify_74_plus/img_10.png)

Note

The SSID created in the Unifi Controller should also be the same as the SSID in the Platform.