import { courses } from './data.js';

const courseGrid = document.querySelector('.course-grid');
const totalCreditsEl = document.getElementById('total-credits');
const searchInput = document.getElementById('search-courses');
const sortBtn = document.getElementById('sort-credits');
const selectedCourseEl = document.getElementById('selected-course');

let displayCourses = [...courses];

const renderCourses = (courseList) => {
    courseGrid.innerHTML = ''; 
    const fragment = document.createDocumentFragment();

    courseList.forEach(course => {
        const article = document.createElement('article');
        article.className = 'course-card';
        article.dataset.id = course.id; 
        article.innerHTML = `
            <h3>${course.name}</h3>
            <p>Code: ${course.code}</p>
            <span>${course.credits} Credits</span>
        `;
        fragment.appendChild(article);
    });

    courseGrid.appendChild(fragment);

    const total = courseList.reduce((sum, c) => sum + c.credits, 0);
    totalCreditsEl.textContent = `Total Credits: ${total}`;
};

renderCourses(displayCourses);

searchInput.addEventListener('input', (e) => {
    const term = e.target.value.toLowerCase();
    displayCourses = courses.filter(course => 
        course.name.toLowerCase().includes(term)
    );
    renderCourses(displayCourses);
});

sortBtn.addEventListener('click', () => {
    displayCourses.sort((a, b) => b.credits - a.credits);
    renderCourses(displayCourses);
});

courseGrid.addEventListener('click', (e) => {
    const card = e.target.closest('.course-card');
    
    if (!card) return; 

    const courseId = parseInt(card.dataset.id, 10);
    const courseData = courses.find(c => c.id === courseId);
    
    if (courseData) {
        selectedCourseEl.textContent = `Selected: ${courseData.name} (Grade: ${courseData.grade})`;
    }
});
