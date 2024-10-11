from aws_cdk import Duration, aws_iam as iam, aws_lambda

from constructs import Construct

LAMBDA_TIMEOUT= 900

BASE_LAMBDA_CONFIG = dict (
    timeout=Duration.seconds(LAMBDA_TIMEOUT),       
    architecture=aws_lambda.Architecture.ARM_64,
    tracing= aws_lambda.Tracing.ACTIVE)


class Lambdas(Construct):

    def __init__(self, scope: Construct, construct_id: str,  **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ======================================================================
        # SQL Agent Serverless using SQL Lite
        # ======================================================================
        self.sql_agent = aws_lambda.DockerImageFunction(
            self, "SQLAgent", memory_size=512,
            code=aws_lambda.DockerImageCode.from_image_asset(
                "./lambdas/code/sql_agent/",
                cmd = [ "lambda_function.lambda_handler" ],
                ),
            **BASE_LAMBDA_CONFIG)
        


        for f in [ self.sql_agent ]:
            f.add_to_role_policy(iam.PolicyStatement(actions=['bedrock:*'],resources=["*"]))
