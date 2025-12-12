# Pandas

## Accessing

```
df.loc[0, 'Name']  # Access by label
df.iloc[0, 0]      # Access by position
```

## Filter

```
df[df['Age'] > 25]
```

## GroupBy Operations

The `groupby()` method allows you to group data based on certain criteria and apply aggregate functions like sum, mean, etc.

You can apply aggregate functions like sum(), mean(), count(), etc., to groups or entire DataFrames.

```
df = pd.DataFrame({'Category': ['A', 'A', 'B', 'B'],
                   'Values': [10, 15, 10, 20]})

df.groupby('Category').agg({'Values': ['sum', 'mean']})
```

## Merging & Joining

- `merge()`: SQL-style merging with a variety of join types (inner, outer, left, right).

```
df1 = pd.DataFrame({'Key': ['A', 'B', 'C'],
                    'Value1': [1, 2, 3]})

df2 = pd.DataFrame({'Key': ['A', 'B', 'D'],
                    'Value2': [4, 5, 6]})

merged_df = pd.merge(df1, df2, on='Key', how='inner')
# inner, outer, left, right
```
- `join()`: Combines DataFrames based on index.

```
df1.join(df2.set_index('Key'), on='Key')
```

- `concat()`: Concatenates along a particular axis (row-wise or column-wise).

## Reshaping DataFrames

- `pivot_table()`: allow you to reorganize data based on specific categorical variables.

```
df.pivot_table(values='Values', index='Category', aggfunc='sum')
```

- `stack()` and `unstack()`: Pivot columns to rows and pivot rows to columns.

```
stacked = df.stack()
unstacked = stacked.unstack()
```

- `apply()`: Applies a custom function to dataframe.

```
def add_two(x):
    return x + 2

df['Values'] = df['Values'].apply(add_two)

df.apply(lambda row: row.sum(), axis=1)
```

## Working with Timeseries

```
df['Date'] = pd.to_datetime(df['Date'])

df.resample('M').sum()  # Resample by month
df.shift(1)             # Shift rows by 1
```

## MultiIndexing

andas allows hierarchical indexing (MultiIndex) for working with more complex data.

```
arrays = [['A', 'A', 'B', 'B'], [1, 2, 1, 2]]
index = pd.MultiIndex.from_arrays(arrays, names=('Group', 'Subgroup'))
df = pd.DataFrame({'Values': [10, 15, 10, 20]}, index=index)

df.loc['A']
df.xs(1, level='Subgroup')
```

## Efficient Data Handling

- `read_csv()` with `chunksize` to process data in chunks for memory efficiency.
- `HDF5` storage using `HDFStore()` for fast reading/writing of large datasets.
