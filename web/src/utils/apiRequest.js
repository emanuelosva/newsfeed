import axios from 'axios';

export const apiRequest = async (endPoint, method, data, _headers) => {
  return await axios({
    url: `https://newsfeedapi.vercel.app${endPoint}`,
    headers: _headers,
    method,
    data: { ...data }
  });
};

export const apiError = (err) => {
  const stringError = String(err);
  const statusCode = Number(stringError.split(" ").slice(-1)[0]);
  if (statusCode === 400) return 'Enter the correct data';
  if (statusCode === 401) return 'Invalid credentials';
  if (statusCode === 409) return 'The email is already registred';
  return 'An error was ocurr';
};
