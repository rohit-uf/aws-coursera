# AWS Step Functions

- Used to create **workflows** a.k.a **State Machines**
- State Machines are composed of **States** (1 Step in a workflow, ex: calling a function)
- No server management required

**State Machine**
- Collection of states
- Allows to perform tasks in a sequence
- Written in  **Amazon States Language**
- States make decision based on input, perform actions and provides output

**Task**

- Represent one unit of work done through activities or AWS Services 


`"Input.$": "$"` : Allows to pass the input recieved in one task to another resource
- Step functions integrate with a lot of AWS Services

3 Ways services can be integrated with AWS Step functions

1. Call a function, and proceed without waiting for the response
2. Call a function, and wait for the response
3. Call a function with a task token
**Blog**

1. [State Types](https://docs.aws.amazon.com/step-functions/latest/dg/input-output-example.html)

- Integrating API Gateway with Step Functions

- In `Method Request`, choose AWS Services and then AWS Step Functions from the dropdown
- It needs to have an **IAM Role** with the relevant permissions for executing the Step Function
- It also needs to provide the Action as **StartExecution** which needs to be started
- `ARN` for the state machine needs to be sent in the Request in the field **stateMachineArn**
  - We can use VTL to inject the ARN in the incoming request

## Integration Patterns
1. Request-Response: Just sends the job, without caring about its completion
2. Run a Job (synchronus)
  1. ARN.sync
  2. Returns whether the job was successful or not

3. Wait for callbacks(task token)
  1. ARN.waitForTaskToken and pass a TaskToken in the body
  2. SendTaskSuccess/SendTaskFailure event needs to be send back with the same TaskToken recieved in the request originally
  3. Job Status + Job Output would be returned

Task Type: Activity
-> External Integration
![image](https://user-images.githubusercontent.com/97154676/156178395-fc7560a3-0a82-441b-b1be-16b5ad81babb.png)


Step Function
1. Standard Workflow
2. Express Workflow

### Express Workflow
1. 20 times Faster
2. Persists state In-Memory only
3. Prices based on Duration, not by the no. of state transitions
4. Does not support Sync or TaskToken pattern of Integration
