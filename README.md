# Stock Trading Mastery: HTML Course Version

Welcome to the complete HTML version of the Stock Trading Mastery course!

## Quick Start

1. Open `index.html` in your web browser
2. Navigate through the course using the sidebar menu
3. Track your progress with the built-in progress tracker
4. Use dark mode for comfortable learning at any time
5. Bookmark favorite lessons for quick access

## What's Included

### Core Features

- **110+ Lesson Pages** - All 93 lessons plus exercises and guides
- **Professional Responsive Design** - Works on desktop, tablet, and mobile
- **Dark/Light Mode Toggle** - Easy on the eyes in any environment
- **Progress Tracking** - Monitor your completion status with local storage
- **Bookmarking System** - Save important lessons for quick reference
- **Search Functionality** - Find specific topics instantly
- **Keyboard Navigation** - Use arrow keys and Ctrl+K for search
- **Print-Friendly CSS** - Print lessons for offline study
- **Syntax Highlighting** - Code blocks are properly formatted

### Course Structure

#### Level 1: Foundation (Chapters 1-5)
- Chapter 1: Market Fundamentals (6 lessons)
- Chapter 2: Getting Started (6 lessons)
- Chapter 3: Risk Management Essentials (6 lessons)
- Chapter 4: Reading Stock Charts (7 lessons)
- Chapter 5: Psychology Foundation (6 lessons)

#### Level 2: Intermediate (Chapters 6-10)
- Chapter 6: Technical Analysis Deep Dive (7 lessons)
- Chapter 7: Fundamental Analysis (7 lessons)
- Chapter 8: Trading Strategies (7 lessons)
- Chapter 9: Advanced Risk Management (6 lessons)
- Chapter 10: Trading Psychology Mastery (6 lessons)

#### Level 3: Advanced (Chapters 11-14)
- Chapter 11: Options Trading (7 lessons)
- Chapter 12: Advanced Trading Strategies (6 lessons)
- Chapter 13: Portfolio Management (7 lessons)
- Chapter 14: Professional Trading Practices (7 lessons)

#### Practical Labs
- 15 Real-world Case Studies
- 10 Simulation Scenarios
- 5 Portfolio Projects
- Mentorship Framework with self-assessment tools

### File Structure

```
Stock_Trading_Course_HTML/
├── index.html              # Main landing page
├── css/
│   └── style.css          # Complete styling (30+ KB)
├── js/
│   └── app.js             # Interactivity and features
├── pages/
│   ├── lesson-*.html      # Individual lesson pages
│   ├── exercises-*.html   # Chapter exercises
│   ├── case-study-*.html  # Case studies
│   ├── scenario-*.html    # Simulation scenarios
│   ├── project-*.html     # Portfolio projects
│   └── [other pages]      # Supporting pages
├── build-course.py        # Python script used to build the course
└── README.md              # This file
```

## Features Explained

### Progress Tracking
Your progress is saved automatically in your browser's local storage:
- Track completed lessons with checkboxes
- See percentage completion
- Export progress to JSON
- Import progress from backup

### Dark Mode
Click the "🌙 Dark Mode" button to toggle between light and dark themes. Your preference is saved automatically.

### Search
Press `Ctrl+K` (or `Cmd+K` on Mac) to open the search box and find lessons by keyword.

### Bookmarks
Each lesson has a bookmark button. Bookmarked lessons are saved and can be accessed later.

### Navigation
- Use the sidebar to navigate between lessons
- Click Previous/Next buttons for sequential progression
- Use arrow keys for quick navigation
- Click "Back to Home" to return to the main page

### Mobile Friendly
The entire course is responsive:
- Touch-friendly interface
- Mobile menu toggle
- Readable on small screens
- Optimized for all devices

## Browser Compatibility

- Chrome/Chromium (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Offline Use

All HTML files are static and can be used offline. However, progress tracking requires JavaScript to be enabled and uses browser local storage.

## Learning Paths

### Complete Beginner (Recommended)
Follow the course sequentially from Chapter 1 → 14
- Duration: 3-6 months
- Best for: Zero trading experience

### Fast Track
Foundation (Ch 1-5) → Trading Strategies (Ch 8) → Risk Management (Ch 9)
- Duration: 6-8 weeks
- Best for: Those with prior financial knowledge

### Technical Trader
Foundation → Technical Analysis (Ch 6) → Trading Strategies (Ch 8) → Advanced
- Duration: 2-4 months
- Best for: Chart analysis focus

### Fundamental Investor
Foundation → Fundamental Analysis (Ch 7) → Portfolio Management (Ch 13) → Professional
- Duration: 2-4 months
- Best for: Long-term investing focus

## Time Estimates

- **Reading**: 25-35 hours
- **Exercises**: 15-20 hours
- **Case Studies**: 10-15 hours
- **Practice/Application**: 40-60 hours
- **Total**: 65-95 hours (self-paced)

## Important Disclaimers

**Educational Content Only**: This course is for educational purposes and does not constitute financial advice.

**Trading Risk**: Stock trading involves substantial risk of loss. Most traders lose money, especially when starting.

**Consult Professionals**: Always consult with licensed financial advisors before making investment decisions.

**Start with Paper Trading**: Begin with simulated trading before using real money.

## Features in Detail

### Color Scheme (Professional & Accessible)
- Primary Blue: #0066cc (links, highlights)
- Green: #28a745 (success, positive)
- Orange: #ff9800 (warnings)
- Red: #dc3545 (danger, errors)
- Dark backgrounds for easy reading

### Typography
- Base font: 16-18px (very readable)
- Line height: 1.6-1.8 (comfortable reading)
- Clear hierarchy with H1-H4 tags
- Monospace fonts for code blocks

### Special Elements
- **Alert Boxes**: Warning, danger, success, and info styles
- **Key Concepts**: Highlighted boxes for important lessons
- **Example Boxes**: Styled for example content
- **Tables**: Responsive and well-formatted
- **Code Blocks**: Syntax-highlighted and scrollable
- **Lists**: Both ordered and unordered with proper styling
- **Blockquotes**: Italicized with left border

## Keyboard Shortcuts

- `Ctrl+K` / `Cmd+K` - Focus search box
- `←` Arrow Left - Previous lesson
- `→` Arrow Right - Next lesson
- `Tab` - Navigate focusable elements

## Progress Data Format

Progress is stored as JSON in browser local storage:

```json
{
  "completed": ["lesson-1-1", "lesson-1-2", ...],
  "bookmarks": ["lesson-5-4", "lesson-10-3", ...],
  "total": 133
}
```

You can export this data for backup or import it on another device.

## Customization

The CSS is well-organized with CSS variables for easy customization:
- Edit `css/style.css` to change colors, fonts, or layouts
- All colors are defined as CSS variables at the top
- Dark mode is automatically applied via `.dark-mode` class

Example custom color changes in the `:root` section:
```css
--accent-primary: #0066cc;
--accent-secondary: #28a745;
--accent-warning: #ff9800;
```

## JavaScript Features

The `js/app.js` file provides:
- Dark mode toggle and persistence
- Progress tracking and storage
- Search functionality
- Keyboard navigation
- Table of contents generation
- Bookmark management
- Mobile menu toggle
- Export/import progress

All JavaScript is modern ES6+ and well-commented.

## Performance

- Total size: ~2.7 MB (all HTML, CSS, and JavaScript)
- Fast page loads (static HTML)
- Minimal dependencies (vanilla JavaScript)
- Optimized CSS with proper media queries
- Mobile-optimized images and assets

## Accessibility

The course includes:
- Semantic HTML structure
- ARIA labels where appropriate
- Keyboard navigation support
- Color contrast compliance
- Focus indicators for keyboard users
- Alt text for important elements
- Readable font sizes and line heights

## Building from Source

The `build-course.py` script was used to convert markdown files to HTML:

```bash
python3 build-course.py
```

This script:
1. Reads all markdown files from the source directory
2. Converts markdown to HTML
3. Creates complete HTML pages with navigation
4. Generates index pages for practical labs
5. Creates supporting pages (overview, glossary, etc.)

## Support & Resources

- Use the sidebar for navigation
- Check the glossary for term definitions
- Review case studies for real-world examples
- Try simulation scenarios for practice
- Follow the mentorship framework for guidance

## Course Statistics

- **93** comprehensive lessons
- **14** in-depth chapters
- **15** real-world case studies
- **10** simulation scenarios
- **5** portfolio projects
- **110+** total HTML pages
- **~2.7 MB** total size
- **100%** responsive design
- **2** theme modes (light/dark)

## Tips for Success

1. **Start with Foundation** - Complete chapters 1-5 before moving forward
2. **Do the Exercises** - Complete chapter exercises for better retention
3. **Take Notes** - Use a trading journal as recommended in Chapter 5
4. **Study Case Studies** - Real examples show how to apply lessons
5. **Practice with Simulations** - Use scenario exercises before trading real money
6. **Track Progress** - Use the progress tracker to stay motivated
7. **Review Regularly** - Bookmark and revisit important lessons
8. **Go at Your Own Pace** - This is a self-paced course

## Frequently Asked Questions

**Q: Can I use this offline?**
A: Yes! All files are static HTML and work offline. Progress tracking will still work locally.

**Q: How do I back up my progress?**
A: Click "Export Progress" on the home page to download a JSON file of your data.

**Q: Can I print the lessons?**
A: Yes! The print-friendly CSS will hide navigation and optimize for printing.

**Q: How do I get support?**
A: Refer to the Mentorship Framework section for guidance and resources.

**Q: Do I need any software?**
A: Just a modern web browser - that's all!

## Version Information

- **Course Version**: 1.0
- **HTML Version**: 1.0
- **Last Updated**: February 2026
- **Build Date**: February 9, 2026

## License

Educational content for learning purposes only. All rights reserved.

---

## Ready to Begin?

1. Open `index.html` in your browser
2. Check the "How to Use This Course" page
3. Verify prerequisites
4. Start with Lesson 1.1
5. Track your progress as you learn
6. Celebrate milestones!

**Remember**: Success in trading requires discipline, continuous learning, and proper risk management. Start with paper trading and never risk money you can't afford to lose.

Happy Learning!
