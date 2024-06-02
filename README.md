# Cricket Auction Project

## Table of Contents
1. [Introduction](#introduction)
2. [Objectives](#objectives)
3. [Modules](#modules)
4. [Survey of Technologies](#survey-of-technologies)
5. [Requirements and Analysis](#requirements-and-analysis)
6. [Program Code](#program-code)
7. [Results and Discussion](#results-and-discussion)
8. [Conclusion](#conclusion)
9. [References](#references)

## Introduction
The Cricket Auction project is a web application designed to simulate an IPL-style auction process. This system allows franchises to log in, view player profiles, place bids on players, and manage their teams. The project utilizes Django for the backend, HTML/CSS/JavaScript for the frontend, and a PostgreSQL database for data storage.

## Objectives
- Develop a user-friendly interface for franchises to participate in player auctions.
- Ensure secure authentication and authorization for different user roles.
- Provide real-time updates of bids and player assignments.
- Maintain an organized database of players, franchises, and bids.

## Modules
1. **User Authentication and Authorization**: Secure login and registration for franchises and admins.
2. **Player Management**: CRUD operations for player profiles.
3. **Auction Management**: Real-time bidding system for players.
4. **Team Management**: View and manage the list of players in a franchise.
5. **Reports**: Generate reports of auction results and franchise teams.

## Survey of Technologies
### Software Description
The project is built using the following technologies:
- **Django**: Backend framework for web development.
- **PostgreSQL**: Database for storing application data.
- **HTML/CSS/JavaScript**: Frontend technologies for creating a responsive user interface.
- **Bootstrap**: CSS framework for styling the application.

### Languages
- **CSS**: Used for styling the web pages.
- **JavaScript**: Used for dynamic content and interactivity.
- **SQL**: Used for database operations.
- **Python**: Used for backend logic with Django.
- **HTML**: Used for structuring the web pages.

## Requirements and Analysis
### Requirement Specification
The system requirements include user authentication, player profile management, bidding functionality, and team management.

### Hardware and Software Requirements
- **Hardware**: A server to host the application and a client device to access the application.
- **Software**: Django, PostgreSQL, and web browsers (Chrome, Firefox, etc.).

### Architecture Diagram
An architecture diagram illustrating the system components and their interactions.

### ER Diagram
An ER diagram representing the relationships between entities like players, franchises, and bids.

### Normalization
The database follows normalization rules up to the third normal form (3NF) to eliminate redundancy and ensure data integrity.

## Program Code
The complete source code for the project is organized in the following directory structure: <br>
├───auctioneer<br>
│   ├───migrations<br>
│   │   └───__pycache__<br>
│   ├───templates<br>
│   └───__pycache__<br>
├───CrickAuction<br>
│   ├───templates<br>
│   │   └───static<br>
│   └───__pycache__<br>
├───franchise<br>
│   ├───migrations<br>
│   │   └───__pycache__<br>
│   ├───templates<br>
│   └───__pycache__<br>
└───players<br>
    ├───migrations<br>
    │   └───__pycache__<br>
    ├───static<br>
    ├───templates<br>
    │   ├───players<br>
    │   └───static<br>
    └───__pycache__<br>

## Results and Discussion
This section discusses the results obtained from the project, including the performance of the bidding system, user feedback, and areas for future improvement.

## Conclusion
The Cricket Auction project successfully simulates an IPL auction, providing a comprehensive platform for franchises to manage their teams. The system ensures secure and efficient handling of player data and bids.

## References
- [Django Documentation](https://docs.djangoproject.com/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.3/)
- [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)


