# ANIMA Architecture

## Purpose

The architecture of ANIMA is designed to support long-term development of an emergent Artificial Life Engine.

Every subsystem has one responsibility.

The simulation engine is independent from the user interface.

---

# Execution Flow

Application Start

↓

Load Configuration

↓

Initialize Engine

↓

Generate World

↓

Spawn Initial Population

↓

Initialize Systems

↓

Simulation Loop

↓

Tick

↓

Render

---

# Tick Pipeline

Every simulation tick follows the exact same order.

1. Update Time
2. Update Weather
3. Update Seasons
4. Update Resources
5. Update Plants
6. Update Animals
7. Update Humans
8. Resolve Events
9. Save Statistics
10. Render UI

---

# Modules

Engine

Responsible for:

- Clock
- Scheduler
- Events
- Configuration

World

Responsible for:

- Map
- Biomes
- Rivers
- Weather
- Resources

Agents

Responsible for:

- Humans
- Body
- Brain
- Memory
- Personality
- Goals

AI

Responsible for:

- Perception
- Planning
- Learning
- Decision Making

Civilization

Responsible for:

- Families
- Villages
- Technology
- Economy
- Diplomacy

UI

Responsible only for visualization.

No game logic is allowed inside the UI.