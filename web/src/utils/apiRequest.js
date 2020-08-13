import axios from 'axios';

export const apiRequest = async (endPoint, method, data, _headers) => {
  return await axios({
    url: `https://newsfeedapi.vercel.app${endPoint}`,
    headers: _headers,
    method,
    data: { ...data }
  });
};
