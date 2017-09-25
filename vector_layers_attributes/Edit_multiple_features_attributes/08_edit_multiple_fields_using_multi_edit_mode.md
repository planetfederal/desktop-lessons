Unlike the previous tools, multi edit mode allows multiple attributes
of different features to be edited simultaneously.

For this example, keeping the same features selected, we will change the
*DESCRIPTIO* field to `COMMERCIAL` and update the *UPDATE_DAT* field as
we did before, but, this time, in one single step.

- In the attribute table toolbar, click the **Toggle multi edit** button.

    ![toggle_multi_edit](toggle_multi_edit.png)

The attribute table will show a form similar to the layer feature form.

![multi_edit_mode](multi_edit_mode.png)

The filled fields with a green icon next to it mean that all
selected features share the same value for that field.

On the opposite, the empty fields with a yellow icon next to it mean
that the selected features have different values for that particular
field.

- In the **DESCRIPTIO** field type `COMMERCIAL` and in the **UPDATE_DAT**
  field type `2017-09-24`.

    ![edited_multiple_fields](edited_multiple_fields.png)

    The red icon next to fields indicates that new values were entered,
    but they haven't been set to the features yet.

    You will also notice a warning message, informing you that the changes
    were not committed yet.

- In the Warning message, click **apply changes**.

    ![apply_multi_edit_changes](apply_multi_edit_changes.png)

A message should inform you that the changes have been applied. Please
notice that, at this point, the **changes were not saved into the data
source yet**, it only updates the fields values for each of the selected
features.

Click **Next step** once you are done.