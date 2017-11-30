The **Select by expression - Buildings** dialog opens. Notice that we
could have left this dialog open, but we would not have been able to
confirm the selection in the attribute table.

Now we want to narrow down the selection by choosing only commercial
buildings that have areas bigger than 30000 sq. ft..

Although it seems that there are some fields with the area information,
in QGIS we can take that get the geometries area (among other
characteristics) using dedicated functions.

- In the search box beneath the functions list, type `area`. From the filtered results below, double-click the $area function to
add it to the expression.

   ![add_area_function](add_area_function.png)

- In the expression, type a `>` (bigger than operand) followed by 30000. Now the expression should look like this:

  `$area > 30000`

- Click the down-arrow next to the **Select** button, and choose
**Select within selection** to apply the new expression.

   ![select_within_selection](select_within_selection.png)

**Note 1:** We could have created an expression that, using the `AND`
operator, combined the two used expressions into one. Something like this:

`"DESCRIPTIO"  =  'COMMERCIAL' and $area > 20000`

**Note 2:** As it is explained in the `$area` function help, the function
returns the geometries area following the project's settings. For this
particular lesson, we set the area measurements units to square feet.