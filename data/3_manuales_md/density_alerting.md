Density Alerting - Platform documentation






[Skip to content](#density-alerting)

# Density Alerting

The **Density Alerting** tool allows you to define limitations to the number of customers at your venue and set SMS, email, or endpoint notifications when those limits are exceeded.

**Note:** To configure the Density Alerting, you should first make sure that in the selected Organisation, you have created a Venue, and it is set to the **Location** mode.

## Creating a Density Alert

1. Go to the **Location Management > Density Alerting** section, and click the **+** button in the bottom right corner.

   ![calibration delete](images/density_alerting/density_alerting_1.png)
2. In the first step, from the toggle button, select the type of space for which you would like to create an alert. It can be either a whole **Venue** or its designated **Area**. Then, click **Next** in the top right corner to proceed further.

   **Note:** To create an alert for a specified Area, you must first define Areas at your Venue.

   ![calibration delete](images/density_alerting/density_alerting_2.png)
3. In the second step, type the name of the Alert Set into the **Alert Set Name** field. Then, add the density limit by clicking the **Add Density Limit** button.

   ![calibration delete](images/density_alerting/density_alerting_3.png)
4. Now, in the pop-up box:

   * In the **Alert Name** field, enter the name of the density limit
   * From the **Areas** selectors, choose areas where you would like to set up a density limit: **All** areas, a **Single** one, or **Multiple** ones. For this instruction, it is *Single Area*.
   * If you select the **Single Area** or the **Multiple Areas** option, then from the **Select Area** dropdown list, choose the desired areas
   * From the toggle button, select the desired option to specify the **size of the surface per customer** or the the **number of customers per area**. For this instruction, it is the *Customer Per Area* option.

   Then, click the **Add Limit** button in the bottom right corner of the pop-up box to finish adding a limit to the Alert Set.

   ![calibration delete](images/density_alerting/density_alerting_4.png)
5. The Density Limit is now added. You can add another one by repeating steps 3-4.

   When you have added all the desired limits, click **Next** in the top right corner to continue to the following step.

   ![calibration delete](images/density_alerting/density_alerting_5.png)
6. In the next step, from the **Notification Type** toggle button, select the type of notification that you would like to receive. It can be **SMS**, **Email**, or **Endpoint**.

   #### The SMS Notification

   In the SMS Notification:

   * Enter the content of the notification into the **Notification Content** field
   * Select the country code and type the phone number in the **Phone Number** field.

   Then, click **Next** in the top right corner to proceed to the last step.

   ![calibration delete](images/density_alerting/density_alerting_6.png)

   #### The Email Notification

   In the Email Notification:

   * Enter the content of the notification into the **Notification Content** field
   * Type the subject of the email in the **Subject** field
   * Enter the desired email address into the **Email Address** field

   Then, click **Save** in the top right corner to finish setting up Geofencing.

   ![calibration delete](images/density_alerting/density_alerting_6c.png)

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
   Request body: [$area]: Customer limit exceeded*

   ![calibration delete](images/density_alerting/density_alerting_6b.png)
7. Now, you can review the Density Alert setup. To finish its configuration, click **Save** in the top right corner.

   ![calibration delete](images/density_alerting/density_alerting_7.png)
8. The Density Alert is now added.

   ![calibration delete](images/density_alerting/density_alerting_8.png)

## Editing a Density Alert

To edit the Density Alert, click the **More** option in the top right corner of the desired Alert, and select **Edit** from the dropdown menu. Then, make the desired changes and finish modifying it by clicking **Save** in the Density Alert Editor.

![calibration delete](images/density_alerting/density_alerting_9.png)

## Deleting a Density Alert

To delete the Density Alert, click the **More** option in the top right corner of the desired Alert, and select **Delete** from the dropdown menu. Then, confirm deleting the Alert in the pop-up box.

![calibration delete](images/density_alerting/density_alerting_10.png)