# Mercer General Project (Day 2 Challenge)

## Task

- First practiced on the GCS data, familiarizing ourselves with the general cleaning processes, especially with the median portion.

- The Pulse Column cleaning process began by inspecting the pulse row data, by checking the count of unique values and the frequency of certain values.

- Then once familiarized with the data, the non-numeric values were converted to numeric, and the valid range was established.

- Incorporated logical masks (`df.loc`) to scan the columns for values outside valid boundaries. Any rows holding these impossible numbers were immediately replaced with `NaN` placeholders.

- Next, the data was imputed with the median because the data was skewed, as seen by both the minimum and maximum values. The median was observed to be the best imputation method.

- A visualization graph was drafted in order to actually see the data after it was cleaned, for further understandability.

---

## Final Result

- The resulting dataset had a final `NaN` count of **0** because the missing values were successfully imputed using the median.
