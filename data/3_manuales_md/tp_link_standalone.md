TP-Link Standalone - Platform documentation






[Skip to content](#tp-link-standalone-configuration-guide)

# TP-Link Standalone Configuration Guide

To configure a TP-Link Standalone device:

1. Log in to the TP-Link interface with your credentials.

   ![tp-link standalone](images/tp_link_standalone/tp_link_standalone_1.png)
2. Once you have successfully signed in to the device interface, select the **Wireless** section in the top navigation bar and click on the **Portal** tab in the bottom bar.

   Then, in the **Portal Configuration** section:

   * From the **SSID** dropdown list, select the Network for which you would like to enable a captive portal.
   * From the **Authentication Type** dropdown list, select **External RADIUS Server**.
   * Into the **RADIUS Server IP** field, enter the IP address. For this instruction, it is `35.234.150.70`.
   * Into the **RADIUS Port** field, enter the RADIUS port. For this instruction, it is `1812`.
   * Into the **RADIUS Password** field, enter the RADIUS password. For this instruction, it is `bAZev44u`.
   * For the **RADIUS Accounting** option, select the **Enable** checkbox.
   * Into the **Accounting Server IP** field, enter the IP address. For this instruction, it is `35.234.150.70`.
   * Into the **Accounting Server Port** field, enter the server port. For this instruction, it is `1813`.
   * Into the **Accounting Server Password** field, enter the password. For this instruction, it is `bAZev44u`.
   * For the **Interim Update** option, select the **Enable** checkbox.
   * Into the **Interim Interval** field, enter the desired number of seconds. For this instruction, it is `600`.
   * From the **Authentication Timeout** dropdown list, select the desired number of hours. For this instruction, it is `1 hour`.
   * For the **Redirect** option, select the **Enable** checkbox.
   * Into the **Redirect URL** field, enter the desired URL address. For this instruction, it is `http://35.324.150.70/welcome`.
   * From the **Portal Customization** dropdown list, select **External Web Portal**.
   * Into the **External Web Portal URL** field, enter the desired external URL address. For this instruction, it is `http://35.324.150.70/login`.

   Then, click the **Save** button at the bottom left to save the configuration.

   ![tp-link standalone](images/tp_link_standalone/tp_link_standalone_2.png)
3. Now, scroll to the **Free Authentication Policy** section and click on the blue **Add** button at the top right of the section.

   Then, provide the specifics of the Policy:

   * Into the **Policy Name** field, enter `External Web Portal Allowed`.
   * Into the **Destination IP Range** field, enter the IP address. For this instruction, it is `35.234.150.70/32`.
   * For the **Status** option, select the **Enable** checkbox.

   Then, click **OK** at the bottom left to save the configuration.

   ![tp-link standalone](images/tp_link_standalone/tp_link_standalone_3.png)

Important

Once the access point is configured, provide your Administrator with the device's MAC address and Network details to allow them to set it up on the Platform server.