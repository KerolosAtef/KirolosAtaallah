// Navigation functionality
document.addEventListener('DOMContentLoaded', function() {
    const navbar = document.getElementById('navbar');
    const navToggle = document.getElementById('nav-toggle');
    const navMenu = document.getElementById('nav-menu');
    const navLinks = document.querySelectorAll('.nav-link');

    // Mobile menu toggle
    navToggle.addEventListener('click', function() {
        navToggle.classList.toggle('active');
        navMenu.classList.toggle('active');
    });

    // Close mobile menu when clicking on a link
    navLinks.forEach(link => {
        link.addEventListener('click', function() {
            navToggle.classList.remove('active');
            navMenu.classList.remove('active');
        });
    });

    // Navbar scroll effect
    window.addEventListener('scroll', function() {
        if (window.scrollY > 100) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Active nav link highlighting
    function highlightActiveSection() {
        const sections = document.querySelectorAll('section[id]');
        const scrollPos = window.scrollY + 100;

        sections.forEach(section => {
            const top = section.offsetTop;
            const bottom = top + section.offsetHeight;
            const id = section.getAttribute('id');
            const correspondingLink = document.querySelector(`.nav-link[href="#${id}"]`);

            if (scrollPos >= top && scrollPos <= bottom) {
                navLinks.forEach(link => link.classList.remove('active'));
                if (correspondingLink) {
                    correspondingLink.classList.add('active');
                }
            }
        });
    }

    window.addEventListener('scroll', highlightActiveSection);

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offsetTop = target.offsetTop - 80; // Account for fixed navbar
                window.scrollTo({
                    top: offsetTop,
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.opacity = '1';
            entry.target.style.transform = 'translateY(0)';
            
            // Animate skill bars
            if (entry.target.classList.contains('skill-category')) {
                const skillBars = entry.target.querySelectorAll('.skill-progress');
                skillBars.forEach((bar, index) => {
                    setTimeout(() => {
                        bar.style.width = bar.style.width || '0%';
                    }, index * 200);
                });
            }

            // Animate timeline items
            if (entry.target.classList.contains('timeline-item')) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateX(0)';
            }

            // Animate cards
            if (entry.target.classList.contains('about-card') || 
                entry.target.classList.contains('research-card') || 
                entry.target.classList.contains('project-card')) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        }
    });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', function() {
    const elementsToObserve = document.querySelectorAll(`
        .skill-category,
        .timeline-item,
        .about-card,
        .research-card,
        .project-card,
        .stat-item
    `);

    // Set initial styles
    elementsToObserve.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'all 0.6s ease-out';
        observer.observe(el);
    });

    // Special handling for timeline items
    const timelineItems = document.querySelectorAll('.timeline-item');
    timelineItems.forEach((item, index) => {
        item.style.opacity = '0';
        item.style.transform = index % 2 === 0 ? 'translateX(-50px)' : 'translateX(50px)';
        item.style.transition = 'all 0.6s ease-out';
    });
});

// Typing effect for hero title
function typeWriter(element, text, speed = 100) {
    let i = 0;
    element.innerHTML = '';
    
    function type() {
        if (i < text.length) {
            element.innerHTML += text.charAt(i);
            i++;
            setTimeout(type, speed);
        }
    }
    
    type();
}

// Initialize typing effect
document.addEventListener('DOMContentLoaded', function() {
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        const titleLines = heroTitle.querySelectorAll('.title-line');
        if (titleLines.length === 0) {
            // Fallback if title structure is different
            setTimeout(() => {
                typeWriter(heroTitle, 'Kirolos Ataallah', 150);
            }, 1000);
        }
    }
});

// Parallax effect for hero section
window.addEventListener('scroll', function() {
    const scrolled = window.pageYOffset;
    const hero = document.querySelector('.hero');
    if (hero) {
        const rate = scrolled * -0.5;
        hero.style.transform = `translateY(${rate}px)`;
    }
});

// Dynamic background particles (optional enhancement)
function createParticles() {
    const hero = document.querySelector('.hero');
    const particleCount = 50;
    
    for (let i = 0; i < particleCount; i++) {
        const particle = document.createElement('div');
        particle.className = 'particle';
        particle.style.cssText = `
            position: absolute;
            width: 2px;
            height: 2px;
            background: rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            left: ${Math.random() * 100}%;
            top: ${Math.random() * 100}%;
            animation: float ${3 + Math.random() * 4}s ease-in-out infinite;
            animation-delay: ${Math.random() * 2}s;
        `;
        hero.appendChild(particle);
    }
}

// Add particle animation CSS
const particleCSS = `
    @keyframes float {
        0%, 100% { transform: translateY(0px); opacity: 0.3; }
        50% { transform: translateY(-20px); opacity: 1; }
    }
`;

const style = document.createElement('style');
style.textContent = particleCSS;
document.head.appendChild(style);

// Initialize particles
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(createParticles, 2000);
});

// Copy email functionality
function copyEmail() {
    const email = 'kirolosatef1997@gmail.com';
    navigator.clipboard.writeText(email).then(function() {
        // Show notification
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: #059669;
            color: white;
            padding: 1rem 2rem;
            border-radius: 10px;
            z-index: 9999;
            animation: slideInRight 0.3s ease-out;
        `;
        notification.textContent = 'Email copied to clipboard!';
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    });
}

// Add click event to email in contact section
document.addEventListener('DOMContentLoaded', function() {
    const emailElement = document.querySelector('.contact-details p');
    if (emailElement && emailElement.textContent.includes('@')) {
        emailElement.style.cursor = 'pointer';
        emailElement.addEventListener('click', copyEmail);
    }
});

// Form validation and submission (if contact form is added later)
function validateForm(form) {
    const requiredFields = form.querySelectorAll('[required]');
    let isValid = true;
    
    requiredFields.forEach(field => {
        if (!field.value.trim()) {
            field.classList.add('error');
            isValid = false;
        } else {
            field.classList.remove('error');
        }
    });
    
    return isValid;
}

// Research paper click tracking (for analytics)
document.addEventListener('DOMContentLoaded', function() {
    const researchLinks = document.querySelectorAll('.research-link');
    researchLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            const paperTitle = this.closest('.research-card').querySelector('h3').textContent;
            const linkType = this.textContent.trim();
            
            // Analytics tracking (replace with your analytics code)
            console.log(`Research paper interaction: ${paperTitle} - ${linkType}`);
        });
    });
});

// Project card hover effects
document.addEventListener('DOMContentLoaded', function() {
    const projectCards = document.querySelectorAll('.project-card');
    
    projectCards.forEach(card => {
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-10px) scale(1.02)';
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });
});

// Skill bar animation trigger
function animateSkillBars() {
    const skillCategories = document.querySelectorAll('.skill-category');
    
    skillCategories.forEach(category => {
        const skillBars = category.querySelectorAll('.skill-progress');
        skillBars.forEach((bar, index) => {
            const width = bar.style.width;
            bar.style.width = '0%';
            
            setTimeout(() => {
                bar.style.width = width;
            }, index * 200);
        });
    });
}

// Dark mode toggle (optional feature)
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
}

// Load dark mode preference
document.addEventListener('DOMContentLoaded', function() {
    if (localStorage.getItem('darkMode') === 'true') {
        document.body.classList.add('dark-mode');
    }
});

// Performance optimization: Lazy loading for images
document.addEventListener('DOMContentLoaded', function() {
    const images = document.querySelectorAll('img[data-src]');
    
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                img.src = img.dataset.src;
                img.classList.remove('lazy');
                imageObserver.unobserve(img);
            }
        });
    });
    
    images.forEach(img => imageObserver.observe(img));
});

// Preloader (optional)
window.addEventListener('load', function() {
    const preloader = document.querySelector('.preloader');
    if (preloader) {
        preloader.style.opacity = '0';
        setTimeout(() => {
            preloader.style.display = 'none';
        }, 500);
    }
});

// Social media sharing
function shareOnSocial(platform) {
    const url = window.location.href;
    const title = 'Kirolos Ataallah - Research Engineer & AI Specialist';
    
    let shareUrl = '';
    
    switch(platform) {
        case 'twitter':
            shareUrl = `https://twitter.com/intent/tweet?url=${encodeURIComponent(url)}&text=${encodeURIComponent(title)}`;
            break;
        case 'linkedin':
            shareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(url)}`;
            break;
        case 'facebook':
            shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`;
            break;
    }
    
    if (shareUrl) {
        window.open(shareUrl, '_blank', 'width=600,height=400');
    }
}

// Console message for developers
console.log(`
🚀 Welcome to Kirolos Ataallah's Portfolio
👨‍💻 Interested in the code? Check it out on GitHub!
📧 Get in touch: kirolosatef1997@gmail.com
`);

// Easter egg: Konami code
let konamiCode = [];
const konamiSequence = [38, 38, 40, 40, 37, 39, 37, 39, 66, 65];

document.addEventListener('keydown', function(e) {
    konamiCode.push(e.keyCode);
    
    if (konamiCode.length > konamiSequence.length) {
        konamiCode.shift();
    }
    
    if (konamiCode.join(',') === konamiSequence.join(',')) {
        // Easter egg triggered
        document.body.style.filter = 'hue-rotate(180deg)';
        setTimeout(() => {
            document.body.style.filter = '';
        }, 3000);
        
        console.log('🎉 Konami code activated! You found the easter egg!');
    }
});

// Error handling for external links
document.addEventListener('DOMContentLoaded', function() {
    const externalLinks = document.querySelectorAll('a[href^="http"]');
    
    externalLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Add loading state
            this.style.opacity = '0.7';
            this.style.pointerEvents = 'none';
            
            setTimeout(() => {
                this.style.opacity = '';
                this.style.pointerEvents = '';
            }, 1000);
        });
    });
});

// Fetch Google Scholar Statistics
async function fetchGoogleScholarStats() {
    try {
        // Using Serpapi service (free tier available) to fetch Google Scholar data
        // Alternative: You can use your own backend API or CORS proxy
        const scholarId = '6gRlYHAAAAAJ'; // Your Google Scholar ID
        
        // Using a CORS proxy to fetch Google Scholar data
        const proxyUrl = 'https://api.allorigins.win/raw?url=';
        const scholarUrl = `https://scholar.google.com/citations?user=${scholarId}&hl=en`;
        
        const response = await fetch(proxyUrl + encodeURIComponent(scholarUrl));
        const html = await response.text();
        
        // Parse the HTML to extract citations and publications
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        
        // Extract citation count
        const citationElements = doc.querySelectorAll('#gsc_rsb_st td.gsc_rsb_std');
        let totalCitations = 0;
        let hIndex = 0;
        let i10Index = 0;
        
        if (citationElements.length >= 3) {
            totalCitations = parseInt(citationElements[0].textContent.replace(/,/g, '')) || 0;
            hIndex = parseInt(citationElements[2].textContent) || 0;
            i10Index = parseInt(citationElements[4].textContent) || 0;
        }
        
        // Count publications
        const publications = doc.querySelectorAll('.gsc_a_tr');
        const publicationCount = publications.length || 3; // Fallback to 3 if can't fetch
        
        // Update the stats on the page
        updateStats(totalCitations, publicationCount, hIndex, i10Index);
        
        return { totalCitations, publicationCount, hIndex, i10Index };
        
    } catch (error) {
        console.error('Error fetching Google Scholar stats:', error);
        // Use fallback values if fetch fails
        updateStats(null, 3, null, null); // Keep published papers at 3 as fallback
        return null;
    }
}

function updateStats(citations, publications, hIndex, i10Index) {
    const statItems = document.querySelectorAll('.stat-item');
    
    if (statItems.length >= 4) {
        // Update Published Papers (2nd stat)
        if (publications && publications > 0) {
            statItems[1].querySelector('h3').textContent = publications.toString();
        }
        
        // Update Total Citations (4th stat)
        if (citations && citations > 0) {
            statItems[3].querySelector('h3').textContent = citations.toLocaleString();
            statItems[3].querySelector('p').textContent = 'Total Citations';
            statItems[3].title = `h-index: ${hIndex || 'N/A'}, i10-index: ${i10Index || 'N/A'}`;
        }
    }
}

// Fetch stats from the local JSON file (updated by GitHub Actions)
async function fetchScholarStatsFromJSON() {
    try {
        const response = await fetch('scholar-stats.json');
        if (!response.ok) {
            throw new Error('Failed to fetch scholar-stats.json');
        }
        const data = await response.json();
        console.log('Loaded Google Scholar stats from JSON:', data);
        updateStats(data.citations, data.publications, data.hIndex, data.i10Index);
        return data;
    } catch (error) {
        console.log('Could not load scholar-stats.json, using default HTML values:', error.message);
        // HTML already has default values, so no need to do anything
        return null;
    }
}

// Initialize Scholar Stats on page load
document.addEventListener('DOMContentLoaded', function() {
    // Use the JSON file approach (updated daily by GitHub Actions)
    fetchScholarStatsFromJSON();
});