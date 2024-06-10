#!/usr/bin/env python3
import aws_cdk as cdk
from cdk_python_stack import CdkPythonStack

app = cdk.App()
CdkPythonStack(app, "CdkPythonStack", env={'region': 'us-east-1'})

app.synth()