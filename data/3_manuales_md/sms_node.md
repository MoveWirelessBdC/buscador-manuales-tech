Adding and Managing Message Nodes - Platform documentation






[Skip to content](#adding-and-configuring-a-message-node)

# Adding and Configuring a Message Node

**Message Nodes** enable the setup of the message dispatch function for users. Message dispatches can be sent via SMS, email, or both.

## Adding a Message Node as the **First** Node

1. In the **Page Flow Editor**, click the blue **+** button to create the first node. From the dropdown list, select the **Message** option, and from the sub-list select either **SMS Dispatch** or **Email Dispatch**.

   ![internet access node creating](../images/adding_nodes/message_node_4.png)

## Adding a Message Node as the **Follow-Up** Node

1. In the **Page Flow Editor**, click the **More** option to create a consecutive node.

   ![internet access node creating](../images/adding_nodes/message_node_1.png)
2. From the list, select the **Add Node** option and from the sub-list, select **Message**. From the sub-sub-list, choose either the **SMS Dispatch** option or the **Email Dispatch** option, depending on your needs.

   ![internet access node creating](../images/adding_nodes/message_node_3.png)

# Message Node Configuration

You should note that for SMS and Email Dispatches to work correctly, the users must verify their Email addresses and phone numbers, and give their consent to receive offers when logging in to the WiFi. To learn more about the User Agreements, go to the **User Agreements** chapter..

## SMS Dispatch

1. In the pop-up box, compose a text message which will be sent to the users. Click **Save** to confirm your changes.

   ![internet access node creating](../images/adding_nodes/message_node_sms_dispatch_1.png)

## Email Dispatch

1. In the pop-up box, create the Email Subject and accompanying text message which will be sent to users. Then, click **Save**.

   ![internet access node creating](../images/adding_nodes/message_node_email_dispatch_1.png)

### To finish the configuration process, save the Page Flow by clicking **Save** in the upper right corner.

**Note: The Page Flow must be completely finished before it is saved and all nodes must be fully configured in order to conclude the process.**

## Editing a Message Node

To edit the text of the message, click the **More** option on the desired Message Node and select **Edit Message** from the menu. In the popup-box, make the desired changes, and click **Save** in the bottom right corner to confirm them.

![editing message node](../images/page_flows/edit_message_node_0.png)

![editing message node](../images/page_flows/edit_message_node_1.png)

## Removing a Message Node

In the top right corner of the Message Node which you would like to remove, click the **More** option. Then, from the dropdown list, select **Remove Node**.

Note: If you remove a node, some nodes can be left disconnected from the Page Flow. Note that it is necessary to connect all nodes before saving and using a Page Flow. A Page Flow with disconnected nodes can only be saved as a **Draft**.

To learn more about removing nodes, read the [Connecting, Disconnecting and Removing Nodes](connect_node.html) chapter.

![removing message node](../images/page_flows/remove_message_node.png)