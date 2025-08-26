import pygame
import random
import math

class WeatherParticle:
    def __init__(self, x, y, particle_type="rain"):
        self.x = x
        self.y = y
        self.particle_type = particle_type
        self.setup_particle()
    
    def setup_particle(self):
        if self.particle_type == "rain":
            self.speed = random.uniform(5, 12)
            self.size = random.randint(1, 3)
            self.color = (100, 150, 255)
            self.wind_effect = random.uniform(-1, 1)
        
        elif self.particle_type == "snow":
            self.speed = random.uniform(1, 3)
            self.size = random.randint(2, 6)
            self.color = (255, 255, 255)
            self.wind_effect = random.uniform(-0.5, 0.5)
            self.rotation = 0
            self.rotation_speed = random.uniform(-0.1, 0.1)
        
        elif self.particle_type == "hail":
            self.speed = random.uniform(8, 15)
            self.size = random.randint(3, 8)
            self.color = (200, 220, 255)
            self.wind_effect = random.uniform(-2, 2)
            self.bounce_height = random.randint(5, 15)
    
    def update(self, wind_strength=0):
        self.y += self.speed
        self.x += self.wind_effect + wind_strength
        
        if self.particle_type == "snow":
            self.rotation += self.rotation_speed
            self.x += math.sin(self.y * 0.01) * 0.5
    
    def draw(self, screen):
        if self.particle_type == "rain":
            pygame.draw.line(screen, self.color, 
                           (int(self.x), int(self.y)), 
                           (int(self.x + self.wind_effect), 
                            int(self.y + self.size * 3)), self.size)
        
        elif self.particle_type == "snow":
            pygame.draw.circle(screen, self.color, 
                             (int(self.x), int(self.y)), self.size)
            # Draw snowflake pattern
            if self.size > 3:
                for i in range(6):
                    angle = i * math.pi / 3 + self.rotation
                    end_x = self.x + math.cos(angle) * self.size
                    end_y = self.y + math.sin(angle) * self.size
                    pygame.draw.line(screen, self.color,
                                   (int(self.x), int(self.y)),
                                   (int(end_x), int(end_y)), 1)
        
        elif self.particle_type == "hail":
            pygame.draw.circle(screen, self.color,
                             (int(self.x), int(self.y)), self.size)
            pygame.draw.circle(screen, (255, 255, 255),
                             (int(self.x), int(self.y)), self.size // 2)

class Lightning:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.active = False
        self.duration = 0
        self.max_duration = 10
        self.branches = []
    
    def strike(self):
        self.active = True
        self.duration = self.max_duration
        self.branches = []
        
        # Create main lightning bolt
        start_x = random.randint(100, self.width - 100)
        self.create_branch(start_x, 0, start_x + random.randint(-50, 50), 
                          self.height, 0, 6)
    
    def create_branch(self, x1, y1, x2, y2, depth, max_depth):
        if depth > max_depth:
            return
        
        # Create zigzag pattern
        segments = random.randint(5, 15)
        points = [(x1, y1)]
        
        for i in range(1, segments):
            progress = i / segments
            x = x1 + (x2 - x1) * progress + random.randint(-30, 30)
            y = y1 + (y2 - y1) * progress
            points.append((x, y))
        
        points.append((x2, y2))
        self.branches.append(points)
        
        # Create sub-branches
        if depth < max_depth - 2 and random.random() < 0.3:
            branch_point = random.choice(points[1:-1])
            end_x = branch_point[0] + random.randint(-100, 100)
            end_y = branch_point[1] + random.randint(50, 150)
            self.create_branch(branch_point[0], branch_point[1], 
                             end_x, min(end_y, self.height), depth + 1, max_depth)
    
    def update(self):
        if self.active:
            self.duration -= 1
            if self.duration <= 0:
                self.active = False
    
    def draw(self, screen):
        if self.active:
            # Flash effect
            alpha = (self.duration / self.max_duration) * 255
            flash_surface = pygame.Surface((self.width, self.height))
            flash_surface.fill((255, 255, 255))
            flash_surface.set_alpha(alpha * 0.3)
            screen.blit(flash_surface, (0, 0))
            
            # Draw lightning bolts
            for branch in self.branches:
                if len(branch) > 1:
                    # Main bolt
                    pygame.draw.lines(screen, (255, 255, 255), False, branch, 3)
                    pygame.draw.lines(screen, (150, 150, 255), False, branch, 6)
                    pygame.draw.lines(screen, (100, 100, 255), False, branch, 8)

class Cloud:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.circles = []
        self.create_cloud()
        self.darkness = random.uniform(0.3, 0.8)
    
    def create_cloud(self):
        num_circles = random.randint(5, 12)
        for _ in range(num_circles):
            offset_x = random.randint(-50, 50)
            offset_y = random.randint(-20, 20)
            radius = random.randint(20, 60)
            self.circles.append((offset_x, offset_y, radius))
    
    def update(self, wind_speed):
        self.x += wind_speed * 0.1
    
    def draw(self, screen):
        for offset_x, offset_y, radius in self.circles:
            cloud_x = self.x + offset_x
            cloud_y = self.y + offset_y
            
            # Cloud color based on darkness
            gray_value = int(255 * (1 - self.darkness))
            color = (gray_value, gray_value, gray_value)
            
            pygame.draw.circle(screen, color, 
                             (int(cloud_x), int(cloud_y)), radius)

class WeatherSystem:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Animated Weather System")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Weather state
        self.weather_type = "clear"
        self.weather_intensity = 0.5
        self.wind_strength = 0
        self.temperature = 20  # Celsius
        
        # Particles and effects
        self.particles = []
        self.clouds = []
        self.lightning = Lightning(width, height)
        
        # Create initial clouds
        for _ in range(random.randint(3, 8)):
            x = random.randint(-100, width + 100)
            y = random.randint(50, 200)
            self.clouds.append(Cloud(x, y))
        
        # UI
        self.font = pygame.font.Font(None, 24)
        self.weather_timer = 0
        self.weather_change_interval = 600  # frames
    
    def change_weather(self):
        weather_types = ["clear", "rain", "snow", "storm", "hail"]
        self.weather_type = random.choice(weather_types)
        self.weather_intensity = random.uniform(0.3, 1.0)
        self.wind_strength = random.uniform(-2, 2)
        
        if self.weather_type == "snow":
            self.temperature = random.uniform(-10, 5)
        elif self.weather_type == "rain":
            self.temperature = random.uniform(5, 25)
        elif self.weather_type == "storm":
            self.temperature = random.uniform(10, 20)
            self.wind_strength = random.uniform(-5, 5)
        else:
            self.temperature = random.uniform(15, 30)
    
    def spawn_particles(self):
        if self.weather_type in ["rain", "snow", "hail", "storm"]:
            particle_type = "rain" if self.weather_type in ["rain", "storm"] else self.weather_type
            
            spawn_rate = int(self.weather_intensity * 20)
            for _ in range(spawn_rate):
                x = random.randint(-50, self.width + 50)
                y = random.randint(-50, -10)
                particle = WeatherParticle(x, y, particle_type)
                self.particles.append(particle)
    
    def update_particles(self):
        for particle in self.particles[:]:
            particle.update(self.wind_strength)
            
            # Remove particles that have fallen off screen
            if (particle.y > self.height + 50 or 
                particle.x < -100 or particle.x > self.width + 100):
                self.particles.remove(particle)
    
    def update_clouds(self):
        for cloud in self.clouds:
            cloud.update(self.wind_strength)
            
            # Wrap clouds around screen
            if cloud.x > self.width + 200:
                cloud.x = -200
            elif cloud.x < -200:
                cloud.x = self.width + 200
    
    def update_lightning(self):
        self.lightning.update()
        
        # Random lightning strikes during storms
        if self.weather_type == "storm" and random.random() < 0.01:
            self.lightning.strike()
    
    def draw_background(self):
        # Sky gradient based on weather
        if self.weather_type == "storm":
            top_color = (40, 40, 80)
            bottom_color = (20, 20, 60)
        elif self.weather_type == "rain":
            top_color = (80, 80, 120)
            bottom_color = (60, 60, 100)
        elif self.weather_type == "snow":
            top_color = (200, 200, 220)
            bottom_color = (180, 180, 200)
        else:  # clear
            top_color = (135, 206, 235)
            bottom_color = (176, 224, 230)
        
        for y in range(self.height):
            ratio = y / self.height
            r = int(top_color[0] + (bottom_color[0] - top_color[0]) * ratio)
            g = int(top_color[1] + (bottom_color[1] - top_color[1]) * ratio)
            b = int(top_color[2] + (bottom_color[2] - top_color[2]) * ratio)
            pygame.draw.line(self.screen, (r, g, b), (0, y), (self.width, y))
    
    def draw_ui(self):
        ui_texts = [
            f"Weather: {self.weather_type.capitalize()}",
            f"Temperature: {self.temperature:.1f}°C",
            f"Wind: {self.wind_strength:.1f} m/s",
            f"Intensity: {self.weather_intensity:.1f}",
            f"Particles: {len(self.particles)}",
            "",
            "Controls:",
            "SPACE - Change weather",
            "↑/↓ - Adjust intensity",
            "←/→ - Adjust wind"
        ]
        
        for i, text in enumerate(ui_texts):
            surface = self.font.render(text, True, (255, 255, 255))
            # Add background for readability
            bg_rect = surface.get_rect()
            bg_rect.topleft = (10, 10 + i * 25)
            bg_rect.width += 10
            bg_rect.height += 5
            pygame.draw.rect(self.screen, (0, 0, 0, 128), bg_rect)
            self.screen.blit(surface, (15, 10 + i * 25))
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.change_weather()
                elif event.key == pygame.K_UP:
                    self.weather_intensity = min(1.0, self.weather_intensity + 0.1)
                elif event.key == pygame.K_DOWN:
                    self.weather_intensity = max(0.0, self.weather_intensity - 0.1)
                elif event.key == pygame.K_LEFT:
                    self.wind_strength -= 0.5
                elif event.key == pygame.K_RIGHT:
                    self.wind_strength += 0.5
    
    def run(self):
        while self.running:
            self.handle_events()
            
            # Auto weather change
            self.weather_timer += 1
            if self.weather_timer >= self.weather_change_interval:
                self.change_weather()
                self.weather_timer = 0
            
            # Update systems
            self.spawn_particles()
            self.update_particles()
            self.update_clouds()
            self.update_lightning()
            
            # Draw everything
            self.draw_background()
            
            # Draw clouds
            for cloud in self.clouds:
                cloud.draw(self.screen)
            
            # Draw weather particles
            for particle in self.particles:
                particle.draw(self.screen)
            
            # Draw lightning
            self.lightning.draw(self.screen)
            
            # Draw UI
            self.draw_ui()
            
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()

if __name__ == "__main__":
    weather = WeatherSystem(1200, 800)
    weather.run()