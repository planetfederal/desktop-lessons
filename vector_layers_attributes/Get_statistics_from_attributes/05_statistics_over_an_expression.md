Instead of a field, you can also calculate the statistics base on an
expression. This feature is useful when the existing fields do not
satisfy your needs.

As an example, let's imagine that we want to obtain some statistics on
the house units occupancy percentage. The Census_blocks_2010* does not
have a column with those values, but there are columns for the Total
House Units (*TOTAL_hu*) and for the Occupied House Units (*OCCUPIED*),
that we can use to calculate the percentage.

- In the **Statistics Panel**, click the **Expression** button.

  ![open_expression_builder.png](open_expression_builder.png)

- The **Expression dialog** will open. Type in the following expression
and click **OK**:

  `"OCCUPIED" / "TOTAL_hu" * 100`

  ![expression.png](expression.png)

The **Statistics Panel** now shows statistics based on the calculated
expression for each feature.

![stats_on_expression.png](stats_on_expression.png)

This step ends the lesson, click *Finish Lesson**.