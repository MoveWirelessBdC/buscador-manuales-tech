Managing a Licence Package - Platform documentation






[Skip to content](#managing-a-licence-package)

# Managing a Licence Package

A **License Package** is a set of Licenses that you can distribute among your clients.

## Creating a Licence Package

1. Go to the **Licences and Roles** section in the main menu, and select the **Licence Manager** tile. Then, in the bottom right corner, click **+** to create a new Licence Package.

   ![licence package](images/licences/licence_package_0.png)

   ![licence package](images/licences/licence_package_1.png)
2. In the **Basic Selection** step, you can choose what kind of Licences you would like to create: a **Licence Package**, or a **Licence**.

   Note

   It is not possible to create Licences if your Organisation has no Licence Packages.

   ![licence package](images/licences/licence_package_2.png)
3. In the first step of the Licence Package Creator, you can set up general settings of the Licence Package:

   * From the **Select Type** toggle button, select the type of the Licence Package that you would like to create: **Commercial**, or **Test**.  
     The **Commercial** type enables you to launch a new Licence Package available for a Client; the **Test** option can be used to create a Licence Package for tests (e.g. checking devices compatibility).
   * In the **Order Number** field, type the order number of the Licence Package.
   * From the **Plan** toggle button, choose the plan which you would like to assign to the Licence Package.  
     Plans are sets of permissions that determine the scope of access to the Platform features; The **Predefined** option allows you to choose plans already defined in the Platform, and the **Custom** option enables you to create a plan specific for this Licence Package.  
     To learn how to create custom plans, read the [Creating a Custom Licence Plan](licence_custom_plan.html) chapter.
   * In the **Description** field, add the description of the Licence Package (optional).
   * The **Maximum Licence Validity Time** option allows you to set the maximum validity time for Licences derived from this Licence Package. To enable it, turn the **Maximum Licence Validity Time** switch **ON**, and specify the time in the below fields.
   * The **License Valid For** option allows you to set the default validity time for all Licences derived from this Licence Package.

   When you have provided the setup details, click **Next** in the top right corner to continue.

   ![licence package](images/licences/licence_package_3.png)
4. The **Limits** step allows you to set limitations to the Licence Package:

   * From the **Validity Time** toggle button, select the validity time setup for the Licence Package:
     + The **Unlimited** option enables the unlimited validity of the Package;
     + The **Specified** option allows you to determine the validity period in the date picker.

     Note

     You can set the future date in the date picker to schedule activating a Licence Package.
   * From the **AP Capacity** toggle button, select the desired AP capacity configuration:
     + The **Unlimited** option enables you to assign the unlimited AP capacity to the Licence Package.
     + The **Specified** option allows you to determine the total number of APs that you would like to allocate to this Package.
     + The **None** option allows you not to set any AP capacity for the Package.
   * From the **Data Transfer** toggle button, select the desired configuration of the Data Transfer limit:
     + The **Unlimited** option enables you to assign unlimited data transfer to the Licence Package.
     + The **Specified** option allows you to determine data transfer that you would like to allocate to this Package, and set its reset interval to a day of the week or month when the new billing period should begin.
     + The **None** option allows you not to set up data transfer limits to the Package.

   After you have specified the Package’s limitations, click **Next** in the top right corner to proceed further.

   ![licence package](images/licences/licence_package_4.png)
5. In the **Client** step, you can designate the Client who would be assigned this Licence Package and receive email notifications on its activity, such as licence updates on creation, modifying, deleting, licensing, status change and licence validity.

   To do this, choose an already existing Platform User from the **Client** dropdown list, or add an external user by providing their email address in the **Email** field. To finish adding a user or an email address to the list, click the **+** icon next to the **Client** and **Email** fields.

   You can also manage notifications which those users should receive by turning the **Notify About Licence Creation** and **Notify When Licences Expire** switches **ON** and **OFF**.

   Then, click **Next** in the top right corner to continue.

   ![licence package](images/licences/licence_package_5.png)
6. In the **Representative** step, you can appoint users responsible for contact with the Client.

   To do this, choose an already existing Platform User from the **Representative** dropdown list, or add an external user by providing their email address in the **Email** field. To finish adding a user or an email address, click the **+** icon next to the **Representative** and **Email** fields.

   You can also manage notifications which those users should receive by turning the **Notify When Licences Expire** switch **ON** and **OFF**.

   Then, click **Next** in the top right corner to proceed further.

   ![licence package](images/licences/licence_package_6.png)
7. In the **Summary** step, you can review all the Package’s setup. To modify it, click the **<** icon in the top left corner to go back to the desired step.

   To finish creating the Licence Package, click **Save** in the top right corner.

   ![licence package](images/licences/licence_package_7.png)
8. The Licence Package has now been created.

   In the **Licence Packages** section, you can preview all Packages created for your Organisation, and in the **Licences** area, you can preview Licences which you have been assigned.

   Depending on the setup, Licence Package panels may consist of up to three progress bars which indicate the latest status of **Licence Package validity**, **AP capacity**, and **Data transfer**, respectively.
   You can also view the Licence Package history by clicking the **Show Notifications** bell icon in the upper right corner of the panel.

   ![licence package](images/licences/licence_package_8.png)

   ![licence package](images/licences/licence_package_10.png)

   For full Licence Package details, click the **More** option in the top right corner of the desired Licence panel, and select **Show Details** from the dropdown list.

   ![licence package](images/licences/licence_package_9.png)

   The Licence Package panel also allows you to control notifications for both Clients and Representatives. To manage them, click the **More** option, and from the dropdown menu, select **Notification Settings**. Then, in the popup-box, specify the setup according to your preferences.

   To save the notifications setup, click **Save** in the bottom right corner of the popup-box.

   ![licence package](images/licences/licence_package_11.png)

   ![licence package](images/licences/licence_package_12.png)

## Editing a Licence Package

To make additional changes to a Licence Package, such as extending the AP capacity or changing the validity time, you should contact your Representative.

## Deleting a Licence Package

To delete a Licence Package, click the **More** option in the top right corner of the desired Package panel, and select **Delete** from the dropdown list. You will then be asked to enter the Licence Package ID in the pop-up box to confirm deleting it.

Note

Deleting an active Licence Package may impact all Licences, and services that they provide may stop working.