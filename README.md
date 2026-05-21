# carisurg-portfolio
# Mercer General Project (Day 1 Challenge)

##This code cleans the data from the Gender column and processes it using libraries from Python such as panda in Google collab.

## Tasks
-Connected the file "EmergencyTriageDataset_Reduced_Dirty.csv" from Google Drive to Google Colab
-Cleaned Gender Column in the file
-Checked for outliers such as Nan Values
-Replaced the unclean Gender column with the cleaned version

## Reduced 6 different entities representing 2 genders male and females as:

-1 = Male
-0 = Female

Mercer General Project (Day 2 Challenge)

##Task
-We first practiced on the GCS data, familiarizing ourselves with the general cleaning processes, especially with the median portion
-The Pulse Column cleaning process began by inspecting of the pulse row data, by checking the count of unique values and the frequency of certain values. 
-Then once familiarized  with the data, the non numeric values was converted to numeric, and also established the range.
-Incorporated logical masks (df.loc) to scan the columns for values outside valid boundaries any rows holding these impossible numbers that were immediately replaced with NaN placeholders.
-Next the data was with median because the data was skewed, as seen by both min and max values. The median was observed to be the best imputation method
-A visualization graph was drafted in order to actually see the data after it was cleaned, for further understandability.

## The resulting dataset was NaN = 0 because it was imputed with the median
