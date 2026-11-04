# Study Agent

An AI-powered study planning assistant built with **Google Agent Development Kit (ADK)** and **Gemini**.

Study Agent helps learners organize their learning goals into structured, personalized study plans. It collects information about the subject, learning objectives, deadlines, current knowledge, and available study time to generate a practical learning schedule.

The project explores how AI agents can go beyond conversational assistance by using specialized skills, external tools, and file operations to perform useful tasks.

## Overview

Planning a learning journey can be challenging, especially when balancing multiple subjects, deadlines, and daily commitments.

Study Agent addresses this problem by acting as a personalized study mentor. Instead of generating generic study schedules, it gathers the information needed to create a plan that reflects each learner's individual circumstances.

Its main capabilities include:

- **Personalized Study Plans:** Generates structured study schedules based on learning goals, deadlines, current skill level, and available time.
- **Interactive Requirements Gathering:** Asks follow-up questions whenever essential information is missing before generating a study plan.
- **Spaced Repetition:** Incorporates review sessions into the learning schedule to reinforce knowledge retention.
- **Active Recall:** Includes a dedicated skill designed to generate flashcards and quizzes from study materials.
- **CSV Export:** Saves study schedules as CSV files that can be imported directly into Google Calendar.
- **Plan Adjustments:** Reorganizes existing schedules when the learner misses sessions or needs to change their availability.

## How It Works

The agent follows a structured workflow:

1. **Understand the Learning Goal** — Collects the subject, objectives, deadline, current knowledge, and study availability.
2. **Build the Study Plan** — Organizes learning activities into scheduled sessions, including review periods.
3. **Generate the Calendar** — Converts the study plan into a structured CSV file.
4. **Save the Output** — Uses the ADK EnvironmentToolset to write the generated file to the local plans directory.
5. **Adapt the Schedule** — Updates the plan when the learner requests changes.

The agent also uses specialized ADK Skills to extend its capabilities beyond the core planning workflow.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Google Agent Development Kit (ADK) | Agent architecture and orchestration |
| Google Gemini | Language model powering the agent |
| ADK Skills | Specialized learning and revision capabilities |
| EnvironmentToolset | Controlled file reading and writing |
| CSV | Study schedule export format |
| Google Calendar | Study schedule management |

## Project Structure

```text
study-agent/
│
├── agente-estudos/
│   ├── app/
│   │   ├── skills/
│   │   │   ├── plano-de-estudos/
│   │   │   └── revisao-ativa/
│   │   └── ...
│   │
│   ├── planos/
│   │   └── plano-de-estudos.csv
│   │
│   ├── .env
│   └── ...
│
├── skills/
│   └── plano-de-estudos/
│       ├── SKILL.md
│       └── assets/
│
└── README.md
```

*The structure above illustrates the main project components. Individual files may vary depending on the implementation.*

## Getting Started

### Prerequisites

- Python
- Google Cloud project with the required APIs enabled
- Google AI Studio API key
- [uv](https://docs.astral.sh/uv/)
- Google Agent Development Kit

### Installation

Clone the repository:

```bash
git clone https://github.com/gtr-1000/study-agent.git
cd study-agent
```

Navigate to the agent directory:

```bash
cd agente-estudos
```

Install dependencies:

```bash
uv sync
```

### Environment Configuration

Create a `.env` file in the agent directory:

```env
GOOGLE_GENAI_USE_VERTEXAI=FALSE
GEMINI_API_KEY=your_api_key_here
MODEL=your_supported_gemini_model
```

Replace the placeholder with your Google AI Studio API key and a supported Gemini model.

**Security:** Never commit API keys or other sensitive credentials to version control.

### Run the Agent

Start the ADK Web interface:

```bash
uv run adk web --allow_origins="*"
```

Open the local address provided by the terminal and select the agent to start interacting with it.

## Example Usage

A learner can request a study plan using a natural language prompt:

> I want to learn JavaScript and build my first portfolio project in five weeks. I can study on Mondays, Wednesdays, and Fridays, for two hours each day at 7 PM. I already know HTML and CSS, but I have never programmed before.

The agent gathers the necessary information, organizes the learning activities, schedules review sessions, and generates a CSV file containing the study calendar.

The learner can then import the CSV into Google Calendar.

The schedule can also be adjusted through follow-up instructions:

> I missed Wednesday and Friday sessions during the first week. Can you reorganize my study plan?

## Project Goals

This project was developed to explore practical applications of AI agents and demonstrate how different components can work together to solve a real-world problem.

The main technical concepts explored include:

- Agent orchestration and tool usage.
- Context-aware interactions and information gathering.
- Modular agent capabilities through specialized skills.
- Controlled interaction with the local file system.
- Structured data generation.
- AI-assisted planning and adaptive workflows.

## Future Improvements

Potential directions for further development include:

- Integration with additional calendar platforms.
- Persistent learner profiles and learning history.
- Progress tracking and performance analytics.
- More advanced spaced repetition algorithms.
- Automated assessment and personalized learning recommendations.
- A graphical interface for managing study plans.

## Author

**Dalbert Moreira**

GitHub: [@gtr-1000](https://github.com/gtr-1000)

---

*Built as a practical exploration of AI agent development using Google's Agent Development Kit and Gemini.*
