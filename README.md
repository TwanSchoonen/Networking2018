# Networking2018
The repository used for Network-Computing course at the RUG
Authors: Peri Rahamim, Jits Schilperoort, Twan Schoonen.

To run the program, it is required to install all of the dependencies.

The first thing to do is to run mapapp (Map/mapapp.py). This will open map's main page, where centers are shown. Initially, the image is blank.

To create a center, open a new terminal window, and run the script center (App/center.py). The input needed to create a center is name, number of cars, and port used. After completion, a new center is added to map's main page. Clicking the circle with the center's name displays a city map with cars (as many as specified above) randomly moving around the city.
To return map's main page, press 'b'.

To add a costumer, first start restapp (RestApp/restapp.py), then open app (App/app.py). A menu will open, asking the user to choose an option between register client, logging in, change server ip, or exit. After user is logged in, choose an option between send a new order, see or change account details, and log out. When sending an order, the costumer is asked for center's name (an unexisting center name will result with an order that is in the queue but never handled), location coordinates (x is between 0-8, y between 0-6), number of passengers (maximum is 3), destination center (the program assumes it is the same center, so this option is not implemented), destination coordinates (again x and y as above). The program asks if the user wants to connect to localhost, if not, it asks for a new address.

When there's an available car to pick up costumer, the costumer along with its destination appear on the map until the car that is assigned to it picks up the costumer and brings them to their destination.
