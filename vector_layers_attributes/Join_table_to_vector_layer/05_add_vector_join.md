* In the **Layers Properties - Blocks 2010**, click the **Join** tab.

    ![open_joins_tab](open_joins_tab.png)

* There are no joins yet for this layer. Click the **Add Join** button
  to create one.

    ![create_join_button](create_join_button.png)

The **Add vector join** dialog will open. Set the following options:

1. Set **Join table** to `2010_demographics`
2. Set **Join field** to `BLOCKID`
3. Set **Target field** to `GEOID10`

These are the minimum necessary settings, but you can also set the
rest of the options.

1. Enable **Choose which fields are joined** and select:

    * `TOTAL_POP`
    * `TOTAL_HU`
    * `OCCUPIED`
    * `VACANT`

2. Enable **Custom field name prefix** and type `2010_`.

* Click **OK** to accept the options and close the **Add Vector join** dialog

    ![add_join_settings](add_join_settings.png)

In the **Layers Properties - Blocks 2010** you will see the newly
created join.

![created_join](created_join.png)

* Click **OK** to apply the changes and close the **Layers Properties** dialog.

Click **Next step** once you are done.