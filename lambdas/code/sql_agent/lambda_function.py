import json

from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_aws import  ChatBedrock
from utils import build_response

model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"

def lambda_handler(event, context):
    print (event)
    consulta = event.get("query")
    db = SQLDatabase.from_uri("sqlite:///Chinook.db")
    print(db.dialect)
    print(db.get_usable_table_names())

    llm =ChatBedrock(model_id = model_id, model_kwargs={"temperature": 0})
    agent_executor = create_sql_agent(llm, db=db, verbose=True)

    response = agent_executor.invoke(consulta)
    
    return build_response(200,json.dumps(response))

