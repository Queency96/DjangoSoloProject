const form = document.getElementById('form');
const submitBtn = document.querySelector('.btn');

let users = JSON.parse(localStorage.getItem('user')) || [];

form.addEventListener('submit', function (e) {
  e.preventDefault();

  // Get values from the input fields
  let username = document.getElementById('username').value;
  let password = document.getElementById('password').value;

  // Check if the username is already taken
  let userExists = users.some((user) => user.username === username);

  if (!userExists) {
    // Create a new user object
    let newUser = { username, password };

    // Add the new user to the users array
    users.push(newUser);

    // Store updated users array in localStorage
    localStorage.setItem('user', JSON.stringify(users));

    // Using SweetAlert as pop to give feedback on registration status

    // Success registration alert
    swal({
      title: 'Good job! 👍',
      text: 'User added successfully!',
      icon: 'success',
      button: 'close!',
    });
  } else {
    // Failed registration alert
    swal({
      title: 'Awww, Sorry! 😔',
      text: 'Username has already taken!',
      icon: 'error',
      button: 'close!',
    });
  }
});
