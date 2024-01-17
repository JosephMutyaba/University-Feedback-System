# University Feedback System

The University Feedback System is a Django-based web application designed to collect feedback from university students about their experiences with lecturers, university facilities, and courses taught during a semester. This system aims to enhance communication between students and the university administration and help improve the overall learning environment.

## Features

- **Lecturer Feedback:** Students can provide feedback on individual lecturers, helping them understand strengths and areas for improvement.
- **Facility Feedback:** Students can share their opinions on university facilities such as libraries, labs, and common areas.
- **Course Feedback:** Students can provide insights into the quality and effectiveness of courses offered during the semester.
- **Admin Dashboard:** Administrators can review and analyze feedback submissions through an intuitive dashboard.
- **Data-driven Insights:** The system generates reports and visualizations to help administrators identify trends and make informed decisions.

## Getting Started

Follow these steps to set up the University Feedback System locally for development and testing purposes.

1. Clone the repository:
   ```bash
   git clone https://github.com/JosephMutyaba/Group_I_Recess.git

2. Navigate to the project directory:
   ```bash
   cd Group_I_Recess
3. Create a superuser account for admin access:
   ```bash
   python manage.py createsuperuser
4. Start the development server:
   ```bash
   python manage.py runserver
5. Access the application in your web browser at http://localhost:8000.

### Further instructions:
The system is designed in a way that its the admin to add info about colleges, schools, departments and courses. Therefore when the admin logs in to his panel, he should populate the models for colleges, schools, departments and courses with data. It's this data which students choose from when registering.

## Contributing
Contributions are welcome! If you want to contribute to this project, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Open a pull request, describing your changes and the problem they solve.

