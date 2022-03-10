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

### Dynamo DB

1. Streams
2. Transactions
3. Accelarator
4. Global Tables

#### Concepts

1. Table
  - Collection of 0 or more items
  - Items that are organized for querying
  - Items are made up of attributes
  - `Primary Key | Partition Key` is the required attribute for all items
  - `Sort Key`
  - Dynamo DB On Demand

#### Limitations

- Table size has no limit
- Maximum Item size -> 400KB
- Partition | Sort Key Min Length: 1 Byte
- Partition Key Max Length: 2048 Byte
- Sort Key Max Length: 1024 Byte
