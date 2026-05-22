# carisurg-portfolio
# Mercer General Project- Tutorial 1 (Day 1 Challenge)

##This code cleans the data from the Gender column and processes it using libraries from Python such as panda in Google collab.

## Tasks
-Connected the file "EmergencyTriageDataset_Reduced_Dirty.csv" from Google Drive to Google Colab
-Cleaned Gender Column in the file
-Checked for outliers such as Nan Values
-Replaced the unclean Gender column with the cleaned version

## Reduced 6 different entities representing 2 genders male and females as:

-1 = Male
-0 = Female

# Mercer General Project-Tutorial 2 (Day 2 Challenge)

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

# Mercer General Project-Tutorial 3 (Day 3 Challenge)

## Task

-Incorporated the cleaned versions of the columns from the data file into the code

-Visualize patterns using histograms between Respiratory Rate with the patients.

-Visualize patterns using histograms between Fio2 with the patients.

-Visualized patterns of Relationship between respiratory rate with Fio2 by plotting a scatter plot diagram with using python functions

-Used python functions to plot a scatter plot diagram to show the relationship of MAP and age
