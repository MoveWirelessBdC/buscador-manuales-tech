Making Connection Between Floors - Platform documentation






[Skip to content](#making-connections-between-floors)

# Making connections between floors

This step concerns only the venues with more than one floor. In order for
the customers to be navigated between different floors, you need to place in
the plan such elements as stairs, escalators, and lifts. Also, for
the navigation to show the nearest approximation of distance, it is
important to place the connectors in the plan as close to their
real-life placement as possible. All those connectors must be connected
so that the location engine knows that in this particular spot floors are
connected with this particular escalator or lift. Note that for a
lift that goes between floors 0-2 you need to make a connection not
only on the floors 0 and 2 but also 1.

To make a connection between floors:

1. Add the following connectors:

   * Stairs: on the left side of the screen, on the taskbar, click ![stairs button](images/image240.png).
   * Escalators: on the taskbar, click:

     + ![escalator up](images/image241.png) - to mark the
       escalator that goes up.
     + ![escalator up](images/image242.png) - to mark the
       escalator that goes down.
   * Lifts: on the taskbar, click ![lift](images/image243.png).

   Note

   It is recommended to add one connector in a particular place for all floors, then perform steps 2-4, and proceed with the remaining connectors.
2. Place the icons on every floor of the plan in the exact place
   of their location in the venue.
3. Right-click one particular button placed on the plan, and from the list,
   select ![edit](images/image227.png) **Edit connection**:

   * In the **Assign to group** window, from the list, select **New group**.
   * Into the **New group name** field, type the name of the
     connection. It is recommended to give names of the premises that
     is close to the connector.

   ![group name](images/image244.png)

   * Click **Save**. As a result, the system adds to the group
     list the name of the connection with the type of connector:

   ![new group name](images/image245.png)

   Tip

   Remember the name of the connection, as it is going to be used on other floors.
4. Go to the next floor to which the stairs or escalators or lifts
   lead to, right-click the button:

   * Select **Edit connection**.
   * In the **Assign to group** window, from the list, select the same connection that you created before.
   * Click **Save**. As a result, the connection has been made and the application can navigate customers between floors using this connection.
5. Repeat steps 3 and 4 for all the connectors in your venue. In the case of
   lifts, remember to make a connection for every floor through which
   it passes.
6. On the right side of the screen, click **Apply changes**.

**What to do next**: [Place cashpoints and toilets](services_placement.html)