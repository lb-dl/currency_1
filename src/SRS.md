# e-mandruy django app

### Vision
E-mandruy web application is based on Django app and various micro-services. It provides
users with functionality of searching and viewing hotels, transport, restaurants and weather
information. As a user you can sign up, sign in and see a profile page, where you can edit
your personal information.

### Intended Audience
This project is a web application which provides users with detailed information that could be used while
planning journeys and trips. Users can easily find the information about hotels, restaurants, transport 
and weather forecast in a chosen city. The application offers online hotels reservation and bookings for cars.
The E-mandruy application also offers a subscription to the services to provide users daily with available information.
The application would be useful for travellers and travel agencies as well.

### The project should provide:
- Store the account information of all the users in a database;
- Get the information about hotels through parsing and storing it in the database;
- Get the information about restaurants through parsing and storing it in the database;
- Get the information about routes and means of transport through parsing and storing it in the database;
- Get the information about weather through REST API and storing it in the database;
- Display a list of all hotels in a choosing city;
- Book a room in the hotel which is chosen;
- Send booking information to the customer's email and telegram chat;
- Get user's comments and rate the hotel, then store them in the database;
- Display a list of all restaurants in a choosing city;
- Display a list of all routes and means of transport between choosing cities;
- Display detailed weather information and a short description for the three next days in a choosing city;
- Update the list of hotels (adding, removing);
- Update the list of restaurants (adding, removing);
- Update the list of routes and means of transport (adding, removing);
- Update the list of weather (adding, removing);
- Search and display statistics data for routes and means of transport;
- Get the user's subscription to chosen services;
- Send daily emails, according  to the user's subscription, with the information 
  from hotel, restaurant, transport and weather applications during the period of subscription.

###  Entity–relationship model 
The major features of database system is shown in below entity–relationship model (ER model)

![static/images](/home/lbdl/Desktop/django/Dp-207_Python/django_app/static/images/model.png)

1. Users
   <br>
   <br>
    1.1 User account control  
<br>
    The application allows multiple, unrelated users to use the same project. That is why, each user should have
   a private login account for the system. 
<br>

- Application displays "Sing Up" form for registration;
- User enters username, email, password, password conformation and presses “Register Account” button;
- If any data is entered incorrectly, incorrect data message is displayed;
- If the user with the email has already existed, then error message is displayed;
- If entered data is valid, then the email and password are adding to database;
- Then the application displays "Sign in" form;
- User enters the username and password and presses "Sign in" button;
- If entered data is valid, the page with "profile" is shown;
- If any data is entered incorrectly, incorrect data message is displayed.  
    <br>
    1.2 Managing user's personal information
  <br>
  <br>
   On the "Home" page, authorized users can manage their personal information, such as email, username and password.
  <br>
- The application shows some input boxes in order to change personal information;
- User enters a nickname or password in order to change them;
- When a new nickname is entered, user presses "Change Nickname" button;
- The message "Nickname has changed successfully" is shown;
- To change a password three input boxes must be filled;
- When "Old password", "New password and "New password-confirmation" fields are filled, 
  user presses "Change Password" button;
- If any data is entered incorrectly, incorrect data message is displayed.
- If the entered data is valid, "Login" form is shown;
- Users can sing out by pressing "Sing out" button;
- When the "Sign out" button is pressed, the "Home" page without "Profile" and "Log in" form is shown.

2. Hotels application
   <br>
   <br>
    2.1 Hotels control  
<br>
    The application allows users to search and view a list of hotels in a chosen city in Ukraine.
<br>

- When a user presses the "Hotels" button on the navbar, the list of the top five hotels is shown;
- The application also shows an input box, which users fill with a city name;
- When a city name is entered, users press "find hotels" button;
- If the city exists, the list of 5 hotels is shown;
- If there are more than five hotels are parsed, users can press the "Next Page" button to see the next five hotels;
- If users want to go back to the previous page, "Previous Page" button must be pressed;
- A list of comments and the hotel rate are shown for both authorized and unauthorized users.
  <br>
  <br>
    2.2 Book a room in a hotel
  <br>
  <br>
   On the "Hotels" page, users can book a room in a  chosen hotel.
  <br>
  <br>
- To book a room in a hotel, users press on the hotel name;
- The detailed booking information and two input fields are shown;
- When dates for sing in and sing out are chosen, users press "check dates" button;
- If available variants for the chosen dates exist, the sort description and prices for each option are shown;
- If users want to book a room, the "забронировать" button must be pressed then the detailed booking
  information and a message "Ваша бронь успешно добавлена" are shown;
- An email with booking information is sent to the user email.
  <br>
  <br>
    2.3 Leave a comment and rate a hotel
  <br>
  <br>
   On the "Hotels" page, authorized users can leave a comment and rate a hotel.
  <br>
  <br>
- If a user is authorized, they can leave a comment or rate a hotel;
- To rate a hotel users chose a number in a range from 1 to 5 and press "Rate" button;
- A message with the chosen rate is shown;
- If a user has already rated the hotel, they cannot rate it again;
- To leave a comment, users fill the text input field and press the "Add Comment" button;
- When "Rate" or/and "Add Comment" button is pressed the input data is saved in the database.

3. Restaurants application
   <br>
   <br>
    3.1 Restaurants control  
<br>
    The application allows users to search and view a list of restaurants in a chosen city in Ukraine.
<br>

- When a user presses the "Restaurants" button on the navbar, the drop-down menu is shown;
- Users can choose a city from a drop-down menu to see a list od parsed restaurants in a chosen city;
- When a city name is entered, users press "Search" button;
- If the city exists, the list of 20 restaurants with detailed information is shown;
- If there are more than 20 restaurants are parsed, users can press the "Next Page" button 
  to see the next 20 restaurants;
- If users want to go back to the previous page, "Previous Page" button must be pressed.

4. Restaurants application
   <br>
   <br>
      4.1 Transport control  
  <br>
      The application allows users to search and view a list of train and car routes between two chosen
      cities in Ukraine which are available for a certain date.
  <br>

- When a user presses the "Transport" button on the navbar, the three input fields are shown;
- The application also shows two boxes to choose means of transport;
- When a departure city name, arrival city name and a date are entered, users press the "Search" button;
- There are two means of transport - train and car, which are chosen by default. If users want to find information only
  for one means of transport, they can untick an unnecessary box;
- If the cities exist, the list of available routes with detailed information for chosen means of transport is shown;
- If car routes exist, the booking service is available;
- To book a car for the chosen date between chosen cities, users press "Reserve" button;
- When the "Reserve" button is pressed, users are redirected to "Bla-bla_car" site to reserve a seat.
  <br>
  <br>
5. Weather application
   <br>
   <br>
      5.1 Weather control  
  <br>
      The application allows users to search and view a detailed weather forecast for a current day and 
      a short weather description for the next three days in a chosen city all round the world.
  <br>

- When a user presses the "Weather" button on the navbar, the input field is shown;
- When a city name is entered, users press the "Submit" button;
- If the city exists, the table with detailed weather information for the chosen city is shown;
- The table is also displays a short weather description for the next three days in the chosen city; 
- If the entered city does not exist, a message 'City does not exist!' is shown.
  <br>
  <br>
6. Telegram bot
   <br>
   <br>
      6.1 Telegram bot control  
  <br>
      Telegram bot works with hotels, transport and weather services.
  <br>

- Users choose a certain service to get available information from an application;
- When the data is received from the chosen service, users are sent a message with the data on telegram;
- When users book a room in a hotel, the telegram bot sends an email with booking information to the users' emails.
  <br>
  <br>
7. Django subscription application
   <br>
   <br>
      7.1 Subscription control  
  <br>
      Django subscription application allows customers to choose services to get daily emails
      with information from hotels, transport, restaurants and weather applications during the 
      period of subscription.
  <br>

- Users subscribe to a certain service to get available information from a chosen application;
- Data is received from the chosen service and users are daily sent an email with the data;
- If users do not want to receive emails anymore, they can unsubscribe from the service.
  <br>
  <br>
