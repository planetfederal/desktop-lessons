This time, since we already know the values we want to filter, instead
of clicking buttons to build the WHERE clause, we will type it directly.

- In the **Provider specific filter expression** text box, type the
following expression:

  `"TRACTCE10" IN ('050400','050100')`

- Click **OK** to apply the filter and close the **Query Builder** dialog.

**Note:** We could have used the **OR** operator and repeat the
`"TRACTCE10" = (...)` equality twice, but the **IN** operator is much
more elegant and will allow you add even more values to the collection
in an easier way.

Click **Next step** once you are done.