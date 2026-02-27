Overview of the platform - Platform documentation






[Skip to content](#platform-overview)

# Platform overview

## What can you do with the platform?

1. Manage Wi-Fi networks in your organisations
2. Create a Wi-Fi login process (User journey)
3. Gather Wi-Fi statistics
4. Promote your business
5. Gather data about customer venue behaviour
6. Create navigation around venues

## How does it work?

### Where can you start?

You simply [reflect the structure](reflect_the_structure_of_your_business.html) of your organisation in the platform, [create a user journey](/guide/use_cases/user_journey.html), and [statistics](wifi_statistics.html) are being gathered automatically.

You can also [promote your business](promote_your_business.html) with various marketing actions.

Additionally, with the location function of the platform, you can [create navigation around venues](creating_navigation_for_customers.html) which customers can open in their web browsers and at the same time provide you with [behavioural data](/guide/use_cases/understanding_the_behaviour_data.html). It doesn't mean you have to create the navigation to gather such data, it's just a great way to invite more customers to log in to Wi-Fi.

### Propagation of settings

Settings are propagated down the organisation tree. The structure of organisations in the platform is represented in a form of a management tree, such as in the image below.

![organisation tree](images/management_tree.png)

With the propagation, you don't need to implement particular settings in every organisation.  
It is enough to implement them in an organisation which is on a higher level in the tree, and they are automatically propagated to all organisations on lower levels.

Also, numerous editors in the platform have panels divided into two sections: **Own** and **Inherited**. Elements in the **Own** section are created by the organisation in which you are currently, whereas in the **Inherited** section are those that were created in higher-level organisations but can also be used in your organisation. An example of such panel is the **Page Flow manager**.
![page flow manager](images/own_inherited.png)

## How to move around?

### Platform main view

The platform main view is the first view you see after logging in.

![main interface](images/interface.png)

The view consists of:

1. Organisation name - the name of an organisation to which you logged in; after clicking it, the organisation management tree opens.
2. Time zone - a time zone according to which the statistics are shown, set in the organisation panel.
3. Username - your username in the platform; clicking it opens a menu with **Account settings** and **Log out** options.
4. Main menu - described below.
5. **Dashboard** - the summary of Wi-Fi statistics from the last 24 hours.

### Main menu

The main menu bar allows you to navigate around the platform by simply clicking its elements.

Note

The bar may vary depending on your user permissions and the licence owned.

It consists of:

1. **Dashboard**
2. **Marketing** - including:

   * **Campaigns** - the marketing campaigns editor and statistics gathered in campaigns (to learn more, read the [marketing campaign overview](../user_guide/marketing/campaign_overview.html)),
3. **User Enrollment** - including:

   * **User journey** - the login process editor (to learn more, read the [User Journey overview](../user_guide/user_enrollment/uj_overview.html)),
   * **User agreements** - the agreements editor for creating [service documents](../user_guide/user_enrollment/user_agreements/service_document.html), [marketing consents](../user_guide/user_enrollment/user_agreements/marketing_consents.html), and [communication channels documents](../user_guide/user_enrollment/user_agreements/communication_channels.html),
   * **Access methods** - the access method editor: [tokens](../user_guide/user_enrollment/tokens/creating_tokens.html), [user account](../user_guide/user_enrollment/user_accounts/creating_user_accounts.html), [PMS](../user_guide/user_enrollment/pms/configuring_PMS.html), and [Pay access](../user_guide/user_enrollment/pay_access_plans/configuring_PtA.md).
4. **Portal Management** - including:

   * **Users** - a panel for adding platform users (to learn more, read [Adding a user account](../user_guide/portal_management/adding_a_user.html)),
   * **Devices** - a panel for adding devices used in organisations (to learn more, read [Adding a device](../user_guide/portal_management/adding_a_device.html)),
   * **Properties** - a panel for adding properties (to learn more, read [Adding properties](/guide/user_guide/portal_management/adding_properties.html)),
   * **Permissions** - a panel for creating permissions groups (to learn more, read [Adding a group of permissions](../../zzz_unused_files/adding_permission.md))
   * **Licences** - a panel showing licence's details and enables to request a new licence (to learn more, read [Checking licences](../../zzz_unused_files/check_licence.md)),
   * **Activity stream** - a panel showing the activity on the platform (to learn more, read [Checking activity stream](../user_guide/portal_management/activity_stream.html)).
5. **Location Management** - including:

   * **Management** - a panel used to configure the platform location function (to learn more, read either [Getting the behavioural data of users in large venues](get_the_behavioral_data_of_users/large_venues.html) or [small venues](get_the_behavioral_data_of_users/small_venues.html)),
   * **Navigation** - the navigation editor (to learn more, read [Creating navigation for customers](creating_navigation_for_customers.html)),
   * **Venue administration** - a panel for managing the created venues and calibrations,
   * **Calibration** - a panel used to create a calibration.
6. **Reporting** - including:

   * **Statistics** - collected statistics about Wi-Fi users (to learn more, read [Finding your way around Wi-Fi Users statistics](wifi_statistics.html),
   * **Email reports** - a panel for configuring the sending of email reports (to learn more, read [Sending email reports](../user_guide/reporting/email_reports.html)),
   * **Behaviour** - collected behavioural data (to learn more, read [Understanding the Behaviour data](/guide/use_cases/understanding_the_behaviour_data.md)).