Panic Button - Platform documentation






[Skip to content](#panic-button)

# Panic Button

The **Panic Button** feature allows you to connect the Platform with alerting devices used in emergencies, and notify the designated recipients when those devices are activated.

## Creating a Panic Button

1. Go to the **Location Management > Panic Button** section, and click the **+** button in the bottom right corner.

   ![panic button](images/panic_button/panic_button_1.png)
2. In the next window:

   * In the **Name** field, type the name of the alerting setup
   * From the **Notification Type** toggle button, select the way the alert should be delivered: by **SMS**, **Email**, or **Endpoint**

   #### The SMS Notification

   In the SMS Notification:

   * Into the **Notification Content** field, enter the content of the notification  
     **Note:** You can use the dedicated tags to customise the message
   * In the **Phone Number** field, select the appropriate country code and enter the phone number that should receive those notifications

   Then, click **Save** to finish creating the Panic Button.

   ![panic button](images/panic_button/panic_button_2.png)

   #### The Email Notification

   In the Email Notification:

   * Enter the content of the notification into the **Notification Content** field
   * Type the subject of the email in the **Subject** field
   * Enter the desired email address into the **Email Address** field

   Then, click **Save** in the top right corner to finish creating the Panic Button.

   ![panic button](images/panic_button/panic_button_2b.png)

   #### The Endpoint Notification

   Instead of an SMS or Email notification, the Platform server can send an HTTP request (POST request) to the specified Endpoint of a different server.

   To configure it:

   * Select **Endpoint** from the Notification type toggle button
   * Type the content of notification in the **Notification Content** field. For this instruction, it is *[$area]: Customer limit exceeded*
   * Into the **API URL** field, enter the end URL to which the notification should be sent. For this instruction, it is *<https://mycompany.com/notifications>* .
   * In the **Authorisation Token** field, enter the token, which authorises the communication between servers. For this instruction, it is *abcd1234*

   As a result, you would receive the below request:

   *HTTP POST  
   URL <https://mycompany.com/notifications>  
   Headers:  
   Authorization: abcd1234  
   Request body: User: $user clicked the panic button in area: $area*

   ![panic button](images/panic_button/panic_button_2c.png)
3. The Panic Button is now created.

   ![panic button](images/panic_button/panic_button_3.png)

## Editing a Panic Button

To edit the Panic Button, click the **More** option in the top right corner of the desired Button, and select **Edit** from the dropdown menu. Then, make the desired changes and finish modifying it by clicking **Save** in the Panic Button Editor.

![panic button](images/panic_button/panic_button_4.png)

## Deleting a Panic Button

To delete the Panic Button, click the **More** option in the top right corner of the desired Button, and select **Delete** from the dropdown menu. Then, confirm deleting the Button in the pop-up box.

![panic button](images/panic_button/panic_button_5.png)