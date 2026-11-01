<!DOCTYPE html>
<html>

<head>
    <title>Test Page</title>
    <style>
        #suggestion-container {
            position: relative;
        }

        #suggestion-list {
            position: absolute;
            top: 100%;
            left: 0;
            z-index: 1;
            list-style: none;
            margin: 0;
            padding: 0;
            background-color: #fff;
            border: 1px solid #ccc;
            border-top: none;
            max-height: 200px;
            overflow-y: auto;
        }

        #suggestion-list li {
            padding: 5px;
            cursor: pointer;
        }

        #suggestion-list li:hover {
            background-color: #f2f2f2;
        }
    </style>
</head>

<body>
    <h1>Input Field with Suggestions</h1>
    <div id="suggestion-container">
        <label for="my-input">Type a fruit name:</label>
        <input type="text" id="my-input" name="my-input">
        <ul id="suggestion-list"></ul>
    </div>

    <script>
        // Define a list of suggestions
        const suggestions = ['apple', 'banana', 'cherry', 'grape', 'orange', 'pear', 'kiwi', 'pineapple', 'strawberry', 'watermelon', 'mango'];

        // Get a reference to the input field
        const inputField = document.getElementById('my-input');

        // Get a reference to the suggestion list
        const suggestionList = document.getElementById('suggestion-list');

        // Add an input event listener to the input field
        inputField.addEventListener('input', function (event) {
            const currentValue = event.target.value.toLowerCase();

            // Clear the suggestion list if the input field is blank
            if (!currentValue) {
                suggestionList.innerHTML = '';
                return;
            }

            // Filter the list of suggestions based on the current input value
            const containingStrings = [];

            for (let i = 0; i < suggestions.length; i++) {
                if (suggestions[i].includes(currentValue)) {
                    containingStrings.push(suggestions[i]);
                }
            }

            // Display the filtered suggestions
            displaySuggestions(containingStrings);
        });

        // Display the filtered suggestions
        function displaySuggestions(suggestions) {
            suggestionList.innerHTML = '';

            suggestions.forEach(function (suggestion) {
                const suggestionItem = document.createElement('li');
                suggestionItem.textContent = suggestion;
                suggestionList.appendChild(suggestionItem);
            });

            // Show the suggestion list container
            document.getElementById('suggestion-container').style.display = 'block';

            // Adjust the max-height of the suggestion list container if necessary
            const suggestionListHeight = suggestionList.getBoundingClientRect().height;
            const maxHeight = parseInt(window.getComputedStyle(suggestionList).maxHeight);
            if (suggestionListHeight > maxHeight) {
                suggestionList.style.maxHeight = maxHeight + 'px';
            } else {
                suggestionList.style.maxHeight = '';
            }
        }
    </script>
</body>

</html>