# Firebase module
##### It's a module for integrate firebase services with the aplication, in this module you find all relations with the database conection and login and signup logic. For the implemententions of this module you must installer requirements.txt 

### auth module
##### In this module you find the controller file, in its file are signup and logic functions.
##### For implement this function you must take into account the following:

##### - *login* funcion recive __email__ and __password__ as positional arguments in it order.
##### _ *login* returns __None__ if user not exists or if user dates not are valids, in other case return user information.
##### - *signup* function receve  __username__, __email__ and __password__ as positional arguments un it order.
##### - *signup* returns __True__ if user already exists and __False__ if user already not exists.

### firestore_service.py
##### In this file you find the logic to connect to firestore database servces in this file are the functions to create and update collections and documents of user.

### Firebase Schemma
##### User collection is the entity and his atributes are:
##### - *email*, user email is the user_id, if user has already created account with his email, he will not be able to other account with the same email.
##### - *username*, this atribut contain an username to view in display
##### - *password*, this attribut contain the password hashed
##### - *news_sites*, this attribut contain the news sites names that user likes.
