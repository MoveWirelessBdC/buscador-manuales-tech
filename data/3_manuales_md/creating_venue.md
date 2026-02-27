Creating, Editing and Deleting a Venue - Platform documentation






[Skip to content](#creating-editing-and-deleting-a-venue)

# Creating, Editing and Deleting a Venue

The Platform allows you to set up **Venues** for your Organisation, which gives you a preview on end-user devices that have been located at your facility.

You can choose from the two modes in which a Venue can operate: **Location** or **Presence**.

### Location Mode

The **Location** mode identifies and localises each end-user device and displays their position on your Venue’s map. It requires a specific type of Access Points that support the Location mode.

To see the list of those APs, read the [Supported Devices](../../device_configuration/supported_devices.html) chapter.

### Presence Mode

The **Presence** mode identifies end-user devices and gives you information on the number of devices currently present at your Venue, but **does not localise** them.

## Creating a Venue

Before you start creating a Venue, you should note that you can only create **one Venue per Organisation**, and its **Sub-Organisations will not inherit it**.

1. Go to the **Portal Management > Structure** section and select the **Venues** tab form the upper bar. Then, click **+** in the bottom right corner to create a Venue.

   ![add venue](images/venues/creating_venue_1.png)
2. In the pop-up box, select how you would like to create it:

   * To create a Venue from the Platform creator, select **Create New**
   * To upload a Venue from a zip file, select **Upload From Zip File**.

   Then, click the **Create Venue** button in the bottom right corner of the pop-up box to proceed further.

   ![add venue](images/venues/creating_venue_2.png)

   ![add venue](images/venues/creating_venue_3.png)
3. In the first step of the Venue Creator:

   * From the **Venue Type** dropdown list, select the type of your Venue
   * From the **Mode** dropdown list, select the mode in which the Venue should operate.   
     The **Presence** mode enables the identification of end-user devices, yet cannot determine their position. The **Location** mode allows localising each device on the Venue map.
   * From the **Device Type** dropdown list, select the type of Access Points which you would like to use to provide end-users internet access.

   **Note:** Not all types of Access Points support the **Location** mode. To see the list of APs that do, read the [Supported Devices](../../device_configuration/supported_devices.html) chapter.

   Then, click **Next** in the top right corner to continue the creation process.

   Below, you can see an example of a Venue setup.

   ![add venue](images/venues/creating_venue_4.png)
4. In the second step, you should provide details specific for the selected AP type. For this example, it is *Ruckus Cloud*.

   **Note:** Depending on the type of AP, you may need to provide different setup details to correctly configure the Venue.

   ![add venue](images/venues/creating_venue_5.png)
5. In the last step, you can review the Venue’s configuration. To finish creating it, click **Save** in the top right corner.

   ![add venue](images/venues/creating_venue_6.png)
6. The Venue has now been created, and you can use its features.

   To learn how to preview devices on a Venue map, read the [Previewing End-User Devices](previewing_user_devices.html).

## Editing a Venue

To edit a Venue, click the **More** option in the top right corner of the Venue panel, and select **Edit** from the dropdown list.

**Note:** You can edit a Venue only to a limited extent which is changing the Venue type. For other changes, you should delete the Venue and create a new one with the desired setup.

![add venue](images/venues/creating_venue_7.png)

## Deleting a Venue

To delete a Venue, click the **More** option in the top right corner of the Venue panel, and select **Delete** from the dropdown list.

![add venue](images/venues/creating_venue_9.png)

## Exporting a Venue

You can also export a Venue and its setup to a zip file. To do this, click the **More** option in the top right corner of the Venue panel, and select **Export** from the dropdown list.

![add venue](images/venues/creating_venue_8.png)