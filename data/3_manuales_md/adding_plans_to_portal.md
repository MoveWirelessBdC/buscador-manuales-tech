Adding Payment Plans to a Portal - Platform documentation






[Skip to content](#adding-payment-plans-to-a-portal)

# Adding Payment Plans to a Portal

The **Payment Plans** feature is one of the Multi-Step Login processes which you can set up on Portals. They differ from other login processes in that they are created from two paired components: **Payment Plans** and **Payment Method**.

Both components must be reflected in Portals and Page Flow. You must first create two Portals and then place them in the Page Flow in their proper order.

**Note:** To use the **Payment Plans** Access Method, you must have a valid PayPal account which should be connected to the platform.

1. First, it is necessary to create two Portals; one where users would choose Payment Plans while logging in to your internet, and the second one where they would select the desired Payment method for internet access.

   To learn how to create a Portal, read the [Creating a Portal](../portal/creating_portal.html) chapter.
2. In the Portal Editor, select the **Multi Step Login** category from the left menu. Then, drag the **Payment Plans** component and drop it into the Portal workspace.

   ![adding payment plans to portal](../images/payment_plans/payment_plan_8.png)

   ![adding payment plans to portal](../images/payment_plans/payment_plan_8a.png)
3. Next, click on the **Select Plan** button to choose Payment Plans that you would like to offer your users.

   ![adding payment plans to portal](../images/payment_plans/payment_plan_9.png)
4. In the **Payment Plans Available** window, click on the desired Plans to select them, and click **Next** in the top right corner to place them on the Portal.

   You can also create an additional plan at this stage by clicking the **+** button in the bottom right corner and following the steps for creating a Payment Plan.

   ![adding payment plans to portal](../images/payment_plans/payment_plan_10.png)
5. The Payment Plans have now been added to the Portal.

   **Note:** To enable the connection between the two Portals (the one that contains Guest Details, and another one that contains Payment Plans), you should place a **Submit Button** on the first one. To do this, select the **Basics** category from the left menu, drag the **Submit Button** component, and drop it on the Portal workspace.

   When you have added all the desired Plans to the Portal, click **Save** in the top right corner, to finish creating it.

   ![adding payment plans to portal](../images/payment_plans/payment_plan_11.png)
6. Now, you should create the second Portal with **Payment Methods**. To learn how to create a Portal, read the [Creating a Portal](../portal/creating_portal.html) chapter.

   ![adding payment plans to portal](../images/payment_plans/payment_plan_12.png)
7. In the Portal Editor, select the **Multi-Step Login** from the left menu. Then, drag the **Payment Method** component and drop it into the Portal workspace.

   **Note:** To connect this Portal with the following Page Flow Nodes, you should place a **Submit Button** on it. To do this, select the **Basics** category from the left menu, drag the **Submit Button** component, and drop it on the Portal workspace.

   When you have finished setting up the Payment Methods component, click **Save** in the top right corner to finish creating the Portal.

   ![adding payment plans to portal](../images/payment_plans/payment_plan_13.png)

   ![adding payment plans to portal](../images/payment_plans/payment_plan_14.png)
8. When the two **Payment Plans** Portals have been created, you should add them to the Page Flow in the proper order. To learn how to add a Portal to a Page Flow, read the [Adding a Portal to a Page Flow](../page_flow/portal_node.html) chapter.

   Firstly, add the Portal which contains the Payment Plans components to allow users to select the desired Payment Plan. Then, continue with the Portal that holds the Payment Methods.

   Below, you can see an example of such an order.

   ![adding payment plans to portal](../images/payment_plans/payment_plan_16.png)