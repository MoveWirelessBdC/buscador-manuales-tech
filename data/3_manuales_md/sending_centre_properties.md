Sending Centre Properties - Platform documentation






[Skip to content](#sending-centre-properties)

# Sending Centre Properties

The **Sending Centre** Properties allow you to integrate and properly configure the GDPR user panel, and the Email and SMS gateways which are responsible for the correct message dispatch.

This section consists of three tabs: **Active Configurations**, **SMS**, and **Email**. The **Active Configurations** tab is divided into **SMS** and **Email** sections, which are broken by three categories: **GDPR**, **Other**, and **Marketing Campaigns**. In the **SMS** and **Email** tabs, you can create respective configurations according to your preferences. These two tabs also serve as libraries of all configurations which you have created for the SMS and Email dispatch.

## SMS Configuration

To configure these properties you should first prepare configurations which you can then assign to each category. To do this, you can create your own configuration, or use one which you inherit from your parent organisations.

### Creating an SMS Configuration

To begin creating an SMS configuration, you should first ensure that you have a client account on the dedicated Gateway platform. To learn more about configuring gateways, read the **Configuring Gateways** chapter of the User Guide.

1. To create a new SMS configuration, click the **+** button in the bottom right corner of the window.
2. Now, in the SMS settings window:

   * In the **Name** field, type the name of the SMS configuration;
   * From the **Gateway** dropdown list, select the desired gateway. For this instruction, it is *Default*.
     Then, click **Next** in the top right corner to proceed further.

   ![sms properties](images/properties/sms_config_properties_1.png)
3. In the next window:

   * Into the **SMS Gateway URL** field, enter the designated gateway URL;
   * From the **SMS API Encoding** dropdown list, select the desired encoding. For this instruction, it is *UTF-8*.

   Finally, click **Save** in the top right corner to finish creating the configuration.

   ![sms properties](images/properties/sms_config_properties_2.png)
4. The SMS configuration is now created. You should note that your sub-organisations can **inherit** it, and will be able to use it for their own SMS gateway configuration.

   Now, to finish the configuration process, you must assign the newly created configuration to the appropriate Property. To learn how to do this, read the **Active Configurations** section of this chapter.

### Editing an SMS Configuration

To edit the SMS configuration, click the **More** option in the upper right corner of the desired configuration, and select **Edit** from the dropdown menu. Then, edit the setup according to your preferences.

You should note that you can edit only your **Own** configurations. If you would like to edit an **Inherited** configuration, you must first copy it into the **Own** section. To learn how to do this, read the following **Copying a SMS Configuration** section.

![sms properties](images/properties/sms_config_properties_3a.png)

### Copying a SMS Configuration

To copy an existing SMS configuration, click the **More** option in the upper right corner of the desired configuration, and select **Copy** from the dropdown menu. Then, in the **SMS Settings** window, type the name of the copied configuration into the **Name** field. Then, click **Save** in the top right corner to confirm copying the setup.

![sms properties](images/properties/sms_config_properties_3b.png)

![sms properties](images/properties/sms_config_properties_4.png)

### Removing an SMS Configuration

To remove the SMS configuration, click the **More** option in the upper right corner of the desired configuration, and select **Remove** from the dropdown menu. Then, confirm the removal in the pop-up box.

Note: You cannot remove a configuration that is currently in use. To remove it, you must first change the active configuration in the **Active Configurations** tab.

![sms properties](images/properties/sms_config_properties_3c.png)

### Testing an SMS Configuration

To test the SMS configuration, click the **More** option in the upper right corner of the desired configuration, and select **Send Test Message** from the dropdown menu. Then, in the **Send Test Message** pop-up box:

* In the **Phone Number** field, select the appropriate **Dialing Code** and type the phone number to which a test message should be delivered;
* Into the **Message Text** field, enter the text of the test message.

Then, to confirm and send the test message to the designated number, click **Send**.

**Note:** To faultlessly test the configuration, you should ensure that your gateway allows dispatching messages to the designated country. To do this, log in to your Client platform, and check the **geopermission configuration**.

![sms properties](images/properties/sms_config_properties_4a.png)

![sms properties](images/properties/sms_config_properties_5.png)

## Email Configuration

**Note:** To begin creating an Email configuration, you should first ensure that you have a client account on the dedicated Gateway platform. To learn more about configuring gateways, read the **Configuring Gateways** chapter of the User Guide.

1. To create a new Email configuration, click the **+** button in the bottom right corner of the window.
2. Now, in the **Email Settings** window:

   * In the **Name** field, type the name of the Email configuration;
   * From the **Gateway** dropdown list, select the desired gateway. For this instruction, it is *Default*.

   Then, click **Next** in the top right corner to proceed further.

   ![email properties](images/properties/email_config_properties_1.png)
3. In the next window, you should provide the Email configuration details

   * The **Auth Enabled** dropdown list allows you to specify whether the Email Authentication is enabled or not, by selecting *true* (for yes) or *false* (if no);
   * In the **Host Name** field, type the host web address;
   * Into the **Password field**, enter the gateway password;
   * Into the **Port** field, enter the gateway port;
   * In the **Source Mail** field, enter the email address from which the messages will be sent;
   * The **SSL Enabled** dropdown list allows you to specify whether the Email dispatch is secured with the SSL certificate, by selecting *true* (for yes) or *false* (if no);
   * The **TSL Enabled** dropdown list dropdown list allows you to specify whether the Email dispatch is secured with the TSL certificate, by selecting *true* (for yes) or *false* (if no);
   * From the **Transport Protocol** dropdown list, select the protocol by which the emails are dispatched - *SMTP* or *SMTPS*;
   * In the **Username** field, enter the gateway username;
   * In the **Sender Name** field, type the name or text, which will display in the email title.

   After you have finished providing the details, click **Save** in the top right corner to finish creating the configuration.

   ![email properties](images/properties/email_config_properties_2.png)
4. The SMS configuration is now created. You should note that your sub-organisations can **inherit** it, and will be able to use it for their own SMS and Email gateway configuration.

   Now, to finish the configuration process, you must assign the newly created configuration to the appropriate Property. To learn how to do this, read the **Active Configurations** section of this chapter.

### Editing an Email Configuration

To edit the Email configuration, click the **More** option in the upper right corner of the desired configuration, and select **Edit** from the dropdown menu. Then, edit the setup according to your preferences.

![email properties](images/properties/email_config_properties_3.png)

### Removing an Email Configuration

To remove the Email configuration, click the **More** option in the upper right corner of the desired configuration, and select **Remove** from the dropdown menu. Then, confirm the removal in the pop-up box.

Note: You cannot remove a configuration that is currently in use. To remove it, you must first change the active configuration in the **Active Configurations** tab.

![email properties](images/properties/email_config_properties_3c.png)

### Copying an Email Configuration

To copy an existing Email configuration, click the **More** option in the upper right corner of the desired configuration, and select **Copy** from the dropdown menu. Then, in the **Email Settings** window, type the name of the copied configuration into the **Name** field. Then, click **Save** in the top right corner to confirm copying the setup.

![email properties](images/properties/email_config_properties_3b.png)

### Testing an Email Configuration

To test the Email configuration, click the **More** option in the upper right corner of the desired configuration, and select **Send Test Message** from the dropdown menu. Then, in the **Send Test Message** pop-up box:

* In the **Email Address** field, type the email address to which the test message should be delivered;
* In the **Subject** field, type the title of the message;
* Into the **Message Text** field, enter the text of the test message.

Then, To confirm and send a test message to the designated number, click **Send**.

![email properties](images/properties/email_config_properties_3d.png)

![email properties](images/properties/email_config_properties_4.png)

## Active Configurations

When you have finished creating appropriate SMS and/or Email configurations, you can now select and set them up as Active Configurations. To do this, go to the Active configurations tab in the Sending Centre Properties.

The **Active Configurations** tab provides you the summary of configurations activated for your Organisation. It allows you to determine which configurations are used for the GDPR, Marketing campaigns, and Other types of dispatch activities, and change them according to your preferences.

### Selecting a Configuration

Depending on where your location is located in the hierarchy, you may select to either **inherit** the desired configuration, or **Select** your own one.

1. To select a configuration, click the **Pen** icon located on the right of the desired category panel.

   ![active configurations](images/properties/active_config_1.png)
2. In the pop-up box, choose either the **Inherit** or **Select** option from the toggle button:

   * The **Inherit** option allows you to use the configuration of your closest parent organisation.
     **Note:** If this parent organisation changes its configuration, your organisation’s configuration will change as well;
   * The **Select** option enables you to choose from both **Own** and **Inherited** configurations.

   You should note that in both cases your sub-organisations inherit your current setup. They can change it by selecting a different configuration through the **Select** option.

   After you have chosen the desired configuration, click **Save** on the bottom right corner of the pop-up box to confirm your selection.

   ![active configurations](images/properties/active_config_2a.png)

   ![active configurations](images/properties/active_config_3a.png)

   **Note:** If your organisation is a parent organisation, the **Inherit** option stays inactive, and you can only select a configuration from your own set of configurations.

   ![active configurations](images/properties/active_config_4b.png)