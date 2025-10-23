# Catapult Project

This project is an object-oriented catapult simulation game. It allows users to build a catapult using various components and launch projectiles at enemies. The project is structured into multiple Python files for better organization and maintainability.

## Project Structure

```
catapulta
├── catapulta
│   ├── __init__.py
│   ├── catapult.py
│   ├── projectile.py
│   ├── physics.py
│   ├── utils.py
│   ├── parts
│   │   ├── __init__.py
│   │   ├── stick.py
│   │   ├── rubber_band.py
│   │   ├── glue.py
│   │   ├── bottle_cap.py
│   │   └── paper_clip.py
│   └── enemies
│       ├── __init__.py
│       ├── enemy.py
│       └── goblin.py
├── main.py
├── tests
│   └── test_catapult.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Components

- **Catapult**: The main class that manages the catapult's parts and launches projectiles.
- **Projectile**: Represents the projectiles launched by the catapult, with properties like weight and velocity.
- **Parts**: Includes various components such as sticks, rubber bands, glue, bottle caps, and paper clips that can be used to build the catapult.
- **Enemies**: Contains enemy classes that the catapult can target, including specific types like goblins.

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using:
   ```
   pip install -r requirements.txt
   ```
4. Run the main application with:
   ```
   python main.py
   ```

## Usage

- Build your catapult by adding different parts.
- Launch projectiles at enemies and see how they perform.
- Modify the properties of the catapult and projectiles to experiment with different configurations.

## Testing

Unit tests are provided in the `tests` directory. You can run the tests using:
```
pytest tests/test_catapult.py
```

## Contributing

Feel free to submit issues or pull requests to improve the project.