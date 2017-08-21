The **Query builder** opens. In it, we can type or build the WHERE
clause of a SQL query to filter the layer.

- From the **Fields** list, double-click the `TRACTCE10` variable to add
it to the query.

- From **Operators**, click the `=` (equality).

- In **Values**, click the **All** to fetch all distinct values in the
*TRACTCE10* field, then double-click the `050400` value from the
list to add it to the query.

By now, the **Provider specific filter expression** text box should look
like this:

`"TRACTCE10"='050400'`

- Click **OK** to apply the filter and close the **Query Builder** dialog.

**Note:** The operands supported in the WHERE clause depend on the
layer's provider. In our case, the layer is saved in a shapefile;
therefore the supported operands are described in the [OGR
SQL documentation](http://www.gdal.org/ogr_sql.html).

Click **Next step** once you are done.