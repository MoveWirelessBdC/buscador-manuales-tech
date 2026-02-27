Configuring Twilio Gateway - Platform documentation






[Skip to content](#configuring-twilio-gateway)

# Configuring Twilio Gateway

The **Twilio Gateway** is another server used for sending SMS campaigns. For this gateway to work as expected, you must also configure it in both systems: the **Twilio**, and **This** platform.

## Configuring Twilio Gateway on Twilio Platform:

1. Go to the ![first icon](images/image88.png) **→ Dashboard** section, and **save**, or **write down** the **ACCOUNT SID** value from the **Project Info** section as you will need it during the configuration process.

   ![account sid](images/image85.png)
2. Now, go to the ![second icon](images/image86.png) and **save**, or **write down** the **Phone Number** as you will need it during the configuration process.
3. Continue to the ![third icon](images/image87.png) **→ Programmable SMS** section, and select the ![fourth icon](images/image88.png). Then, click ![fifth icon](images/image89.png).
4. Now, in the **New API Key** panel:

   * Into the **Friendly Name** field, type the key name. For this instruction, it is *Test*.
   * From the **Key Type** list, select **Standard**,
   * Select countries to which you would like to send text messages.

   ![account sid](images/image90.png)
5. To create the key, click **Create API Key**.
   Note: Save, or write down the **SID** and **Secret** values as you will need them during the configuration process.

   ![account secret](images/image91.png)

## Configuring Twilio Gateway on This Platform

1. Go to the **Portal Management → Properties** section, and continue to the **Sending Centre**: Then, select the **SMS Settings** tab.
2. Now, in the **SMS Settings** tab, click the **Pen** icon to edit the details:

   * From the **Gateway List**, select **Twilio**.
   * Into the appropriate fields, enter the **Twilio Account ID**, the **Twilio Key**, and the **Twilio Password**.
3. To finish the configuration process, click **Save**.