# <h1 align="center"> My Web Browser 🌐</h1>

## What is a Web Browser 🔁?
A web browser (also referred to as an Internet browser or simply a browser) is application software for accessing the World Wide Web or a local website. When a user requests a web page from a particular website, the web browser retrieves its files from a web server and then graphically renders the page on the user's screen.

## What is a Search engine 🔍?
A search engine is a kind of website through which users can search the content available on the Internet. For this purpose, users enter the desired keywords into the search field. Then the search engine looks through its index for relevant web pages and displays them in the form of a list.

### NOTE :
A web browser is not the same thing as a search engine, though the two are often confused. A search engine is a website that provides links to other websites. However, to connect to a website's server and display its web pages, a user must have a web browser installed.

![image](https://user-images.githubusercontent.com/104165177/191278259-052adddb-7319-462f-96ed-fb63cb8a7332.png)

#### This project is a browser made using python.
This browser has features like:
- Previous - Navigates to previous page
- Next - Navigates to the next page
- Refresh - Reloads the page
- Home - Navigaves to home page
### About technologies used :
- The module used here is PyQt5.
-  About Qt :- Qt is set of cross-platform C++ libraries that implement high-level APIs for accessing many aspects of modern desktop and mobile systems. 
-  These include location and positioning services, multimedia, NFC and Bluetooth connectivity, a Chromium based web browser, as well as traditional UI development.
-  About PyQt5 :- PyQt5 is a comprehensive set of Python bindings for Qt v5. 
-  It is implemented as more than 35 extension modules and enables Python to be used as an alternative application development language to C++ on all supported platforms including iOS and Android. 
-  PyQt5 may also be embedded in C++ based applications to allow users of those applications to configure or enhance the functionality of those applications.
 
### Tab 1
![tab1](https://user-images.githubusercontent.com/104165177/191575462-6b807a05-4f3b-4fc0-9e5e-6cda594c6892.png)
### Tab 2
![tab3](https://user-images.githubusercontent.com/104165177/191575527-1c0b6bcc-7e2e-4d28-ad9b-711fa1d92365.png) 
### Tab 3
![tab4](https://user-images.githubusercontent.com/104165177/191577454-dd9d295d-47b3-42df-bb6a-b53a5656046e.png)
### Code Explanation:
- a. sys : Different parts of the runtime module are manipulated with this module. It provides various functions and variables to do this.
- b. PyQt5: It is a module which helps in building Graphical User Interface modules in Python.
- c. QtCore: This module contains Non-Graphical User Interface functionality.
- d. Qtwidgets: User Interface is created in Qt with the help of them.
- e. QtWebEngineWidgets: This framework embeds the web content in the application.
- f. QAction(): Each command is represented as an action with the help of QAction.
- g. triggered : For instance: if the Home button is clicked it will connect it to the NavigateHome. It means that if we click the button it will be triggered to perform some action.
- h. connect(): For instance: if we click ReloadButton it will connect it to the browser. Basically, it is used to connect.
- i. addAction(): For adding any action this method is used.
- j. QLineEdit(): Keyboard input is received with this widget.
- k. text(): It is used to get the value.
- l. urlChanged: If the url is changed, urlChanged is used.
- m.setText: The value of the textbox is set with this widget.
- n. QApplication:This class manages main settings and Graphical User Interface control flow.
- o. setApplicationName(): Title of the main window is set by this widget.
- p. exec(): Execution of the QApplication object in the event loop is done with exec().
### Tab 4
![tab3](https://user-images.githubusercontent.com/104165177/191654957-679d93f6-7f53-45e3-b9b7-cc4135b79ef7.png)


### Reason why I have used Ecosia as my search engine :
- Plant trees by doing nothing
#### Ecosia Is a Privacy-Friendly Search Engine

- While Ecosia uses a tracking tool to collect a small amount of data to optimize their services, they don't use any external or third parties. This way, they can prevent others from accessing your searches and using the data.
- Each time we search for a result the count of trees increases in the right most corner of the browser indicating the number of searches we have done so far and those many trees will be planted by the Ecosia organization or they make money through the searches and release reports about how much they have spent on trees.


### The main advantage of this browser is :

- Ecosia cares about its users’ privacy. They don’t sell your data to advertisers and they allow you to turn off all tracking.
- It doesn't save browsing history
- So it is completely safe to use.
