#!/usr/bin/env python3
"""
Script para exportar o glossário para PDF, Word e TXT atualizados
"""

import os
import yaml
from pathlib import Path
from datetime import datetime
import subprocess
import sys

def install_packages():
    """Install required packages if not available"""
    try:
        import markdown
        import weasyprint
        from docx import Document
    except ImportError:
        print("📦 Instalando dependências...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", 
                              "markdown", "weasyprint", "python-docx"])
        import markdown
        import weasyprint
        from docx import Document

def load_docs_content():
    """Load all documentation content"""
    docs_dir = Path('docs')
    content = {}
    
    # Categories mapping
    categories = {
        'conceitos-fundamentais': 'Conceitos Fundamentais',
        'ia-generativa': 'IA Generativa',
        'agentes-ia': 'Agentes de IA',
        'escopo-ias': 'Escopo das IAs',
        'etica-seguranca-governanca': 'Ética, Segurança e Governança',
        'habilidades-praticas': 'Habilidades e Práticas',
        'infraestrutura-processos': 'Infraestrutura e Processos'
    }
    
    for category_dir, category_name in categories.items():
        category_path = docs_dir / category_dir
        if category_path.exists():
            content[category_name] = []
            
            # Get all .md files except index
            for md_file in sorted(category_path.glob('*.md')):
                if md_file.name != 'index.md':
                    with open(md_file, 'r', encoding='utf-8') as f:
                        file_content = f.read()
                    
                    # Extract title and content
                    lines = file_content.split('\n')
                    title = lines[0].replace('# ', '') if lines else md_file.stem
                    body = '\n'.join(lines[1:]).strip()
                    
                    content[category_name].append({
                        'title': title,
                        'content': body,
                        'id': md_file.stem
                    })
    
    return content

def generate_html(content):
    """Generate HTML from content"""
    install_packages()
    import markdown
    
    html_parts = ["""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Glossário de Inteligência Artificial</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }
            h1 { color: #2c3e50; border-bottom: 3px solid #3498db; padding-bottom: 10px; }
            h2 { color: #34495e; border-bottom: 1px solid #bdc3c7; padding-bottom: 5px; margin-top: 40px; }
            h3 { color: #2980b9; margin-top: 30px; }
            .term { margin-bottom: 30px; border-left: 4px solid #3498db; padding-left: 20px; }
            .meta { color: #7f8c8d; font-size: 0.9em; }
            .toc { background: #f8f9fa; padding: 20px; margin: 20px 0; border-radius: 5px; }
            .toc ul { list-style-type: none; }
            .toc a { text-decoration: none; color: #2980b9; }
            .footer { margin-top: 50px; text-align: center; color: #95a5a6; }
        </style>
    </head>
    <body>
    """]
    
    # Header
    html_parts.append(f"""
        <h1>Glossário de Inteligência Artificial</h1>
        <div class="meta">
            <p><strong>Versão:</strong> {datetime.now().strftime('%Y-%m-%d')}</p>
            <p><strong>Total de categorias:</strong> {len(content)}</p>
            <p><strong>Gerado em:</strong> {datetime.now().strftime('%d/%m/%Y às %H:%M')}</p>
        </div>
    """)
    
    # Table of Contents
    html_parts.append('<div class="toc"><h2>Índice</h2><ul>')
    for category_name in content.keys():
        html_parts.append(f'<li><a href="#{category_name.lower().replace(" ", "-")}">{category_name}</a></li>')
    html_parts.append('</ul></div>')
    
    # Content
    md = markdown.Markdown(extensions=['extra', 'toc'])
    
    for category_name, terms in content.items():
        html_parts.append(f'<h2 id="{category_name.lower().replace(" ", "-")}">{category_name}</h2>')
        
        for term in terms:
            html_parts.append(f'<div class="term">')
            html_parts.append(f'<h3>{term["title"]}</h3>')
            html_parts.append(md.convert(term["content"]))
            html_parts.append('</div>')
    
    # Footer
    html_parts.append(f"""
        <div class="footer">
            <hr>
            <p>Glossário de Inteligência Artificial - {datetime.now().year}</p>
            <p>Gerado automaticamente a partir do repositório: github.com/peninha/glossario-ia</p>
        </div>
    """)
    
    html_parts.append('</body></html>')
    
    return '\n'.join(html_parts)

def export_to_pdf(html_content, output_file='glossario_ia.pdf'):
    """Export HTML to PDF"""
    try:
        import weasyprint
        weasyprint.HTML(string=html_content).write_pdf(output_file)
        print(f"✅ PDF exportado: {output_file}")
        return True
    except Exception as e:
        print(f"❌ Erro ao exportar PDF: {e}")
        return False

def export_to_word(content, output_file='glossario_ia.docx'):
    """Export content to Word document"""
    try:
        from docx import Document
        from docx.shared import Inches
        
        doc = Document()
        
        # Title
        title = doc.add_heading('Glossário de Inteligência Artificial', 0)
        
        # Metadata
        p = doc.add_paragraph()
        p.add_run(f'Versão: {datetime.now().strftime("%Y-%m-%d")}\n').bold = True
        p.add_run(f'Total de categorias: {len(content)}\n')
        p.add_run(f'Gerado em: {datetime.now().strftime("%d/%m/%Y às %H:%M")}\n')
        
        # Content
        for category_name, terms in content.items():
            doc.add_heading(category_name, level=1)
            
            for term in terms:
                doc.add_heading(term['title'], level=2)
                doc.add_paragraph(term['content'])
        
        doc.save(output_file)
        print(f"✅ Word exportado: {output_file}")
        return True
    except Exception as e:
        print(f"❌ Erro ao exportar Word: {e}")
        return False

def export_to_txt(content, output_file='glossario_ia.txt'):
    """Export content to plain text"""
    try:
        lines = [
            "GLOSSÁRIO DE INTELIGÊNCIA ARTIFICIAL",
            "=" * 50,
            f"Versão: {datetime.now().strftime('%Y-%m-%d')}",
            f"Total de categorias: {len(content)}",
            f"Gerado em: {datetime.now().strftime('%d/%m/%Y às %H:%M')}",
            "",
            "=" * 50,
            ""
        ]
        
        for category_name, terms in content.items():
            lines.append(f"\n{category_name.upper()}")
            lines.append("-" * len(category_name))
            lines.append("")
            
            for term in terms:
                lines.append(f"📖 {term['title']}")
                lines.append("")
                lines.append(term['content'])
                lines.append("")
                lines.append("-" * 40)
                lines.append("")
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
        
        print(f"✅ TXT exportado: {output_file}")
        return True
    except Exception as e:
        print(f"❌ Erro ao exportar TXT: {e}")
        return False

def main():
    """Main export function"""
    print("📄 Exportando Glossário de IA...")
    print("=" * 50)
    
    # Load content from docs
    content = load_docs_content()
    
    if not content:
        print("❌ Nenhum conteúdo encontrado na pasta docs/")
        return
    
    total_terms = sum(len(terms) for terms in content.values())
    print(f"📊 {len(content)} categorias, {total_terms} termos encontrados")
    print()
    
    # Generate HTML
    html_content = generate_html(content)
    
    # Export options
    exports = {
        'PDF': lambda: export_to_pdf(html_content),
        'Word': lambda: export_to_word(content),
        'TXT': lambda: export_to_txt(content)
    }
    
    # Ask user which formats to export
    print("Formatos disponíveis:")
    for i, format_name in enumerate(exports.keys(), 1):
        print(f"{i}. {format_name}")
    print("4. Todos")
    
    choice = input("\nEscolha o formato (1-4): ").strip()
    
    if choice == "4":
        # Export all
        for name, func in exports.items():
            func()
    elif choice in ["1", "2", "3"]:
        format_names = list(exports.keys())
        chosen_format = format_names[int(choice) - 1]
        exports[chosen_format]()
    else:
        print("❌ Opção inválida")
        return
    
    print("\n✅ Exportação concluída!")

if __name__ == "__main__":
    main()
