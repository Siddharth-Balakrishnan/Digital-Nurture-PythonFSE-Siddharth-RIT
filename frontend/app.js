import { courses } from './data.js';

const courseGrid = document.querySelector('.course-grid');
const totalCreditsEl = document.getElementById('total-credits');

const renderCourses = (courseList) => {
    // Clear container first
    courseGrid.innerHTML = ''; 
    

    const fragment = document.createDocumentFragment();

    courseList.forEach(course => {
        const article = document.createElement('article');
        article.className = 'course-card';
        // Assigning data-id for use in Task 3
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


renderCourses(courses);
