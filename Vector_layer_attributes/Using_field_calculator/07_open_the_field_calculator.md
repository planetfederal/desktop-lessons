If the *Buildings* layer were to be updated in the future, sooner or
later the *area_m2* would end up outdated. QGIS has a neat functionality
that allows you to create **virtual fields** based on expressions, which
are calculated on-the-fly. These fields, being virtual, are only visible
in the project and will not be stored in the data source.

You can create virtual fields using the Field calculator. Open the field
calculator once more.

- In the **Attribute table** toolbar, click the **Open field
  calculator** or press `CTRL + I`.

    ![open_field_calculator](open_field_calculator.png)

- Alternatively, in QGIS main window, you can open the **Field
  calculator** using the similar button in the **Attributes toolbar**.

    ![open_field_calculator_2](open_field_calculator_2.png)

Click **Next step** once you are done.