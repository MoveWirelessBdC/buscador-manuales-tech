Troubleshooting - Platform documentation






[Skip to content](#troubleshooting)

# Troubleshooting

The **Troubleshooting** section allows you to track all the configuration issues between Access Points and Page Flows in
your Organisation. To access it, go to the **User Enrollment** section in the left menu, and select **Troubleshooting**
from the dropdown list.

![troubleshooting](images/troubleshooting.png)

In the **Configuration Issues** table you can find details of issues which occur in your Organisation and
Sub-Organisation:

* the **Date** column shows the date an issue occurred,
* the **Issue Type** column informs about the type of this issue,
* the **Count** column displays the number of problems that need resolving,
* the **Device ID** column provides the ID of the Device in which the issue has occurred,
* the **Organisation** column displays the Organisation which is impacted by the issue,
* the **Request Information** column provides you with the detailed information on the Access Point (AP Name) and
  Network (SSID Name) in which the issue has occurred.

## Configuration Issues

The most common configuration issues that you might encounter include **AP not found**, **SSID not found**, **SSID and
AP not found**, **Flow not attached to Network**, **Licence error encountered**, **Social config not found**, and
**Login loop encountered**.

### AP not found

The message `AP not found` highlights issues related to the AP (Access Point). It could indicate that the AP name in the
Platform is misspelled or incorrect, the AP has not been added to the Platform, or has been added but to an incorrect
Organisation.

To resolve this issue, you should verify the AP setup in both the AP and the Platform, ensuring accuracy on both ends.

### SSID not found

The message `SSID not found` indicates issues related to the Network (SSID). This could mean that the specified Network
cannot be found on the Platform, has not been added to it, or differs from the Network configured on the AP (Access
Point).

To resolve this issue, you should examine the Network setup in both the AP and the Platform, ensuring accuracy on both
ends.

### SSID and AP not found

The message `SSID and AP not found` points to issues with both the AP (Access Point) and the Network (SSID), combining
the two scenarios mentioned above.

To resolve this issue, you should inspect the Network and AP setups in both the AP and the Platform, ensuring their
accuracy across all aspects.

### Flow not attached to Network

The message `Flow not attached to Network` indicates that no Page Flow has been connected to the specified Network
(SSID).

To resolve this issue, you should link the desired Page Flow to this Network.

### Licence error encountered

The message `Licence error encountered` indicates that processing could not be performed due to a licensing error within
the Organisation.

To resolve this issue, you should ensure that the Organisation has a proper and valid Licence set up on the Platform.

### Social config not found

The message `Social config not found` indicates that processing could not be performed due to the absence of a Social
Media login configuration.

To resolve this issue, you should ensure that the Organisation either has a primary Social Media configuration selected,
or the Captive Portal used in the Page Flow utilises a custom selected Social Media configuration. Please note that this
issue may occur with various types of social media.

### Login loop encountered

The message `Login loop encountered` indicates that processing was halted due to the detection of a login loop. This
typically suggests that either the RADIUS is incorrectly set up, or it is being blocked by some firewalls.

To resolve this issue, you should ensure that the proper RADIUS configuration is applied on AP (Access Point) and that
the Platform's RADIUS server is reachable from the AP. Additionally, verify that there are no firewalls blocking UDP
communication on ports 1812 and 1813.