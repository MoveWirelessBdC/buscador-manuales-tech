Managing a Portal Node - Platform documentation






[Skip to content](#managing-a-portal-node)

# Managing a Portal Node

## Managing a Portal Node

You can manage the Portal Nodes by previewing, setting timeout, editing, and removing them in the Page Flow.

### Previewing a Portal Node

You preview the specific Portal Node. click the **More** option on the desired Portal Node, and select **Preview** from the menu.

![preview portal node](../images/page_flows/preview_portal_node_0.png)

In the next window, you can select the preferred settings (the language and the display mode, if applicable) to see the Portal. To go back to the Page Flow, click the **Close Preview** option in the top right corner.

![preview portal node](../images/page_flows/preview_portal_node_1.png)

### Setting Up a Portal’s Timeout

Portal Nodes allow you to set up the **Timeout** which is a designated period after which, when no action undertaken, the user is redirected to the beginning of the login path. This option is particularly useful in Flows which contain more than one Portal.

To set it up, click the **More** option on the desired Portal Node, and select **Timeout** from the menu. It is especially useful in Flows with more than one Portal.

![portal node timeout](../images/page_flows/portal_timeout_0.png)

Now, in the pop-up box, select one of three options which determine the timeout of the Portal:

* The **Time** option determines time after which the user is redirected to the beginning of the login path,
* The **Number** option allows you to designate the number of times the specific Portal is displayed to the user before redirecting them to the beginning of the login path,
* The **Unlimited** option enables unlimited access to the Portal, and the user is not redirected to the beginning of the login path.

When you have finished designating the timeout, click **Save** in the bottom right corner to confirm your changes.

![portal node timeout](../images/page_flows/portal_timeout_1.png)

### Editing a Portal Node

You can edit a Portal directly from the Page Flow, however, such Portal can be edited only to some extent (for instance, submit buttons cannot be edited in this mode). You should also note that **the changes applied to such Portal are visible in all Page Flows which use this Portal.**

To learn more about editing Portals, read the [Editing, Copying and Deleting a Portal](../portal/copying_portal.html) chapter.

![editing portal node](../images/page_flows/edit_portal_node.png)

### Removing a Portal Node

To remove a Portal Node from the Page Flow, click the **More** option on the desired Portal Node and select **Delete Node** from the menu.

**Note: If you remove a node, some nodes can be left disconnected from the Page Flow. You should note that it is necessary to connect all nodes before saving and using a Page Flow. A Page Flow with disconnected nodes can only be saved as a Draft.**

To learn more about removing nodes, read the [Connecting, Disconnecting and Removing Nodes](connect_node.html) chapter.

![removing portal node](../images/page_flows/remove_portal_node.png)