Creating, Editing, and Deleting a Payment Plan - Platform documentation






[Skip to content](#creating-editing-and-deleting-a-payment-plan)

# Creating, Editing, and Deleting a Payment Plan

The **Payment Plans** feature allows you to configure paid internet access.

**Note:** Before you start setting up Payment Plans, you should ensure that you have the below properties configured for your organisation. To learn how to configure them, contact your administrator.

**OrganizationProperty.PayToAccess.PayPal**

| key | description | type | default |
| --- | --- | --- | --- |
| payPalClientId | PayPal ClientId of the PayPal application. The account associated with it will be the receiver of the payments. | string | {@link CreatePaypalPaymentStep#defaultClientId()} |
| payPalSecret | PayPal Secret of the PayPal application.Security matter. | string | {@link CreatePaypalPaymentStep#defaultSecret()} |
| payPalEndpoint | PayPal endpoint URL used for PayPal requests. Default one is sandbox one: <https://api.sandbox.paypal.com/v1/> The real one is the same, but without ‘sandbox’ | string | {@link CreatePaypalPaymentStep#defaultPayPalBaseUrl()} |

## Creating a Payment Plan

1. Go to the **User Enrollment → Access Methods** section and click the **Payment Plans** option.

   ![create payment plan](../images/payment_plans/payment_plan_1.png)
2. In the bottom right corner of the **Payment Plans** window, click the **+** button to create a new Payment Plan.

   **Note:** To use the **Payment Plans** Access Method, you must first have a valid PayPal account which should be connected to the Platform.

   ![create payment plan](../images/payment_plans/payment_plan_2.png)
3. In the first step of the Payment Plan Creator, type the **Name** of the Plan in the **Name** field, and select its **Type**:

   * The **Free** Plan enables free internet access;
   * The **Paid** Plan allows you to specify the price of internet access.

   Once you select the **Paid** option, you can specify the price for internet access in the input field.

   Then, click **Next** in the top right corner to continue to the next step.

   ![create payment plan](../images/payment_plans/payment_plan_3.png)
4. In the second step, determine internet limitations for the Plan. To enable them, turn the switch **ON** next to the desired ones, and enter the preferred parameters.

   After you have finished defining your internet’s limitations, click **Next** in the top right corner to proceed further.

   ![create payment plan](../images/payment_plans/payment_plan_4.png)
5. In the last step, you can review the Payment Plan’s setup. To finish creating it, click **Save** in the top right corner.

   ![create payment plan](../images/payment_plans/payment_plan_5.png)
6. The Payment Plan is now created. You can also create other ones according to your preferences. To do this, re-follow the steps 1-5.

   ![create payment plan](../images/payment_plans/payment_plan_6.png)
7. Now, you should enable users to choose from Plans, by adding them to a Portal. To learn how to do this, read the [Adding Payment Plans to a Portal](adding_plans_to_portal.html) chapter.

## Editing a Payment Plan

To edit a Payment Plan, click the **More** option on the desired Plan, and select **Edit** from the dropdown list.

![edit payment plan](../images/payment_plans/payment_plan_7.png)

## Deleting a Payment Plan

To delete a Payment Plan, click the **More** option on the desired Plan, and select **Delete** from the dropdown list.

![edit payment plan](../images/payment_plans/payment_plan_7b.png)