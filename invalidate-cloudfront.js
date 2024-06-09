const AWS = require('aws-sdk');
AWS.config.update({ region: 'us-east-1' });

// Read distribution ID from environment variable
const distributionId = process.env.CLOUDFRONT_DISTRIBUTION_ID;

if (!distributionId) {
    console.error("Error: CloudFront distribution ID is not set.");
    process.exit(1);
}

const cloudfront = new AWS.CloudFront();

const params = {
    DistributionId: distributionId,
    InvalidationBatch: {
        Paths: {
            Quantity: 1,
            Items: ['/*'],
        },
        CallerReference: `${Date.now()}`
    }
};

cloudfront.createInvalidation(params, function (err, data) {
    if (err) {
        console.error("Error creating invalidation:", err, err.stack);
    } else {
        console.log("Invalidation created successfully:", data);
    }
});