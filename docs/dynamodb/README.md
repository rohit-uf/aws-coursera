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

- contains a subset of attributes from a Base Table along with an Alternate Key to support Query Operations
- make other fields searchable by making them `Key`
- This table is kept in sync with the Primary Table `Asynchronusly`
- Local Secondary Index: Enables to create an alternate SORT KEY
- Global Secondary Index: Enables to create alternate PARTITION KEY and SORT KEY

## Backup and Restoration

### Backup

- **Amazon DynamoDB On-Demand Backup**: Request -> Backup is done Asynchronously
- **Point in Time Recovery**: Automatic

```sh
# pass table-name and backup-name
aws dynamodb create-backup

# pass backup-arn
aws dynamodb describe-backup
```

### Restoring

- Restoring from **On-Demand Backup** -> Requires a destination table, Specify `Backup ARN`, Destination Table will be ready for use after Backup is complete
- Restoring from **Point in Time Backup** -> Specify Point in Time, which needs to be recovered

```sh
# pass target-table-name and backup-arn
aws dynamodb restore-table-from-backup
```

On the restored table, following needs to be set manually
- Autoscaling
- IAM Policy
- Cloudwatch Metrics
- Tags
- Time To Live Settings

> SCAN are paginated by default. No. of records returned are equal to --max-items limit or 1 MB whichever comes first
`--max-items` flag can be passed with an integer, specifying the upper limit for the no. of records to be returnecd

### BatchWriteItem

- Define multiple items to write to one table / multiple tables together in **1 Request**
- `Write` and `Delete` allowed. `Update` not allowed
- Failed items would be returned in `unprocessed item`

### BatchGetItem

- Allows to read multiple items across multiple tables
- Failed items would be returned in `unprocessed keys`

## Monitoring Amazon DynamoDB Tables

- Cloudtrail
- Cloudwatch
  - Read, Write Capacity Unit (RCU, WCU)
  - 1 RCU : 1 Strongly Consistent Read per sec / 2 Eventually Consisten Read per sec upto 4 KB
  - 1 WCU : 1 Write / Sec upto 1 KB
  - No of Items returned in each query
  - Latency
- AWS X-Ray

### RCU / WCU

- Consumed RCU / WCU over a time period, provided by Cloudwatch
- Total Consumed RCU / WCU
- Slow throughput --> Consumed RCU > Provisioned RCU (or WCU)
- More RCU would be used for entire table SCANs. Prefer Query and Filters

### DynamoDB Auto Scaling

- Dynamically adjust provisioned capacity
- Handle sudden increase in traffic


## Partition Keys

### Partition

- Data in DynamoDB is stored in Partitions
- Partitions are unit of storage, backed by SSD, replicated in multiple availability zones within the AWS Region
- As table grows, more partitions are added
- If only `partition key` is used for an item -> Hash the `partition key` and determine the partition to put the Item in
- If both `partition key` and `sort key` are used
  - Hash the `partition key` and determine the partition to put the Item in
  - Sort the item within that partition based on the `partition key`
- `Adaptive Capacity` : Automatically provision capacity (increase/decrease)

Notes: Read [here](https://www.coursera.org/learn/dynamodb-nosql-database-driven-apps/supplement/0u5SD/week-2-notes-and-resources)

## Security State

- All dynamodb data, related information and backups are encrypted at rest by default (On the hard drive)
- Can integrate with AWS Key Management Service
- `dynamodb-encryption-client` is a library, allows to include client side encryption in dynamodb library
- Server side encryption is provided by default
- Dynamo DB is HIPAA Compliant
- When integrating with Cloudfront, can choose **Key Level Encryption**
- Can use `Tokenization` for other compliance standards like PCI DSS (Payment card)

## TTL

- Time to live
- Once current time is greater than the TTL Attribute, the item is marked as expired
- Items that are expired, will be deleted within 48 hours
- Items that are expired, but not deleted will show up in Reads, Scans and Queries
- Can enable on each table
- When items are deleted, they are also deleted from any Secondary Index (Eventually Consistent) manner

## Access Control

- Authentication is used to access DynamoDB Resources, with **Credentials**
- Authorization is used to modify DynamoDB Resources, with **Permissions**
- Can be handled using IAM Roles
- Role Based Access Keys should be used as they expire and are rotated after a configured time 
- IAM Policy to assign permissions to API Endpoints for specific users
- VPC: Isolate virtual private cloud
  - If lambda code is inside a VPC, it needs to go through the Internet Gateway to reach DynamoDB
  - Any request to lambda code, must go through the Internet Gateway to reach VPC
  - VPC Endpoints: Used to route any request to a Regional Service, using Amazon's Private Network and not the Internet


## Global Tables
- To reduce latency for international users, tables can be replicated in different **AWS Regions**
- **Global Tables** can be created, which is used to replicate tables in different regions
- All replicated tables are kept in sync with the each other using `Streams`
- Whenever any `write` happens in one of the table, the change is pushed to all other tables via Streams
- Read is eventually consistent

### Streams
- Provide a `time-ordered` sequence of `item-level` changes in a table
- Allow to capture changes to a DynamoDB Table
  - Changes are applied `in-order`
  - Changes are applied in `real-time`
- Can also be used to capture certain events, and run business logic on invocation of those events
- Are kept independent of DynamoDB Implementation
> Full Text searching is not available in DynamoDB
- Can associate streams with fields that need to be text-searched. Once a new event appears in the stream, a Lambda Function can put that field with other relevant data inside an ElasticSearch Cluster

## Concurrency

### Concurrent Updates

- When multiple clients are reading and writing from the database at the same time, we need to make sure the data they are accessing is Consistent. 
- DynamoDB does not provide any row locking mechanism by itself. It needs to be handled by the developer 

### Optimistic Locking
- Can be implemented with `Conditional Writes`
  - PutItem
  - UpdateItem
  - DeleteItem
- Keep an attribute `version_number` on the Item to be updated or deleted
  1. Retrieve the version number before updating
  2. Check if the version number sent with update request, is the same as the version number in the table. Only then make the update
  3. After the update is complete, increment the version number  

## Secondary Index in detail

### LSI: Local Secondary Index
- Can only be created when the table is created
- Can not be created after the table has been created
- Have a different SORT KEY for indexing
- When a table is deleted, its LSIs are also deleted

### GSI: Global Secondary Index
- Can be created during table creation or later
- DynamoDB Handles synchronization of Base Tables with the GSIs
- On a provisioned Base Table, must specify Read/Write units

> Only create secondary indexes on attributes that are queried very often

## Querying
- `> , < , =` operators are available to query
- `AND, OR, IN, BETWEEN` operators can be used to filter
- `begins_with` , `contains`

### Single Table

- Unlike relational tables, where schema precedes queries. In dynamodb we should first know which queries we will require, and based on that we should design the tables
- To make querying efficient, create LSI and GSI
- **Transactions API** : To make a set of queries atomic.

### Time series data

- Data which is segregated on time series like quarterly, monthly etc, should be kept in separate tables for each time interval
- Data which is older, can be provisioned with less Read/Write Units
- Data which is newer can be provisioned to use more Read/Write units
- Amazon Timestream : Dedicated DB for time series data

## Faster Retrieval of Data

- In-Memory Cache
- Dynamo DB Accelarator (DAX)
  - Fully managed in-memory cache
  - microsecond response time
  - Scale easily
