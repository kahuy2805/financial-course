#!/usr/bin/env python3
"""
Build the Stock Trading Course HTML - Converts all MD files to complete HTML pages
"""

import os
import re
import sys
from pathlib import Path
from typing import Tuple, List, Dict

SOURCE_DIR = Path("/sessions/kind-charming-bardeen/mnt/Course/Stock_Trading_Course")
OUTPUT_DIR = Path("/sessions/kind-charming-bardeen/mnt/Course/Stock_Trading_Course_HTML/pages")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Lesson registry to track all lessons for navigation
LESSONS = []
LESSON_MAP = {}

def sanitize_for_filename(text: str) -> str:
    """Convert text to URL-safe filename"""
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = re.sub(r'-+', '-', text).strip('-')
    return text

def extract_title(content: str) -> str:
    """Extract title from markdown content"""
    for line in content.split('\n')[:20]:
        if line.startswith('# '):
            return line[2:].strip()
    return "Untitled Lesson"

def escape_html(text: str) -> str:
    """Escape HTML characters"""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;'))

def md_to_html(markdown: str) -> str:
    """Convert markdown to HTML"""
    if not markdown:
        return ""

    html = []
    lines = markdown.split('\n')
    in_code = False
    in_ul = False
    in_ol = False
    i = 0

    while i < len(lines):
        line = lines[i]

        # Code blocks
        if line.startswith('```'):
            if not in_code:
                in_code = True
                html.append('<pre><code>')
            else:
                in_code = False
                html.append('</code></pre>')
            i += 1
            continue

        if in_code:
            html.append(escape_html(line) + '\n')
            i += 1
            continue

        # Headers
        if line.startswith('### '):
            if in_ul:
                html.append('</ul>')
                in_ul = False
            if in_ol:
                html.append('</ol>')
                in_ol = False
            text = line[4:].strip()
            text = process_inline_md(text)
            html.append(f'<h3>{text}</h3>')
            i += 1
            continue

        if line.startswith('## '):
            if in_ul:
                html.append('</ul>')
                in_ul = False
            if in_ol:
                html.append('</ol>')
                in_ol = False
            text = line[3:].strip()
            text = process_inline_md(text)
            html.append(f'<h2>{text}</h2>')
            i += 1
            continue

        if line.startswith('# '):
            if in_ul:
                html.append('</ul>')
                in_ul = False
            if in_ol:
                html.append('</ol>')
                in_ol = False
            text = line[2:].strip()
            text = process_inline_md(text)
            html.append(f'<h1>{text}</h1>')
            i += 1
            continue

        # Blockquotes
        if line.startswith('> '):
            text = line[2:].strip()
            text = process_inline_md(text)
            html.append(f'<blockquote>{text}</blockquote>')
            i += 1
            continue

        # Horizontal rules
        if line.strip() in ['---', '***', '___']:
            html.append('<hr>')
            i += 1
            continue

        # Lists
        if line.startswith(('* ', '- ')):
            if not in_ul and in_ol:
                html.append('</ol>')
                in_ol = False
            if not in_ul:
                html.append('<ul>')
                in_ul = True
            text = line[2:].strip()
            text = process_inline_md(text)
            html.append(f'<li>{text}</li>')
            i += 1
            continue

        # Ordered lists
        if re.match(r'^\d+\.\s', line):
            if not in_ol and in_ul:
                html.append('</ul>')
                in_ul = False
            if not in_ol:
                html.append('<ol>')
                in_ol = True
            match = re.match(r'^\d+\.\s(.+)', line)
            if match:
                text = process_inline_md(match.group(1))
                html.append(f'<li>{text}</li>')
            i += 1
            continue

        # Empty lines
        if line.strip() == '':
            if in_ul:
                html.append('</ul>')
                in_ul = False
            if in_ol:
                html.append('</ol>')
                in_ol = False
            i += 1
            continue

        # Regular paragraphs
        if line.strip():
            if in_ul:
                html.append('</ul>')
                in_ul = False
            if in_ol:
                html.append('</ol>')
                in_ol = False
            text = process_inline_md(line)
            html.append(f'<p>{text}</p>')

        i += 1

    # Close any open tags
    if in_ul:
        html.append('</ul>')
    if in_ol:
        html.append('</ol>')

    return '\n'.join(html)

def process_inline_md(text: str) -> str:
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

def find_all_lessons() -> List[Tuple[str, Path]]:
    """Find all markdown lesson files"""
    lessons = []

    for md_file in SOURCE_DIR.rglob('*.md'):
        # Skip MASTER_INDEX and README
        if md_file.name in ['MASTER_INDEX.md', 'README.md', 'MASTE_INDEX.md']:
            continue

        # Only process lesson, exercise, and relevant files
        name = md_file.stem
        if any(x in name for x in ['lesson', 'exercise', 'case_study', 'scenario', 'project',
                                     'self_assessment', 'learning_paths', 'progress_tracking',
                                     'coaching_guides', 'troubleshooting', 'how_to_use',
                                     'prerequisites', 'glossary']):
            lessons.append((name, md_file))

    return sorted(lessons)

def extract_lesson_number(filename: str) -> Tuple[int, float, str]:
    """Extract chapter and lesson number from filename"""
    # Match lesson_1.1, lesson_2.3, etc
    match = re.search(r'lesson[_-](\d+)[_-](\d+)', filename)
    if match:
        return (int(match.group(1)), float(f"{match.group(1)}.{match.group(2)}"), filename)

    # Match exercises_1, exercises_2, etc
    match = re.search(r'exercise[s]?[_-](\d+)', filename)
    if match:
        chapter = int(match.group(1))
        return (chapter, chapter + 0.99, filename)

    # Other files
    return (0, 0, filename)

def create_html_page(title: str, content: str, lesson_id: str, chapter: int) -> str:
    """Create complete HTML page for a lesson"""

    # Find position in lessons list for navigation
    prev_btn = '<button class="nav-btn disabled">← Previous Lesson</button>'
    next_btn = '<button class="nav-btn disabled">Next Lesson →</button>'

    for i, (lid, _, _, _, _) in enumerate(LESSONS):
        if lid == lesson_id:
            if i > 0:
                prev_id = LESSONS[i-1][0]
                prev_btn = f'<a href="{prev_id}.html" class="nav-btn">← Previous Lesson</a>'
            if i < len(LESSONS) - 1:
                next_id = LESSONS[i+1][0]
                next_btn = f'<a href="{next_id}.html" class="nav-btn">Next Lesson →</a>'
            break

    breadcrumb = f'<div class="breadcrumb"><a href="../index.html">Home</a> <span>/</span> <span>Chapter {chapter}</span> <span>/</span> <span>{escape_html(title)}</span></div>'

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape_html(title)} - Stock Trading Mastery</title>
    <link rel="stylesheet" href="../css/style.css">
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='75' font-size='75' fill='%230066cc'>📈</text></svg>">
</head>
<body>
    <header>
        <div class="header-content">
            <a href="../index.html" class="logo">📈 Stock Trading Mastery</a>
            <div class="nav-controls">
                <div class="search-box">
                    <input type="text" id="searchInput" placeholder="Search lessons..." class="tab-focus">
                </div>
                <button id="darkModeToggle" class="theme-toggle tab-focus">🌙 Dark Mode</button>
                <button id="menuToggle" class="menu-toggle tab-focus">☰ Menu</button>
            </div>
        </div>
    </header>

    <div class="container">
        <aside id="sidebar" class="sidebar mobile-hidden">
            <div class="nav-section">
                <div class="nav-section-title">Navigation</div>
                <a href="../index.html" class="nav-item">Home</a>
                <a href="course-overview.html" class="nav-item">Course Overview</a>
            </div>
        </aside>

        <main class="main-content">
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
                    <h1 class="lesson-title">{escape_html(title)}</h1>
                    <div class="lesson-meta">
                        <div class="lesson-meta-item">
                            <span>Chapter {chapter}</span>
                        </div>
                    </div>
                </div>

                {content}

                <div class="lesson-checkbox">
                    <input type="checkbox" id="lessonComplete">
                    <label for="lessonComplete">Mark this lesson as complete</label>
                </div>
            </article>

            <div class="lesson-navigation">
                {prev_btn}
                <a href="../index.html" class="nav-btn" style="background: var(--accent-secondary);">Back to Home</a>
                {next_btn}
            </div>
        </main>
    </div>

    <footer>
        <p>&copy; 2026 Stock Trading Mastery Course | Educational Content Only</p>
    </footer>

    <script src="../js/app.js"></script>
</body>
</html>'''

    return html

def main():
    """Main build function"""
    print("Stock Trading Course HTML Builder")
    print("=" * 50)

    # Find all lessons
    all_lessons = find_all_lessons()
    print(f"Found {len(all_lessons)} lesson files")

    # Sort lessons by chapter and number
    sorted_lessons = sorted(all_lessons, key=lambda x: extract_lesson_number(x[0]))

    # Process each lesson
    for i, (name, filepath) in enumerate(sorted_lessons):
        chapter, sort_key, _ = extract_lesson_number(name)

        # Read markdown
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                md_content = f.read()
        except Exception as e:
            print(f"✗ Error reading {name}: {e}")
            continue

        # Extract title
        title = extract_title(md_content)

        # Convert to HTML
        html_content = md_to_html(md_content)

        # Create HTML page
        output_filename = f"{sanitize_for_filename(name)}.html"
        output_path = OUTPUT_DIR / output_filename

        # Store lesson info
        LESSONS.append((sanitize_for_filename(name), title, chapter, filepath.stem, html_content))

        print(f"  Processing: {name}")

    # Now write all files with proper navigation
    print("\nWriting HTML files...")
    for i, (lesson_id, title, chapter, _, html_content) in enumerate(LESSONS):
        output_path = OUTPUT_DIR / f"{lesson_id}.html"

        full_html = create_html_page(title, html_content, lesson_id, chapter)

        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(full_html)
            print(f"✓ {output_path.name}")
        except Exception as e:
            print(f"✗ Error writing {output_path}: {e}")

    # Create index pages for case studies, scenarios, projects
    print("\nCreating index pages...")
    create_index_page("case-studies", "Case Studies", "Real-world market examples and analysis")
    create_index_page("simulation-scenarios", "Simulation Scenarios", "Practice trading in realistic scenarios")
    create_index_page("portfolio-projects", "Portfolio Projects", "Build complete portfolio strategies")

    # Create course overview pages
    create_course_overview()
    create_how_to_use()
    create_prerequisites()
    create_glossary()

    print("\n" + "=" * 50)
    print("✓ Build complete!")
    print(f"✓ Created {len(LESSONS)} lesson pages")

def create_index_page(page_id: str, title: str, description: str):
    """Create index page for practical labs"""
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{escape_html(title)} - Stock Trading Mastery</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <header>
        <div class="header-content">
            <a href="../index.html" class="logo">📈 Stock Trading Mastery</a>
            <div class="nav-controls">
                <div class="search-box">
                    <input type="text" id="searchInput" placeholder="Search lessons...">
                </div>
                <button id="darkModeToggle" class="theme-toggle">🌙 Dark Mode</button>
            </div>
        </div>
    </header>

    <div class="container">
        <main class="main-content">
            <div class="breadcrumb"><a href="../index.html">Home</a> <span>/</span> <span>{escape_html(title)}</span></div>

            <h1>{escape_html(title)}</h1>
            <p>{escape_html(description)}</p>

            <div class="alert alert-info">
                <strong>Coming Soon:</strong> Detailed content for this section is being generated.
            </div>

            <a href="../index.html" class="nav-btn">Back to Home</a>
        </main>
    </div>

    <footer>
        <p>&copy; 2026 Stock Trading Mastery Course</p>
    </footer>

    <script src="../js/app.js"></script>
</body>
</html>'''

    output_path = OUTPUT_DIR / f"{page_id}.html"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)

def create_course_overview():
    """Create course overview page"""
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Course Overview - Stock Trading Mastery</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <header>
        <div class="header-content">
            <a href="../index.html" class="logo">📈 Stock Trading Mastery</a>
            <div class="nav-controls">
                <button id="darkModeToggle" class="theme-toggle">🌙 Dark Mode</button>
            </div>
        </div>
    </header>

    <div class="container">
        <main class="main-content">
            <div class="breadcrumb"><a href="../index.html">Home</a> <span>/</span> <span>Course Overview</span></div>

            <h1>Course Overview</h1>

            <h2>What You'll Learn</h2>
            <p>This comprehensive course covers all aspects of stock trading, from fundamentals to professional-level strategies.</p>

            <h3>The 3-Level Progression</h3>
            <ul>
                <li><strong>Level 1: Foundation (Chapters 1-5)</strong> - Essential knowledge and basics</li>
                <li><strong>Level 2: Intermediate (Chapters 6-10)</strong> - Advanced analysis and strategies</li>
                <li><strong>Level 3: Advanced (Chapters 11-14)</strong> - Professional practices and mastery</li>
            </ul>

            <h2>Course Statistics</h2>
            <ul>
                <li>93 comprehensive lessons</li>
                <li>14 in-depth chapters</li>
                <li>15 real-world case studies</li>
                <li>10 simulation scenarios</li>
                <li>5 portfolio projects</li>
                <li>65-95 hours of content</li>
            </ul>

            <a href="../index.html" class="nav-btn">Back to Home</a>
        </main>
    </div>

    <footer>
        <p>&copy; 2026 Stock Trading Mastery Course</p>
    </footer>

    <script src="../js/app.js"></script>
</body>
</html>'''

    with open(OUTPUT_DIR / "course-overview.html", 'w') as f:
        f.write(html)

def create_how_to_use():
    """Create how to use page"""
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>How to Use This Course - Stock Trading Mastery</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <header>
        <div class="header-content">
            <a href="../index.html" class="logo">📈 Stock Trading Mastery</a>
            <div class="nav-controls">
                <button id="darkModeToggle" class="theme-toggle">🌙 Dark Mode</button>
            </div>
        </div>
    </header>

    <div class="container">
        <main class="main-content">
            <div class="breadcrumb"><a href="../index.html">Home</a> <span>/</span> <span>How to Use</span></div>

            <h1>How to Use This Course</h1>

            <h2>Getting the Most Out of Your Learning</h2>
            <p>This course is designed to be flexible, allowing you to learn at your own pace while following a structured path.</p>

            <h3>Recommended Approach</h3>
            <ol>
                <li>Start with the Foundation level (Chapters 1-5)</li>
                <li>Complete exercises at the end of each chapter</li>
                <li>Use the progress tracker to monitor your advancement</li>
                <li>Bookmark lessons you want to revisit</li>
                <li>Progress to Intermediate level when ready</li>
                <li>Study case studies to see real-world applications</li>
                <li>Build your own trading strategies in Advanced level</li>
            </ol>

            <h3>Features to Use</h3>
            <ul>
                <li><strong>Progress Tracker:</strong> See how much you've completed</li>
                <li><strong>Bookmarks:</strong> Save important lessons for quick access</li>
                <li><strong>Search:</strong> Find specific topics quickly</li>
                <li><strong>Dark Mode:</strong> Comfortable reading at any time</li>
                <li><strong>Mobile Friendly:</strong> Learn on any device</li>
            </ul>

            <a href="../index.html" class="nav-btn">Back to Home</a>
        </main>
    </div>

    <footer>
        <p>&copy; 2026 Stock Trading Mastery Course</p>
    </footer>

    <script src="../js/app.js"></script>
</body>
</html>'''

    with open(OUTPUT_DIR / "how-to-use.html", 'w') as f:
        f.write(html)

def create_prerequisites():
    """Create prerequisites page"""
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Prerequisites - Stock Trading Mastery</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <header>
        <div class="header-content">
            <a href="../index.html" class="logo">📈 Stock Trading Mastery</a>
            <div class="nav-controls">
                <button id="darkModeToggle" class="theme-toggle">🌙 Dark Mode</button>
            </div>
        </div>
    </header>

    <div class="container">
        <main class="main-content">
            <div class="breadcrumb"><a href="../index.html">Home</a> <span>/</span> <span>Prerequisites</span></div>

            <h1>Prerequisites</h1>

            <h2>What You Need to Know</h2>
            <p>This course starts from the absolute basics, so no prior trading experience is required.</p>

            <h3>Helpful Background</h3>
            <ul>
                <li>Basic understanding of finance concepts (optional)</li>
                <li>Ability to read financial statements (taught in the course)</li>
                <li>Comfort with using online platforms</li>
                <li>Access to a computer or tablet</li>
            </ul>

            <h3>What You'll Need</h3>
            <ul>
                <li>Pen and paper for note-taking</li>
                <li>A brokerage account (for live trading, optional)</li>
                <li>Access to market data and charts (many free options available)</li>
                <li>Time commitment (flexible, self-paced)</li>
            </ul>

            <a href="../index.html" class="nav-btn">Back to Home</a>
        </main>
    </div>

    <footer>
        <p>&copy; 2026 Stock Trading Mastery Course</p>
    </footer>

    <script src="../js/app.js"></script>
</body>
</html>'''

    with open(OUTPUT_DIR / "prerequisites.html", 'w') as f:
        f.write(html)

def create_glossary():
    """Create glossary page"""
    html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Glossary - Stock Trading Mastery</title>
    <link rel="stylesheet" href="../css/style.css">
</head>
<body>
    <header>
        <div class="header-content">
            <a href="../index.html" class="logo">📈 Stock Trading Mastery</a>
            <div class="nav-controls">
                <button id="darkModeToggle" class="theme-toggle">🌙 Dark Mode</button>
            </div>
        </div>
    </header>

    <div class="container">
        <main class="main-content">
            <div class="breadcrumb"><a href="../index.html">Home</a> <span>/</span> <span>Glossary</span></div>

            <h1>Trading Glossary</h1>

            <p>A comprehensive glossary of trading and finance terms used throughout the course.</p>

            <div class="alert alert-info">
                <strong>Note:</strong> Key terms are defined throughout the course lessons. This page provides a reference for all terminology.
            </div>

            <h2>Common Trading Terms</h2>
            <dl>
                <dt><strong>Bull Market</strong></dt>
                <dd>A market in which prices are rising and investor sentiment is positive</dd>

                <dt><strong>Bear Market</strong></dt>
                <dd>A market in which prices are declining and investor sentiment is negative</dd>

                <dt><strong>Bid-Ask Spread</strong></dt>
                <dd>The difference between the price buyers are willing to pay and sellers are asking</dd>

                <dt><strong>Volume</strong></dt>
                <dd>The total number of shares traded during a specific period</dd>

                <dt><strong>Support Level</strong></dt>
                <dd>A price level where a stock tends to find buying support</dd>

                <dt><strong>Resistance Level</strong></dt>
                <dd>A price level where a stock tends to encounter selling pressure</dd>
            </dl>

            <a href="../index.html" class="nav-btn">Back to Home</a>
        </main>
    </div>

    <footer>
        <p>&copy; 2026 Stock Trading Mastery Course</p>
    </footer>

    <script src="../js/app.js"></script>
</body>
</html>'''

    with open(OUTPUT_DIR / "glossary.html", 'w') as f:
        f.write(html)

if __name__ == "__main__":
    main()
