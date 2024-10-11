import aws_cdk as core
import aws_cdk.assertions as assertions

from serverless_sql_agent.serverless_sql_agent_stack import ServerlessSqlAgentStack

# example tests. To run these tests, uncomment this file along with the example
# resource in serverless_sql_agent/serverless_sql_agent_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ServerlessSqlAgentStack(app, "serverless-sql-agent")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })