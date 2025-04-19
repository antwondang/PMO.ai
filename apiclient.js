// ApiClient.js
import { withAuthInfo } from '@propelauth/react';
import axios from 'axios';

export default withAuthInfo(({ accessToken, makePrediction }) => {
  const predict = async (prompt) => {
    try {
      const response = await axios.post(
        'https://your-api.execute-api.region.amazonaws.com/predict',
        { prompt },
        { headers: { Authorization: `Bearer ${accessToken}` } }
      );
      return response.data.prediction;
    } catch (error) {
      console.error('Prediction failed:', error);
    }
  };

  return (
    <Button 
      title="Get Financial Prediction" 
      onPress={() => makePrediction(prompt)} 
    />
  );
});
