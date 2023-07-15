lign="center" style="color: #007BFF;">0x00. AirBnB Clone - The Console</h1>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.7%2B-blue">
    <img alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-18.04-orange">
      <img alt="Linux" src="https://img.shields.io/badge/Linux-Debian-red">
        <img alt="Vim" src="https://img.shields.io/badge/Vim-8.2%2B-brightgreen">
	  <img alt="JSON" src="https://img.shields.io/badge/JSON-Lightweight-yellow">
	  </p>

	  <p align="center">
	    <a href="#description" style="color: #FF4500;">Description</a> •
	      <a href="#command-interpreter" style="color: #FF4500;">Command Interpreter</a> •
	        <a href="#how-to-start-the-command-interpreter" style="color: #FF4500;">How to Start</a> •
		  <a href="#how-to-use-the-command-interpreter" style="color: #FF4500;">How to Use</a> •
		    <a href="#examples" style="color: #FF4500;">Examples</a>
		    </p>

## Description

		    The <span style="color: #007BFF;">AirBnB Clone</span> project is a recreation of the popular AirBnB application. It aims to provide a simplified version of the original platform's functionalities. This repository focuses on developing the command-line interface (CLI) known as "The Console" for managing and interacting with the AirBnB objects and data.

## Command Interpreter

		    The Command Interpreter, also known as "The Console," is a powerful tool for managing the AirBnB objects. It offers a user-friendly command-line interface that allows users to create, retrieve, update, and delete objects in the AirBnB database.

### How to Start the Command Interpreter

		    To start "The Console," follow these steps:

		    1. Clone the project repository.
		    2. Navigate to the project directory.
		    3. Run the following command: <span style="color: #FF0000;">./console.py</span>

### How to Use the Command Interpreter

		    Once "The Console" is running, you can enter various commands to interact with the AirBnB objects. Here are some examples:

		    - <span style="color: #FF8C00;">create &lt;class&gt;</span>: Create a new instance of the specified class.
		    - <span style="color: #FF8C00;">show &lt;class&gt; &lt;id&gt;</span>: Display the details of a specific instance.
		    - <span style="color: #FF8C00;">update &lt;class&gt; &lt;id&gt; &lt;attribute&gt; &lt;value&gt;</span>: Update the attribute of a specific instance.
		    - <span style="color: #FF8C00;">destroy &lt;class&gt; &lt;id&gt;</span>: Delete a specific instance.
		    - <span style="color: #FF8C00;">all &lt;class&gt;</span>: Display all instances of the specified class.

		    For a complete list of supported commands and their usage, you can enter the <span style="color: #000000;">help</span> command within "The Console."

### Examples

		    Here are some examples of how to use "The Console":
		       ```python
		       Create a new instance of the State class:
			          (hbnb) create State
				      ```
					 ```python
						 Display the details of a specific instance:
							(hbnb) show State 12345
							       ```
							       ```python
							       Update the attribute of a specific instance:
							       (hbnb) update State 12345 name "New Name"
							       ```
							       ```python
							       Delete a specific instance:
							       (hbnb) destroy State 12345
							       ```
							       ```python
							       Display all instances of a specific class:
								       (hbnb) all State
									```
