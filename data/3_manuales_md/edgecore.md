Edgecore - Platform documentation






[Skip to content](#edgecore-configuration-guide)

# Edgecore Configuration Guide

## Prerequisites and Basic Configuration

To configure the Edgecore Access Point with the platform, you should first fulfill specific prerequisites, and prepare the Basic Configuration.

### The Configuration Prerequisites

You should verify that:

* The Edgecore has correctly configured IP settings, and is connected with the DNS server,
* The Edgecore resolves the platform domain address, and can access the platform using the following ports – 80, 443, 1812 and 1813,

### The Basic Configuration

Below, you can find the table providing the data for the **Production Environments**, which are the cloud servers of the platform.

| Name | URL | IP |
| --- | --- | --- |
| Linkyfi UVA | uva.linkyfi.com | 35.245.165.143 |

### Configuration Steps

1. Log in to the **Edgecore GUI**.
2. Navigate to the WiFi network configuration panel (**WiFi5 / WiFi6**) and select the **Wireless SSID** tab.
3. Select the SSID of the network you wish to edit from the list.
   ![image](images/edgecore/image_01.png)
   ![image](images/edgecore/image_02.png)
   **Important:** Copy the SSID value, as you will need it later when configuring the Network Name on the Platform side.
4. Navigate to **Network Settings**, set `Hotspot-controlled` as the network behavior, and add platform domain to the [whitelist](#whitelist). The whitelist should be updated as needed.
   ![image](images/edgecore/image_03.png)
5. Access the **Hotspot Tab**, ensure that the **Hotspot Enabled** toggle is activated and select **External Captive Portal Service**.
   ![image](images/edgecore/image_04.png)
6. Configure **RADIUS Server Settings**:
   * Enable the RADIUS Server.
   * Enter your RADIUS server address (for example, domain.com) – this address is for a test instance.
   * Enter `bAZev44u` as the RADIUS server shared secret.
   * Set `1812` as the RADIUS server authentication port.
   * Set `1813` as the RADIUS server accounting port.
   * **Important:** Make sure to add a **NAS ID**, as this will be required later in the Platform. Configuring NAS ID is essential for identifying the Access Point and the organization from which the traffic originates, ensuring the proper functioning of the login process in the Platform.
     ![image](images/edgecore/image_05.png)
7. Set up **Captive Portal Settings**:
   * Enter your domain URL (e.g., <https://domain.com/login>).
   * Specify your domain's landing page URL (e.g., <https://domain.com/welcome>).
     ![image](images/edgecore/image_06.png)
8. Go to **Platform** - **Portal Management** - **Structure** and choose the **Devices** tab. Add a new device by clicking the **(+)** button.
   ![image](images/commons/enter_device_editor.jpg)
9. Choose `Edgecore` and add the **NAS ID** created in the controller menu.
   ![image](images/edgecore/image_07.png)
10. Go to **User Enrollment** -> **User Journey** -> **Access Settings** and add a new Network. It must have the same **Network Name** as on the controller.
    ![image](images/commons/user_journey_menu.png)
    ![image](images/commons/network_name.png)

## Whitelist

### Domain

`domain.com`

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
gstatic.com  
clients3.google.com

```

### Microsoft (required for loging in with Microsoft)

```
msftncsi.com
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

```

## PayPal

```
paypal.com  
omtrdc.net  
mediaplex.com  
paypalobjects.com  
abmr.net  
dotomi.com  

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

```

### Google

```
accounts.google.com  
gstatic.com  
googleusercontent.com  
google.com  
googleapis.com  
accounts.youtube.com  

```

### Line.me

```
line.me  
line-apps.com  
line-scdn.net  

```

### Kakao

```
kakao.com  
google.com  
m2.daumcdn.net  

```