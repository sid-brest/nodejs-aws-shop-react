from aws_cdk import (
    Stack,
    aws_iam as iam,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
    aws_cloudfront_origins as origins,
    aws_s3_deployment as s3deploy,
    RemovalPolicy,
    App,
    CfnOutput
)
from constructs import Construct

class CdkPythonStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create S3 bucket for static website
        bucket = s3.Bucket(self, "NodejsAwsShopReactDzmitryStruneuskiBucket",
                           bucket_name="nodejs-aws-shop-react-dzmitry-struneuski",
                           removal_policy=RemovalPolicy.DESTROY,
                           block_public_access=s3.BlockPublicAccess(
                               block_public_acls=False,
                               block_public_policy=False,
                               ignore_public_acls=False,
                               restrict_public_buckets=False
                           ),
                           auto_delete_objects=True,
                           versioned=False)

        oai = cloudfront.OriginAccessIdentity(self, "NodejsAwsShopReactDzmitryStruneuskiOAI",
                                              comment="Allows CloudFront to reach S3 bucket")

        # Create CloudFront distribution
        distribution = cloudfront.Distribution(self, "NodejsAwsShopReactDzmitryStruneuskiWebsiteDistribution",
                                               default_root_object="index.html",
                                               default_behavior=cloudfront.BehaviorOptions(
                                                   origin=origins.S3Origin(bucket, origin_access_identity=oai),
                                                   viewer_protocol_policy=cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS
                                               ))

        bucket.add_to_resource_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions=["s3:GetObject"],
            resources=[bucket.arn_for_objects("*")],
            principals=[iam.CanonicalUserPrincipal("cloudfront.amazonaws.com")],
            conditions={"StringEquals": {"AWS:SourceArn": f"arn:aws:cloudfront::{self.account}:distribution/{distribution.distribution_id}"}}))
        bucket.grant_read(oai)

        # Create S3 deployment
        s3deploy.BucketDeployment(self, "NodejsAwsShopReactDzmitryStruneuskiDeployWithInvalidations",
                                  sources=[s3deploy.Source.asset("./dist")],
                                  destination_bucket=bucket,
                                  distribution=distribution,
                                  distribution_paths=["/*"])

        # Output CloudFront Distribution ID
        CfnOutput(self, "CloudFrontDistributionId",
                  value=distribution.distribution_id,
                  description="The CloudFront distribution ID")

app = App()
CdkPythonStack(app, "CdkPythonStack", env={'region': 'us-east-1'})

app.synth()