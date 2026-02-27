Managing a Licence - Platform documentation






[Skip to content](#managing-a-licence)

# Managing a Licence

A **Licence** is a set of Licences which you can assign to your Client. They can only be derived from Licence Packages. So to create a Licence, you must first have a Licence Package assigned to you for distribution.

To learn how to create a Licence Package, read the [Managing a Licence Package](licence_package.html) chapter.

## Creating a Licence

1. Go to the **Licences and Roles** section in the main menu and select the **Licence Manager** tile.

   ![sublicence](images/licences/licence_package_0.png)
2. First, you should ensure to have switched the current Organisation to the Sub-Organisation for which you would like to derive a Licence, or create a new Sub-Organisation.

   To switch the Organisations, select the desired Sub-Organisation from the Organisation tree on the right. To learn how to create a new Sub-Organisation, read the [Creating, Editing and Removing an Organisation](adding_an_organisation.html) chapter.

   When you have switched to the desired Sub-Organisation, click **+** in the bottom right corner to create a Licence.

   ![sublicence](images/licences/sublicence_1.png)
3. In the **Basic Selection** preliminary step,

   * Select the **Licence** option from the toggle button
   * From the **Licence Package** list, select the Licence Package from which you would like to derive a Licence.

   Then, click **Next** in the top right corner to continue.

   Note

   A Licence can only be derived from Licence Packages. So to create a Licence, you must first have a Licence Package assigned to you for distribution. To learn how to create a Licence Package, read the [Managing a Licence Package](licence_package.html) chapter.

   ![sublicence](images/licences/sublicence_2.png)
4. In the first step of the Licence Creator, you can set up general settings of the Licence:

   * In the **Licence Order Number** field, type the order number of the Licence
   * In the **Plan** section, choose the Licence Plan. Plans are sets of permissions that determine the scope of access to the Platform features.
   * In the **Description** field, add the description of the Licence (optional).

   Then, click **Next** in the top right corner to proceed.

   ![sublicence](images/licences/sublicence_3.png)
5. The **Limits** step allows you to set limitations to the Licence:

   * In the **Validity Time** date picker, specify the Licence validity time.

   Note

   You can set the future date in the date picker to schedule activating a Licence Package.

   * From the **AP Capacity** toggle button, select the desired AP capacity configuration:
     + The **Specified** option allows you to determine the total number of APs that you would like to allocate to this Licence;
     + The **None** option allows you not to set any AP capacity for the Licence.
     + The **Inherited** option allows you to inherit the AP capacity setup from your parent Organisation.
   * From the **Data Transfer** toggle button, select the desired configuration of the Data Transfer limit:
     + The **None** option allows you not to set up data transfer limits to the Licence.
     + The **Inherited** option enables you to inherit the data transfer setup from your parent Organisation.

   Then, click **Next** in the top right corner to proceed further.

   ![sublicence](images/licences/sublicence_4.png)
6. In the **Client** step, you can designate the Client who would be assigned this Licence and receive email notifications on its activity, such as licence updates on creation, modifying, and deleting, derived licences, status change and licence validity.

   To do this, choose an already existing Platform User from the **Client** dropdown list, or add an external user by providing their email address in the **Email** field. To finish adding a user or an email address to the list, click the **+** icon next to the **Client** and **Email** fields.

   You can also manage notifications which those users should receive by turning the **Notify About Licence Creation** and **Notify When Licences Expire** switches **ON** and **OFF**.

   Then, click **Next** in the top right corner to continue.

   ![sublicence](images/licences/sublicence_5.png)
7. In the **Representative** step, you can appoint users responsible for contact with the Client.

   To do this, choose an already existing Platform User from the **Representative** dropdown list, or add an external user by providing their email address in the **Email** field. To finish adding a user or an email address, click the **+** icon next to the fields.

   You can also manage notifications which those users should receive by turning the **Notify When Licences Expire** switch **ON** and **OFF**.

   Then, click **Next** in the top right corner to proceed further.

   ![sublicence](images/licences/sublicence_6.png)
8. In the **Summary** step, you can review all the Licence's setup. To modify it, click the **<** icon in the top left corner to go back to the desired step.

   To finish creating the Licence, click **Save** in the top right corner.

   ![sublicence](images/licences/sublicence_7.png)
9. The Licence has now been created.

   In the **Licences** section, you can preview all Licences created for your Clients, and in the **Licence Packages** area, you can preview Licence Packages which you have been assigned.

   Depending on the setup, Licence panels may consist of up to three progress bars which indicate the latest status of **Licence validity**, **AP capacity**, and **Data transfer**, respectively.

   You can also view the Licence history by clicking the **Show Notifications** bell icon in the upper right corner of the panel.

   ![sublicence](images/licences/sublicence_8.png)

   ![sublicence](images/licences/sublicence_10.png)

   For full Licence details, click the **More** option in the top right corner of the desired Licence panel, and select **Show Details** from the dropdown list.

   ![sublicence](images/licences/sublicence_9.png)

   The Licence panel also allows you to control notifications for both Clients and the Representatives. To manage them, click the **More** option, and from the dropdown menu, select **Notification Settings**. Then, in the popup-box, specify the setup according to your preferences.

   To save the notification setup, click **Save** in the bottom right corner of the popup-box.

   ![sublicence](images/licences/sublicence_11.png)

   ![sublicence](images/licences/sublicence_12.png)

## Editing a Licence

To make additional changes to a Licence, such as extending the AP capacity or changing the validity time, you should contact your Representative.

## Deleting a Licence

To delete a Licence, click the **More** option in the top right corner of the desired Licence panel, and select **Delete** from the dropdown menu. You will then be asked to enter the Licence ID in the pop-up box to confirm deleting it.

Note

Deleting an active Licence may impact all services that it provides and they may stop working.