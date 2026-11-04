# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Testes unitários do agente-estudos."""

from datetime import date
from unittest.mock import MagicMock

import pytest

from app.agent import (
    DIAS_DA_SEMANA,
    MODEL,
    PLANOS_DIR,
    SKILLS_DIR,
    ferramentas_de_arquivo,
    instrucao_do_agente,
    root_agent,
    skill_plano_de_estudos,
    skill_revisao_ativa,
)


@pytest.mark.asyncio
async def test_ferramentas_de_arquivo_expoem_apenas_read_e_write() -> None:
    """Garante que o EnvironmentToolset expõe apenas ReadFile e WriteFile (sem shell)."""
    tools = await ferramentas_de_arquivo.get_tools()
    tool_names = {tool.name for tool in tools}
    assert tool_names == {"ReadFile", "WriteFile"}
    assert "Execute" not in tool_names
    assert "EditFile" not in tool_names


def test_instrucao_do_agente_inclui_data_de_hoje_e_gating() -> None:
    """Garante que a instrução injeta a data atual, dia da semana e regra de gating."""
    hoje = date.today()
    dia_esperado = DIAS_DA_SEMANA[hoje.weekday()]
    instrucao = instrucao_do_agente(MagicMock())

    assert hoje.isoformat() in instrucao
    assert hoje.strftime("%d/%m/%Y") in instrucao
    assert dia_esperado in instrucao
    assert "plano-de-estudos" in instrucao
    assert "revisao-ativa" in instrucao
    assert "load_skill_resource" in instrucao
    assert "WriteFile" in instrucao
    assert "ReadFile" in instrucao


def test_configuracao_do_root_agent_e_diretorios() -> None:
    """Verifica o carregamento das skills, diretório de planos e modelo do agente."""
    assert skill_plano_de_estudos.name == "plano-de-estudos"
    assert (SKILLS_DIR / "plano-de-estudos" / "SKILL.md").is_file()
    assert skill_revisao_ativa.name == "revisao-ativa"
    assert (SKILLS_DIR / "revisao-ativa" / "SKILL.md").is_file()
    assert PLANOS_DIR.name == "planos"
    assert PLANOS_DIR.is_dir()
    assert root_agent.name == "agente_estudos"
    assert root_agent.model.model == MODEL
    assert len(root_agent.tools) == 2

