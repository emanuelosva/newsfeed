# News Feed -- Backend

### About
A simple REST api to serve the backend service to the "**NewsFeed**" client build in REACT.
The api works with json-web-token authentication to access to routes and firebase storage and authentication for users info.

### Porpuse
- Make CRUD operations about the user information
- Get news info throgh a scraper implemented in xpath and send it to client

### Specifications
- The user can make sigup and storage his/her data
- The user can make login and acces to his/her data
- The user can subscribe to any news chanels
- The user can unsuscribe to any news chanel
- The api must send the info of the user to the client
- The api must send the principal 3 news of each chanel to wich the user is subscribed

### Work Instructions
In the backend dir route create a nuew python env
Run:

```bash
python3 -m venv .env
pip3 install -r requirements.txt
```

Each time you add a new package run:
```bash
pip3 freeze > requirements.txt
```

To start the server run the start.bash file
```bash
source start.bash
```

### API docs (Resume)

##### Entities
- User:
```js
// Schema

{
  id: str, // The user id (index)
  email: str, // The user email (index)
  name: str, // The user name
  password: str, // The user password
  subscriptions: [News] // The user subscriptions
}
```

- News:
```js
// Schema

{
  id: str // The new provider id
  name: str, // The name of the news provider
  url: str, // The url to site
}
```

- NewsResponse:

```js
// Schema

{
  name: str, // The name of the new
  abstract: str // Summary of new
  url_image: str // The url to news portrait
  url: str, // The url to site
}
```

##### End points

**Users**

> metjod: POST -- path: /users

Description: Add a news subscription to user subscriptions list
Body: { id: str, news_name: str }
Returns:
- Status: 201
- Type: Application/json
- Value: {
    "error": false,
    "message": "Suscribed"
}

> metjod: DELETE -- path: /users

Description: Remove a news subscription to user subscriptions list
Body: { id: str, news_name: str }
Returns:
- Status: 200
- Type: Application/json
- Value: {
    "error": false,
    "message": "Unsuscribed"
}

> method: POST -- path: /useres/signup

Description: Register a new user
Body: { name: str, email: str, password:str }
Returns:
- Status: 201
- Type: Application/json
- Value: {
    "error": false,
    "message": "User created"
}

> method: POST -- path: /usres/login

Description: Login a user
Body: { User schema }
Returns:
- Status: 201
- Type: Application/json
- Value: {
    "data": {
      "token": str, // jwt
      "user": {
          "name": str,
          "subscriptions": [str]
      }
    },
    "error": false,
    "message": "Logged"
}

**News**

> method: GET -- path: /news

Description: Retrieve the news info
Body: { url: url-to-news-provider }
Returns:
- Status: 200
- Type: Application/json
- Value: { NewsResponse schema }

**Complete documentation** 
Go to [docs](https://...)

