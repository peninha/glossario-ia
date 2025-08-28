#!/usr/bin/env python3
"""
Script para sincronizar o YAML a partir dos arquivos MD existentes
Útil quando verbetes são editados diretamente no GitHub
"""

import os
import yaml
import re
from pathlib import Path
from typing import Dict, List, Any

def extract_frontmatter_and_content(file_path: str) -> tuple:
    """Extract frontmatter and content from a markdown file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has frontmatter
    if content.startswith('---\n'):
        parts = content.split('---\n', 2)
        if len(parts) >= 3:
            frontmatter = yaml.safe_load(parts[1])
            content_body = parts[2].strip()
            return frontmatter, content_body
    
    # No frontmatter, extract from markdown
    lines = content.split('\n')
    title = lines[0].replace('# ', '') if lines else ''
    content_body = '\n'.join(lines[1:]).strip()
    
    return {'title': title}, content_body

def extract_tags_from_content(content: str) -> List[str]:
    """Extract tags from content (get from actual tags line)"""
    import re
    
    # Look for tags line in content
    tag_match = re.search(r'\*\*Tags:\*\*\s*([^\n]+)', content)
    if not tag_match:
        return []
    
    tags_line = tag_match.group(1)
    # Extract tags between backticks
    tags = re.findall(r'`([^`]+)`', tags_line)
    
    return tags

def determine_category_from_path(file_path: str) -> str:
    """Determine category from file path"""
    path_parts = Path(file_path).parts
    
    category_mapping = {
        'conceitos-fundamentais': 'fundamentos',
        'ia-generativa': 'generative',
        'agentes-ia': 'agents',
        'escopo-ias': 'scope',
        'etica-seguranca-governanca': 'ethics',
        'habilidades-praticas': 'skills',
        'infraestrutura-processos': 'infrastructure'
    }
    
    for part in path_parts:
        if part in category_mapping:
            return category_mapping[part]
    
    return 'fundamentos'  # default

def scan_docs_directory() -> Dict[str, Any]:
    """Scan docs directory and build YAML structure"""
    
    docs_dir = Path('docs')
    terms = {}
    
    # Find all .md files except index and navigation files
    for md_file in docs_dir.rglob('*.md'):
        # Skip navigation files
        if md_file.name in ['index.md', 'alfabetico.md', 'tags.md', 'sobre.md']:
            continue
            
        # Extract term info
        frontmatter, content = extract_frontmatter_and_content(str(md_file))
        
        # Get term ID from filename
        term_id = md_file.stem
        
        # Build term entry
        term_entry = {
            'nome': frontmatter.get('title', term_id.replace('-', ' ').title()),
            'categoria': determine_category_from_path(str(md_file)),
            'definicao': content.split('\n')[0][:200] + '...' if len(content) > 200 else content.split('\n')[0],
            'explicacao': content,
            'tags': extract_tags_from_content(content),
            'relacionados': []  # This would need manual curation
        }
        
        terms[term_id] = term_entry
    
    return {
        'metadata': {
            'versao': '2.0',
            'ultima_atualizacao': '2025-01-27',
            'total_termos': len(terms),
            'fonte': 'Sincronizado a partir dos arquivos MD'
        },
        'categorias': {
            'fundamentos': 'Conceitos Fundamentais',
            'generative': 'IA Generativa', 
            'agents': 'Agentes de IA',
            'scope': 'Escopo das IAs',
            'ethics': 'Ética, Segurança e Governança',
            'skills': 'Habilidades e Práticas',
            'infrastructure': 'Infraestrutura e Processos'
        },
        'termos': terms
    }

def main():
    """Main function to sync YAML from docs"""
    print("🔄 Sincronizando YAML a partir dos arquivos MD...")
    
    # Scan docs and build YAML
    yaml_data = scan_docs_directory()
    
    # Save to glossario.yaml
    with open('glossario_synced.yaml', 'w', encoding='utf-8') as f:
        yaml.dump(yaml_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
    
    print(f"✅ YAML sincronizado salvo em 'glossario_synced.yaml'")
    print(f"📊 Total de termos encontrados: {yaml_data['metadata']['total_termos']}")
    
    # Optional: backup original and replace
    response = input("\n❓ Substituir o glossario.yaml original? (y/N): ")
    if response.lower() == 'y':
        import shutil
        shutil.copy('glossario.yaml', 'glossario_backup.yaml')
        shutil.copy('glossario_synced.yaml', 'glossario.yaml')
        print("✅ glossario.yaml atualizado (backup salvo como glossario_backup.yaml)")

if __name__ == "__main__":
    main()
