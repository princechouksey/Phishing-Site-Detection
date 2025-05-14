import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'; // FastAPI backend URL

export const detectPhishing = async (url) => {
  try {
    console.log('url at api ---->', url);
    
    const response = await axios.post(`${API_URL}/detect_phishing`, { url });
    return response;
  } catch (error) {
    throw new Error('Failed to fetch data from the backend');
  }
};
