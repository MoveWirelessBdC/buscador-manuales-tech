Geofencing - Platform documentation






[Skip to content](#geofencing)

# Geofencing

The **Geofencing** tool allows you to set SMS, email, or endpoint notifications when users enter and exit specified areas at your venue.

## Configuring Geofencing

1. Go to the **Location Management > Geofencing** section, and click the **+** button in the bottom right corner.

   ![geofencing](images/geofencing/geofencing_1.png)
2. In the new window:

   * In the **Name** field, type the name of the Geofencing configuration
   * From the **Triggering Events** toggle button, select on what actions should you receive notifications. You can choose **All**, **Enters** or **Exits**. For this instruction, it is *Enters*.
   * From the **Devices Triggered** list, choose the type of devices you would like to be notified about: **All**, **Named**, or **Selected**.  
     **Note:**  
     **Named** devices are the devices that have been given custom names by their users, for example, *My device* instead of MAC number.  
     **Selected** devices are those that you choose from the dropdown list.
   * From the **Areas** list select areas which you would like to get notified on.

   Then, click **Next** to proceed with the setup.

   ![geofencing](images/geofencing/geofencing_2.png)
3. In the next step, from the **Notification Type** toggle button, select the type of notification that you would like to receive. It can be **SMS**, **Email**, or **Endpoint**.

   #### The SMS Notification

   In the SMS Notification:

   * Enter the content of the notification into the **Notification Content** field
   * Select the country code and type the phone number in the **Phone Number** field.

   Then, click **Next** in the top right corner to proceed to the last step.

   ![geofencing](images/geofencing/geofencing_3b.png)

   #### The Email Notification

   In the Email Notification:

   * Enter the content of the notification into the **Notification Content** field
   * Type the subject of the email in the **Subject** field
   * Enter the desired email address into the **Email Address** field

   Then, click **Save** in the top right corner to finish setting up Geofencing.

   ![geofencing](images/geofencing/geofencing_3a.png)

   #### The Endpoint Notification

   Instead of an SMS or Email notification, the Platform server can send an HTTP request (POST request) to the specified Endpoint of a different server.

   To configure it:

   * Select \*\* Endpoint\*\* from the Notification type toggle button
   * Type the content of notification in the **Notification Content** field. For this instruction, it is *[$area]: Customer limit exceeded*
   * Into the **API URL** field, enter the end URL to which the notification should be sent. For this instruction, it is *<https://mycompany.com/notifications>* .
   * In the **Authorisation Token** field, enter the token, which authorises the communication between servers. For this instruction, it is *abcd1234*

   As a result, you would receive the below request:

   *HTTP POST  
   URL <https://mycompany.com/notifications>  
   Headers:  
   Authorization: abcd1234   
   Request body:User: $user entered area: $area*

   ![geofencing](images/geofencing/geofencing_3c.png)
4. The Geofencing is now set up.

   ![geofencing](images/geofencing/geofencing_4.png)

## Editing a Geofencing Configuration

To edit the Geofencing configuration, click the **More** option in the top right corner of the desired configuration, and select **Edit** from the dropdown menu. Then, make the desired changes and finish modifying it by clicking **Save** in the Geofencing Editor.

![geofencing](images/geofencing/geofencing_5.png)

## Deleting a Geofencing Configuration

To delete the Geofencing configuration, click the **More** option in the top right corner of the desired Geofencing configuration, and select **Delete** from the dropdown menu. Then, confirm deleting the configuration in the pop-up box.

![geofencing](images/geofencing/geofencing_6.png)