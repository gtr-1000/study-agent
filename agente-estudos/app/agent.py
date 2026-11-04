import os
from datetime import date
from pathlib import Path

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.agents.readonly_context import ReadonlyContext
from google.adk.apps import App
from google.adk.environment import LocalEnvironment
from google.adk.models.google_llm import Gemini
from google.adk.skills import load_skill_from_dir
from google.adk.tools.environment import EnvironmentToolset
from google.adk.tools.skill_toolset import SkillToolset
from google.genai import types

APP_DIR = Path(__file__).resolve().parent
load_dotenv(APP_DIR.parent / ".env")

SKILLS_DIR = APP_DIR / "skills"
PLANOS_DIR = APP_DIR.parent / "planos"
PLANOS_DIR.mkdir(parents=True, exist_ok=True)

MODEL = os.getenv("MODEL", "gemini-3.8-flash")

DIAS_DA_SEMANA = (
    "segunda-feira",
    "terça-feira",
    "quarta-feira",
    "quinta-feira",
    "sexta-feira",
    "sábado",
    "domingo",
)


class FerramentasDeArquivo(EnvironmentToolset):
    """Expõe apenas ReadFile e WriteFile do EnvironmentToolset (sem shell)."""

    async def get_tools(self, readonly_context=None):
        tools = await super().get_tools(readonly_context)
        return [t for t in tools if t.name in ("ReadFile", "WriteFile")]


def instrucao_do_agente(readonly_context: ReadonlyContext) -> str:
    """Injeta a data atual na instrução do agente."""
    hoje = date.today()
    dia_semana = DIAS_DA_SEMANA[hoje.weekday()]
    return (
        f"Hoje é {hoje.isoformat()} ({hoje.strftime('%d/%m/%Y')}, {dia_semana}). "
        "Use esta data como referência para calcular expressões relativas como "
        "'amanhã', 'segunda que vem' ou 'daqui a duas semanas'.\n\n"
        "Você é o agente-estudos, um mentor especialista em organização de estudos "
        "que conversa sempre em português do Brasil.\n"
        "Use as skills disponíveis por meio das ferramentas de skill "
        "(`load_skill` e `load_skill_resource`):\n"
        "- `plano-de-estudos`: para montar ou ajustar planos de estudo.\n"
        "- `revisao-ativa`: para gerar flashcards e um quiz de 5 perguntas a partir "
        "de um material de estudo.\n"
        "Respeite rigorosamente a regra de ativação (gating) de cada skill: nunca "
        "carregue recursos adicionais (`load_skill_resource`) antes de confirmar "
        "as informações obrigatórias pedidas pela skill.\n"
        "Para salvar ou atualizar o arquivo `plano-de-estudos.csv`, utilize apenas "
        "as ferramentas `WriteFile` e `ReadFile`."
    )


skill_plano_de_estudos = load_skill_from_dir(SKILLS_DIR / "plano-de-estudos")
skill_revisao_ativa = load_skill_from_dir(SKILLS_DIR / "revisao-ativa")
skill_toolset = SkillToolset(
    skills=[skill_plano_de_estudos, skill_revisao_ativa]
)
ferramentas_de_arquivo = FerramentasDeArquivo(
    environment=LocalEnvironment(working_dir=PLANOS_DIR)
)

root_agent = Agent(
    name="agente_estudos",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(
            attempts=5,
            initial_delay=2.0,
            exp_base=2.0,
            http_status_codes=[429, 500, 502, 503, 504],
        ),
    ),
    description=(
        "Mentor de estudos que monta planos personalizados com revisão espaçada, "
        "exporta a agenda em CSV para o Google Agenda e gera flashcards e quizzes "
        "de revisão ativa."
    ),
    instruction=instrucao_do_agente,
    tools=[skill_toolset, ferramentas_de_arquivo],
)

app = App(
    root_agent=root_agent,
    name="app",
)
