PMS - Platform documentation






[Skip to content](#pms-configuration)

# PMS Configuration

The Platform allows you to connect **Payment Plans** with the PMS systems which are used by hotels to provide paid internet access for their guests. Those systems may require users to give details of their stay, such as name and room number, to include costs of internet access in hotel bills.

**Note:** Before you start configuring the PMS system, you should create Payment Plans to which the PMS would be connected. To learn how to do this, read the [Creating, Editing, and Deleting a Payment Plan](../payment_plans/configuring_plans.html) chapter.

1. First, it is necessary to create two Portals; one where users would provide details of their stay and the second one where they would select the desired Payment Plan.

   To learn how to create a Portal, read the [Creating a Portal](../portal/creating_portal.html) chapter.
2. In the Portal editor, select the **Multi-Step Login** section from the left menu. Then, drag the **Guest Details** component into the Portal workspace.

   **Note:** To enable the connection between the two Portals (the one that contains Guest Details, and another one that contains Payment Plans), you should place a **Submit Button** on the first one. To do this, select the **Basics** category from the left menu, drag the **Submit Button** component, and drop it on the Portal workspace.

   When you have finished setting up the Guest Details component, click **Save** in the top right corner to finish creating the Portal.

   ![configure pms](../images/pms/pms_1.png)

   ![configure pms](../images/pms/pms_2.png)

   ![configure pms](../images/pms/pms_3.png)
3. Now, you should create the second Portal with Payment Plans. To learn how to do this, read the [Creating a Portal](../portal/creating_portal.html) chapter.

   To learn more about managing Payment Plans, go to the **Payment Plans** chapter.

   ![configure pms](../images/pms/pms_4.png)
4. In the Portal Editor, select the **Multi-Step Login** from the left menu. Then, drag the **Payment Plans** component from the **PMS** category, and drop it into the Portal workspace.

   **Note:** To connect this Portal with the following Page Flow Nodes, you should place a **Submit Button** on it. To do this, select the **Basic** category from the left menu, drag the **Submit Button** component, and drop it on the Portal workspace.

   When you have finished setting up the Payment Plans component, click **Save** in the top right corner to finish creating the Portal.

   ![configure pms](../images/pms/pms_5.png)

   ![configure pms](../images/pms/pms_6.png)

   ![configure pms](../images/pms/pms_7.png)

   ![configure pms](../images/pms/pms_8.png)

   ![configure pms](../images/pms/pms_9.png)
5. When the two Portals have been created, you should add them to a Page Flow in the proper order.

   Firstly, add the Portal which contains the **Guest Details** component, then, continue with the Portal that holds the Payment Plans.

   Below, you can see an example of such an order.

   ![configure pms](../images/pms/pms_10.png)