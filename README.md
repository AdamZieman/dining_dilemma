<h1 align="center">Dining Dilemma</h1>

<!-- TODO: Description -->
<!-- TODO: Video -->

<!-- Requirements Section -->
<h2>Requirements</h2>
<ul>
  <li>Language:</li>
  <ul>
    <li>Python 3</li>
  </ul>
  <li>Frameworks:</li>
  <ul>
    <li>unittest</li>
  </ul>
  <li>Libraries:</li>
  <ul>
    <li>tkinter</li>
    <li>random</li>
  </ul>
  <li>IDE:</li>
  <ul>
    <li>(preferred) Visual Studio Code</li>
  </ul>
</ul>

<br>

<!-- Execution Section -->
<h2>Execution</h2>
<dl>
  <dt>
    <h3>Executing Application Using an IDE</h3>
  </dt>
  <dd>
    <ul>
      <li>This program was developed and tested with Visual Studio Code.</li>
      <li>Run main.py from any IDE that supports Python.</li>
    </ul>
  </dd>
  
  <dt>
    <h3>Execute Application Using a Command Line Interface</h3>
  </dt>
  <dd>
    <ol>
      <li>Traverse to the dining_dilemma directory</li>
      <li>Command: <code>python src/main.py</code></li>
    </ol>
  </dd>

  <dt>
    <h3>Executing Unit Tests Using a Command Line Interface</h3>
  </dt>
  <dd>
    <ol>
      <li>Traverse to the dining_dilemma directory</li>
      <li>Command: <code>python -m unittest -v tests.test_restaurants</code></li>
      <ul>
        <li><code>-v</code> (verbose) flag is optional. It will provide a more detailed output.</li>
      </ul>
    </ol>
  </dd>
</dl>

<br>

<!-- GUI Explanation -->
<h2>GUI Explanation</h2>
<dl>
  <dt>
    <h3>Order Method</h3>
  </dt>
  <dd>
    <img src="https://github.com/AdamZieman/dining_dilemma/blob/main/demo/screenshots/order-method-frame.png" alt="Screenshot of the order method frame" width="578.5" height="410">
    <p>The user makes a choice between dine-in and take-out restaurants.</p>
    <p>The user's selection will be stored in a global variable (within main.py). This value will later be used as a parameter, when instantiating a Restaurants object. The parameter is the determiner to which list the user will have access to. Both lists contain a nested dictionary, which stores the establishment's name and the reason (the food) the user likes to get there. The dine-in list contains information regarding the establishments the user enjoys going to when she wants to eat out. The take-out list contains information regarding the establishments the user enjoys getting food from, to take back home to eat; this includes restaurants and fast food.</p>
    <p>After either button is clicked, the application will proceed to the next frame, the Option Selector frame.</p>

  <dt>
    <h3>Option Selector</h3>
  </dt>
  <dd>
    <img src="https://github.com/AdamZieman/dining_dilemma/blob/main/demo/screenshots/option-selector-frame.png" alt="Screenshot of the option selector frame" width="578.5" height="410">
    <p>The user makes a choice between generating a single random restaurant, generating a list (of 3) random restaurants, or viewing all the restaurants in the selected list., and a button to go back to Order Method</p>
    <p>After a Restaurants object has been instantiated, the choice selected by the user will be call the appropriate function. The Random Restaurant button will call the generate_random_list function from the Restaurants object. This function call is paramterless, therefore it will return a list of default length 1. The application will then proceed to the Random Restaurant frame. The Random List button will also call the generate_random_list function from the Restaurants object. However, it will pass LIST_SIZE as a parameter (declared to 3); therefore, it will return a list of length 3. The application will then proceed to the Random List frame. The View All Options button will call the get_restaurants_list function from the Restaurants object. This function will return a list of all of the restaurant's names for the selected list. The application will proceed to the View All frame.</p>
  </dd>

  <dt>
    <h3>Random Restaurant</h3>
  </dt>
  <dd>
    <img src="https://github.com/AdamZieman/dining_dilemma/blob/main/demo/screenshots/random-restaurant-frame.png" alt="Screenshot of the random restaurant frame" width="578.5" height="410">
    <p>Displays the randomly selected restaurant, the description of what the user likes to get at the establishment, a button to regenerate the response, and a button to go back to Option Selection.</p>
    <p>The randomly selected index that was returned by the Restaurants object is split amongst two labels. Both labels are concatenated with Strings to better understand the texts. The first label asks the user if they are in the mood for, the food that they like to get at this establishment. The second label then names the restaurant. The Regen button will select a random index again from the instantiated Restaurants object. Note: that it may select the same index as before.</p>
  </dd>

  <dt>
    <h3>Random List</h3>
  </dt>
  <dd>
    <img src="https://github.com/AdamZieman/dining_dilemma/blob/main/demo/screenshots/random-list-frame.png" alt="Screenshot of the random list frame" width="578.5" height="410">
    <p>Displays the name of the 3 randomly selected restaurants, a button to regenerate the response, and a button to go back to the Option Selection.</p>
    <p>The 3 randomly selected indices that where returned by the Restaurants object is split into 3 labels, concatenated to give them an ordered precedence. The labels only include the name of the restaurants'. The Regen button will select 3 random indices again from the instantiated Restaurants object. Note: that it may select the same indices, in the same order as before.</p>
  </dd>

  <dt>
    <h3>View All</h3>
  </dt>
  <dd>
    <img src="https://github.com/AdamZieman/dining_dilemma/blob/main/demo/screenshots/view-all-frame.png" alt="Screenshot of the view all frame" width="578.5" height="410">
    <p>Displays a list of the name of all the restaurants, includes a scroll wheel if the list grows to large, and a button to go back to the Option Selection.</p>
    <p>The list that was returned by the Restaurants object will be iterated through, and populate a list box. The list box will be configured to a vertical scroll bar, so that the user can scroll up and down the list, if it were to grow to large to view all at once.</p>
  </dd>

  
</dl>
