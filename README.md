# Animated Weather System Simulator

A realistic weather simulation system built with Python and Pygame, featuring dynamic weather patterns, particle systems, and interactive controls.



## Features

### Weather Types
- ☀️ **Clear Sky** - Beautiful blue gradients
- 🌧️ **Rain** - Realistic raindrops with wind effects
- ❄️ **Snow** - Animated snowflakes with rotation
- ⛈️ **Storm** - Lightning strikes with thunder effects
- 🧊 **Hail** - Bouncing ice particles

### Interactive Controls
- **SPACE** - Change weather type
- **↑/↓** - Adjust weather intensity
- **←/→** - Control wind strength
- **ESC** - Exit simulation

### Visual Effects
- Dynamic sky gradients based on weather
- Realistic particle physics
- Animated lightning with branching
- Moving clouds with wind effects
- Real-time weather information display

## Screenshots

| Clear Sky | Rain Storm | Snow |Rain |Hail |
|-----------|------------|------|-----------|-----------|
| ![Clear](https://github.com/reezmahanan/weather-system/blob/main/clear.png) | ![Rain](https://github.com/reezmahanan/weather-system/blob/main/rain.png) | ![Snow](screenshots/snow.png) | ![Lightning](screenshots/lightning.png) |![Hail](https://github.com/reezmahanan/weather-system/blob/main/hail.png) |

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/weather-system-simulator.git
cd weather-system-simulator
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the simulation:**
```bash
python weather_system.py
```

## Requirements

- Python 3.6+
- Pygame 2.0+

## Code Architecture

The project demonstrates advanced OOP concepts with `__init__` methods:

### Classes Overview

- **`WeatherParticle`** - Base class for all weather particles (rain, snow, hail)
- **`Lightning`** - Handles lightning strikes with realistic branching
- **`Cloud`** - Animated cloud system with wind effects
- **`WeatherSystem`** - Main simulation controller

### Key `__init__` Features

Each class uses initialization methods to:
- Set up particle physics properties
- Configure visual appearance
- Initialize animation states
- Establish weather parameters

## Customization

### Adding New Weather Types

```python
# In WeatherParticle.setup_particle()
elif self.particle_type == "fog":
    self.speed = random.uniform(0.5, 1.5)
    self.size = random.randint(10, 30)
    self.color = (200, 200, 200)
    self.alpha = random.randint(50, 100)
```

### Modifying Weather Parameters

```python
# In WeatherSystem.__init__()
self.weather_change_interval = 300  # Change weather every 5 seconds
self.max_particles = 1000  # Limit particle count
```

## Performance

- Optimized particle system with automatic cleanup
- 60 FPS smooth animations
- Dynamic particle spawning based on intensity
- Memory-efficient trail rendering

## Educational Value

This project teaches:
- Object-oriented programming with inheritance
- Particle system design
- Real-time animation techniques
- Event handling in games
- Mathematical modeling of weather

## Future Enhancements

- [ ] Sound effects for weather types
- [ ] Wind speed visualization
- [ ] Temperature effects on particles
- [ ] Seasonal changes
- [ ] Weather forecast system

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Your Name**
- GitHub: [@yourusername](https://github.com/reezmahanan)
- Email: reezmahanan@gmail.com

## Acknowledgments

- Inspired by real weather phenomena
- Built with Python and Pygame
- Thanks to the open-source community

---

*Enjoy exploring different weather patterns! 🌦️*
