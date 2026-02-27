Configuring Email Dispatch - Platform documentation






[Skip to content](#configuring-email-dispatch)

# Configuring Email Dispatch

To dispatch marketing offers to users via emails, you should first configure the authentication of dedicated mailing servers, by adding appropriate properties to them.

1. Go to the **Portal Management > Properties** section, and continue to the **Sending Centre**. Then, select the **SMS Settings** tab.
2. In the **SMS Settings** tab, click the **Pen** icon to edit the details.
3. Now, enter the following values into the **Email Properties** window.

| Field | Value |
| --- | --- |
| Gateway | A gateway you use |
| Transport protocol | Mail Transport Protocol, either SMTP or SMTPS |
| Host | Property Mail Host |
| Password | Email password used for authentication |
| Port | Property Mail Port |
| Username | Property Mail Username - Mail username used for authentication |
| Authorisation enabled | Turns mail authentication on (true) or off (false) |
| TLS enabled | Turns the TLS protocol used during authentication on (true) or off (false) |
| SSL enabled | Turns the SSL protocol used during authentication on (true) or off (false) |
| mailSourceEmail | Sets sender of sent emails |

1. After you have finished, click **Save** to complete the configuration process.