import pandas as pd
numbers = pd.read_csv('02_numbers.txt', header=None, sep=' ')
print(numbers)

row_diff = numbers.diff(axis=1)

row_diff.drop(columns=[0], inplace=True)
print(row_diff)

results_positive = []  # Store results for each row
for index, row in row_diff.iterrows():
    row_no_nans = row.dropna()  # Drop NaN values
    if ((row_no_nans > 0) & (row_no_nans < 4)).all():  # Check if all entries satisfy the condition
        results_positive.append(True)
    else:
        results_positive.append(False)

print(sum(results_positive))

results_negative = []  # Store results for each row
for index, row in row_diff.iterrows():
    row_no_nans = row.dropna()  # Drop NaN values
    if ((row_no_nans < 0) & (row_no_nans > -4)).all():  # Check if all entries satisfy the condition
        results_negative.append(True)
    else:
        results_negative.append(False)

#print(sum(results_negative))

#print(sum(results_positive) + sum(results_negative))

# puzzle 2
count = 0
results_positive = []  # Store results for each row
for index, row in row_diff.iterrows():
    row_no_nans = row.dropna()  # Drop NaN values
    row_result_positive = []
    for i, col in enumerate(row_no_nans.index):
    # Drop the i-th element of the row
        modified_row = row_no_nans.drop(labels=col)
        #print(modified_row)
        if ((modified_row > 0) & (modified_row < 4)).all():  # Check if all entries satisfy the condition
            row_result_positive.append(True)
        else:    
            row_result_positive.append(False)
        #print(row_result_positive)
    if any(row_result_positive):
        count = count +1

print(sum(results_positive))

results_negative = []
count = 0# Store results for each row
for index, row in row_diff.iterrows():
    row_no_nans = row.dropna()  # Drop NaN values
    row_result_negative = []
    for i, col in enumerate(row_no_nans.index):
    # Drop the i-th element of the row
        modified_row = row_no_nans.drop(labels=col)
        #print(modified_row)
        if ((modified_row < 0) & (modified_row > -4)).all():  # Check if all entries satisfy the condition
            row_result_negative.append(True)
        else:    
            row_result_negative.append(False)
    #print(row_result_negative)
    if any(row_result_negative):
        count = count +1
        
print(count)
        

#print(sum(results_negative))
#print(sum(results_positive))
#print(sum(results_positive) + sum(results_positive))
            

#print(sum(results_negative))

#print(sum(results_positive) + sum(results_negative))
