Ruckus One - Platform documentation






[Skip to content](#ruckus-one-configuration-guide)

# Ruckus One Configuration Guide

1. Log in to your Ruckus One account.
2. On the main R1 dashboard, navigate to the Venues section. Select your desired venue and go to Networks.
3. Click Add Network to create a new WLAN as demonstrated below.

   ![image](images/ruckus_one/image7.png)
4. Fill in the Network Name and select Network Type as Captive Portal

   ![image](images/ruckus_one/image8.png)
5. Then select 3rd Party Captive Portal as the portal type and click Next

   ![image](images/ruckus_one/image11.png)
6. Configure the portal settings as shown below. Copy the Integration key - it must be added to the Linkyfi later.

   ![image](images/ruckus_one/image14.png)
   ![image](images/ruckus_one/image3.png)
7. Click Add Server to add the RADIUS server settings, as demonstrated below.

   ![image](images/ruckus_one/image10.png)
8. Configure Radius Accounting by clicking Add Server as shown below, then click Apply to save the configuration.

   ![image](images/ruckus_one/image1.png)
9. Log in to your Linkyfi account. Open the Portal Management - Structure and Devices tab. Click + and choose Ruckus One from the expandable list. Add the MAC address of your device and click Save. In the next window add the integration key as API username and API password.

   ![image](images/ruckus_one/image4.png)
10. Go to the User Enrollment - User Journey - Access Settings tab and add the network you created on Ruckus One.

    ![image](images/ruckus_one/image13.png)
    ![image](images/ruckus_one/image5.png)