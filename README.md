# The Caesar Cipher

Welcome to the **Caesar Cipher** project! This program allows you to encode or decode messages written in English using the classic Caesar Cipher encryption technique.
With an interactive command-line interface, you can easily secure your messages or decode encrypted ones.


## Introduction
The Caesar Cipher is one of the simplest and most well-known encryption methods. It involves shifting the letters of the alphabet by a fixed amount to encode or decode a
message. This project implements the Caesar Cipher in a user-friendly way, providing an ASCII art introduction and guiding users through the encoding/decoding process.


## Features

- **ASCII Art Display:** The program starts by displaying an ASCII art, creating an engaging and visually appealing introduction to the cipher.

- **User Interaction:** The user is prompted to make a choice between three options: `exit`, `encode`, or `decode`.

- **Loop Execution:** Once a choice is made, the program runs in a loop until the user selects the `exit` option. This allows for continuous interaction without the need
  to restart the program.

- **Error Handling:** The program is designed to handle invalid user inputs gracefully. If the user provides unexpected or incorrect input at any point during execution,
   the program will not crash but instead guide the user to enter valid input.

- **Encoding and Decoding:** When the user chooses the `encode` or `decode` option:
  - The user is prompted to enter the `message` to be encoded or decoded.
  - The user is then prompted to enter a `shift value`, which determines the amount of displacement for each character in the message.
  - The Caesar Cipher supports both `positive` and `negative shift values`, allowing for encoding and decoding in both directions.
  - The encoded or decoded message is displayed to the user, providing the result of the chosen operation.


## Getting Started
To get started with the project, follow these steps:

1. Clone the repository to your local machine using the following command:
   ```bash
   git clone https://github.com/AryabhattSingh/TheCaesarCipher.git
   ```

2. Navigate to the project directory:
   ```bash
   cd TheCaesarCipher
   ```

3. Run the program:
   ```bash
   python main.py
   ```


## Contributing
Contributions to the Caesar Cipher project are welcome and encouraged! If you find any issues or want to add enhancements, feel free to submit pull requests. Make sure to follow the existing coding style and guidelines.

1. Fork the repository.
2. Create a new branch for your feature/fix: `git checkout -b feature-new-feature`.
3. Commit your changes: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-new-feature`.
5. Open a pull request explaining your changes.

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code as permitted by the license.

---

Enjoy secure communication with the Caesar Cipher! If you have any questions or suggestions, don't hesitate to contact us or open an issue. Have fun exploring the world of cryptography!








