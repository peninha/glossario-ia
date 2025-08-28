#!/usr/bin/env python3
"""
Script para adicionar novos termos ao glossário
"""

import os
from pathlib import Path
from datetime import datetime
import re

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = text.lower()
    text = re.sub(r'[àáâãäå]', 'a', text)
    text = re.sub(r'[èéêë]', 'e', text)
    text = re.sub(r'[ìíîï]', 'i', text)
    text = re.sub(r'[òóôõö]', 'o', text)
    text = re.sub(r'[ùúûü]', 'u', text)
    text = re.sub(r'[ç]', 'c', text)
    text = re.sub(r'[ñ]', 'n', text)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'-+', '-', text)
    return text.strip('-')

def get_categories():
    """Get available categories"""
    return {
        '1': ('conceitos-fundamentais', 'Conceitos Fundamentais'),
        '2': ('ia-generativa', 'IA Generativa'),
        '3': ('agentes-ia', 'Agentes de IA'),
        '4': ('escopo-ias', 'Escopo das IAs'),
        '5': ('etica-seguranca-governanca', 'Ética, Segurança e Governança'),
        '6': ('habilidades-praticas', 'Habilidades e Práticas'),
        '7': ('infraestrutura-processos', 'Infraestrutura e Processos')
    }

def create_term_file(term_name, category_dir, category_name, definition, explanation, examples, related_terms, tags):
    """Create a new term file"""
    
    # Create filename
    filename = slugify(term_name) + '.md'
    file_path = Path('docs') / category_dir / filename
    
    # Ensure directory exists
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Format examples
    examples_section = ""
    if examples:
        examples_section = "\n## Exemplos\n\n"
        for i, example in enumerate(examples, 1):
            examples_section += f"### Exemplo {i}\n{example}\n\n"
    
    # Format related terms
    related_section = ""
    if related_terms:
        related_section = "\n## Termos Relacionados\n\n"
        for term in related_terms:
            term_slug = slugify(term)
            related_section += f"- [{term}]({term_slug}.md)\n"
    
    # Create content
    content = f"""# {term_name}

{definition}

## Explicação Detalhada

{explanation}{examples_section}{related_section}

## Referências

- Adicionar fontes relevantes

---

**Tags:** {', '.join(f'`{tag}`' for tag in tags)}  
**Categoria:** {category_name}  
**Última atualização:** {datetime.now().strftime('%Y-%m-%d')}
"""
    
    # Write file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return file_path

def update_category_index(category_dir, term_name, filename):
    """Update category index file"""
    index_path = Path('docs') / category_dir / 'index.md'
    
    if index_path.exists():
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Add term to the list (simple approach - just append)
        term_slug = filename.replace('.md', '')
        new_line = f"- [{term_name}]({term_slug}.md)"
        
        # Find where to insert (look for existing list)
        if '- [' in content:
            lines = content.split('\n')
            for i, line in enumerate(lines):
                if line.startswith('- ['):
                    # Insert in alphabetical order
                    if term_name.lower() < line.split('[')[1].split(']')[0].lower():
                        lines.insert(i, new_line)
                        break
            else:
                # Add at the end of the list
                for i in range(len(lines) - 1, -1, -1):
                    if lines[i].startswith('- ['):
                        lines.insert(i + 1, new_line)
                        break
            
            content = '\n'.join(lines)
        else:
            # No list found, add at the end
            content += f"\n\n{new_line}"
        
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    """Main function to add a new term"""
    print("📝 Adicionar Novo Termo ao Glossário")
    print("=" * 40)
    
    # Get term name
    term_name = input("Nome do termo: ").strip()
    if not term_name:
        print("❌ Nome do termo é obrigatório")
        return
    
    # Get category
    categories = get_categories()
    print("\nCategorias disponíveis:")
    for key, (_, name) in categories.items():
        print(f"{key}. {name}")
    
    category_choice = input("\nEscolha a categoria (1-7): ").strip()
    if category_choice not in categories:
        print("❌ Categoria inválida")
        return
    
    category_dir, category_name = categories[category_choice]
    
    # Get term details
    print(f"\n📖 Criando termo '{term_name}' na categoria '{category_name}'")
    print("-" * 50)
    
    definition = input("Definição curta (1 frase): ").strip()
    if not definition:
        print("❌ Definição é obrigatória")
        return
    
    print("\nExplicação detalhada (pressione Enter duas vezes para finalizar):")
    explanation_lines = []
    while True:
        line = input()
        if line == "" and explanation_lines and explanation_lines[-1] == "":
            break
        explanation_lines.append(line)
    
    explanation = '\n'.join(explanation_lines).strip()
    if not explanation:
        explanation = definition
    
    # Get examples
    examples = []
    print("\nExemplos (opcional, Enter para pular):")
    while True:
        example = input(f"Exemplo {len(examples) + 1}: ").strip()
        if not example:
            break
        examples.append(example)
    
    # Get related terms
    related_terms = []
    print("\nTermos relacionados (opcional, Enter para pular):")
    while True:
        related = input(f"Termo relacionado {len(related_terms) + 1}: ").strip()
        if not related:
            break
        related_terms.append(related)
    
    # Get tags
    tags_input = input("\nTags (separadas por vírgula): ").strip()
    tags = [tag.strip() for tag in tags_input.split(',') if tag.strip()]
    
    # Create the file
    try:
        file_path = create_term_file(
            term_name, category_dir, category_name, 
            definition, explanation, examples, related_terms, tags
        )
        
        # Update category index
        update_category_index(category_dir, term_name, file_path.name)
        
        print(f"\n✅ Termo criado com sucesso!")
        print(f"📁 Arquivo: {file_path}")
        print(f"🌐 Será visível em: https://peninha.github.io/glossario-ia/{category_dir}/{file_path.stem}")
        
        print(f"\n📋 Próximos passos:")
        print(f"1. git add {file_path}")
        print(f"2. git commit -m 'Adiciona termo: {term_name}'")
        print(f"3. git push origin main")
        print(f"4. Aguardar deploy automático")
        
    except Exception as e:
        print(f"❌ Erro ao criar termo: {e}")

if __name__ == "__main__":
    main()
