import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam


# 1. Dataset Preparation
def generate_fake_chess_data(num_samples=2000):
    """
    Generate fake chess game states and move training data.
    Each chessboard state is represented as a vector of 64 integers:
    - -1 for black pieces
    - 0 for empty spaces
    - 1 for white pieces
    Each move is represented as one of 4672 possible moves (standard move generation in chess).
    """
    board_size = 8 * 8  # The chessboard is 8x8
    num_possible_moves = 4672  # Standard number of possible legal chess moves

    # Features: Random board states
    board_states = np.random.randint(-1, 2, size=(num_samples, board_size))

    # Labels: Random moves (as indices)
    moves = np.random.randint(0, num_possible_moves,
                              size=(num_samples,))  # Target moves

    return board_states, moves


# Generate synthetic training data
X_train, y_train = generate_fake_chess_data(num_samples=5000)

# Convert moves to one-hot encoded labels
num_possible_moves = 4672
y_train_one_hot = np.zeros((y_train.size, num_possible_moves))
y_train_one_hot[np.arange(y_train.size), y_train] = 1


# 2. Build the Neural Network
def build_chess_model(input_size, output_size):
    """
    Create a neural network architecture for predicting chess moves.
    """
    model = Sequential()
    model.add(Dense(256, input_dim=input_size,
                    activation='relu'))  # First hidden layer
    model.add(Dropout(0.3))  # Add dropout to avoid overfitting
    model.add(Dense(256, activation='relu'))  # Second hidden layer
    model.add(Dropout(0.3))
    model.add(Dense(output_size,
                    activation='softmax'))  # Output layer for move probabilities

    # Compile the model with Adam optimizer and categorical crossentropy loss
    model.compile(optimizer=Adam(learning_rate=0.001),
                  loss='categorical_crossentropy',
                  metrics=['accuracy'])
    return model


# Initialize the model
input_size = X_train.shape[1]  # Input size is 64 (board squares: 8x8)
output_size = num_possible_moves  # Possible moves in chess
model = build_chess_model(input_size, output_size)

# 3. Train the Model
print("Training the model...")
model.fit(X_train, y_train_one_hot, epochs=10, batch_size=32,
          validation_split=0.2)


# 4. Predict Moves with the Trained Model
def predict_chess_move(model, board_state):
    """
    Predict the best move given the current board state.
    """
    board_state = np.array(board_state).reshape(1, -1)  # Reshape to match inp
    probabilities = model.predict(
        board_state)  # Predict probabilities for all moves
    predicted_move = np.argmax(
        probabilities)  # Select the move with highest probability
    return predicted_move


# Example usage
example_board = np.random.randint(-1, 2, size=(
    input_size,))  # Generate a random board state
predicted_move = predict_chess_move(model, example_board)
print(f"Predicted Move: {predicted_move}")
