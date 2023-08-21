# AI-MOUSE

This repository contains two projects that demonstrate the concept of controlling a computer's mouse pointer using different methods: hand gestures and eye movements.

## Hand Gesture Mouse

The "hand_gesture_mouse" project allows you to control the mouse pointer using hand gestures. It utilizes the Mediapipe library for hand tracking, and the movement of the tip of the first finger determines the mouse pointer movement. A click is simulated when the tips of the thumb and the first finger touch.

### How to Use

1. Install the required dependencies listed in the `requirements.txt` file.
2. Run the `main.py` script.
3. Move your index finger for moving the mouse pointer and touch your index finger and thumb to click

## Eye Controlled Mouse

The "eye_controlled_mouse" project enables you to control the mouse pointer using eye movements. It employs the Mediapipe library for eye tracking, and the mouse pointer follows the movement of the user's eyes. A left eye blink is detected as a click action.

### How to Use

1. Install the required dependencies listed in the `requirements.txt` file.
2. Run the `main.py` script.
3. Move your eyes to move the mouse pointer and blink your left eye to click.

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, enhance, and adapt these projects according to your needs. If you encounter any issues or have ideas for improvements, please open an issue or submit a pull request.


