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

  <dt>
    <h3>Option Selector</h3>
  </dt>
  <dd>
    <img src="https://github.com/AdamZieman/dining_dilemma/blob/main/demo/screenshots/option-selector-frame.png" alt="Screenshot of the option selector frame" width="578.5" height="410">
  </dd>

  <dt>
    <h3>Random Restaurant</h3>
  </dt>
  <dd>
    <img src="https://github.com/AdamZieman/dining_dilemma/blob/main/demo/screenshots/random-restaurant-frame.png" alt="Screenshot of the random restaurant frame" width="578.5" height="410">
  </dd>

  <dt>
    <h3>Random List</h3>
  </dt>
  <dd>
    <img src="https://github.com/AdamZieman/dining_dilemma/blob/main/demo/screenshots/random-list-frame.png" alt="Screenshot of the random list frame" width="578.5" height="410">
  </dd>

  <dt>
    <h3>View All</h3>
  </dt>
  <dd>
    <img src="https://github.com/AdamZieman/dining_dilemma/blob/main/demo/screenshots/view-all-frame.png" alt="Screenshot of the view all frame" width="578.5" height="410">
  </dd>

  
</dl>
