Terabee People Counting L - Platform documentation






[Skip to content](#terabee-people-counting-l-configuration-guide)

# Terabee People Counting L Configuration Guide

To configure the Terabee People Counting L devices, you must set them up in the Terabee web user interface.

Note

To display data collected from Terabee cameras in the Platform, you must have a Venue set up in the Platform.

## Configuring Terabee People Counting L in the Web User Interface

1. First, log in to the Terabee People Counting L web user interface either by a computer or by mobile phone:

   * For **computers**, open the browser and paste the following URL into the browser field: *<http://terabee->`< device_id >`.local*
   * For **mobile phones**, flash the QR code located on the People Counter ID card to access the mobile **Terabee People Counting Setup** app.

   Then, enter the following ID into the login fields:
   - Username: *people\_counting\_admin*
   - Password: *`< device_id >`--admin* (for example: 123abc456def--admin).

   !!! note
   You cannot yet access the advanced interface from the mobile app. To access this interface, open it on your computer's internet browser.
2. Now, you can configure the device's parameters:

   * The **Reverse Direction** checkbox allows you to switch between areas of **entries** and **exits**. If you leave this option **unselected**, the camera will be set to areas of **entries**. Selecting this checkbox will switch the camera's setup to areas of **exits**.
   * From the **Camera Height** list, choose the height (in millimetres) at which the device is installed (from 2400 to 3200 mm).
   * From the **Exclusion Height** list, select the height (in millimetres) below which the traffic will not be detected (starting from the ground).

   ![terabee](images/terabee/terabee_1.png)
3. In the following options, you can set up parameters of data which will be transferred to the Platform:

   * Select the **Enable Custom Data Push** checkbox to enable sending data to the Platform
   * Into the **Push URL** field, enter the URL to which the device should push data.
   * Into the **Protocol** field, enter the protocol used when pushing data: *http-get* or *http-post*.

   Note

   Look below for the example configuration of these two protocols.

   * In the **Payload Format** field, enter the adequate format (only for **http-post**).

   Note

   Look below for the example configuration of these two protocols.

   * From the **Push Interval** list, choose how many seconds must pass between the data pushout. For this instruction, it is *60*.
   * Select the **Enable Push On Event** checkbox to enable pushing data at each detection event.

   Note

   For configuring Terabee cameras with the Platform, it is advised to leave this checkbox **unselected**.

   * In the **Reset Hour** field, specify the time at which the device should reset the daily count (in the HH:MM format). The default is 00:00.

   Note

   It is advised to set that time to when the area is empty.

   Look at the below configuration of the Protocol and Push URL:

   #### Example one: Get

   Protocol: *http-get*

   Push URL: *http[s]://`< installation_url >`/camera/terabee/`< organization_id >`/`< sensor_name >`/{nb\_in}/{nb\_out}*

   where  
   `[s]` - you can use either *http* or *https*  
   `< installation_url >` - domain to which data should be pushed. For this instruction, it is *platform.com*.  
   `< organization_id >` - ID of the Organisation that collects the data  
   `< sensor_name >` - the camera name. This name will be used to display the camera’s statistics in the Platform.

   Note

   Cameras’ names must be unique in the Organisation.

   Example:
   <http://platform.com/camera/terabee/23/Printer/{nb_in}/{nb_out>}

   #### Example two: Post

   Protocol: *http-post*

   Push URL: *http[s]://`< installation_url >`/camera/terabee/`< organization_id >`*

   Payload format: *{{"sensorId":"`< sensor_name >`","counter":{{"in":{nb\_in},"out":{nb\_out}}}}}*

   where  
   `[s]` - you can use either *http* or *https*  
   `< Installation_url >` - domain to which data should be pushed. For this instruction, it is *platform.com*.  
   `< organization_id >` - ID of the Organisation that collects the data  
   `< sensor_name >` - the camera name. This name will be used to display the camera’s statistics in the Platform.

   Note

   Cameras’ names must be unique in the Organisation.

   Example:  
   <http://platform.com/camera/terabee/23>  
   {{"sensorId":"Printer","counter":{{"in":{nb\_in},"out":{nb\_out}}}}}

   ![terabee](images/terabee/terabee_2.png)
4. To confirm the setup, click the yellow **Send** button at the bottom of the page.

   Note

   Avoid clicking the **Send** button too often, as it may freeze the device. In such event, restart the camera by turning it off and on.
5. In the end, check if the two LEDs on the camera are green. If yes, the camera is correctly configured and is now pushing the data to the Platform.

   If the LEDs are not green, restart the camera as described in pt. 4.