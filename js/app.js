// Stock Trading Course - Main Application JavaScript

class CourseApp {
    constructor() {
        this.loadDarkMode();
        this.initEventListeners();
        this.loadProgress();
        this.setActiveNavItem();
    }

    /* Dark Mode Management */
    loadDarkMode() {
        const darkMode = localStorage.getItem('darkMode');
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;

        if (darkMode === 'true' || (darkMode === null && prefersDark)) {
            this.enableDarkMode();
        }
    }

    enableDarkMode() {
        document.documentElement.classList.add('dark-mode');
        localStorage.setItem('darkMode', 'true');
        const btn = document.getElementById('darkModeToggle');
        if (btn) btn.textContent = '☀️ Light Mode';
    }

    disableDarkMode() {
        document.documentElement.classList.remove('dark-mode');
        localStorage.setItem('darkMode', 'false');
        const btn = document.getElementById('darkModeToggle');
        if (btn) btn.textContent = '🌙 Dark Mode';
    }

    toggleDarkMode() {
        if (document.documentElement.classList.contains('dark-mode')) {
            this.disableDarkMode();
        } else {
            this.enableDarkMode();
        }
    }

    /* Event Listeners */
    initEventListeners() {
        // Dark mode toggle
        const darkModeBtn = document.getElementById('darkModeToggle');
        if (darkModeBtn) {
            darkModeBtn.addEventListener('click', () => this.toggleDarkMode());
        }

        // Menu toggle for mobile
        const menuToggle = document.getElementById('menuToggle');
        const sidebar = document.getElementById('sidebar');
        if (menuToggle && sidebar) {
            menuToggle.addEventListener('click', () => {
                sidebar.classList.toggle('mobile-hidden');
            });
        }

        // Search functionality
        const searchInput = document.getElementById('searchInput');
        if (searchInput) {
            searchInput.addEventListener('input', (e) => this.search(e.target.value));
        }

        // Lesson checkbox for progress tracking
        const progressCheckbox = document.getElementById('lessonComplete');
        if (progressCheckbox) {
            progressCheckbox.addEventListener('change', (e) => {
                this.saveLessonProgress(e.target.checked);
            });
        }

        // Navigation expand buttons
        document.querySelectorAll('.nav-expand-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                const parent = btn.closest('.nav-section');
                const subsection = parent?.querySelector('.nav-subsection');
                if (subsection) {
                    subsection.classList.toggle('collapsed');
                    btn.classList.toggle('expanded');
                }
            });
        });

        // Navigation item clicks
        document.querySelectorAll('.nav-item').forEach(item => {
            item.addEventListener('click', () => {
                this.closeSubMenu();
            });
        });

        // Keyboard shortcuts
        document.addEventListener('keydown', (e) => {
            if (e.ctrlKey || e.metaKey) {
                if (e.key === 'k' || e.key === 'K') {
                    e.preventDefault();
                    const searchInput = document.getElementById('searchInput');
                    if (searchInput) searchInput.focus();
                }
            }
            // Left/Right arrow navigation
            if (e.key === 'ArrowLeft') {
                const prevBtn = document.querySelector('.nav-btn:first-of-type');
                if (prevBtn && !prevBtn.classList.contains('disabled')) {
                    prevBtn.click();
                }
            }
            if (e.key === 'ArrowRight') {
                const nextBtn = document.querySelector('.nav-btn:last-of-type');
                if (nextBtn && !nextBtn.classList.contains('disabled')) {
                    nextBtn.click();
                }
            }
        });

        // Bookmark functionality
        const bookmarkBtn = document.getElementById('bookmarkBtn');
        if (bookmarkBtn) {
            bookmarkBtn.addEventListener('click', () => this.toggleBookmark());
        }
    }

    closeSubMenu() {
        const sidebar = document.getElementById('sidebar');
        if (sidebar) {
            sidebar.classList.add('mobile-hidden');
        }
    }

    /* Search Functionality */
    search(query) {
        if (!query.trim()) {
            document.querySelectorAll('.nav-item, .nav-sub-item').forEach(item => {
                item.style.display = '';
            });
            return;
        }

        const lowerQuery = query.toLowerCase();
        document.querySelectorAll('.nav-item, .nav-sub-item').forEach(item => {
            const text = item.textContent.toLowerCase();
            item.style.display = text.includes(lowerQuery) ? '' : 'none';
        });
    }

    /* Progress Tracking */
    loadProgress() {
        const currentPage = this.getCurrentPageId();
        const progress = this.getProgress();

        // Update progress bar
        const progressBar = document.querySelector('.progress-bar');
        const progressText = document.querySelector('.progress-text');
        if (progressBar && progressText) {
            const completed = progress.completed.length;
            const total = progress.total;
            const percentage = total > 0 ? (completed / total * 100) : 0;
            progressBar.style.width = percentage + '%';
            progressText.textContent = `${completed} / ${total} lessons completed (${Math.round(percentage)}%)`;
        }

        // Check current lesson
        const checkbox = document.getElementById('lessonComplete');
        if (checkbox && currentPage) {
            checkbox.checked = progress.completed.includes(currentPage);
        }

        this.updateBookmarkButton();
    }

    getProgress() {
        const saved = localStorage.getItem('courseProgress');
        if (saved) {
            try {
                return JSON.parse(saved);
            } catch (e) {
                console.error('Error parsing progress:', e);
            }
        }

        return {
            completed: [],
            bookmarks: [],
            total: 133 // Update with actual lesson count
        };
    }

    saveLessonProgress(completed) {
        const currentPage = this.getCurrentPageId();
        if (!currentPage) return;

        const progress = this.getProgress();
        if (completed) {
            if (!progress.completed.includes(currentPage)) {
                progress.completed.push(currentPage);
            }
        } else {
            progress.completed = progress.completed.filter(p => p !== currentPage);
        }

        localStorage.setItem('courseProgress', JSON.stringify(progress));
        this.loadProgress();
    }

    getCurrentPageId() {
        const match = window.location.pathname.match(/\/pages\/(.+?)\.html/);
        return match ? match[1] : null;
    }

    /* Bookmarks */
    toggleBookmark() {
        const currentPage = this.getCurrentPageId();
        if (!currentPage) return;

        const progress = this.getProgress();
        const index = progress.bookmarks.indexOf(currentPage);

        if (index > -1) {
            progress.bookmarks.splice(index, 1);
        } else {
            progress.bookmarks.push(currentPage);
        }

        localStorage.setItem('courseProgress', JSON.stringify(progress));
        this.updateBookmarkButton();
    }

    updateBookmarkButton() {
        const currentPage = this.getCurrentPageId();
        const progress = this.getProgress();
        const bookmarkBtn = document.getElementById('bookmarkBtn');

        if (bookmarkBtn && currentPage) {
            if (progress.bookmarks.includes(currentPage)) {
                bookmarkBtn.textContent = '⭐ Bookmarked';
                bookmarkBtn.classList.add('bookmarked');
            } else {
                bookmarkBtn.textContent = '☆ Bookmark';
                bookmarkBtn.classList.remove('bookmarked');
            }
        }
    }

    setActiveNavItem() {
        const currentPage = this.getCurrentPageId();
        if (!currentPage) return;

        document.querySelectorAll('.nav-item, .nav-sub-item').forEach(item => {
            item.classList.remove('active');
            if (item.getAttribute('href')?.includes(currentPage)) {
                item.classList.add('active');

                // Expand parent if this is a sub-item
                const parent = item.closest('.nav-section');
                if (parent) {
                    const subsection = parent.querySelector('.nav-subsection');
                    if (subsection) {
                        subsection.classList.remove('collapsed');
                        const btn = parent.querySelector('.nav-expand-btn');
                        if (btn) btn.classList.add('expanded');
                    }
                }
            }
        });
    }
}

/* Markdown Parser for Converting MD to HTML */
class MarkdownParser {
    static parse(markdown) {
        let html = markdown;

        // Headers
        html = html.replace(/^### (.*?)$/gm, '<h3>$1</h3>');
        html = html.replace(/^## (.*?)$/gm, '<h2>$1</h2>');
        html = html.replace(/^# (.*?)$/gm, '<h1>$1</h1>');

        // Horizontal rule
        html = html.replace(/^---$/gm, '<hr>');

        // Bold
        html = html.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');

        // Italic
        html = html.replace(/\*(.*?)\*/g, '<em>$1</em>');

        // Links
        html = html.replace(/\[(.*?)\]\((.*?)\)/g, '<a href="$2">$1</a>');

        // Code blocks
        html = html.replace(/```(.*?)```/gs, '<pre><code>$1</code></pre>');

        // Inline code
        html = html.replace(/`(.*?)`/g, '<code>$1</code>');

        // Lists
        html = html.replace(/^\* (.*?)$/gm, '<li>$1</li>');
        html = html.replace(/^(\d+)\. (.*?)$/gm, '<li>$1. $2</li>');

        // Blockquote
        html = html.replace(/^> (.*?)$/gm, '<blockquote>$1</blockquote>');

        // Paragraphs
        html = html.split('\n\n').map(para => {
            if (!para.match(/^<|^>/)) {
                return '<p>' + para.replace(/\n/g, '<br>') + '</p>';
            }
            return para;
        }).join('\n');

        return html;
    }
}

/* Table of Contents Generation */
function generateTableOfContents() {
    const content = document.querySelector('.lesson-content');
    if (!content) return;

    const headings = content.querySelectorAll('h2, h3');
    if (headings.length === 0) return;

    const toc = document.createElement('div');
    toc.className = 'table-of-contents';
    toc.innerHTML = '<strong>Table of Contents</strong><ul>';

    headings.forEach((heading, index) => {
        const id = `heading-${index}`;
        heading.id = id;

        const level = heading.tagName === 'H3' ? 2 : 1;
        const indent = level === 2 ? 'margin-left: 1.5rem;' : '';
        toc.innerHTML += `<li style="${indent}"><a href="#${id}">${heading.textContent}</a></li>`;
    });

    toc.innerHTML += '</ul>';

    const firstHeading = content.querySelector('h2');
    if (firstHeading) {
        firstHeading.parentNode.insertBefore(toc, firstHeading);
    }
}

/* Initialize on page load */
document.addEventListener('DOMContentLoaded', () => {
    window.app = new CourseApp();
    generateTableOfContents();
});

/* Print functionality */
function printPage() {
    window.print();
}

/* Export progress to JSON */
function exportProgress() {
    const progress = localStorage.getItem('courseProgress');
    const data = JSON.stringify(JSON.parse(progress || '{}'), null, 2);
    const blob = new Blob([data], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'course-progress.json';
    a.click();
}

/* Import progress from JSON */
function importProgress() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.json';
    input.onchange = (e) => {
        const file = e.target.files[0];
        const reader = new FileReader();
        reader.onload = (event) => {
            try {
                const data = JSON.parse(event.target.result);
                localStorage.setItem('courseProgress', JSON.stringify(data));
                location.reload();
            } catch (error) {
                alert('Error importing progress: ' + error.message);
            }
        };
        reader.readAsText(file);
    };
    input.click();
}

/* Reset progress */
function resetProgress() {
    if (confirm('Are you sure you want to reset all progress? This cannot be undone.')) {
        localStorage.removeItem('courseProgress');
        location.reload();
    }
}
