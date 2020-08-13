import sirv from 'sirv';
import compression from 'compression';
// import helmet from 'helmet';
import * as sapper from '@sapper/server';
import axios from 'axios';
const coockieSession = require('cookie-session');
const express = require('express');

const { PORT, NODE_ENV } = process.env;
const dev = NODE_ENV !== 'production';
const API = 'https://newsfeedapi.vercel.app';

const server = express();

// Security headers
// server.use(helmet());

// Parse req
server.use(express.json());
server.use(express.urlencoded({ extended: true }));

// Session manage
server.use(coockieSession({
  secure: !dev,
  httpOnly: !dev,
  secret: process.env.SECRET_COCKIE || 'secret',
  maxAge: 1000 * 60 * 60 * 24 * 5,
}));


/**
 * ------------- Proxy api routes --------------
 */

// Manage login
server.post('/server/login', async (req, res) => {
  const { body } = req;
  try {
    const { status, data } = await axios({
      url: `${API}/users/login`,
      method: 'POST',
      data: { ...body },
    });

    req.session.token = data.data.token;
    res.send(data.data.user);
  } catch (error) {
    res.status(error.response.status).send(error)
  }
});

// Destroy coockie session
server.post('/server/logout', (req, res) => {
  req.session = null;
  res.status(200).send('Logout')
});

// New subscription
server.post('/server/subscribe', async (req, res) => {
  const { body } = req;
  try {
    const { status, data } = await axios({
      url: `${API}/users`,
      headers: { Authorization: `Bearer ${req.session.token}` },
      method: 'POST',
      data: { ...body },
    });

    res.status(200).send('Subscrined');
  } catch (error) {
    res.status(error.response.status).send(error)
  }
});

// New subscription
server.delete('/server/unsubscribe', async (req, res) => {
  const { body } = req;
  try {
    const { status, data } = await axios({
      url: `${API}/users`,
      headers: { Authorization: `Bearer ${req.session.token}` },
      method: 'DELETE',
      data: { ...body },
    });

    res.status(200).send('Unubscrined');
  } catch (error) {
    res.status(error.response.status).send(error)
  }
});

// Static server
server.use(compression({ threshold: 0 }));
server.use(sirv('static', { dev }));
server.use(sapper.middleware());

// Server initialization
server.listen(PORT, (err) => {
  if (err) throw new Error('Server Error');
});
