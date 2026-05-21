#Mercer General Project (Day 2 Challenge)

##Task
-We first practiced on the GCS data, familiarizing ourselves with the general cleaning processes, especially with the median portion
-The Pulse Column cleaning process began by inspecting of the pulse row data, by checking the count of unique values and the frequency of certain values. 
-Then once familiarized  with the data, the non numeric values was converted to numeric, and also established the range.
-Incorporated logical masks (df.loc) to scan the columns for values outside valid boundaries any rows holding these impossible numbers that were immediately replaced with NaN placeholders.
-Next the data was with median because the data was skewed, as seen by both min and max values. The median was observed to be the best imputation method
-A visualization graph was drafted in order to actually see the data after it was cleaned, for further understandability.

## The resulting dataset was NaN = 0 because it was imputed with the median
