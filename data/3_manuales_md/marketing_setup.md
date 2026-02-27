Marketing Campaign Setup - Platform documentation






[Skip to content](#marketing-campaign-setup)

# Marketing Campaign Setup

## Organisation settings

#### 1. Firstly you should make sure that your organisation is **Data Administrator** and your **Email/SMS** sending configuration is **admin**.

* Go to: **Portal Management** > **Structure** > **Organisation** and Select additional settings. ( 3 vertical dots on the left of the organisation name).
  ![marketing](images/mark_info/mark_info_0.png)

#### 2. Create SMS Configuration:

To create SMS configuration go to: **Portal Management** > **Sending centre** > **Sending Configuration** > **SMS** tab.
![marketing](images/mark_info/mark_info_87.png)
**Note**: To begin creating an **SMS configuration**, you should first ensure that you have a client account on the dedicated **Gateway** platform.

* To create a new **SMS configuration**, click the **+** button in the bottom right corner of the window.
  ![marketing](images/mark_info/mark_info_88.png)
* Now, in the **SMS** settings window:
* In the **Name** field, type the name of the **SMS** configuration;
* From the **Gateway** dropdown list, select the desired gateway. For this instruction, it is Default. Then, click **Next** in the top right corner to proceed further.
  ![marketing](images/mark_info/mark_info_3.png)
* In the next window:
* Into the **SMS Gateway URL** field, enter the designated gateway URL;
* From the **SMS API Encoding** dropdown list, select the desired encoding. For this instruction, it is UTF-8.

Finally, click **Save** in the top right corner to finish creating the configuration.
![marketing](images/mark_info/mark_info_4.png)

* The SMS configuration is now created. You should note that your sub-organisations can inherit it, and will be able to use it for their own SMS gateway configuration.
* Now, to finish the configuration process, you must assign the newly created configuration to the appropriate Property. To learn how to do this, read the Active Configurations section of this chapter.

#### 3. Create Email Configuration

* Go to: **Portal Management** > **Sending centre** > **Sending Configuration** > **Email** tab.
  ![marketing](images/mark_info/mark_info_89.png)

**Note**: To begin creating an Email configuration, you should first ensure that you have a client account on the dedicated Gateway platform.

* To create a new Email configuration, click the **+** button in the bottom right corner of the window.
* Now, in the **Email Settings** window:
* In the **Name** field, type the name of the Email configuration;
* From the **Gateway** dropdown list, select the desired gateway. For this instruction, it is Default.
* Then, click **Next** in the top right corner to proceed further.
  ![marketing](images/mark_info/mark_info_5.png)
* In the next window, you should provide the Email configuration details
* The **Auth Enabled** dropdown list allows you to specify whether the Email Authentication is enabled or not, by selecting true (for yes) or false (if no);
* In the **Host Name** field, type the host web address;
* Into the **Password field**, enter the gateway password;
* Into the **Port** field, enter the gateway port;
* In the **Source Mail** field, enter the email address from which the messages will be sent;
* The **SSL Enabled** dropdown list allows you to specify whether the Email dispatch is secured with the SSL certificate, by selecting true (for yes) or false (if no);
* The **TSL Enabled** dropdown list allows you to specify whether the Email dispatch is secured with the TSL certificate, by selecting true (for yes) or false (if no);
* From the **Transport Protocol** dropdown list, select the protocol by which the emails are dispatched - SMTP or SMTPS;
* In the **Username** field, enter the gateway username;
* In the **Sender Name** field, type the name or text, which will display in the email title.

After you have finished providing the details, click **Save** in the top right corner to finish creating the configuration.

* The **SMS** configuration is now created. You should note that your sub-organisations can **inherit** it, and will be able to use it for their own **SMS** and **Email** gateway configuration.

Now, to finish the configuration process, you must assign the newly created configuration to the appropriate Property.

#### 4. Select Active configuration

* Go to: **Portal Management** > **Sending centre** > **Sending Configuration** > **ACTIVE CONFIGURATION** tab.
  ![marketing](images/mark_info/mark_info_90.png)
* Select appropriate SMS and/or Email configurations, and set them up for Marketing Campaigns as Active Configurations.
  ![marketing](images/mark_info/mark_info_91.png)
  ![marketing](images/mark_info/mark_info_9.png)

## User Agreements

### 1. Create Marketing Category

* Go to the **User Enrollment** → **User Agreements** section and select the **Marketing Categories** option.
  ![marketing](images/mark_info/mark_info_10.png)
* In the bottom right corner, click the **+** button.
  ![marketing](images/mark_info/mark_info_11.png)
* In the first step:

  + Type the Marketing Category’s name into the **Marketing Category name** field
  + From the **Offer frequency** dropdown list, select how often the document should be displayed to the users. For this instruction, it is *Once*.
* **Note**: only when users give their consent to receive offers, can these offers be sent to them.
* After you have finished providing these details, click **Next** in the top right corner of the window.
  ![marketing](images/mark_info/mark_info_12.png)
* In the following step, compose the text of the **Marketing Category**.
  ![marketing](images/mark_info/mark_info_13.png)
* In the last step, you can review the summary of selected settings and preview the Marketing Category by clicking the **Preview Marketing Category** button.
  ![marketing](images/mark_info/mark_info_14.png)
  ![marketing](images/mark_info/mark_info_15.png)
* The document has now been created as a **Draft**.
  ![marketing](images/mark_info/mark_info_16.png)
* **All User Agreement** documents including **Marketing Categories** are initially created as **Drafts**. Before they can be added to the Portal, they must be **published**.

#### Publishing a Marketing Category

* Go to the **User Enrollment** → **User Agreements** → **Marketing Categories** section and select the document which you would like to publish.
* In the selected **Marketing Category** panel, click the **More** option and select **Publish** from the dropdown menu. Then, confirm publishing the Document in the pop-up box.
  ![marketing](images/mark_info/mark_info_17.png)
* The Document’s status has now been changed to **Published**.
  ![marketing](images/mark_info/mark_info_18.png)

### 2. Create a Communication Channel

The **Communication Channels** function allows you to ask users about their preferred method of receiving marketing offers.

* Go to the **User Enrollment** → **User Agreements** section and select the **Communication Channels** option.
  ![marketing](images/mark_info/mark_info_19.png)
* In the bottom right corner of the window, click the **+** button to add a new Communication Channel.
  ![marketing](images/mark_info/mark_info_20.png)
* In the first step:
* Type the Communication Channel name in the **Communication Channel name** field
* (Optional) Allow users to edit the initially chosen preferences in their GDPR panel by turning the **Allow Users** to **Edit** switch **ON**
* Then, click **Next** to proceed.
  ![marketing](images/mark_info/mark_info_21.png)
* In the following step:
* Composing both the **Consent** and the **Selection** texts the **Selection Text** appears at the top of the list of Communication Channels available for selection. Then, click **Next** to continue.
  ![marketing](images/mark_info/mark_info_22.png)
* Now, select Communication Channels which you would like to offer to users for selection. You can choose the predefined ones by selecting the **Predefined** option from the toggle button, or select the **Custom** option to add additional ones.
  To remove options, click the **Bin** button next to the desired channel. You can also specify the default status of these methods to **selected by default** by turning the switches **ON** and **OFF**.
  ![marketing](images/mark_info/mark_info_23.png)
* In the last step, you can review the summary of selected settings and preview the Communication Channels by clicking the **Preview Communication Channel** button.
  ![marketing](images/mark_info/mark_info_24.png)
  ![marketing](images/mark_info/mark_info_25.png)
* The document has now been created as a **Draft**.
  ![marketing](images/mark_info/mark_info_26.png)

#### Publishing Communication Channels

* Go to the **User Enrollment** → **User Agreements** → **Communication Channels** section and select the document which you would like to publish.
* In the selected Communication Channels panel, click the **More** option and select **Publish** from the dropdown menu. Then, confirm publishing the Document in the pop-up box.
  ![marketing](images/mark_info/mark_info_27.png)
* The Document’s status has now been changed to **Published**.
  ![marketing](images/mark_info/mark_info_28.png)

## User Journey

#### 1. Create Captive Portal with Marketing Categories and Communication Channels

* Go to the **User Enrollment** → **User Journey** section and click the **Portal** option.
  ![marketing](images/mark_info/mark_info_29.png)
* On the **Portal Manager** page, click **+** to create a new Portal in the bottom right corner.
  ![marketing](images/mark_info/mark_info_30.png)
* Type the name of the Portal and select its language. In the upper right corner, click **Next** to confirm your selection.
  ![marketing](images/mark_info/mark_info_31.png)
* On the **Portal Editor** page select the **Basics** option from the menu on the left.
  ![marketing](images/mark_info/mark_info_32.png)
* Now, drag the **Marketing Categories** tile to the Portal workspace and drop it inside.
  ![marketing](images/mark_info/mark_info_33.png)
* In the menu on the left, select the needed document from the dropdown list and click **+**
  ![marketing](images/mark_info/mark_info_34.png)
  ![marketing](images/mark_info/mark_info_35.png)
  ![marketing](images/mark_info/mark_info_37.png)
* The selected document now appears in the workspace.
  ![marketing](images/mark_info/mark_info_38.png)
* You can add more than one document with marketing categories
  ![marketing](images/mark_info/mark_info_39.png)
* Now click **+** to add a new component in the bottom right corner.
  ![marketing](images/mark_info/mark_info_40.png)
* Select again the **Basics** option from the menu on the left and drag the **Communication channels** tile to the Portal workspace and drop it inside.
  ![marketing](images/mark_info/mark_info_41.png)
* In the menu on the left, select the needed document from the dropdown list
  ![marketing](images/mark_info/mark_info_42.png)
  ![marketing](images/mark_info/mark_info_43.png)
* The selected document now appears in the workspace.
  ![marketing](images/mark_info/mark_info_44.png)
* In the upper right corner, click **Save** to confirm your design changes.
  ![marketing](images/mark_info/mark_info_45.png)
* Before saving, you can preview the **Portal** for both web and mobile versions. To do this, click **Next** in the upper right corner of the page. If you would like to skip this step, click **Skip and Save** in the upper right corner.
  ![marketing](images/mark_info/mark_info_47.png)

#### 2. Create a Captive Portal with the appropriate login method.

Messages from marketing campaigns are sent only to people who have shared their Email and / or phone number via the login path.
It is imperative to create a **Captive Portal** with such a login method which will allow the collection of this data.

#### You can use these login methods:

* **Login** > **Form** - A questionnaire about Email, Phone number (possibly about Date of birth or Gender for narrowing the target group at a later time).
  ![marketing](images/mark_info/mark_info_48.png)
  ![marketing](images/mark_info/mark_info_49.png)
* **Login** > **Email**
  ![marketing](images/mark_info/mark_info_50.png)
  ![marketing](images/mark_info/mark_info_51.png)
* **Login** > **User registration**
  ![marketing](images/mark_info/mark_info_52.png)
  ![marketing](images/mark_info/mark_info_53.png)
* **Multi step login** > **Phone number verification**
  ![marketing](images/mark_info/mark_info_54.png)
  ![marketing](images/mark_info/mark_info_55.png)

#### 3. Create Page Flow with previously created Captive Portals and Internet access.

* Go to the **User Enrollment** → **User Journey** section and click the **Page flow** option.
  ![marketing](images/mark_info/mark_info_56.png)
* In the **Page Flow Manager**, click **+** in the bottom right corner.
  ![marketing](images/mark_info/mark_info_57png.png)
* In the **Settings** panel, type the Flow name. In the top right corner, click **Next**.
  ![marketing](images/mark_info/mark_info_58.png)
* In the **Page Flow Editor**, click **+** to create the first node. Then, from the list, select the **Portal** option.
  ![marketing](images/mark_info/mark_info_59.png)
* On the **Portals Available** page, select the Portal with login method that you created earlier. In the upper right corner, click **Select** to confirm your choice.
  ![marketing](images/mark_info/mark_info_60.png)
* Portal has been added.
  ![marketing](images/mark_info/mark_info_61.png)
* Add another portal to the login path - with **Marketing Categories** and **Communication Channels**.
  ![marketing](images/mark_info/mark_info_62.png)
  ![marketing](images/mark_info/mark_info_63.png)
* Another portal has been added.
  ![marketing](images/mark_info/mark_info_64.png)
* Add Internet Access node to login path.
  ![marketing](images/mark_info/mark_info_65.png)
* On the **Network Parameters** page, configure the network settings. To confirm changes, click **Save** in the upper right corner.
  ![marketing](images/mark_info/mark_info_66.png)
* Finish creating the login path and click **Save**.
  ![marketing](images/mark_info/mark_info_67.png)

#### 4. Attach the created Page Flow to the network that you share with your clients to log into Wi-Fi.

* Go to the **User Enrollment** → **User Journey** section and select the **Access Settings** option.
  ![marketing](images/mark_info/mark_info_68.png)
* In the **Network Manager**, click the **More** option. Then, from the dropdown list, select **Attach Flow**.
  ![marketing](images/mark_info/mark_info_69.png)
  ![marketing](images/mark_info/mark_info_70.png)
* On the **Page Flows Available** page, select the Page Flow you just created. In the upper right corner, click **Select** to confirm.
  ![marketing](images/mark_info/mark_info_71.png)
* The **Page Flow** is now published.
  ![marketing](images/mark_info/mark_info_72.png)
* After your customers log into the network and share their contact details you can create a **Marketing Campaign**.

## Marketing campaign

1. Go to the **Marketing** > **Campaigns section**, and click **+** in the bottom right corner to create a new campaign .
   ![marketing](images/mark_info/mark_info_73.png)
2. Select the desired type of campaign by clicking on the appropriate tile. Then, follow the configuration steps in the **Campaign Editor**.
   **Note**: One-shot campaign is the basic available type of campaign.
   ![marketing](images/mark_info/mark_info_74.png)
3. In the **Campaign Overview** step, type the name of the campaign in the Name field, and enter the campaign **description** into the Description field. (The description is not displayed to end-users).
   ![marketing](images/mark_info/mark_info_75.png)
4. In the **Target Group** step, select the desired target group by clicking on the appropriate tile. If you have no target group yet, you can create a new one or select the existing one from the default section.

**Note**: If data about gender and age were collected in the login process, you can choose a narrowed target group, and if not - select ALL.
![marketing](images/mark_info/mark_info_76.png)

1. In the **Marketing Categories** step, you can choose the marketing categories by which the selected group should be targeted.
   ![marketing](images/mark_info/mark_info_77.png)

   * Messages will be sent to users who agreed to these categories while logging in.
   * You can also choose the SKIP option and then will be sent regardless of the consent.
2. In the **Contact Methods** step, you can choose the contact methods to reach your users.
3. Messages will be sent to users who, by going through the login path, agreed to be contacted by Email or SMS.

By default, both SMS and email are selected. To deactivate a contact method, turn the switch next to it **OFF**.

Next, determine the number of users to whom you would like to send the message in the **Number of SMS** and/or **Number of Emails** fields.

**Tip**: The contact method at the top of the list is the primary one. You can manage the priority of these methods by dragging and dropping them according to your preferences.

* If the Only verified addresses checkbox is marked, messages will be sent only to the confirmed Email addresses/phone numbers, if the checkbox is left unmarked, messages will be sent to ALL users.
* **Note**: The Email addresses/phone numbers collected through the questionnaire are unconfirmed.
  ![marketing](images/mark_info/mark_info_78.png)
* In the **Message** step, you can compose the message which you would like to send to your users. Depending on your selection in the previous step, this may be an SMS, an email, or both. Type the text in the **Message Content** field.
  ![marketing](images/mark_info/mark_info_79.png)
  ![marketing](images/mark_info/mark_info_80.png)
  ![marketing](images/mark_info/mark_info_81.png)
  **NOTE**: It is possible to send a test Email or SMS during the message creating process.
* In the **Delivery Schedule** step, set the campaign delivery details - date and time.
  ![marketing](images/mark_info/mark_info_82.png)
* In the **Summary** step, you can review the campaign details. To finish the configuration process and schedule the campaign, click **Send Campaign** in the top right corner.
  ![marketing](images/mark_info/mark_info_83.png)
* The campaign is now set to be dispatched at the designated time.
  ![marketing](images/mark_info/mark_info_84.png)

**IMPORTANT**: Make sure that **before** sending the campaign to **real** customers, it is **checked** on the test database of Emails / phone numbers.

After the campaign is completed, you can view its results by clicking **Check results**.
![marketing](images/mark_info/mark_info_85.png)