Page Flow Overview - Platform documentation






[Skip to content](#page-flow-overview)

# Page Flow Overview

As described in the User Journey Overview, a Page Flow (also called a Flow) is a graphic illustration of a login path which you can adjust according to your preferences.

Before you start building a Page Flow, prepare the initial idea of what your login path should look like in order to reflect it in the system.

## The Structure of a Page Flow

“START” represents the moment when a user connects to your WiFi. This is also when you start to build your users’ login path. Then, you design the login process and form the structure which will be displayed to users at each stage.

The windows that represent each step are called **nodes**. There are four types of nodes in the system: **Portal**, **Internet Access**, **Condition** and **Message**. You may access them by clicking the blue circle on the right side of a particular node:

![add nodes](../images/uj_page_flow_add_nodes.png)

By selecting **Portal**, you will be able to add a Portal to the Flow. You can select an already existing one or create a new one from scratch. Portals are used to gather user data through different methods of logging-in and various Forms.

**Internet access** gives users access to WiFi and enables them to set up network parameters. Since internet access is the main goal of the Flow, it is the core node in each login path. It can appear at different stages depending on how complex your user journey is.

**Condition** allows you to display personalised content to various user groups. For instance, based on the gender you may redirect your users to different Portals and send them advertisements aligned with their preferences.

There are several options from which you can address your users, including:

* user profile data: age, gender
* login data: account user, roaming user, service document, social login user, verified user
* other: locale, operating system, property, time of day

## Keep to Some Rules

There is no limit to the number of nodes in the Flow. However, there are some rules for creating it:

* Every login option creates a new exit from the node,
* The connection between the nodes must be ‘closed’ in order to finish the login path. This means that the node must be connected with another one (either an existing node or a new one),
* All nodes must be fully configured for the Page Flow to work correctly.

Pay attention to any error information which might be displayed in the Page Flow Editor to easily identify where a problem is and how to solve it.