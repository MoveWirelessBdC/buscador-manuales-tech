Configuring the Engine - Platform documentation






[Skip to content](#configuring-the-engine)

# Configuring the engine

If you decided that the most basic engine is enough or you finished the
calibration process, then you should configure the engine that runs the
location.

To configure the engine:

1. Go to **Location Management → Management** and then click the **Engine** tile.
2. In the **Engine configuration** panel, from the **Mode** list, select
   the mode in which you want the engine to operate. You can select one
   of the below options:

   * **Without calibration** – uses the location of access points. Less
     accurate, but you do not need to perform calibration.
   * **With calibration** – uses calibration data. Recommended.
   * **Directional calibration** – uses calibration data and takes the
     device orientation into account.

     Note

     The **Directional calibration** works only on devices with the sending data period of 2
     seconds and very precise calibration (the rotation speed during the
     calibration process must be constant). It may increase the accuracy of
     the location, but recommended methods for achieving it are:

     • changing the access point location  
     • changing the channels on which the access point operates  
     • repeating the gathering calibration data process  
     • changing the calibration points.

     If you want to use the engine with directional calibration, perform
     very precise calibration and compare the accuracy of the location of the
     engine with calibration and engine with directional calibration and
     select the most precise option.
3. If in step 3, you selected the engine with calibration or with
   directional calibration, from the **Calibration** list, select the
   name of your calibration.
4. **Only for advanced users**: Into the **Engine parameters** field,
   type proper parameters of the engine.

   ![engine configuration](images/image175.png)
5. Click **Save**. The configuration is going to be
   implemented within 10 minutes.

**See also**: [Naming devices](../name_device.html)