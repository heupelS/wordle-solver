# Wordle Solver & Game Implementation

This is an implementation of the Wordle game that can be played by a human player in the console. The Wordle game involves guessing a secret word within a limited number of attempts and receiving feedback for each guess.

**Solving Wordle:**

This implementation focuses on the solving aspect of the Wordle game and offers two distinct approaches to find the secret word:

1. **Expected Information Gain Approach:** This approach uses the concept of entropy to calculate the expected information gain for each possible word. It is more accurate in selecting the next guess but can be slower due to its computational complexity.

2. **Relative Probability Approach:** The relative probability approach offers a faster method to select the next guess but with slightly reduced accuracy compared to the expected information gain approach.

In addition, there is a full C++ implementation of the first approach to explore potential performance improvements when solving Wordle with C++.

## How to Use

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/heupelS/wordle-solver.git
   cd wordle-solver
   ```

2. Ensure you have Python installed on your machine.

3. Install the required dependencies using pip:

   ```bash
   pip install requirements.txt
   ```

   or using conda:

   ```bash
    conda env create -f environment.yml
    conda activate wordle-env
   ```

### Playing Wordle

To play Wordle, follow these steps:

1. Run a simple Wordle game:

   ```bash
   python wordle_main.py
   ```

2. You will be prompted to enter your guesses. You have a limited number of attempts to guess the secret word. The feedback for each guess will be provided based on the following conventions:

   - 0: Letter is not in the solution (gray).
   - 1: Letter is in the solution but in a different position (yellow). It can also appear in the solution multiple times.
   - 2: Letter is in the solution at the correct position (green).

3. Keep guessing until you either correctly guess the word or run out of attempts.

### Wordle Solver

If you need help with solving Wordle, you can use the Wordle Solver:

1. Open the `solver.py` file:

   ```bash
   python solver.py
   ```

2. You can input a word and a pattern, and the solver will suggest the best next guess based on expected information gain.

### Running Simulations

You can also run simulations of the Wordle game to gather statistics:

1. Open the `simu.py` file:

   ```bash
   python simu.py
   ```

2. This will run simulations of the Wordle game and provide statistics on the average number of attempts required to guess the word.

## Data Files

Make sure to provide the necessary data files:

- [wordle_answers](./Data/wordle_answers.txt): Contains possible solution words.
- [wordle_guesses](./Data/wordle_guesses.txt): Contains words that are allowed to be guessed.

## Credits

This Wordle implementation was created by [@breible](https://github.com/breible) and myself [@heupelS](https://github.com/heupelS).

Enjoy playing and solving Wordle!

## License

This Wordle implementation is open-source and available under the [MIT License](LICENSE).

You are free to use, modify, and distribute this code as per the terms of the MIT License.
