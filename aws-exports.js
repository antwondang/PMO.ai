// aws-exports.js
const awsConfig = {
    Auth: {
      identityPoolId: 'YOUR_COGNITO_IDENTITY_POOL',
      region: 'YOUR_REGION',
      userPoolId: 'YOUR_USER_POOL_ID',
      userPoolWebClientId: 'YOUR_CLIENT_ID',
    },
    API: {
      endpoints: [
        {
          name: 'financeApi',
          endpoint: 'YOUR_API_GATEWAY_URL',
          region: 'YOUR_REGION'
        }
      ]
    }
  };
  
  export default awsConfig;
  