# AWS Lambda

- Compute Service
- Run code without managing instance --> On demand
- The code is run on highly available infrastructure
- Performs all administration of Compute Resources
  - Server Maintainance
  - Capacity Provisioning
  - Automatic Scaling
  - Code Monitoring and Logging

- Run Code :
  - In response to events
  - Integrate with REST API
  - Invoke using SDK/CLI


**LAMBDA FUNCTION**: Packaging of Code that processes events

**RUNTIME**: Allows functions in different languages to execute in same `Base Environment`

Responsible for relaying
- Context information
- Event information

### PROPERTIES

1. Event
   1. JSON Formatted document containing data for a function to process
   2. LAMBDA Runtime converts event to an object, and passes it to our function
2. Concurrency
   1. No of requests, our function is serving at any given time
3. Trigger
   1. Resource / Configuration that invokes the lambda function
   2. EVENT SOURCE MAPPING: Reads item from a stream/queue and invokes a function


**Lambda Execution Environment / Runtime**

1. Environment in which the code runs
2. A micro virtual machine, which uses Open source virtualization technology- [Firecracker](https://firecracker-microvm.github.io/) spins up by default
3. Custom runtime can be modified using `Configuration Settings`

- **Runtime**
  - Has the resources in the language of the code
  - Responsible for running function code
  - Responsible for taking input data from Lambda Runtime API, and passing it to the function (Handler), and then posts function response back to Lambda Service
- **Custom Runtime**: Needs to be built ourselves

TIMEOUT: Time for which the lambda function will wait, before timing out on the request. **(Can be maximum of 15 Minutes)**

**Environment Variables**

Pass environment variables without having to change the code


### Permissions

- Role Based Access
  - Create a IAM Role
  - Assign Permission Policy to that IAM Role
  - Any AWS Service can apply for `Temporary Credentials` provided by:
  - Credentials are provided by `AWS Security Token Service`
  
1. **Execution Permissions**
   1. Defines, what Lambda Function is allowed to do
   2. Create an IAM Role with access to the relevant permissions, that Lambda Function will need
   3. Associate that role with Lambda Function 
2. **Resource Based Policy**
     - Defines who is allowed to access and manage Lambda Function


### [Invocation Latency](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html)

- When lambda function is invoked for the first time, it takes time to start up resources (VM, Memory) --> Cold start
- After the first invocation, these resources are kept up for a while, to wait for another lambda function invocation


### Cold Start

- When a lambda funcion is invoked:
  - It loads the Micro VM
  - It loads the Lambda Function Code
  - It runs all the code except the handler() method (imports libraries, makes connections)
  - At last, it runs the **handler()** method

- This is called **Execution Context**
- This context is saved for some time limit (15 mins) before it is destroyed
- **Provision Concurrency**: Feature that keeps calling the lambda function and keeps N no of contexts warm and ready to be used

### VPC Connections

- ENI



### Invocation Methods

- PUSH
  - When an **external event** is pushed to the Lambda Function. By API Gateway, or by some external trigger
  - Synchronus or Asynchronus

- PULL
  - When Lambda function pulls some events from external sources. Like from a Queue
  - Need an `Event Source Mapping`, to tell **Lambda Service** to pull events from Amazon SQS, and pass them on to **Lambda Function**
  - Amazon Kinesis Stream
  - Amazon Dynamo DB Stream
  - Asynchronus
  
### Invocation - PUSH Method

**Synchronous**
1. Request + Wait for Response
2. Keep the connection open until the response is received

**Asynchronous**

1. Request + Get response, stating that lambda will execute asynchronusly

2. Client need not wait for lambda to execute

3. Problematic, if an error occurs during lambda execution

4. `Maximum Retries`: A setting that tells lambda to re-execute if an error occurs, how many number of times

5. `Maximum Age of Events`: How long to keep uncompleted asynchronus lambda events in the queue

6. `Dead letter queue`: If maximum age + maximum no of retries exceeds, the event can be moved to an Amazon SNS/SQS queue

### Lambda Destinations

1. Send messages to **SQS/SNS/Another Lambda** on success, failure (Completion of execution) of lambda

> System creates a new version of the function, each time the lambda function is Published

A Version contains
- Code
- Configurations
- Amazon Resource Name (ARN)

**ALIAS**

- Can be used to refer to the latest published version of Lambda
- Can be accessed via its ARN
```sh
create-alias --function-name --name --alias-name
update-alias --function-name --name --alias-name
``` 

### Handler

```py
def handler(event, context):

event = Details about the incoming request
context = Details about the invocation (Request ID, Version Number, ARN, Execution environment details)
```