# Recipe search application
## Project description
The program should allow the user to enter a list of foods into an entry widget, that are currently in stock at home.

Based on this search query, the application should then output a recipe selection based on the available ingredients as a formatted list in an extra window.

The user can then click on a recipe in this extra window, whereupon the corresponding recipe opens in a new window.

## Features in scope of this project
### Must-haves
* Already 10-20 included recipes ✔️
* Reading of recipe data from a (JSON) file ✔️
* Entering a single food key ✔️
* Output field in the terminal for the listed recipe suggestions ✔️
* Simple GUI with Tkinter
    * Input field or entry widget for the food keys ✔️
    * Output field in an extra listbox for the listed recipe suggestions or indication that no recipe is available for it ✔️
    * Linking within the output list to the corresponding recipe ✔️

### Nice-to-have
* Implementation of a help button with a small introduction ✔️
* Implementation of an exit button with security query ✔️
* Bilingual program selection (German and English)
* All recipes can be listed with the help of an extra button or with a special command in the input field ✔️
* Implementation of a scrollbar for lists, texts, etc. that may be too long for the Layout ✔️
* Implementation a Hamming-Distance for an extansive search query
* Entering a list of Foodkeys
* Food that is available in the household is displayed in green, otherwise in red
* Sorting options by effort/difficulty, duration, meal times (breakfast, lunch or dinner) or recipe ranges (pasta-, potato-, rice- or meat dishes)

## Features out of project scope
* An advanced search function on the internet
* The independet addition of recipes
* Forwarding. downloading, printing and saving options of selected recipes
* A marking function for favorite recipes
* Remembering function
* Various filter applications