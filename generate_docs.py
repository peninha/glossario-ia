#!/usr/bin/env python3
"""
Gerador de documentação para o Glossário de IA
Converte o arquivo glossario.yaml em páginas Markdown para MkDocs
"""

import yaml
import os
from pathlib import Path
from typing import Dict, List, Any

def load_glossary(file_path: str = "glossario.yaml") -> Dict[str, Any]:
    """Carrega o arquivo YAML do glossário"""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def build_term_map(glossary: Dict[str, Any]) -> Dict[str, str]:
    """Constrói um mapa de slug -> caminho completo para todos os termos"""
    term_map = {}
    for category in glossary['categories']:
        for term in category['terms']:
            term_map[term['slug']] = f"../{category['id']}/{term['slug']}.md"
    return term_map

def fix_internal_links(text: str, glossary: Dict[str, Any]) -> str:
    """Corrige links internos [texto](#slug) para caminhos relativos corretos"""
    import re
    
    term_map = build_term_map(glossary)
    
    # Padrão para encontrar links do tipo [texto](#slug)
    pattern = r'\[([^\]]+)\]\(#([^)]+)\)'
    
    def replace_link(match):
        text = match.group(1)
        slug = match.group(2)
        
        if slug in term_map:
            return f"[{text}]({term_map[slug]})"
        else:
            # Mantém o link original se não encontrar o termo
            return match.group(0)
    
    return re.sub(pattern, replace_link, text)

def ensure_docs_structure():
    """Cria a estrutura de diretórios docs/"""
    dirs = [
        "docs",
        "docs/conceitos-fundamentais",
        "docs/ia-generativa", 
        "docs/agentes-ia",
        "docs/escopo-ias",
        "docs/etica-seguranca-governanca",
        "docs/habilidades-praticas",
        "docs/infraestrutura-processos",
        "docs/stylesheets",
        "docs/javascripts"
    ]
    
    for dir_path in dirs:
        Path(dir_path).mkdir(parents=True, exist_ok=True)

def create_term_page(term: Dict[str, Any], category_id: str, glossary: Dict[str, Any]) -> str:
    """Cria uma página Markdown para um termo individual"""
    
    # Título principal
    content = f"# {term['title_pt']}\n\n"
    
    # Título em inglês e aliases
    if 'title_en' in term:
        content += f"**{term['title_en']}**"
        if 'aliases' in term:
            aliases = ", ".join(term['aliases'])
            content += f" · *{aliases}*"
        content += "\n\n"
    
    # Definição com links corrigidos
    definition = fix_internal_links(term['definition_pt'], glossary)
    content += f"{definition}\n\n"
    
    # Tags
    if 'tags' in term:
        content += "**Tags:** "
        tags = [f"`{tag}`" for tag in term['tags']]
        content += " · ".join(tags) + "\n\n"
    
    # Links de navegação
    content += "---\n\n"
    content += f"[:material-arrow-left: Voltar para {get_category_title(category_id)}](index.md){{ .md-button }}\n"
    content += "[📝 Editar este termo](https://github.com/seu-usuario/glossario-ia/edit/main/glossario.yaml){ .md-button .md-button--primary }\n"
    
    return content

def get_category_title(category_id: str) -> str:
    """Retorna o título amigável da categoria"""
    titles = {
        'conceitos-fundamentais': 'Conceitos Fundamentais',
        'ia-generativa': 'IA Generativa', 
        'agentes-ia': 'Agentes de IA',
        'escopo-ias': 'Escopo das IAs',
        'etica-seguranca-governanca': 'Ética, Segurança e Governança',
        'habilidades-praticas': 'Habilidades e Práticas',
        'infraestrutura-processos': 'Infraestrutura e Processos'
    }
    return titles.get(category_id, category_id)

def create_category_index(category: Dict[str, Any], glossary: Dict[str, Any]) -> str:
    """Cria a página índice de uma categoria"""
    
    content = f"# {category['title']}\n\n"
    
    if 'description' in category:
        content += f"{category['description']}\n\n"
    
    # Lista de termos em cards
    content += "## Termos nesta categoria\n\n"
    content += '<div class="grid cards" markdown>\n\n'
    
    for term in category['terms']:
        # Card para cada termo
        content += f"- **[{term['title_pt']}]({term['slug']}.md)**\n\n"
        
        # Título em inglês e aliases
        if 'title_en' in term:
            content += f"    *{term['title_en']}*"
            if 'aliases' in term:
                aliases = ", ".join(term['aliases'])
                content += f" · `{aliases}`"
            content += "\n\n"
        
        # Definição completa com links corrigidos
        definition = fix_internal_links(term['definition_pt'], glossary).strip()
        content += f"    {definition}\n\n"
    
    content += "</div>\n\n"
    
    # Estatísticas
    content += f"**Total de termos:** {len(category['terms'])}\n\n"
    
    return content

def create_main_index(glossary: Dict[str, Any]) -> str:
    """Cria a página inicial do site"""
    
    content = """# Glossário de Inteligência Artificial

Bem-vindo ao glossário mais abrangente de termos de Inteligência Artificial em português! 

Este glossário foi criado para ser uma referência completa e acessível para estudantes, profissionais e entusiastas da área de IA.

## 🎯 Navegação

Escolha uma das formas de explorar o conteúdo:

<div class="grid cards" markdown>

- :material-book-open-variant:{ .lg .middle } **Por Categoria**

    ---

    Explore os termos organizados por áreas temáticas

    [:octicons-arrow-right-24: Ver categorias](#categorias)

- :material-sort-alphabetical-ascending:{ .lg .middle } **Ordem Alfabética**

    ---

    Encontre rapidamente qualquer termo em ordem alfabética

    [:octicons-arrow-right-24: Lista A-Z](alfabetico.md)

- :material-tag-multiple:{ .lg .middle } **Por Tags**

    ---

    Descubra termos relacionados através de tags temáticas

    [:octicons-arrow-right-24: Ver tags](tags.md)

</div>

## 📚 Categorias

"""
    
    # Lista das categorias
    for category in glossary['categories']:
        content += f"### [{category['title']}]({category['id']}/index.md)\n\n"
        content += f"{category['description']}\n\n"
        content += f"**{len(category['terms'])} termos**\n\n"
    
    # Estatísticas gerais
    total_terms = sum(len(cat['terms']) for cat in glossary['categories'])
    content += f"""
## 📊 Estatísticas

- **{total_terms}** termos totais
- **{len(glossary['categories'])}** categorias
- **Última atualização:** {glossary['metadata']['created']}

## 🤝 Contribuindo

Este é um projeto em constante evolução! Contribuições são bem-vindas:

- [:material-github: Repositório no GitHub](https://github.com/seu-usuario/glossario-ia)
- [:material-pencil: Sugerir melhorias](https://github.com/seu-usuario/glossario-ia/issues)
- [:material-book-plus: Propor novos termos](https://github.com/seu-usuario/glossario-ia/issues)

---

> **Dica:** Use a barra de busca no topo da página para encontrar rapidamente qualquer termo!
"""
    
    return content

def create_alphabetical_index(glossary: Dict[str, Any]) -> str:
    """Cria a página com todos os termos em ordem alfabética"""
    
    content = "# Índice Alfabético\n\n"
    content += "Todos os termos do glossário em ordem alfabética:\n\n"
    
    # Coleta todos os termos
    all_terms = []
    for category in glossary['categories']:
        for term in category['terms']:
            term_with_category = term.copy()
            term_with_category['category_id'] = category['id']
            term_with_category['category_title'] = category['title']
            all_terms.append(term_with_category)
    
    # Ordena alfabeticamente
    all_terms.sort(key=lambda x: x['title_pt'].lower())
    
    # Agrupa por letra inicial
    current_letter = ""
    for term in all_terms:
        first_letter = term['title_pt'][0].upper()
        if first_letter != current_letter:
            if current_letter:  # Não é a primeira letra
                content += "\n"
            content += f"## {first_letter}\n\n"
            current_letter = first_letter
        
        content += f"- **[{term['title_pt']}]({term['category_id']}/{term['slug']}.md)** "
        content += f"*({term['category_title']})*"
        if 'title_en' in term:
            content += f" — {term['title_en']}"
        content += "\n"
    
    return content

def create_tags_page(glossary: Dict[str, Any]) -> str:
    """Cria a página de tags"""
    
    content = "# Tags\n\n"
    content += "Explore termos por tags temáticas:\n\n"
    
    # Coleta todas as tags
    all_tags = {}
    for category in glossary['categories']:
        for term in category['terms']:
            if 'tags' in term:
                for tag in term['tags']:
                    if tag not in all_tags:
                        all_tags[tag] = []
                    all_tags[tag].append({
                        'term': term,
                        'category_id': category['id'],
                        'category_title': category['title']
                    })
    
    # Ordena tags alfabeticamente
    sorted_tags = sorted(all_tags.keys())
    
    for tag in sorted_tags:
        terms = all_tags[tag]
        content += f"## {tag.replace('-', ' ').title()}\n\n"
        content += f"**{len(terms)} termos:**\n\n"
        
        for item in sorted(terms, key=lambda x: x['term']['title_pt']):
            term = item['term']
            category_id = item['category_id']
            content += f"- **[{term['title_pt']}]({category_id}/{term['slug']}.md)** "
            content += f"*({item['category_title']})*"
            if 'title_en' in term:
                content += f" — {term['title_en']}"
            content += "\n"
        
        content += "\n"
    
    return content

def create_about_page() -> str:
    """Cria a página Sobre"""
    
    return """# Sobre este Glossário

## 🎯 Objetivo

Este glossário foi criado para ser uma referência completa e acessível de termos de Inteligência Artificial em português brasileiro. Nosso objetivo é democratizar o conhecimento sobre IA, fornecendo definições claras e precisas para estudantes, profissionais e entusiastas.

## 🧠 Metodologia

- **Organização temática:** Os termos são organizados em categorias lógicas para facilitar o aprendizado progressivo
- **Definições claras:** Cada termo é explicado em linguagem acessível, sem perder a precisão técnica
- **Links internos:** Termos relacionados são interligados para facilitar a navegação e compreensão
- **Bilíngue:** Todos os termos incluem equivalentes em inglês quando aplicável

## 🛠 Tecnologias

Este site é construído com:

- **[MkDocs Material](https://squidfunk.github.io/mkdocs-material/):** Framework para documentação estática
- **[YAML](https://yaml.org/):** Formato estruturado para os dados do glossário
- **[Python](https://python.org/):** Scripts para geração automática das páginas
- **[GitHub Pages](https://pages.github.com/):** Hospedagem gratuita

## 📄 Licença

Este projeto é disponibilizado sob licença aberta. Você pode:

- ✅ Usar o conteúdo para fins educacionais
- ✅ Compartilhar e redistribuir
- ✅ Sugerir melhorias e correções
- ✅ Criar trabalhos derivados

## 🤝 Contribuições

Contribuições são muito bem-vindas! Você pode:

1. **Reportar erros** via [GitHub Issues](https://github.com/seu-usuario/glossario-ia/issues)
2. **Sugerir novos termos** com definições
3. **Melhorar definições existentes**
4. **Corrigir links ou formatação**

## 📧 Contato

- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- Issues: [Reportar problema](https://github.com/seu-usuario/glossario-ia/issues)

---

**Versão atual:** 1.0.0 | **Última atualização:** Janeiro 2025
"""

def create_css_extras() -> str:
    """Cria CSS customizado"""
    
    return """/* Estilos customizados para o Glossário de IA */

/* Cards de termos */
.grid.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 1.5rem;
    margin: 1.5rem 0;
}

.grid.cards li {
    background: var(--md-default-bg-color);
    border: 1px solid var(--md-default-fg-color--lightest);
    border-radius: 0.5rem;
    padding: 1.5rem;
    list-style: none;
    transition: all 0.2s ease;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

.grid.cards li:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    transform: translateY(-2px);
}

.grid.cards li p {
    margin-bottom: 0.8rem;
    line-height: 1.6;
}

/* Tags de termos */
.tags {
    margin: 0.5rem 0;
}

.tags code {
    background: var(--md-accent-bg-color);
    color: var(--md-accent-fg-color);
    padding: 0.1rem 0.3rem;
    border-radius: 0.2rem;
    font-size: 0.8rem;
}

/* Navegação de breadcrumbs */
.breadcrumbs {
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: var(--md-default-fg-color--light);
}

/* Definições de termos */
.definition {
    font-size: 1.1rem;
    line-height: 1.6;
    margin: 1rem 0;
}

/* Links internos destacados */
a[href^="#"] {
    color: var(--md-accent-fg-color);
    text-decoration: none;
    border-bottom: 1px dotted;
}

a[href^="#"]:hover {
    border-bottom: 1px solid;
}
"""

def create_js_extras() -> str:
    """Cria JavaScript customizado"""
    
    return """// JavaScript customizado para o Glossário de IA

document.addEventListener('DOMContentLoaded', function() {
    // Adiciona ícones aos links externos
    const externalLinks = document.querySelectorAll('a[href^="http"]');
    externalLinks.forEach(link => {
        if (!link.hostname === window.location.hostname) {
            link.classList.add('external-link');
            link.setAttribute('target', '_blank');
            link.setAttribute('rel', 'noopener noreferrer');
        }
    });
    
    // Scroll suave para âncoras
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});
"""

def generate_all_docs():
    """Função principal que gera toda a documentação"""
    
    print("🚀 Gerando documentação do Glossário de IA...")
    
    # Carrega o glossário
    glossary = load_glossary()
    
    # Cria estrutura de diretórios
    ensure_docs_structure()
    
    # Página inicial
    print("📝 Criando página inicial...")
    with open("docs/index.md", "w", encoding="utf-8") as f:
        f.write(create_main_index(glossary))
    
    # Página alfabética
    print("🔤 Criando índice alfabético...")
    with open("docs/alfabetico.md", "w", encoding="utf-8") as f:
        f.write(create_alphabetical_index(glossary))
    
    # Página sobre
    print("ℹ️ Criando página Sobre...")
    with open("docs/sobre.md", "w", encoding="utf-8") as f:
        f.write(create_about_page())
    
    # CSS e JS customizados
    print("🎨 Criando estilos customizados...")
    with open("docs/stylesheets/extra.css", "w", encoding="utf-8") as f:
        f.write(create_css_extras())
    
    with open("docs/javascripts/extra.js", "w", encoding="utf-8") as f:
        f.write(create_js_extras())
    
    # Páginas das categorias
    print("📚 Criando páginas de categorias...")
    for category in glossary['categories']:
        category_dir = f"docs/{category['id']}"
        
        # Página índice da categoria
        with open(f"{category_dir}/index.md", "w", encoding="utf-8") as f:
            f.write(create_category_index(category, glossary))
        
        # Páginas individuais dos termos
        print(f"  📖 Criando {len(category['terms'])} termos da categoria {category['title']}")
        for term in category['terms']:
            with open(f"{category_dir}/{term['slug']}.md", "w", encoding="utf-8") as f:
                f.write(create_term_page(term, category['id'], glossary))
    
    # Página de tags
    print("🏷️ Criando página de tags...")
    with open("docs/tags.md", "w", encoding="utf-8") as f:
        f.write(create_tags_page(glossary))
    
    print("✅ Documentação gerada com sucesso!")
    print("\n📋 Próximos passos:")
    print("1. Instalar dependências: pip install -r requirements.txt")
    print("2. Testar localmente: mkdocs serve")
    print("3. Publicar: mkdocs gh-deploy")

if __name__ == "__main__":
    generate_all_docs()
