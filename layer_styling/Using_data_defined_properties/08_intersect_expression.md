In the **Style** tab of the **Layers Properties** dialog:

- Beneath **Line**, click **Simple Line** ;
- Click the **data-override** button next to **Color** and, beneath **Expression**, choose **Edit...**;
-   In the **Expression builder**, type the following expression:

    `if(intersects( $geometry, geometry( get_feature( 'Wake_ZIP_Codes', 'ZIPCODE', 'GARNER 27529' ) ) ), '#ff3300', '#65754f')`

- Click **OK** to accept the expression and close the **Expression Builder**.

Click **OK** to apply the changes and close the **Layers Properties** dialog.

Click **Next step**.