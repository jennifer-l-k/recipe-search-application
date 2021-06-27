# Recipe search application
## Project description
The recipe search program allows the user to enter a food key in a corresponding entry widget, whereupon a list box, located on the left side, displays the matching recipes according to the recipe name.

If there is no corresponding recipe for this ingredient, the end user will receive an error message.

If the end user wants to view an entire recipe, he can click on it within the list box and the recipe will appear on the right side in a text box.

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
* Implementation a Levenshtein distance for an extansive search query ✔️
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