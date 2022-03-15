# Dynamo DB

## Relational Database

- Problem with Horizontal Scalability
- Normalization, JOINs are CPU Intensive Tasks
- NoSQL -> means `Not Only SQL` 

### CAP Theorem

For distributed systems, we can only guarantee two out of the following three properties:

1. Consistency : How the data is consistent in all the places. Strongly / Eventually Consistent Data
2. Availability : Data must be available for retrieval quickly
3. Partition Tolerance : System's Ability to maintain functionality, data-retention and promises through failures of network and components (This is generally a MUST)

## NoSQL Database

Don't work well for:

1. Self managed systems: Provisioning needs to be done manually
2. Data is stored in de-normalized form, so querying might become complex
3. No cross table relationship

### Types of NoSQL DB

1. Key-Value: DynamoDB
2. Column Based: Cassandra, HBASE
3. Document Based: MongoDB

## Dynamo DB

1. Streams
2. Transactions
3. Accelarator
4. Global Tables

### Concepts

1. Table
  - Collection of 0 or more items
  - Items that are organized for querying
  - Items are made up of attributes
  - `Primary Key | Partition Key` is the required attribute for all items
  - `Sort Key` : Can also be used to distinguish data. Ex: Artist: Partition Key, Song: Sort Key
  - Both can be used together to create a **Composite Key**
  - Dynamo DB On Demand

### Limitations

- Table size has no limit
- Maximum Item size -> 400KB
- Partition | Sort Key Min Length: 1 Byte
- Partition Key Max Length: 2048 Byte
- Sort Key Max Length: 1024 Byte

### Input Data Format
```js
{
  "Artist": {"S": "Artist Name"},
  "Field_name": {"field_type": "field_value"}
}
```

### Retrieving Data

#### Key Condition Expression

- Helps us query data from the DynamoDB Table based on certain values of Keys
- `--key-condition-expression "FieldName = :var_name AND FieldName = :var_name" --expression-attribute-values file://path_to_query_file`

```js
{
  ":var_name": {"field_type": "query value"}
}
```
- To delete items from DynamoDB we have to specify both Partition Key AND Sort Key (If sort key is defined)

> QUERY - Helps retrieve data using `Partition Key` or `Partition Key + Sort Key`
> SCAN - Retrieves all items from a table, similar to `SELECT * FROM TABLE`

- `--filter-expression` can be used to filter values from a SCAN result, to search on fields other than the Primary / Sort Key
- filtering happens after SCAN returns all its results, so it does not increase its efficiency

### Secondary Index

- Creates a copy of table, with an alternate schema
- Make other fields searchable by making them `Key`
- This table is kept in sync with the Primary Table `Asynchronusly`

> Local Secondary Index: Enables to create an alternate SORT KEY
> Global Secondary Index: Enables to create alternate PARTITION KEY and SORT KEy
