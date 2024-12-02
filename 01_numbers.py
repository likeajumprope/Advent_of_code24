#first puzzle
import pandas as pd
numbers = pd.read_csv('01_numbers.txt', header=None, sep=' ')
print(numbers)

numbers = numbers.drop(columns=[1, 2])

print(numbers.columns.to_list())
df_sorted = numbers.apply(lambda col: col.sort_values().reset_index(drop=True), axis=0)
print(df_sorted)

df_sorted['AbsoluteDifference'] = (df_sorted[0] - df_sorted[3]).abs()
print(df_sorted['AbsoluteDifference'].sum())

# second puzzle
print(numbers[3].value_counts())

first_list_count = numbers[0].value_counts()
second_list_count = numbers[3].value_counts()


common_indices = first_list_count.index.intersection(second_list_count.index)
print(common_indices)
print(sum(first_list_count))


df2_subsection = second_list_count.loc[common_indices]
df2_subsection['multiplied'] = df2_subsection * df2_subsection.index
print(df2_subsection['multiplied'].sum())


    
