#!/usr/bin/env python3
from aws_cdk import App,Environment
from aws_lookout_vision.aws_lookout_vision_stack import AwsLookoutVisionStack
from AppConfig.config import Config

_config = Config()

app = App()

env = Environment(account=_config.account, region=_config.region)

AwsLookoutVisionStack(app,_config.stackname,env=env)

app.synth()
