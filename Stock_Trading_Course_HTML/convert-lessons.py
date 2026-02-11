#!/usr/bin/env python3
"""
Convert all markdown lessons from the Stock Trading Course to HTML
"""

import os
import re
import json
from pathlib import Path
from collections import defaultdict

# Configuration
SOURCE_DIR = "/sessions/kind-charming-bardeen/mnt/Course/Stock_Trading_Course"
OUTPUT_DIR = "/sessions/kind-charming-bardeen/mnt/Course/Stock_Trading_Course_HTML/pages"
BASE_URL = "../"

# Ensure output directory exists
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

class MarkdownToHTML:
    def __init__(self):
        self.lessons = defaultdict(dict)
        self.lesson_order = []

    def read_markdown(self, filepath):
        """Read markdown file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading {filepath}: {e}")
            return None

    def sanitize_filename(self, text):
        """Convert text to safe filename"""
        # Remove special characters
        text = re.sub(r'[^a-z0-9]', '-', text.lower())
        # Remove consecutive dashes
        text = re.sub(r'-+', '-', text)
        # Strip dashes from start/end
        text = text.strip('-')
        return text

    def markdown_to_html(self, content):
        """Convert markdown to HTML"""
        if not content:
            return ""

        lines = content.split('\n')
        html = []
        in_code_block = False
        code_language = ""
        in_list = False
        in_ordered_list = False

        i = 0
        while i < len(lines):
            line = lines[i]

            # Code blocks
            if line.startswith('```'):
                if not in_code_block:
                    code_language = line.replace('```', '').strip()
                    in_code_block = True
                    html.append('<pre><code>')
                else:
                    in_code_block = False
                    html.append('</code></pre>')
                i += 1
                continue

            if in_code_block:
                # Escape HTML in code blocks
                html.append(self.escape_html(line) + '\n')
                i += 1
                continue

            # Headers
            if line.startswith('### '):
                if in_list:
                    html.append('</ul>')
                    in_list = False
                if in_ordered_list:
                    html.append('</ol>')
                    in_ordered_list = False
                html.append(f"<h3>{self.process_inline(line[4:])}</h3>")
                i += 1
                continue

            if line.startswith('## '):
                if in_list:
                    html.append('</ul>')
                    in_list = False
                if in_ordered_list:
                    html.append('</ol>')
                    in_ordered_list = False
                html.append(f"<h2>{self.process_inline(line[3:])}</h2>")
                i += 1
                continue

            if line.startswith('# '):
                if in_list:
                    html.append('</ul>')
                    in_list = False
                if in_ordered_list:
                    html.append('</ol>')
                    in_ordered_list = False
                html.append(f"<h1>{self.process_inline(line[2:])}</h1>")
                i += 1
                continue

            # Blockquote
            if line.startswith('> '):
                html.append(f"<blockquote>{self.process_inline(line[2:])}</blockquote>")
                i += 1
                continue

            # Horizontal rule
            if line.strip() in ['---', '***', '___']:
                html.append("<hr>")
                i += 1
                continue

            # Lists
            if line.startswith('* ') or line.startswith('- '):
                if not in_list and in_ordered_list:
                    html.append('</ol>')
                    in_ordered_list = False
                if not in_list:
                    html.append('<ul>')
                    in_list = True
                html.append(f"<li>{self.process_inline(line[2:])}</li>")
                i += 1
                continue

            # Ordered lists
            if re.match(r'^\d+\.\s', line):
                if not in_ordered_list and in_list:
                    html.append('</ul>')
                    in_list = False
                if not in_ordered_list:
                    html.append('<ol>')
                    in_ordered_list = True
                match = re.match(r'^\d+\.\s(.+)', line)
                if match:
                    html.append(f"<li>{self.process_inline(match.group(1))}</li>")
                i += 1
                continue

            # Close lists for blank lines or other content
            if line.strip() == '':
                if in_list:
                    html.append('</ul>')
                    in_list = False
                if in_ordered_list:
                    html.append('</ol>')
                    in_ordered_list = False
                if html and html[-1] not in ['</ul>', '</ol>', '<hr>']:
                    html.append('<p></p>')
                i += 1
                continue

            # Regular paragraph
            if line.strip():
                if in_list:
                    html.append('</ul>')
                    in_list = False
                if in_ordered_list:
                    html.append('</ol>')
                    in_ordered_list = False
                html.append(f"<p>{self.process_inline(line)}</p>")

            i += 1

        # Close any open lists
        if in_list:
            html.append('</ul>')
        if in_ordered_list:
            html.append('</ol>')

        return '\n'.join(html)

    def process_inline(self, text):
        """Process inline markdown (bold, italic, links, code)"""
        # Bold
        text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
        text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)

        # Italic
        text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
        text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)

        # Links
        text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', text)

        # Inline code
        text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)

        return text

    def escape_html(self, text):
        """Escape HTML special characters"""
        return (text
                .replace('&', '&amp;')
                .replace('<', '&lt;')
                .replace('>', '&gt;')
                .replace('"', '&quot;')
                .replace("'", '&#39;'))

    def extract_title(self, content):
        """Extract title from markdown content"""
        lines = content.split('\n')
        for line in lines[:10]:
            if line.startswith('# '):
                return line[2:].strip()
        return "Untitled"

    def generate_html_page(self, title, content, lesson_id, chapter_num, lesson_num):
        """Generate complete HTML page"""

        # Determine navigation
        prev_id = None
        next_id = None

        # Try to find previous and next lessons
        for i, lid in enumerate(self.lesson_order):
            if lid == lesson_id:
                if i > 0:
                    prev_id = self.lesson_order[i - 1]
                if i < len(self.lesson_order) - 1:
                    next_id = self.lesson_order[i + 1]
                break

        prev_link = f'<a href="{prev_id}.html" class="nav-btn">← Previous Lesson</a>' if prev_id else '<button class="nav-btn disabled">← Previous Lesson</button>'
        next_link = f'<a href="{next_id}.html" class="nav-btn">Next Lesson →</a>' if next_id else '<button class="nav-btn disabled">Next Lesson →</button>'

        html_content = content

        # Create breadcrumb
        breadcrumb = f'<div class="breadcrumb"><a href="../index.html">Home</a> <span>/</span> <a href="../index.html">Chapter {chapter_num}</a> <span>/</span> <span>{title}</span></div>'

        html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Stock Trading Mastery</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='75' font-size='75' fill='%230066cc'>📈</text></svg>">
</head>
<body>
    <!-- Header -->
    <header>
        <div class="header-content">
            <a href="../index.html" class="logo">📈 Stock Trading Mastery</a>
            <div class="nav-controls">
                <div class="search-box">
                    <input type="text" id="searchInput" placeholder="Search lessons... (Ctrl+K)" class="tab-focus">
                </div>
                <button id="darkModeToggle" class="theme-toggle tab-focus">🌙 Dark Mode</button>
                <button id="menuToggle" class="menu-toggle tab-focus">☰ Menu</button>
            </div>
        </div>
    </header>

    <div class="container">
        <!-- Sidebar Navigation -->
        <aside id="sidebar" class="sidebar mobile-hidden">
            <div class="nav-section">
                <div class="nav-section-title">Navigation</div>
                <a href="../index.html" class="nav-item">Home</a>
                <a href="course-overview.html" class="nav-item">Course Overview</a>
            </div>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <!-- Progress Tracker -->
            <div class="progress-section">
                <div class="progress-header">Your Progress</div>
                <div class="progress-bar-container">
                    <div class="progress-bar" style="width: 0%"></div>
                </div>
                <div class="progress-text">0 / 133 lessons completed (0%)</div>
            </div>

            {breadcrumb}

            <article class="lesson-content">
                <div class="lesson-header">
                    <h1 class="lesson-title">{title}</h1>
                    <div class="lesson-meta">
                        <div class="lesson-meta-item">
                            <span>Chapter {chapter_num}</span>
                        </div>
                        <div class="lesson-meta-item">
                            <span>Lesson {lesson_num}</span>
                        </div>
                        <div class="lesson-meta-item">
                            <button id="bookmarkBtn" class="nav-btn" style="display: inline-block; padding: 0.5rem 1rem; font-size: 0.9rem;">☆ Bookmark</button>
                        </div>
                    </div>
                </div>

                {html_content}

                <div class="lesson-checkbox">
                    <input type="checkbox" id="lessonComplete">
                    <label for="lessonComplete">Mark this lesson as complete</label>
                </div>
            </article>

            <!-- Navigation Between Lessons -->
            <div class="lesson-navigation">
                {prev_link}
                <a href="../index.html" class="nav-btn" style="background: var(--accent-secondary);">Back to Home</a>
                {next_link}
            </div>
        </main>
    </div>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 Stock Trading Mastery Course | Educational Content Only</p>
    </footer>

    <script src="../js/app.js"></script>
</body>
</html>'''

        return html

    def convert_all(self):
        """Convert all markdown files to HTML"""

        # Walk through source directory
        for root, dirs, files in os.walk(SOURCE_DIR):
            for file in sorted(files):
                if file.endswith('.md') and file != 'MASTER_INDEX.md':
                    filepath = os.path.join(root, file)
                    relative_path = os.path.relpath(filepath, SOURCE_DIR)

                    # Skip README files
                    if file == 'README.md':
                        continue

                    markdown_content = self.read_markdown(filepath)
                    if not markdown_content:
                        continue

                    title = self.extract_title(markdown_content)

                    # Create output filename
                    # Examples: lesson_1.1_what_is_stock_market.md -> lesson-1.1.html
                    filename_base = file.replace('.md', '')

                    # Parse lesson number
                    lesson_match = re.search(r'lesson[_-](\d+)\.(\d+)', filename_base)
                    if lesson_match:
                        chapter = lesson_match.group(1)
                        lesson = lesson_match.group(2)
                        output_filename = f"lesson-{chapter}.{lesson}.html"
                    elif 'exercises' in filename_base:
                        chapter_match = re.search(r'(\d+)', filename_base)
                        if chapter_match:
                            chapter = chapter_match.group(1)
                            output_filename = f"exercises-{chapter}.html"
                        else:
                            output_filename = self.sanitize_filename(filename_base) + '.html'
                    else:
                        output_filename = self.sanitize_filename(filename_base) + '.html'

                    output_path = os.path.join(OUTPUT_DIR, output_filename)

                    # Store lesson info for navigation
                    lesson_key = output_filename.replace('.html', '')
                    self.lesson_order.append(lesson_key)
                    self.lessons[lesson_key] = {
                        'title': title,
                        'path': output_path,
                        'chapter': chapter if lesson_match else 0,
                        'lesson': lesson if lesson_match else 0
                    }

        # Now convert and write all files
        for lesson_key in self.lesson_order:
            lesson_info = self.lessons[lesson_key]
            filepath = lesson_info['path'].replace('.html', '.md')

            # Find actual file
            for root, dirs, files in os.walk(SOURCE_DIR):
                for file in files:
                    if file.endswith('.md'):
                        full_path = os.path.join(root, file)
                        expected_name = lesson_key.replace('-', '_').replace('.', '.') + '.md'
                        if file == expected_name or (
                            'lesson' in file and lesson_key.replace('-', '.').replace('lesson', '').strip('.') in file
                        ):
                            markdown_content = self.read_markdown(full_path)
                            if markdown_content:
                                html_content = self.markdown_to_html(markdown_content)
                                title = lesson_info['title']
                                chapter = lesson_info['chapter']
                                lesson_num = lesson_info['lesson']

                                full_html = self.generate_html_page(
                                    title,
                                    html_content,
                                    lesson_key,
                                    chapter,
                                    lesson_num
                                )

                                with open(lesson_info['path'], 'w', encoding='utf-8') as f:
                                    f.write(full_html)

                                print(f"✓ Created: {lesson_key}.html - {title}")
                            break

# Run conversion
if __name__ == "__main__":
    converter = MarkdownToHTML()
    converter.convert_all()
    print("\n✓ Conversion complete!")
