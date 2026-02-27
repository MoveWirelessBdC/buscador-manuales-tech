Mist - Platform documentation






[Skip to content](#mist-configuration-guide)

# Mist Configuration Guide

* To claim the APs, go to the **Organization > Subscriptions** page and select the **Add Activation Code** button in the top right corner. Once the activation code is added and **Activated**, all the APs will automatically get claimed to the organization. You can see the list of APs in the Inventory page (**Organization > Inventory**).

![mist configuration](images/mist/mist_0.png)

* You can individually claim APs to your organization by navigating to **Organization > Inventory > Claim APs** and entering in the claim code found on the back of each AP.

![mist configuration](images/mist/mist_1.png)

* The **claim code** of the AP is written in the backside of the AP where the **QR code** of the AP is printed.

![mist configuration](images/mist/mist_2.jpg)

## WLAN Configuration

1. Login in to the **Mist Portal**.
2. Click on the **Networks** icon in the left hand column and click on **WLANS**.
3. Click the **Add WLAN button** in the top right hand corner to add your network.
4. In the **SSID section** create the network name which must be the same as in the platform.
5. Under **WLAN Status** click the **Enabled** button, choose **Radio Band** 2.4 GHz and 5 GHz and the **Drop Rate**.
6. Under **Data Rates** choose **Compatible**.
7. Under **WiFi Protocols** select **Enabled**.
8. **WLAN Rate Limit** should be **Disabled**.
9. Under **Security** you have the option of choosing whether your network has a passphrase or not and then choose the default option under **Fast Roaming**.
10. **VLAN** should be **Untagged**.
11. Under **Guest Portal** make the following changes.
    * Click on the **Forward to external portal**.
    * In the **Portal URL** field enter the desired address.
    * Add the **Default Walled Garden** entries to the **Allowed Host Names** field.

Note

Make sure to put commas in between walled garden entries.

![mist configuration](images/mist/mist_3.png)

## Configuring the Platform

To configure an access point on the Platform, you should first add it to the Platform. Then, you should configure the network in which the access point will be used.

### Adding an Access Point to The Platform

To add an Access Point, you should first log in to the Platform. Then, go to the **Portal Management > Structure** section, and select the **Devices** tab from the upper bar.

1. Now, click the **+** button in the bottom right corner to add a new device.

![aruba central configuration](images/aruba_central/aruba_platform_config_1.png)

1. From the **Device Type** list, select **Mist**. Then, provide the access point details:
2. In the **AP MAC** field, type the access point's **MAC** address,
3. Into the **IP Address** field, enter the access point’s IP address (recommended),
4. Into the **Serial Number** field, enter the access point’s serial number,
5. In the **Descriptive Name**, you can type the name that would help you differentiate this access point from the other ones,

![aruba central configuration](images/aruba_central/aruba_platform_config_2.png)

![mist configuration](images/mist/mist_6.png)

1. In the below section, in order to retrieve the **Site ID** you must first go to <https://manage.eu.mist.com/> and log in to your organisation. Next, go to **Organization > Site Configuration** and choose your organisation. There you will find the **Site ID**. To retrieve the **WLAN ID** and **API Secret** go to **Network > WLANs** and choose the network. There you will find the **WLAN ID** and **API Secret**.

![mist configuration](images/mist/mist_7.png)

After you have finished providing the details, click **Save** in the top right corner to finish adding the access point to the Platform.

### Creating MIST API Token

* **API Tokens** are used to authenticate each **Mist API** call to a particular user.
* Each user has a role which authorizes the user to perform certain operations to the organization or site (ie: “**administrator**” or “**read-only**” roles).
* To create **API Token** go to <https://api.mist.com/api/v1/self/apitokens> and click the **POST** button to create a new token.

![mist configuration](images/mist/mist_8.jpg)

Note

Store the key somewhere safe; the full **API token** string will not be revealed again!

![mist configuration](images/mist/mist_9.jpg)

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