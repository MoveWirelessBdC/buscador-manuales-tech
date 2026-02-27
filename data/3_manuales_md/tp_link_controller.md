TP-Link Omada Controller - Platform documentation






[Skip to content](#tp-link-omada-controller-configuration-guide)

# TP-Link Omada Controller Configuration Guide

To configure the TP-Link Omada Controller access point you should set it up with an Open WiFi network.

1. To begin the configuration process, log in to the TP-Link Omada controller interface with your credentials.

   ![tp-link controller](images/tp_link_controller/tp_link_controller_1.png)
2. When you have successfully logged in to the device interface, go to the **Authentication > Portal** option.

   Then, in the Portal configuration window:

   * For the **Portal** option, turn the switch **ON**.
   * In the **Basic Info** section:
     + From the **SSID & Network** dropdown list, select the desired network.
     + From the **Authentication Type** dropdown list, select **External RADIUS Server**.
     + From the **Authentication Timeout** dropdown list, select the desired time interval. For this instruction, it is `8 hours`.
     + From the **RADIUS Profile** dropdown list, select an already existing RADIUS Profile or create a new one (see step 3).

   ![tp-link controller](images/tp_link_controller/tp_link_controller_2.png)
3. To create a new RADIUS Profile, click the blue **Manage RADIUS Profile** link. Then, in the **Create New RADIUS Profile** section:

   * Into the **Name** field, enter the name of the RADIUS profile.
   * Into the **Authentication Server IP** field, enter the server’s IP address. For this instruction, it is `35.234.150.70`.
   * Into the **Authentication Port** field, enter the server’s port. For this instruction, it is `1812`.
   * In the **Authentication Password** field, type the server’s password. For this instruction, it is `bAZev44u`.
   * For the **RADIUS Accounting** option, select the **Enable** checkbox.
   * For the **Interim Update** option, select the **Enable** checkbox.
   * Into the **Interim Update Interval** field, enter the desired number of seconds. For this instruction, it is `600`.
   * Into the **Accounting Server IP** field, enter the server’s IP. For this instruction, it is `35.234.150.70`.
   * Into the **Accounting Port** field, enter the server’s port. For this instruction, it is `1813`.
   * In the **Accounting Password** field, type the server’s password. For this instruction, it is `bAZev44u`.

   Then, click the **Confirm** button at the bottom left to save the new RADIUS Profile.

   ![tp-link controller](images/tp_link_controller/tp_link_controller_3.png)
4. Next, scroll down to set up authentication options and access control:

   * For the **Authentication Mode** option, select **PAP**.
   * For the **Portal Customization** option, select **External Web Portal** and enter the portal’s URL address. For this instruction, it is `http://35.234.150.70/login`.
   * For the **HTTPS Redirection** option, select the **Enable** checkbox.
   * For the **Landing Page** option, select **The Promotional URL** and enter the URL address. For this instruction, it is `http://35.234.150.70/welcome`.

   ![tp-link controller](images/tp_link_controller/tp_link_controller_4.png)

   In the **Access Control** section, for the **Pre-Authentication Access List**, select the **Enable** checkbox.

   Then, manage the **Pre-Authentication Access List** by adding or removing the desired entries.

   ![tp-link controller](images/tp_link_controller/tp_link_controller_5.png)

Important

Once the access point is configured, provide your Administrator with the device's MAC address and Network details to allow them to set it up on the Platform server.