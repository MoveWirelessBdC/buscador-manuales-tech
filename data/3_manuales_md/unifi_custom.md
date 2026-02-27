Unifi Custom - Platform documentation






[Skip to content](#unify-network-controller-configuration-guide-v73-or-below)

# Unify Network Controller Configuration Guide (v7.3 or below)

*Also works (as workaround) with **v7.4 or above** when below configuration was done on **v7.3 or below** and was updated to newer version.*

To set up a Unifi device:

1. First, log in to the Unifi interface with your login credentials:

   ![unifi custom](images/unifi_custom/ubiquiti_1.png)
2. When you have successfully logged in to the Unifi interface, go to the **Settings > Wireless Network** section.

   Then, select the desired network and click on **Edit** in the **Actions** column.

   ![unifi custom](images/unifi_custom/ubiquiti_2.png)
3. Now, in the **Edit Wireless Network** window:

   * In the **Name/SSID** field, modify the name of the network, or leave an existing one.
   * For the **Enabled** option, select the **Enable This Network** checkbox.
   * From the list of the **Security** options, select **Open**.
   * For the **Guest Policy** option, select the **Apply Guest Policies** checkbox.
   * From the **Network** dropdown list, select **LAN**.

   ![unifi custom](images/unifi_custom/ubiquiti_3.png)
4. When you have provided the network details, go to the **Settings > Guest Control** section.

   Then, in the **Guest Policies** section:

   * For the **Guest Portal** option, select the **Enable Guest Portal** checkbox.
   * From the **Authentication** options, select **Hotspot**.
   * From the **Default Expiration** dropdown list, select **24 Hours**.
   * From the list of the **Landing Page** options, select **Promotional URL**, and enter the Administrator’s URL address into the field.

   Note

   All the **Redirection** option checkboxes should stay **deselected**.

   ![unifi custom](images/unifi_custom/ubiquiti_4.png)

   Next, scroll down and in the **Portal Customisation** section:

   * From the **Template Engine** options, select **AngularJS**.
   * For the **Override Default Templates** option, select the **Override Templates With Custom Changes** checkbox.

   ![unifi custom](images/unifi_custom/ubiquiti_5.png)

   Following, in the **Hotspot** section:

   * For the **RADIUS** option, select the **Enable RADIUS-Based Authorization** checkbox.

   ![unifi custom](images/unifi_custom/ubiquiti_6.png)
5. Now, go to the **Guest Control > Profiles > RADIUS** section and click the **Create New RADIUS Profile** button.

   ![unifi custom](images/unifi_custom/ubiquiti_7.png)

   Then, in the **Edit RADIUS Profile** window:

   * Into the **Profile Name** field, enter the name of the RADIUS Profile. For this instruction, it is `GuestWiFi`.
   * For the **RADIUS Auth Server** option:
     + Into the **IP Address** field, enter your Platform IP address. For this instruction, it is `35.234.150.70`.
     + Into the **Port** field, enter the IP port. For this instruction, it is `1812`.
     + In the **Password Shared Secret** field, type the shared secret password. For this instruction, it is `bAZev44u`.
   * For the **Accounting** option, select the **Enable Accounting** checkbox.
   * For the **Interim Update** option, select the **Enable Interim Update** checkbox.
   * Into the **Interim Update Interval** field, enter the desired number of seconds. For this instruction, it is `10`.
   * For the **RADIUS Accounting Server** option:
     + Into the **IP Address** field, enter your Platform IP address. For this instruction, it is `35.234.150.70`.
     + Into the **Port** field, enter the IP port. For this instruction, it is `1812`.
     + In the **Password Shared Secret** field, type the shared secret password. For this instruction, it is `bAZev44u`.

   ![unifi custom](images/unifi_custom/ubiquiti_8.png)
6. After you have finished setting up the RADIUS profile, go back to the **Guest Control > Profiles > RADIUS** section:

   * From the **Profile** dropdown list, select the newly created RADIUS Profile. For this instruction, it is `GuestWiFi`.
   * From the **Authentication Type** dropdown list, select **CHAP**.

   ![unifi custom](images/unifi_custom/ubiquiti_9.png)
7. Finally, scroll to the **Access Control** section, and in the **Pre-Authorization Access** field, enter the access IP. For this instruction, it is `35.234.150.70/32`.

   ![unifi custom](images/unifi_custom/ubiquiti_10.png)

Important

* Files that you receive from your Administrator should be located in the following folder on the controller machine:
  `/usr/lib/unifi/data/sites/default/app-unifi-hotspot-portal`
* You should also insert your URL address in the `const wifiPortal` line to ensure the correct configuration:

`javascript
const wifiPortal = "Replace this with your server address, starting with http:// or https://";`

* Once the access point is configured, provide your Administrator with the device's MAC address and Network details to allow them to set it up on the Platform server.

## References

Below, you can find the list of entities that can be added to the Walled Garden during the configuration process. After you have finished adding them, continue configuring the Access Control.

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