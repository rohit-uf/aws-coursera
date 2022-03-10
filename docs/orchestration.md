# Orchestration

## Event

- Indicate something happened
- PRODUCER -> CONSUMER

### EventRouter 

- Producer publishes events to the Router
- EventRouter will filter and PUSH the events to Consumers
- Producer and Consumer are decoupled --> Better Scaling

### SQS: Simple Queue Service

- Can send, store and retrieve messages between producers and consumers
- Standard Queue
  - Maximum throughput
  - Best effort ordering
  - Atleast one delievery

2. FIFO
- Guarantee that messages are delievered once
- Maintain order in which the messages were sent while retrieving

Both Producers and Consumers need to send HTTP Requests to Publish/Retrieve messages

### SNS: Simple Notification Service

- Follows a Pub/Sub (Publish/Subscribe) Model
- Push based Many to Many messaging
- Supports Mobile Push, SMS and Email

### EventBridge

- Service Bus
- Has a feature called **Schema Registry**. stores Event Structure or Schema in a Shared Central Location 
