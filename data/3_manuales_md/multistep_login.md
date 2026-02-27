Creating a Multistep Login - Platform documentation






[Skip to content](#creating-a-multi-step-login-process)

# Creating a Multi-Step Login Process

The multi-step login process differs from other login processes in that it is created from two paired components:

**Phone Number Input** and **Phone Number Verification** is used for two-step phone number verification,
**Pay to Access** and **Payment Method** is used for paid access.

Both components must be reflected in Portals and the Page Flow. You must first create two Portals and then place them in the Page Flow in their proper order.

**You should note that in order to use the Pay to Access method, you must first have a valid PayPal account which should be connected to the platform.**

1. First, it is necessary to create two Portals. To learn how to create a Portal, read the [Creating a Portal](creating_portal.html) chapter.
2. Within each Portal, place one of the components from the pair.

   Example: See an example of the **Phone Number Verification** in the **Preview** mode below.

   ![multistep login](../images/portal/multistep_login_1.png)
3. First, create a new Page Flow. To learn how to create a Page Flow, read the [Creating and Editing a Page Flow](../page_flow/creating_and_editing_a_page_flow.html) chapter.
4. Add one **Portal Node** for each Portal.

   Note: The editor limits the selection of available Portals based on which step in the flow that you want to add. It will not allow you to start the Flow from the second verification step.

   ![multistep login](../images/portal/multistep_login_2.png)