Gathering Calibration Data - Platform documentation






[Skip to content](#gathering-calibration-data)

# Gathering calibration data

The next step of the calibration is to gather calibration data. In this
step, you basically tell the platform that you are about to go and gather
data from all the calibrating points on the given floor on the given
channel band and then perform it. The whole procedure is divided into
two stages, the first is to create a link with a map of calibration
points (steps 1-3) and the second is to perform the calibration at every
calibration point (steps 4-10). For the second stage, it is recommended
to read all the steps before performing the action.

Note

* The calibration should be conducted within the opening hours of the venue.
* Every time the venue or the access points change, calibration should
  be done again. To learn more, read the [Calibrating after editing a venue](recalibration.html) chapter.
* Before performing the calibration, it is useful to forget all other
  Wi-Fi connections so that your mobile device does not connect
  automatically to a different connection while calibrating.

To gather calibration data:

1. Go to **Location Management → Calibration**.
2. In the **Create link to calibration** panel:

   * From the **Venue** list, select the name of your venue.
   * Into the **Calibration device MAC address** field, type a MAC address of the device that you will use for calibration.
   * From the **Calibration name** list, select the name of your calibration.
   * From the **Floor** list, select the floor number on which you are going to perform the calibration.
   * Select the channel band at which you calibrate the access point (**2.4 GHz channel band** or **5 GHz channel band**).
   * **Only for advanced users**: If you want to allow adding new
     calibration points while you calibrate, enable the **Allow new points** option.   
     While this is not recommended, it may be necessary for those venues where it's difficult to add a point to the plan.

   ![generate link](images/image165.png)
3. Click **Generate link**. As a result, the system generates
   a link to the venue plan that you can open on your mobile device:

   * To copy the link, click **Copy to clipboard**.
   * To send the link to your mobile device, in the **Phone** section,
     from the list, select the area code of your country, then type
     your phone number and click **Send link via sms**.

   Note

   The generated link is active for 10 minutes. If you do not start performing the calibration within this time frame, or you will have a break longer than 10 minutes, the link will expire and you'll need to [add a new calibration](creating_calibration.html).

   ![generate link full screen](images/image166.png)

   Tip

   Calibration can be done simultaneously by more than one person. To do this, you need to add a calibration for everyone and you will be able to keep track of other people’s calibration progress on your device.
4. Connect the device defined via the MAC address to the proper Wi-Fi
   channel. Open the link generated in step 3.
5. Go to one of the places where you placed a calibration point on the
   plan.
6. Hold your mobile device so that you do not obstruct the antenna of
   the device.
7. On the plan, click a calibration point.

   ![calibration points map app](images/image167.png)
8. At the top of the screen, click **Calibrate**. As a result, the
   **Calibration Point** window with a compass opens and its arrow
   points to the top of the screen. **Note the point indicated by the
   compass arrow.**
9. Slowly rotate yourself 360 degrees clockwise. One rotation
   should take 30 seconds and the arrow should always indicate
   the same point it indicated at the beginning.

   ![calibration rotation](images/image168.png)

   Note

   In case you want to abort the calibration process, click **Cancel Calibration**.

   The **Calibration Point** window closes, and the marker point of the calibration point
   changes its colour.

   Tip

   Different marker point colours have different meanings. Just after calibrating a particular point:

   * ![green point](images/image169.png) means that the calibration of that point was successful.
   * ![red point](images/image170.png) means that the calibration of that point was unsuccessful.

   When you go to the next point, the just calibrated point changes its colour (depending on the already gathered data) to the colour of the channel band it's calibrated for:

   * ![blue point](images/image171.png) means that the point is not calibrated on any channel band.
   * ![purple point](images/image172.png) means that the point is calibrated only on the channel band 2.4 GHz.
   * ![orange point](images/image173.png) means that the point is calibrated only on the channel band 5 GHz.
   * ![dark blue point](images/image174.png) means that the point is calibrated on both channel bands.
10. If the calibration was successful, go to the next calibration point
    from the map and repeat steps 6-10. Repeat these steps for all the
    points on a given floor.
11. If the calibration was unsuccessful, repeat the steps 6-10 for the
    same calibration point.
12. **Only for advanced users:** If in step 2 you selected the
    **Allow new points** option, you can add them now. On the map, click
    a particular place where you want to add a new calibration point and
    calibrate it straight away.

    Note

    Not calibrated new points will not be saved.

**What to do next**: [Configure engine](configuring_engine_location.html)